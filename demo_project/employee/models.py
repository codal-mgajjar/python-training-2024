from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def delete_employee(self):
        # Delete profile photo if it exists
        if self.profile_photo:
            storage, path = self.profile_photo.storage, self.profile_photo.path
            storage.delete(path)
        # Delete the employee instance
        self.delete()
