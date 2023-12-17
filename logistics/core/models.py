from django.db import models

class Package(models.Model):
    code = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.code

class PackageLocation(models.Model):
    package = models.ForeignKey(Package, related_name='locations', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.package.code} - {self.location} - {self.timestamp}"