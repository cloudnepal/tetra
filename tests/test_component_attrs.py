
from tests.conftest import extract_component
from tests.main.helpers import render_component_tag


def test_basic_component(request):
    """Tests a simple component with / end"""
    content = render_component_tag(
        request, "{% @ main.default.simple_component_with_attrs / %}"
    )
    assert extract_component(content) == "foo"
