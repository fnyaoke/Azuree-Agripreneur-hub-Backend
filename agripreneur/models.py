from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,blank=True)
    location = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()


class Farmer(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField
    product = models.CharField(max_length=20)
    address = models.CharField
    production_quantity = models.AutoField

    def __str__(self):
        return self.name

    def save_farmer(self):
        self.save()

    def delete_farmer(self):
        self.delete()

    @classmethod
    def find_farmer(cls, name):
        return cls.objects.filter(name_icontains=name)

    @classmethod
    def update_farmer(cls, id, name):
        update = cls.objects.filter(id=id).update(name=name)
        return update


class AgriInfo(models.Model):
    name = models.CharField
    product=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    resource=models.CharField
    location=models.AutoField

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

class ProductCategory(models.Model):
    name = models.AutoField
    location = models.CharField
    price_range=models.IntegerField

    def __str__(self):
        return self.name

    def save_product_category(self):
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