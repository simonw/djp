import djp


@djp.hookimpl
def settings(current_settings):
    current_settings["FROM_PLUGIN"] = "x"
