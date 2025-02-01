from django.urls import path
from .views import FAQList, FAQDetail#, faq_list, faq_detail

urlpatterns = [
    path('faqs/', FAQList.as_view(), name='faq-list'),
    path('faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),
    # path('faq/', faq_list, name='faq-list'),
    # path('faq/<int:pk>/', faq_detail, name='faq-detail'),
]
