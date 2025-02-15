from pyodide.ffi import to_js

async def fetch(request):
    body = "Hello! Your Python Cloudflare Worker is running."
    headers = {"Content-Type": "text/plain"}
    return to_js((body, {"status": 200, "headers": headers}))
