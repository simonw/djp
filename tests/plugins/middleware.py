import djp


@djp.hookimpl
def middleware():
    return [
        "tests.test_project.middleware.Middleware",
        djp.Before("tests.test_project.middleware.MiddlewareBefore"),
        djp.After("tests.test_project.middleware.MiddlewareAfter"),
    ]
