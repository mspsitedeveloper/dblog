from django.shortcuts import render
from django.views.generic import ListView
from .models import message

# def message(request):
#     return render(request, 'message.html')
class Messageview(ListView):
    model = message
    template_name = 'message.html'

    