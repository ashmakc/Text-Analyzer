#i have created this file -Ashma
from django.http import HttpResponse
from django.shortcuts import render

def nav(request):
    s='''<h1> Navigation Bar <br></h1> <a href="https://www.google.com/"> Google</a>'''
    return HttpResponse(s)

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Get checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
#check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

        #analyze the text
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if(extraspaceremove=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extra space', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps !="on" and newlineremove !="on" and extraspaceremove !="on" ):
        return HttpResponse("Please select any Operation and try again")
    return render(request, 'analyze.html', params)




