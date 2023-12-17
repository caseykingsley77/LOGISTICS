from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, PackageLocation
import uuid

def package_info(request):
    if request.method == 'POST':
        code = request.POST.get('code_input')

        try:
            package = Package.objects.get(code=code)
            return render(request, 'package_info.html', {'package': package})
        except Package.DoesNotExist:
            error_message = "Code not found in the database"
            return render(request, 'input_form.html', {'error_message': error_message})

    return render(request, 'input_form.html')

def update_package_location(request, package_id):
    if request.method == 'POST':
        location = request.POST.get('location')
        package = get_object_or_404(Package, pk=package_id)
        PackageLocation.objects.create(package=package, location=location)
        return render(request, 'location_updated.html', {'package': package})

    return render(request, 'update_location.html')


def package_timeline(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    locations = package.locations.order_by('timestamp')  # Assuming 'locations' is the related name in Package model

    return render(request, 'package_timeline.html', {'package': package, 'locations': locations})

def generate_package_code(request):
    if request.method == 'POST':
        new_package = Package.objects.create(code=uuid.uuid4())  # Generate a UUID as the package code
        new_package.save()
        return redirect('package_detail', package_id=new_package.id)

    return render(request, 'generate_package_code.html')

def package_detail(request, package_id):
    package = Package.objects.get(pk=package_id)
    return render(request, 'package_detail.html', {'package': package})