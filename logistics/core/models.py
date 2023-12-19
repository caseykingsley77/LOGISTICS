from django.db import models



class Package(models.Model):
    STATUS = (
        ('Out on Delivery', 'Out on Delivery'),
        ('Cancelled Delivery', 'Cancelled Cancelled'),
        ('Arrived for Pickup', 'Arrived for Pickup'),
        ('Successfully Delivered', 'Successfully Delivered'),
    )
    code = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    delivery_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.code

class PackageLocation(models.Model):
    package = models.ForeignKey(Package, related_name='locations', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.package.code} - {self.location} - {self.timestamp}"