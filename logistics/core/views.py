from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, PackageLocation
import uuid
from django.utils import timezone

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
        package = get_object_or_404(Package, pk=package_id)

        # Update status
        new_status = request.POST.get('new_status')
        package.status = new_status

        # Update location
        location = request.POST.get('location')
        PackageLocation.objects.create(package=package, location=location, timestamp=timezone.now())

        # Save the updated status
        package.save()

        # Redirect to package detail page after updating status and location
        return redirect('package_detail', package_id=package_id)

    return render(request, 'update_location.html')  # Create/update a form for status and location


def package_timeline(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    locations = package.locations.order_by('timestamp')  # Assuming 'locations' is the related name in Package model

    return render(request, 'package_timeline.html', {'package': package, 'locations': locations})

def generate_package_code(request):
    if request.method == 'POST':
        # Retrieve data from the form
        delivery_date = request.POST.get('delivery_date')
        status = request.POST.get('status')

        # Create a new package with UUID as code, delivery date, and status
        new_package = Package.objects.create(
            code=str(uuid.uuid4())[:10],
            delivery_date=delivery_date,
            status=status
        )
        new_package.save()

        # Redirect to package detail page
        return redirect('package_detail', package_id=new_package.id)

    return render(request, 'generate_package_code.html')

def package_detail(request, package_id):
    package = Package.objects.get(pk=package_id)
    return render(request, 'package_detail.html', {'package': package})