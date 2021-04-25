from django.db import models
class Userreg(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.IntegerField()
class Category(models.Model):
    ctype = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
class Subcategory(models.Model):
    cate = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)
class Design(models.Model):
    ddesign = models.CharField(max_length=30)
    subdesign = models.CharField(max_length=30)
    proname = models.CharField(max_length=30)
    prodis = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    shipping = models.CharField(max_length=30)
    photo = models.FileField()
    photo1 = models.FileField()
    photo2 = models.FileField()
    poc=models.CharField(max_length=30)
class Craftcategory(models.Model):
    crafttype = models.CharField(max_length=30)
    craftdescription = models.CharField(max_length=30)
class Craftsubcategory(models.Model):
    craftstype = models.CharField(max_length=30)
    craftsubtype = models.CharField(max_length=30)
class Craft(models.Model):
    craft = models.CharField(max_length=30)
    subcraft = models.CharField(max_length=30)
    craftname = models.CharField(max_length=30)
    craftdis = models.CharField(max_length=30)
    cprice = models.CharField(max_length=30)
    cshipping = models.CharField(max_length=30)
    cphoto = models.FileField()
    cphoto1 = models.FileField()
    cphoto2 = models.FileField()
    cpoc=models.CharField(max_length=30)
class Designcart(models.Model):
    did=models.ForeignKey(Design,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    qty = models.IntegerField()
    size=models.CharField(max_length=30)
    gtotal = models.IntegerField()
    status = models.IntegerField()
class Craftcart(models.Model):
        cid = models.ForeignKey(Craft, on_delete=models.CASCADE)
        user = models.CharField(max_length=30)
        qty = models.IntegerField()
        gtotal = models.IntegerField()
        status = models.IntegerField()




