from django.shortcuts import render

def base_view(request, template_name, context=None):
    if context is None:
        context = {}
    return render(request, template_name, context)

# Create your views here.
def About(request):
    return render(request, 'about.html', {'show_navigation': True})

def Home(request):
    return render(request, 'home.html', {'show_navigation': True})
