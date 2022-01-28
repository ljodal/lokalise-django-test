from django.http import HttpRequest, HttpResponse
from django.utils.translation import get_language
from django.utils.translation import gettext as _


def my_view(request: HttpRequest) -> HttpResponse:
    print(get_language())
    print(_("Foo"))

    # Translators: This is a test
    text = _("Hello {name}, I'm Django!").format(
        name=request.GET.get("name", _("world"))
    )
    return HttpResponse(text)
