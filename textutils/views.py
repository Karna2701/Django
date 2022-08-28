from django.http import HttpResponse
from django.shortcuts import render


def index(request):

   return render(request,'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'Off')
    fullcaps = request.POST.get('fullcaps', 'Off')
    newlineremover = request.POST.get('newlineremover', 'Off')
    extraspaceremover = request.POST.get('extraspaceremover','Off')
    charcounter = request.POST.get('charcounter','Off')

    if removepunc == 'on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)



    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:

            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":


                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


    elif (extraspaceremover == 'on'):
        analyzed = ""
        for index , char in enumerate(djtext):

            if djtext[index] == " " and djtext[index+1]==" ":
                pass

            else:
                analyzed = analyzed + char


        params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)



    elif(charcounter=='on'):
        analyzed = ""

        analyzed = analyzed + str(len(djtext))

        params = {'purpose': 'charcounter', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")
