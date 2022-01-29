from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


def my_view(request: HttpRequest) -> HttpResponse:

    # Translators: This is a test
    text = _("Hello {name}, I'm Django!").format(
        name=request.GET.get("name", _("world"))
    )
    return HttpResponse(text)


def template_view(request: HttpRequest) -> HttpResponse:

    return render(request, "test.html", {"name": request.GET.get("name", _("world"))})
