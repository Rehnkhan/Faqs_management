from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FAQ
        fields = '__all__'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'get_translated_question', 'get_translated_answer', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Translations', {
            'fields': ('question_translated', 'answer_translated')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')