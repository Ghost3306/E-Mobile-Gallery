from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User


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
        return self.os_name +' '+ str(self.os_version)

    
class RamRom(BaseModel):
    ram_size = models.IntegerField()
    rom_size = models.IntegerField()
    price_to_add = models.IntegerField(default=0)
    def __str__(self) ->str:
        return str(self.ram_size)+'+'+str(self.rom_size) +" + "+str(self.price_to_add)
    
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
    display_name = models.CharField(max_length=60)
    resolution_x = models.IntegerField()
    resolution_y = models.IntegerField()
    display_size = models.FloatField()
    pixel_per_inch = models.IntegerField(null=True,blank=True)
    hz = models.IntegerField(null=True,blank=True)
    touch_response = models.IntegerField(null=True,blank=True)
    color_depth = models.CharField(max_length=20,null=True,blank=True)
    brightness = models.IntegerField(null=True,blank=True)

    def __str__(self) ->str:
        return self.display_name

class Connectivity(BaseModel):
    connectivity_name = models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.connectivity_name


class CameraFeatures(BaseModel):
    feature = models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.feature


class CPUSpecs(BaseModel):
    cpu_name = models.CharField(max_length=50)
    cpu_speed = models.FloatField(null=True,blank=True)
    def __str__(self)->str:
        return self.cpu_name

class BatteryDetails(BaseModel):
    capacity = models.IntegerField()
    charging_speed = models.IntegerField()
    
    def __str__(self) ->str:
        ret = str(self.capacity)+' : '+str(self.charging_speed)
        return ret

class InTheBox(BaseModel):
    items = models.CharField(max_length=25)
    quantity = models.IntegerField()

    def __str__(self) ->str:
        a = self.items + ' x '+str(self.quantity)
        return a


class PhoneList(BaseModel):
    phone_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name='category')
    cellular_net = models.ManyToManyField(CellularNetwork)
    os_details = models.OneToOneField(OSDetails,on_delete=models.DO_NOTHING,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    ram_rom = models.ManyToManyField(RamRom) 
    original_price = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.DO_NOTHING,related_name='brand')
    display = models.OneToOneField(Display,on_delete=models.DO_NOTHING,null=True)
    connectivity = models.ManyToManyField(Connectivity)
    cpu = models.OneToOneField(CPUSpecs,on_delete=models.DO_NOTHING,null=True)
    battery = models.OneToOneField(BatteryDetails,on_delete=models.DO_NOTHING,null=True)
    inthebox = models.ManyToManyField(InTheBox)
    weight = models.FloatField()
    country_of_origin = models.CharField(max_length=25)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.phone_name)
        super(PhoneList,self).save(*args,**kwargs)

    def __str__(self) ->str:
        return self.phone_name

    def get_price_by_color(self,color):
        return self.original_price +color
    
    def get_price_by_storage(self,price_add):
        return self.original_price+price_add


class CameraDetails(BaseModel):
    phone = models.ForeignKey(PhoneList,on_delete=models.CASCADE,related_name='camera')
    camera_name = models.CharField(max_length=30)
    camera_megapixel = models.IntegerField()

class PhoneImages(BaseModel):
    phone = models.ForeignKey(PhoneList,on_delete=models.CASCADE,related_name='phone_images')
    color = models.CharField(max_length=30)
    price_to_add = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')


class Cart(BaseModel):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='username_id')
    phone = models.ForeignKey(PhoneList,on_delete=models.DO_NOTHING,related_name='phonename_id')
    color = models.CharField(max_length=50)
    ram = models.IntegerField()
    rom = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self) ->str:
        ret = str(self.user.email)+'->'+str(self.phone.phone_name)
        return ret
    

class Address(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    village_city = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    
    pincode = models.CharField(max_length=100)


class PlacedOrders(BaseModel):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='place_username_id')
    address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='address')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart')
