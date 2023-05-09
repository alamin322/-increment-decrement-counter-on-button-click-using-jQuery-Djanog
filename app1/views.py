from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        print(value)
        print(type(value))
        return JsonResponse({'status': 'success'})


    return render(request, 'home.html')