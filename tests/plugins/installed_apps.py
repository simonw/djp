import djp


@djp.hookimpl(specname="installed_apps")
def installed_apps():
    return ["tests.test_project.app1"]


@djp.hookimpl(specname="installed_apps", tryfirst=True)
def installed_apps_ordered():
    return [
        "tests.test_project.app2",
        djp.After("tests.test_project.fake_app_after"),
        djp.Before("tests.test_project.fake_app_before"),
    ]
