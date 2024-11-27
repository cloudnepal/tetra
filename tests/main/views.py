from django.http import HttpResponse

from tests.main.helpers import render_component_tag


def simple_basic_component_with_css(request):
    return HttpResponse(
        render_component_tag(
            request, "{% @ main.default.simple_basic_component_with_css / %}"
        )
    )
