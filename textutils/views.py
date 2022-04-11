# Created by : Surmayi
import re

from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1> Surmayi</h1> <a href='https://github.com/surmayi' target ='blank'> My gitHub </a>"
#                         "<hr><a href='https://google.com' target ='blank'> Google </a>")
#
#
# def about(request):
#     return HttpResponse('<h1>About World</h1>')
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunc', 'off')
    upperCase = request.POST.get('upperCase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraSpaceremove = request.POST.get('extraSpaceremove', 'off')
    print(text, removePunc, upperCase, newlineremove, extraSpaceremove)
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    purpose=''
    if removePunc == 'on':
        purpose += 'Remove Punctuation'
        for chr in text:
            if chr not in punctuations:
                analyzed += chr
    else:
        analyzed = text
    if upperCase == 'on':
        purpose += ' UpperCase'
        analyzed = analyzed.upper()
    if newlineremove == 'on':
        purpose += ' New line Removal'
        analyzed = ' '.join([line.strip() for line in analyzed.strip().splitlines() if line.strip()])
        analyzed = re.sub('[\r\n]+', ' ', analyzed)
    if extraSpaceremove == 'on':
        purpose += ' Extra Space Removal'
        analyzed = re.sub('\s{2,}', ' ', analyzed)
    params = {
        'purpose': purpose,
        'analyzed_text': analyzed
    }
    return render(request, 'analyze.html', params)
