import sys, os, tempfile, logging, segno, flask

logger = logging.getLogger()

def qr_gen(request):
	background = None
	qrtext = flask.request.args.get('text') # gets query string params
	scale = flask.request.args.get('scale')
	background = flask.request.args.get('bg')
	ext = flask.request.args.get('ext')
	print("Got %s %s" % (str(qrtext), str(scale)))
	if(scale == None):
		print("Defaulting scale to 1")
		scale = 1
	if(ext == None):
		print("Defaulting to png")
		ext = '.png'

	temp_dir = "/tmp" # this is the only writable location in gcloud
	os.chdir(temp_dir)

	# make temp file
	result_file = tempfile.NamedTemporaryFile(mode="w+b",suffix=ext, dir=temp_dir, delete=True)

	# generate qrcode
	print("Generating QR Code...")
	mk_qr(result_file.name, int(scale), qrtext, background, ext)

	# return in browser
	print("Sending %s" % (str(result_file.name)))
	response = flask.send_file(result_file, mimetype="image/png", as_attachment=False)
	return response

def mk_qr(ofile, qrsize, text, bg, ext):
	print(ofile, text)
	qr = segno.make(str(text))
	print("Saving qr code as %s" % (ofile))
	if(ext == 'png'):
		qr.save(ofile, scale=qrsize, border=2, background=bg)
	else:
		img = qr.to_pil(scale=scale, background=background)
		img.save(ofile)


# For testing locally
ofile, scale, qrtext, background, ext = sys.argv[1:]
mk_qr(ofile, int(scale), qrtext, background, ext)
