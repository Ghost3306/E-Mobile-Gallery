from django.shortcuts import redirect, render
from products.models import PhoneList
from django.contrib import messages
from products.models import Cart,Address,PlacedOrders
from django.views.decorators.csrf import csrf_exempt


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
              
                phoneobj = PhoneList.objects.get(slug=slug)
                pobj = phoneobj.ram_rom.all()
                price_add_ = 0

               
                for x in pobj: 
                    
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
    phone = PhoneList.objects.get(slug=slug)
    ret = '/phone/'+slug
    if not color:
        messages.error(request, 'Please select phone specifications!')
        return redirect(ret)
    
    if not ram and not rom:
        messages.error(request, 'Please select phone specifications!')
        return redirect(ret)

    colors = phone.phone_images.filter(color=color)
    storage = phone.ram_rom.filter(ram_size=int(ram),rom_size=int(rom))
    if len(colors)==0 or len(storage)==0:
        messages.success(request, 'Invalid Order')
        return redirect(ret)

    user = request.user
    cart = Cart(user=user,phone=phone,color=color,ram=int(ram),rom=int(rom),quantity=int(quntity),status='incart')
    cart.save()
    messages.success(request, 'Order Placed Successfull')
    return redirect(ret)


def buynow(request,slug):
    color = request.GET.get('color')
    ram = request.GET.get('ram')
    rom = request.GET.get('rom')
    quntity = request.GET.get('quntity')
    phone = PhoneList.objects.get(slug=slug)
    ret = '/phone/'+slug+f"?ram={ram}&rom={rom}&color={color}"
    if not color:
        messages.error(request, 'Please select phone specifications!')
        return redirect('/phone/'+slug)
    
    if not ram and not rom:
        messages.error(request, 'Please select phone specifications!')
        return redirect('/phone/'+slug)
    
    phone = PhoneList.objects.get(slug=slug)
    colors = phone.phone_images.filter(color=color)
    storage = phone.ram_rom.filter(ram_size=int(ram),rom_size=int(rom))
    if len(colors)==0 or len(storage)==0:
        messages.success(request, 'Invalid Order')
        return redirect('/phone/'+slug)
    colors = phone.phone_images.filter(color=color).first()
    stor_pri = phone.ram_rom.filter(ram_size=int(ram),rom_size=int(rom)).first()
    t_price = phone.original_price+colors.price_to_add+stor_pri.price_to_add
    total_price = t_price*int(quntity)
    


    context = {
        'phone':phone,
        'phone_images':colors,
        'color':color,
        'ram':ram,
        'rom':rom,
        'quntity':quntity,
        'total_price':total_price,
        'actual_price':t_price
    }

    if request.method == 'POST':
        name = request.POST.get('full_name')
        phone_number = request.POST.get('mobile')
        street = request.POST.get('street')
        locality = request.POST.get('locality')
        village_city = request.POST.get('village_city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        # print(name)
        user = request.user
        # print('after inset',total_price)
        # print(user.username)
        if 'cod' in request.POST:
            cart = Cart.objects.create(user=user,phone=phone,color=color,ram=int(ram),rom=int(rom),quantity=int(quntity),status='buynow')
            address = Address.objects.create(name=name,phone=phone_number,street=street,locality=locality,village_city=village_city,taluka=taluka,district=district,state=state,pincode=pincode)
            place_order = PlacedOrders(user=user,address=address,cart=cart)
            place_order.save()
            print('cash on delivery saved')
            return redirect('/')
      

    return render(request,'phones/buynow.html',context)


def buyfromcart(request):
    user = request.user
    cart = Cart.objects.filter(user=user,status="incart")
    carts = []
    total_price = 0
    for c in cart:
        images = c.phone.phone_images.filter(color=c.color).first()
        carts.append({
            'cart':c,
        'phone_image':images
            })
        storage = c.phone.ram_rom.get(ram_size=c.ram,rom_size=c.rom)
        t=c.phone.original_price+images.price_to_add+storage.price_to_add
        total_price+=t*c.quantity
    if request.method == 'POST':
        name = request.POST.get('full_name')
        phone_number = request.POST.get('mobile')
        street = request.POST.get('street')
        locality = request.POST.get('locality')
        village_city = request.POST.get('village_city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        user = request.user
        if 'cod' in request.POST:
            cart = Cart.objects.filter(user=user,status="incart")
            address = Address.objects.create(name=name,phone=phone_number,street=street,locality=locality,village_city=village_city,taluka=taluka,district=district,state=state,pincode=pincode)
            for c in cart:
                place_order = PlacedOrders(user=user,address=address,cart=c)
                place_order.save()
                cd = Cart.objects.get(uid=c.uid)
                cd.status='buy'
                cd.save()
                print('order saved')
                
            
            print('cash on delivery saved')
            return redirect('/')
        
    context = {
        'carts':carts,
        'num_items':len(cart),
        'total_price':total_price
    }

    return render(request,'phones/buyfromcart.html',context)


def yourorders(request):
    user = request.user
    
    return render(request,'sidebar/yourorders.html')

def yourcart(request):
    user = request.user
    try:
        cart = Cart.objects.filter(user=user,status="incart")
    
        carts = []
        total_price = 0
        for c in cart:
            images = c.phone.phone_images.filter(color=c.color).first()
            carts.append({
                'cart':c,
                'phone_image':images
            })
            storage = c.phone.ram_rom.get(ram_size=c.ram,rom_size=c.rom)
            t=c.phone.original_price+images.price_to_add+storage.price_to_add
            total_price+=t*c.quantity
        print("total amount: ",total_price)

            
        
        context = {
            'carts':carts,
            'num_items':len(cart),
            'total_price':total_price
        }
        return render(request,'sidebar/yourcart.html',context)
    except Exception as e:
        print(e)
        return redirect('/')
    
    
    
def deletecart(request,uid):
    cart = Cart.objects.get(uid=uid)
    cart.delete()
    return redirect('/phone/cart/')

def savelater(request,uid):
    cart = Cart.objects.get(uid=uid)
    cart.status='savelater'
    cart.save()
    return redirect('/phone/cart/')



def yoursavelater(request):
    user = request.user
    
    return render(request,'sidebar/yoursavelater.html')