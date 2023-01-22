from django.shortcuts import render
from django.http import JsonResponse
import random


def find_index_of_max(request):
    arr = [random.randint(1, 30) for i in range(0, 10)]
    max_val = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    context = {'max_index': max_index,
               'all_array': arr}
    return render(request, 'find_index.html', context)

