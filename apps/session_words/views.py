from django.shortcuts import render, redirect
from time import strftime, localtime

# Create your views here.

def home(request):

    if 'word_log'not in request.session:
        request.session['word_log'] = []

    return render(request, "index.html")

def new(request):

    temp_list = request.session['word_log']

    if 'big_font' in request.POST:
        showbig = 1
        temp_list.append({"word": request.POST['word'], "color": request.POST['color'], "show_big":  request.POST['big_font'], 'time': strftime('%m/%d/%Y  %I:%M %p',localtime())})

    else:
        showbig = 0
        temp_list.append({"word": request.POST['word'], "color": request.POST['color'], "show_big": request.POST['big_font'], 'time': strftime('%m/%d/%Y  %I:%M %p',localtime())})
    
    request.session['word_log'] = temp_list

    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')