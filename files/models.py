from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.user.id, '%Y/%m/%d/' , filename)

class Upload(models.Model):
    name = models.CharField(max_length=60)
    object = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1, related_name="user")

    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'