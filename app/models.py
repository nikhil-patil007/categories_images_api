from django.db import models

# Create your models here.
class Resolutions(models.Model):
    resolution = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.resolution}"
class Categories(models.Model):
    name = models.CharField(max_length=25)
    Resolution = models.ForeignKey('Resolutions',null=True, on_delete=models.CASCADE,blank=True)
    parent_category = models.ForeignKey('Categories',null=True, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        if self.parent_category:
            return f"{self.name}----({self.parent_category.name})"
        else:
            return f"{self.name}"


class File_store(models.Model):
    type_of = models.CharField(max_length=15,default='Image',choices=[("Image","Image"),("Music","Music"),("Notification","Notification")])
    parent_category = models.ForeignKey(Categories,null=True, on_delete=models.CASCADE,blank=True)
    file_view = models.FileField(upload_to="categories/files/",blank=True,null=True)
    Recommended = models.CharField(max_length=15,default='Yes',choices=[("Yes","Yes"),("No","No")])