from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sum_if(request):
    input_text = request.POST['input_text']
    menu = request.POST['menu']
    numbers = input_text.split(' ')
    sum = 0
    for item in numbers:
        if item.isdigit():
            if int(item) < int(menu):
                sum += int(item)
    return render(request, 'sum_if.html', {'sum': sum, 'menu': menu})

