from django.shortcuts import render, redirect
from .models import WordPair
from openpyxl import Workbook
from django.http import HttpResponse
import os

def input_words(request):
    if request.method == 'POST':
        korean = request.POST.get('korean')
        english = request.POST.get('english')
        WordPair.objects.create(korean=korean, english=english)
        return redirect('input_words')
    
    return render(request, 'savewords/form.html')

def download_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.append(['Korean', 'English'])

    for word in WordPair.objects.all():
        ws.append([word.korean, word.english])

    response = HttpResponse(
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=word_pairs.xlsx'
    wb.save(response)
    return response



# Create your views here.
