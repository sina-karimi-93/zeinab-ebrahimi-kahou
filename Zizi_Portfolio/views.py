from django.shortcuts import render

def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/header.html', context)

def footer(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/footer.html', context)
