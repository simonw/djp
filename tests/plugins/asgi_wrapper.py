import djp


@djp.hookimpl
def asgi_wrapper():
    return wrap


def wrap(app):
    async def wrapper(scope, receive, send):
        if scope["type"] == "http" and scope["path"] == "/hello":
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": b"Hello world",
                }
            )
        else:
            await app(scope, receive, send)

    return wrapper
