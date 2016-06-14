from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'accidents/index.html'
    
    def get_context_data(self, **kwargs):
        return kwargs