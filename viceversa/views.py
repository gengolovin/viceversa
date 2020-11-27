from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    number_word = len(user_text.split())

    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reversedtext': reversed_text,
                                            'number_of_words': number_word})

