def handler(request, response):
    # Parse JSON body safely
    try:
        data = request.json()
    except Exception:
        data = {}

    return response.json({
        "message": "Hello from analyze!",
        "received": data
    })
