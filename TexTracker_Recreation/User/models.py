from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    Admin = 1
    Employee = 2
    Client = 3

    ROLE_CHOICES = (
        (Admin, 'Admin'),
        (Employee, 'Employee'),
        (Client, 'Client'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class CustomUser(AbstractUser):
    '''
    Customized user class
    '''
    email = models.EmailField()
    roles = models.ManyToManyField(Role)


class CustomUserProfile(models.Model):
    '''
    A Model For User profile,
    It Contains all common atributes which are related to user
    '''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    current_role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    profilePic = models.ImageField(default='default.png', upload_to='profilePics/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
