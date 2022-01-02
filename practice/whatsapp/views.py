from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import graph
import os

def whatsappchat(request):
    if request.method == 'POST':
        chat = request.FILES['chatfile']
        fss = FileSystemStorage()
        file_path = fss.path(chat.name)
        if os.path.exists(file_path) == False:
            fss.save(chat.name, chat)
        graph.Overall(file_path, fss.location)
        file_url = fss.url('overall.jpg')
        print('FILELOCATION',fss.location ,'\nFILEURL', file_url)
        return render(request, 'whatsapp.html', {'file_url': file_url})
    return render(request, 'whatsapp.html')