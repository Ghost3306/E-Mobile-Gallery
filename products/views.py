from django.shortcuts import render
from products.models import PhoneList

# Create your views here.
def get_product(request,slug):
    
    try:    
        phoneobj = PhoneList.objects.get(slug=slug)
        c = phoneobj.phone_images
       
        colors = phoneobj.phone_images.order_by('color').values_list('color', flat=True).distinct()
        context = {
            'phoneobj':phoneobj,
            'colors': colors

            }
        return render(request,'phones/mainphone.html',context)
    except Exception as e:
        print(e)
        return render(request,'phones/mainphone.html')