def request_note(request, response, note):
    if not hasattr(request, "_notes"):
        request._notes = []
    request._notes.append(note)
    response._request = request


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-DJP-Middleware"] = "Middleware"
        request_note(request, response, "Middleware")
        return response


class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        request_note(request, response, self.__class__.__name__)
        return response


class Middleware3(Middleware2):
    pass


class Middleware4(Middleware2):
    pass


class Middleware5(Middleware2):
    pass


class MiddlewareBefore:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-DJP-Middleware-Before"] = "MiddlewareBefore"
        request_note(request, response, "MiddlewareBefore")
        return response


class MiddlewareAfter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-DJP-Middleware-After"] = "MiddlewareAfter"
        request_note(request, response, "MiddlewareAfter")
        return response
