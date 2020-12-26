from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, обращайтесь по телефону', '555 55 55']})
