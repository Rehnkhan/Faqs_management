from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializer import FAQSerializer

@api_view(['GET'])
def faq_list(request):
    faqs = FAQ.objects.all()
    lang = request.query_params.get('lang', 'en')
    for faq in faqs:
        faq.question = faq.get_translated_question(lang)
        faq.answer = faq.get_translated_answer(lang)
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def faq_detail(request, pk):
    try:
        faq = FAQ.objects.get(pk=pk)
    except FAQ.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        lang = request.query_params.get('lang', 'en')
        faq.question = faq.get_translated_question(lang)
        faq.answer = faq.get_translated_answer(lang)
        serializer = FAQSerializer(faq)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        faq.delete()
        return Response(status=204)
    
class FAQList(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang', 'en')
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        return queryset

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_object(self):
        obj = super().get_object()
        lang = self.request.query_params.get('lang', 'en')
        obj.question = obj.get_translated_question(lang)
        obj.answer = obj.get_translated_answer(lang)
        return obj