```markdown
# iframe-fastapi

Simple FastAPI app that exposes one URL (/) which serves a page embedding
https://moccasin-crab-465492.com in an iframe.

Requirements
- Poetry
- Python 3.10+

Setup & run
1. Install dependencies:
   poetry install

2. Run the app (development):
   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Then open http://127.0.0.1:8000/ in your browser.

Notes
- The target site may prevent being embedded using X-Frame-Options or Content-Security-Policy. If the site sets those headers, the browser will refuse to show it inside an iframe and there's nothing this app can do to override that from the client side.
- If you control the target site, ensure it does not send X-Frame-Options: DENY or a CSP frame-ancestors directive that blocks embedding.
- If you need to bypass restrictions you would need a proxy that rewrites/strips those headers (be aware of legal and security considerations).
```