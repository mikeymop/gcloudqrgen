# GCloud QRGen

<div style="text-align:center"
<img src="https://raw.githubusercontent.com/mikeymop/gcloudqrgen/master/example.png?token=AA6RJGIT26OPNP7UR3TORLS47GP52" width="600">
</div>

The purpose of this function is to create a QR Code containing a specified url. The size can be specified (default = 1). The resulting QR code is then displayed on the browsers canvas. 

This is useful for generating QR Codes in an ephemeral manner.

### Deploying the Function

Because Google Cloud requires function names to be globally unique, you will have to change the function name on line 5. Use that same function name in the deploy command below.

```
gcloud --project [Project name] functions deploy [Function Name] --runtime python37 --trigger-http --timeout=540
```

### Calling the Function

This is an example `curl` request.
```
https://[region][projecturl].cloudfunctions.net/[Function Name]?text=PythonIsAwesome&scale=10
```

### Testing: Using the venv

```
pipenv install
pipenv shell
python main.py [args]...
```
