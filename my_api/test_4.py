from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def home_factorial(request):
    return render(request, 'factorial.html')


@api_view(['POST'])
def calculate_factorial(request):
    n = request.POST['number']
    fact = factorial(int(n))
    context = {'response' : fact,
               'number' : n}
    return render(request, 'factorial_2.html', context)

    
def factorial(number):
    try:
        return 1 if number == 0 else number * factorial(number-1)
    except Exception as E:
        print('error :: ', E)
