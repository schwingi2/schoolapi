from django.db import models

# Create your models here.

from django.db import models
import uuid


class Sitznachbar(models.Model):
    """
    Model for storing Sitznachbars.
    """
    pers_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    rec_time = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey('auth.User', related_name='User', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='Sitznachbar', on_delete=models.CASCADE)
   # owner = models.ForeignKey('auth.User', related_name='Sitznachbar_user', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-rec_time']

    def __str__(self):
        return self.last_name
    
    def save(self, *args, **kwargs):
        """ 
        Use the `pygments` library to create a highlighted HTML
        representation of the Sitznachbar.
        """
        super().save(*args, **kwargs)

