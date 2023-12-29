from dogblog.sitedog.utils import menu


def get_sitedog_context(request):
    return {'mainmenu': menu}
