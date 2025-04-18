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

def AdminDashboard(request):
    return render(request, 'admin_dashboard.html', {'show_navigation': True})

def Login(request):
    return render(request, 'login.html', {'show_navigation': True})

def Register(request):
    return render(request, 'register.html', {'show_navigation': True})

def SuperAdminDashboard(request):
    return render(request, 'superadmin_dashboard.html', {'show_navigation': True})
