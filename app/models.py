from django.db import models

# Create your models here.
class Resolutions(models.Model):
    resolution = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.resolution}"
        
class Categories(models.Model):
    type_of = models.CharField(max_length=15,default='Image',choices=[("Image","Image"),("Music","Music"),("Notification","Notification")])
    name = models.CharField(max_length=25)
    Resolution = models.ForeignKey('Resolutions',null=True, on_delete=models.CASCADE,blank=True)
    parent_category = models.ForeignKey('Categories',null=True, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        if self.parent_category:
            self.Resolution = self.parent_category.Resolution
            self.save()
            return f"{self.name}----({self.parent_category.name})"
        else:
            return f"{self.name}"


class DataStorage(models.Model):
    parent_category = models.ForeignKey(Categories,null=True, on_delete=models.CASCADE,blank=True)
    file_view = models.FileField(upload_to="files/%Y%m%d/%H%M%S/",blank=True,null=True)
    file_url = models.CharField(max_length=255,blank=True,null=True)
    Recommended = models.CharField(max_length=15,default='No',choices=[("Yes","Yes"),("No","No")])
    Resolution = models.ForeignKey('Resolutions',null=True, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        if self.parent_category:
            self.Resolution = self.parent_category.Resolution
            self.save()
        self.file_url = self.file_view.url
        self.save() 
        return f"{self.parent_category.type_of} for {self.parent_category} category" 

class Favorite(models.Model):
    image_id = models.ForeignKey(DataStorage,null=True, on_delete=models.CASCADE,blank=True)
    device_id = models.CharField(max_length=255,blank=True,null=True)