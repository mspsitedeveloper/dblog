from django.shortcuts import render
from django.views.generic import TemplateView

# def message(request):
#     return render(request, 'message.html')
class Messageview(TemplateView):
    template_name = 'message.html'
    