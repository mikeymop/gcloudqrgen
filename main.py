import sys, os, tempfile, logging, segno, flask
from google.cloud import storage

logger = logging.getLogger()

def mqr_gen(request):
	qrtext = flask.request.args.get('text')
	scale = flask.request.args.get('scale')
	# lazy load json vars
	# # qrtext, scale = parse_request(request)
	print("Got %s %s" % (str(qrtext), str(scale)))
	# return "Got, {}".format(qrtext)

	# client = storage.Client() # open a bucket connection
	# result_bucket = client.get_bucket(str(bucket))
	temp_dir = "/tmp"
	os.chdir(temp_dir)

	# make temp files
	result_file = tempfile.NamedTemporaryFile(mode="w+b",suffix='.png', dir=temp_dir, delete=True)

	# generate qrcode
	print("Generating QR Code...")
	mk_qr(result_file.name, scale, qrtext)

	# return in browser
	print("Sending %s" % (str(result_file.name)))
	response = flask.send_file(result_file, mimetype="image/png", as_attachment=False)
	return response

	# upload back to cloud
	# print("Uploading QR image to gcloud")
	# result_blob = result_bucket.blob(str(os.path.basename(result_file.name)))
	# result_blob.upload_from_filename(str(os.path.basename(result_file.name)))
	# print("Renaming blob to the name you requested")
	# result_bucket.rename_blob(result_blob, str(ofile))

def mk_qr(ofile, qrsize, text):
	print(ofile, text)
	qr = segno.make(str(text))
	print("Saving qr code as %s" % (ofile))
	qr.save(ofile, scale=qrsize, border=2, background=None)


def parse_request(request):
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        request_json = request.get_json(silent=True) # creates a dict

    if request_json:
        # try: 
        #     ofile = request_json['output_file']
        # except:
        #     print("Missing: %s in json" % ("output_file"))
        try:
            scale = request_json['scale']
        except:
            print("Missing: %s in json" % ("scale"))
        try:
            qrtext = request_json['text']
        except:
        	print("Missing: %s in json" % ("qrtext"))
        # try:
        #     bucket = request_json['result_bucket']
        # except:
        # 	print("Missing: %s in json" % ("result_bucket"))

    objects = (qrtext, scale)
    return objects

# ofile, scale, text, result_bucket = sys.argv[1:]
# mk_qr(ofile, scale, text, result_bucket)