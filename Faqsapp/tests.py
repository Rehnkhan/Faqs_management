from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def faq():
    return FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

@pytest.mark.django_db
def test_faq_model_translation(faq):
    assert faq.get_translated_question('hi') == faq.question_hi or faq.question
    assert faq.get_translated_question('bn') == faq.question_bn or faq.question

@pytest.mark.django_db
def test_faq_list(api_client, faq):
    url = reverse('faq-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['question'] == faq.question

@pytest.mark.django_db
def test_faq_detail(api_client, faq):
    url = reverse('faq-detail', args=[faq.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['question'] == faq.question