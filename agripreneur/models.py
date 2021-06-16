from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
ProductCategory=[('Vegetables','Vegetables'),
('Chicken','Chicken'),
('Chilli','Chilli'),
('Rabbit','Rabbit'),
('Spices','Spices'),
('Farm Animals','Farm Animals'),
('None','None')
]
volume=[('Small Scale','Small Scale'),
('Large Scale', 'Large Scale'),
('Export Volume','Export Volume'),
('None', 'None')
]

Category =[
    ('Consumer','Consumer'),
    ('Farmer','Farmer'),
    ('Small Scale Trader', 'Small Scale Trader'),
    ('Large Scale Trader', 'Large Scale Trader'),
    ('Exporter','Exporter')
]
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,blank=True)
    location = models.CharField(max_length=20)
    category = models.CharField(max_length=50,choices=Category,default='Consumer')
    product_category = models.CharField(max_length=50,choices=ProductCategory,default='Vegetables')
    product_volume = models.CharField(max_length=50,choices=volume,default='Small Scale')

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, created=False, **kwargs):
      instance.profile.save()

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class AgriInfo(models.Model):
    name = models.CharField(max_length=50)
    produce_category = models.CharField
    author=models.CharField(max_length=20,null=True,default='unknown')
    resource=models.CharField(max_length=50,null=True,default='unknown')

    def __str__(self):
        return self.name

    def save_agri_info(self):
        self.save()

    def delete_agri_info(self):
        self.delete()

    @classmethod
    def find_agri_info(cls, name):
        return cls.objects.filter(name_icontains=name)

    @classmethod
    def update_agri_info(cls, id, name):
        update = cls.objects.filter(id=id).update(name=name)
        return update

class Market(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField
    seller=models.CharField
    contact_seller=models.CharField
    price_range=models.IntegerField

    def __str__(self):
        return self.name

    def save_market(self):
        self.save()

    def delete_product_category(self):
        self.delete()

    @classmethod
    def find_product_category(cls, name):
        return cls.objects.filter(name_icontains=name)

    @classmethod
    def update_product_category(cls, id, name):
        update = cls.objects.filter(id=id).update(name=name)
        return update