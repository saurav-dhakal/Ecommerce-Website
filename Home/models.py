from django.db import models

# Create your models here.

class Folder(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_cat = models.CharField(max_length=50,default="FOLDER")
    product_name= models.CharField(max_length=50)
    pd1 = models.TextField(max_length=100,default='It is made using high quality PU leather.')
    pd2 = models.TextField(max_length=100,default='Paper size is bigger than A4, used to safely keep documents of almost all size.')
    pd3 = models.TextField(max_length=100,default='Chain zipper is given to secure everything inside the folder.')
    pd4 = models.TextField(max_length=100,default='It is waterproof.')
    pd5 = models.TextField(max_length=100,default='Many compartments to organize documents, cards, id ,pen and many more...')


    main_image= models.ImageField(upload_to="Home/images/folder", default="")
    back_image= models.ImageField(upload_to="Home/images/folder", default="")
    inner_image=models.ImageField(upload_to="Home/images/folder", default="")
    price = models.IntegerField(default=0)
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    

# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_cat = models.CharField(max_length=50,default="FOLDER")
#     product_name= models.CharField(max_length=50)
#     image= models.ImageField(upload_to="Home/images/product", default="")

#     def __str__(self):
#         return self.product_name
    
size = (
    ('Small','Small'),
    ('Medium','Medium'),
    ('Large','Large'),
    ('xL','xL'),
    ('XXL','XXL'),
    ('B4 size','B4 size'),
    ('A4 size','A4 size')
)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50,default="")
    size=models.CharField( max_length=50, choices=size, default='')
    color= models.CharField( max_length=50, default='')
    quantity=models.IntegerField(default=0)
    addinfo=models.CharField(max_length=500,default="#")
    name=models.CharField(max_length=12,default=0)
    contact=models.CharField(max_length=12,default=0)
    location=models.CharField(max_length=250,default=0)
    image=models.ImageField(upload_to="order",default="")

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Folder, models.CASCADE)
    customer_name=models.CharField(max_length=50,default="")
    comment = models.CharField(max_length=250,default="")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
class Message(models.Model):
    message_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default='')
    email=models.EmailField(max_length=50,default='')
    message=models.CharField(max_length=250,default='')

    def __str__(self):
        return self.name
