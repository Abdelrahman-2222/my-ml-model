from django.shortcuts import render


# Create your views here.
def my_page(request):
    return render(request, 'base.html')


def my_view(request):
    id_value = 1  # Replace with the actual id value
    context = {'id_value': id_value}
    return render(request, 'base.html', context)
