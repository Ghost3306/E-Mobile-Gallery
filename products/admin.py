from django.contrib import admin

# Register your models here.
from products.models import Category,CellularNetwork,OSDetails,Color,RamRom,Brand,Display,Connectivity,FrontCamera,RearCamera,CameraFeatures,CPUSpecs,BatteryDetails,InTheBox,AdditionalDetails,PhoneImages,PhoneList


class PhoneImagesAdmin(admin.StackedInline):
    model = PhoneImages

class PhoneAdmin(admin.ModelAdmin):
    inlines = [PhoneImagesAdmin]

@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    model=Display

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model=Category

@admin.register(CellularNetwork)
class CellularAdmin(admin.ModelAdmin):
    model=CellularNetwork

@admin.register(OSDetails)
class OSAdmin(admin.ModelAdmin):
    model=OSDetails


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    model=Color

@admin.register(RamRom)
class RamRomAdmin(admin.ModelAdmin):
    model=RamRom

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model=Brand


@admin.register(Connectivity)
class ConnectivityAdmin(admin.ModelAdmin):
    model=Connectivity

@admin.register(FrontCamera)
class FrontCameraAdmin(admin.ModelAdmin):
    model=FrontCamera

@admin.register(RearCamera)
class RearCameraAdmin(admin.ModelAdmin):
    model=RearCamera

@admin.register(CameraFeatures)
class CameraFeaturesAdmin(admin.ModelAdmin):
    model=CameraFeatures


@admin.register(CPUSpecs)
class CPUSpecsAdmin(admin.ModelAdmin):
    model=CPUSpecs

@admin.register(BatteryDetails)
class BatteryAdmin(admin.ModelAdmin):
    model=BatteryDetails

@admin.register(InTheBox)
class IntheboxAdmin(admin.ModelAdmin):
    model=InTheBox

@admin.register(AdditionalDetails)
class AdditionalsAdmin(admin.ModelAdmin):
    model=AdditionalDetails
    
admin.site.register(PhoneList,PhoneAdmin)