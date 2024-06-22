from django.contrib import admin

# Register your models here.
from products.models import Category,CameraDetails,CellularNetwork,OSDetails,RamRom,Brand,Display,Connectivity,CameraFeatures,CPUSpecs,BatteryDetails,InTheBox,PhoneImages,PhoneList,Cart


class PhoneImagesAdmin(admin.StackedInline):
    model = PhoneImages

class PhoneCameraAdmin(admin.StackedInline):
    model = CameraDetails

class PhoneAdmin(admin.ModelAdmin):
    inlines = [PhoneImagesAdmin,PhoneCameraAdmin]




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



@admin.register(RamRom)
class RamRomAdmin(admin.ModelAdmin):
    model=RamRom

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model=Brand


@admin.register(Connectivity)
class ConnectivityAdmin(admin.ModelAdmin):
    model=Connectivity



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


@admin.register(Cart)
class IntheboxAdmin(admin.ModelAdmin):
    model=Cart
    
admin.site.register(PhoneList,PhoneAdmin)
