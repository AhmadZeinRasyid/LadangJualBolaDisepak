from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406408395',
        'name' : 'Haru Urara',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)