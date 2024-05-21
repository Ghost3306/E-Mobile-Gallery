from django.db import models
from base.models import BaseModel
from django.utils.text import slugify



class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_image = models.ImageField(upload_to='categories')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self) ->str:
        return self.category_name

class CellularNetwork(BaseModel):
    network_type = models.CharField(max_length=10)
    
    def __str__(self)->str:
        return self.network_type

class OSDetails(BaseModel):
    os_name = models.CharField(max_length=25)   
    os_version = models.FloatField()
    
    def __str__(self)->str:
        return self.os_name


class Color(BaseModel):
    color_name = models.CharField(max_length=25)

    def __str__(self) ->str:
        return self.color_name
    
class RamRom(BaseModel):
    ram_size = models.IntegerField()
    rom_size = models.IntegerField()

    def __str__(self) ->str:
        return str(self.ram_size)+'+'+str(self.rom_size)
    
class Brand(BaseModel):
    brand_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True,null=True)
    brand_logo = models.ImageField(upload_to='brands')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.brand_name)
        super(Brand,self).save(*args,**kwargs)
    
    def __str__(self)->str:
        return self.brand_name
    
class Display(BaseModel):
    display_name = models.CharField(max_length=20)
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    display_size = models.FloatField()
    pixel_per_inch = models.IntegerField()
    hz = models.IntegerField()
    touch_response = models.IntegerField()
    color_depth = models.CharField(max_length=20)
    brightness = models.IntegerField()

    def __str__(self) ->str:
        return self.display_name

class Connectivity(BaseModel):
    connectivity_name = models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.connectivity_name

class FrontCamera(BaseModel):
    front_camera_name = models.CharField(max_length=50,default='standard')
    front_camera_mp = models.IntegerField()

    def __str__(self) ->str:
        return self.front_camera_name

class CameraFeatures(BaseModel):
    feature = models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.feature


class RearCamera(BaseModel):
    rear_primary_camera_name = models.CharField(max_length=50,default='standard')
    rear_primary_camera_mp = models.IntegerField()
    rear_macro_camera_name = models.CharField(max_length=50,null=True,blank=True)
    rear_macro_camera_mp = models.IntegerField(null=True,blank=True)
    rear_telephoto_camera_name = models.CharField(max_length=50,null=True,blank=True)
    rear_telephoto_camera_mp = models.IntegerField(null=True,blank=True)
    rear_ultrawide_camera_name = models.CharField(max_length=50,null=True,blank=True)
    rear_ultrawide_camera_mp = models.IntegerField(null=True,blank=True)
    flash_type = models.CharField(max_length=20)
    ois = models.BooleanField(default=False)
    eis = models.BooleanField(default=False)
    features = models.ManyToManyField(CameraFeatures,blank=True)
    
    def __str__(self) ->str:
        return self.rear_primary_camera_name
    


class CPUSpecs(BaseModel):
    cpu_name = models.CharField(max_length=50)
    cpu_speed = models.FloatField(null=True,blank=True)
    def __str__(self)->str:
        return self.cpu_name

class BatteryDetails(BaseModel):
    capacity = models.IntegerField()
    charging_speed = models.IntegerField()
    

    def __str__(self) ->str:
        return str(self.capacity)

class InTheBox(BaseModel):
    items = models.CharField(max_length=25)
    quantity = models.IntegerField()

    def __str__(self) ->str:
        return self.items

class AdditionalDetails(BaseModel):
    weight = models.FloatField()
    country_of_origin = models.CharField(max_length=25)

    def __str__(self) ->str:
        return self.country_of_origin

class PhoneList(BaseModel):
    phone_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name='category')
    cellular_net = models.ManyToManyField(CellularNetwork)
    os_details = models.ManyToManyField(OSDetails,blank=True)
    colors = models.ManyToManyField(Color)
    price = models.IntegerField()
    slug = models.SlugField(unique=True,null=True,blank=True)
    ram_rom = models.ManyToManyField(RamRom) 
    brand = models.ForeignKey(Brand,on_delete=models.DO_NOTHING,related_name='brand')
    display = models.ManyToManyField(Display)
    connectivity = models.ManyToManyField(Connectivity)
    front_camera = models.ManyToManyField(FrontCamera)
    rear_camera = models.ManyToManyField(RearCamera)
    cpu = models.ManyToManyField(CPUSpecs)
    battery = models.ManyToManyField(BatteryDetails)
    inthebox = models.ManyToManyField(InTheBox)
    additional = models.ManyToManyField(AdditionalDetails)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.phone_name)
        super(PhoneList,self).save(*args,**kwargs)

    def __str__(self) ->str:
        return self.phone_name




class PhoneImages(BaseModel):
    phone = models.ForeignKey(PhoneList,on_delete=models.CASCADE,related_name='phone_images')
    image = models.ImageField(upload_to='images')