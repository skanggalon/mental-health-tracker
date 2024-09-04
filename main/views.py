from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306224410',
        'name': 'Muhammad Zaid Ats Tsabit',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)