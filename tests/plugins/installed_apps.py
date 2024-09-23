import djp


@djp.hookimpl
def installed_apps():
    return ["tests.test_project.app1"]
