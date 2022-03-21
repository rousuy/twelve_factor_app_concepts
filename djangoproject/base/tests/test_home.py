import pytest
from django.urls import reverse
from djangoproject.django_assertions import assert_contains


@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title> Django Project</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Django Project</a>')
