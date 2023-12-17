from django.shortcuts import render, redirect
from core.models import Package  # Import Package model from core app

def home(request):
    return render(request, 'user/home.html')

def enter_code(request):
    if request.method == 'POST':
        code = request.POST.get('code_input')
        return redirect('user:package_timeline', code=code)
    return render(request, 'user/enter_code.html')

def package_timeline(request, code):
    package = Package.objects.get(code=code)
    locations = package.locations.order_by('timestamp')
    return render(request, 'user/package_timeline.html', {'package': package, 'locations': locations})
