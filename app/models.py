from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='category_images/')
#     #audio_file = models.FileField(blank=True,null=True)

#     def __str__(self):
#         return self.name

# class Subcategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='subcategory_images/')
#     #audio_file = models.FileField(blank=True,null=True,upload_to='SONG')

#     def __str__(self):
#         return self.name

# class Brand(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
#     logo = models.ImageField(upload_to='brand_logos/')

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images/')

#     def __str__(self):
#         return self.name


class Categories(models.Model):
    name = models.CharField(max_length=25)
    parent_category = models.ForeignKey('Categories',null=True, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        if self.parent_category:
            return f"{self.name}----({self.parent_category.name})"
        else:
            return f"{self.name}"


class File_store(models.Model):
    type_of = models.CharField(max_length=15,default='Image',choices=[("Image","Image"),("Music","Music"),("Notification","Notification")])
    parent_category = models.ForeignKey(Categories,null=True, on_delete=models.CASCADE,blank=True)
    File = models.FileField(upload_to="files/",blank=True,null=True)
>>>>>>> 42730824292b9cc53d66012571fc521759564095
