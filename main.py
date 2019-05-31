import sys, os, tempfile, logging, segno, flask

logger = logging.getLogger()

def qr_gen(request):
	background = None
	qrtext = flask.request.args.get('text') # gets query string params
	scale = flask.request.args.get('scale')
	background = flask.request.args.get('bg')
	print("Got %s %s" % (str(qrtext), str(scale)))
	if(scale == None):
		print("Defaulting scale to 1")
		scale = 1

	temp_dir = "/tmp"
	os.chdir(temp_dir)

	# make temp files
	result_file = tempfile.NamedTemporaryFile(mode="w+b",suffix='.png', dir=temp_dir, delete=True)

	# generate qrcode
	print("Generating QR Code...")
	mk_qr(result_file.name, int(scale), qrtext, background)

	# return in browser
	print("Sending %s" % (str(result_file.name)))
	response = flask.send_file(result_file, mimetype="image/png", as_attachment=False)
	return response

def mk_qr(ofile, qrsize, text, bg):
	print(ofile, text)
	qr = segno.make(str(text))
	print("Saving qr code as %s" % (ofile))
	qr.save(ofile, scale=qrsize, border=2, background=bg)

"""
For testing locally
ofile, scale, text, result_bucket = sys.argv[1:]
mk_qr(ofile, scale, text, result_bucket)
"""