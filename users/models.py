from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.avatar.path) 


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()
            
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2) # Usar DecimalField é a melhor prática para dinheiro
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - R$ {self.value}'

    # Propriedade para classificar facilmente como entrada ou saída
    @property
    def is_income(self):
        return self.value > 0

    @property
    def is_expense(self):
        return self.value < 0
