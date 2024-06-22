from django.shortcuts import redirect, render
from products.models import PhoneList
from django.contrib import messages
# Create your views here.
def get_product(request,slug):
    
    try:    
        phoneobj = PhoneList.objects.get(slug=slug)
        colors = phoneobj.phone_images.order_by('color').values_list('color', flat=True).distinct()
        context = {
            'phoneobj':phoneobj,
            'colors': colors
            }
        if request.GET.get('color') or request.GET.get('ram'):
            price = 0
            if request.GET.get('color'):
                color = request.GET.get('color')
                print(color)
                phoneobj = PhoneList.objects.get(slug=slug)
                pobj = phoneobj.phone_images.all()
                price_add = 0
                for x in pobj:
                    if x.color==color:
                        price_add = x.price_to_add
                        break
                
                phoneobj = PhoneList.objects.get(slug=slug)
                colors = phoneobj.phone_images.order_by('color').values_list('color', flat=True).distinct()
                context = {
                'phoneobj':phoneobj,
                'colors': colors
                }
                colored_images = phoneobj.phone_images.filter(color=color)
                context['updated_images'] = colored_images
                updated_price = phoneobj.get_price_by_color(price_add)
                price=updated_price
                print(f'color {color},updated : {updated_price}')
                context['selected_color']=color
                context['updated_price'] = updated_price
                
            if request.GET.get('ram'):
                ram = request.GET.get('ram')
                rom = request.GET.get('rom')
                print(ram,rom)
                phoneobj = PhoneList.objects.get(slug=slug)
                pobj = phoneobj.ram_rom.all()
                price_add_ = 0

               
                for x in pobj: 
                    print(x.ram_size,x.rom_size)
                    if str(x.ram_size) == str(ram) and str(x.rom_size)==str(rom):
                        price_add_ = x.price_to_add
                        break
                phoneobj = PhoneList.objects.get(slug=slug)
                colors = phoneobj.phone_images.order_by('color').values_list('color', flat=True).distinct()
                context = {
                'phoneobj':phoneobj,
                'colors': colors
                }
               
                if price==0:
                    updated_price = phoneobj.get_price_by_storage(price_add_)  
                else:
                    updated_price = price+price_add_
                if request.GET.get('color'):
                    print('color exist in storage')
                    colored_images = phoneobj.phone_images.filter(color=color)
                    context['updated_images'] = colored_images
                    context['selected_color']=color
                context['updated_price'] = updated_price
                context['selected_ram'] = int(ram)
                context['selected_rom'] = int(rom)


            return render(request,'phones/mainphone.html',context)
            
                
        return render(request,'phones/mainphone.html',context)
    except Exception as e:
        print(e)
        return render(request,'phones/mainphone.html')
    
def addtocart(request,slug):
    color = request.GET.get('color')
    ram = request.GET.get('ram')
    rom = request.GET.get('rom')
    quntity = request.GET.get('quntity')
    ret = '/phone/'+slug
    if not color:
        messages.error(request, 'Please select phone specifications!')
        return redirect(ret)
    
    if not ram and not rom:
        messages.error(request, 'Please select phone specifications!')
        return redirect(ret)



    return redirect(ret)