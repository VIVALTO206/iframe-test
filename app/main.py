from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

TARGET_URL = "https://moccasin-crab-465492.com"


@app.get("/", response_class=HTMLResponse)
async def index():
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Embedded site</title>
  <style>
    html, body, #iframe {{
      height: 100%;
      margin: 0;
      padding: 0;
      background: #000;
    }}
    #iframe {{
      width: 100%;
      border: none;
    }}
  </style>
</head>
<body>
  <iframe id="iframe" src="{TARGET_URL}" sandbox="allow-scripts allow-forms allow-same-origin allow-popups" allowfullscreen></iframe>
</body>
</html>"""
    return HTMLResponse(content=html)