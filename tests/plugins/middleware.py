import djp


@djp.hookimpl(specname="middleware", tryfirst=True)
def middleware1():
    return [
        "tests.test_project.middleware.Middleware",
        "tests.test_project.middleware.Middleware2",
        "tests.test_project.middleware.Middleware3",
        djp.Before("tests.test_project.middleware.MiddlewareBefore"),
        djp.After("tests.test_project.middleware.MiddlewareAfter"),
    ]


@djp.hookimpl(specname="middleware")
def middleware2():
    return [
        djp.Position(
            "tests.test_project.middleware.Middleware4",
            before="tests.test_project.middleware.Middleware2",
        ),
        djp.Position(
            "tests.test_project.middleware.Middleware5",
            before="tests.test_project.middleware.Middleware3",
        ),
    ]
