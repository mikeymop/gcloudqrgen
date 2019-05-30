# GCloud QRGen

The purpose of this function is to create a QR Code containing a specified url. The size can be specified (default = 1). This is useful for appending the qr to documents with an online link.

### Deploying the Function

```
gcloud --project [Project name] functions deploy qr_gen --runtime python37 --trigger-http --timeout=540
```

### Calling the Function

This is an example `curl` request.
```
curl -g -X POST [Project URL] -H "Content-Type:application/json" -d '{"output_file":"oqr.png","scale":"10","text":"hello there","result_bucket":"pdfstamp"}'
```

### Testing: Using the venv

```
pipenv install
pipenv shell
python main.py [args]...
```