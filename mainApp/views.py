from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    if (request.method == "POST"):
        msg = request.POST.get('message')
        ata = AttaChakki.objects.filter(Q(name__icontains=msg))
        ac = AirCooler.objects.filter(Q(name__icontains=msg))
        ref = Refrigerator.objects.filter(Q(name__icontains=msg))
        tv = Tv.objects.filter(Q(name__icontains=msg))
        ht = HomeTheater.objects.filter(Q(name__icontains=msg))
        tt = TowerTheater.objects.filter(Q(name__icontains=msg))
        jm = JuicerMixer.objects.filter(Q(name__icontains=msg))
        jmg = JuicerMixerGrinder.objects.filter(Q(name__icontains=msg))
        hp = HotPlate.objects.filter(Q(name__icontains=msg))
        i = Iron.objects.filter(Q(name__icontains=msg))
        return render(request, "shop.html", {"Product": ata,
                                             "Product2": ac,
                                             "Product3": ref,
                                             "Product4": tv,
                                             "Product5": ht,
                                             "Product6": tt,
                                             "Product7": jm,
                                             "Product8": jmg,
                                             "Product9": hp,
                                             "Product10": i,
                                             })
    return render(request,"index.html")
# Create your views here.

def error404(request):
    return render(request,"404.html")


def contact(request):
    if (request.method == "POST"):
        c = Query()
        c.fname = request.POST.get('fname')
        c.lname = request.POST.get('lname')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.msg = request.POST.get('message')
        c.save()
        messages.success(request, "Message Sent")
        return HttpResponseRedirect('/contact/')
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def career(request):
    if (request.method == "POST"):
        c = Career()
        c.fname = request.POST.get('fname')
        c.lname = request.POST.get('lname')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.msg = request.POST.get('message')
        c.save()
        messages.success(request, "Form Submitted")
        return HttpResponseRedirect('/career/')
    return render(request,"career.html")


def aboutus(request):
    return render(request,"about.html")

def comingsoon(request):
    return render(request,"coming-soon.html")

def loginDetails(request):
    if(request.method=="POST"):
        uname=request.POST.get('uname')
        pward=request.POST.get('password')
        user=auth.authenticate(username=uname,password=pward)
        if(user is not None):
            auth.login(request,user)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,"Invalid UserName or Password")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def signupUser(request):
    if (request.method == "POST"):
        b=Buyer()
        b.name = request.POST.get('name')
        b.uname = request.POST.get('username')
        b.email = request.POST.get('email')
        pward = request.POST.get('password')
        try:
            user=User.objects.create_user(username=b.uname,
                                          email=b.email,
                                          password=pward)
            b.save()
            messages.success(request,"Account created successfully!!  LOGIN PLEASE")
            return HttpResponseRedirect('/login/')
        except:
            messages.error(request,"UserName Already Taken / Email Exists")
    return render(request,"signin.html")


@login_required(login_url='/login/')
def profile(request):
    user=User.objects.get(username=request.user)

    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        b = Buyer.objects.get(uname=request.user)
        u = User.objects.get(username=request.user)
        if (request.method == "POST"):
            u.email=request.POST.get('email')
            b.name = request.POST.get('name')
            b.email = request.POST.get('email')
            b.phone = request.POST.get('phone')
            b.address1 = request.POST.get('address1')
            b.address2 = request.POST.get('address2')
            b.city = request.POST.get('city')
            b.state = request.POST.get('state')
            b.pin = request.POST.get('pin')
            u.save()
            b.save()
            return HttpResponseRedirect('/profile/')
        return render(request, "profile-details.html", {"User": b})



def shopDetails(request,cat):
    if(cat=="AUDIO"):
        ht=HomeTheater.objects.all()
        th = TowerTheater.objects.all()
        return render(request, "shop.html",{
                        "Product":ht,
                        "Product2":th,})
    elif(cat=="TV"):
        p=Tv.objects.all()
    elif(cat=="LARGE APPLIANCES"):
        acr = AirCooler.objects.all()
        r = Refrigerator.objects.all()
        ''' wm=WashingMachine.objects.all()
            f=Fan.objects.all()'''
        return render(request, "shop.html", {

            "Product": acr,
            "Product2": r,
                            })
    elif(cat=="KITCHEN"):
        ac = AttaChakki.objects.all()
        jm = JuicerMixer.objects.all()
        jmg = JuicerMixerGrinder.objects.all()
        hp = HotPlate.objects.all()
        return render(request, "shop.html", {

            "Product": ac,
            "Product2": jm,
            "Product3": jmg,
            "Product4": hp,
                            })
    elif(cat=="ELECTRICAL APPLIANCES"):
        p = Iron.objects.all()
        '''f = Fan.objects.all() '''
        return render(request, "shop.html", {
            "Product": p})
    elif(cat=="OLED TV"):
        p=Tv.objects.filter(subcategory=cat)
    elif(cat=="NANOCELL TV"):
        p=Tv.objects.filter(subcategory=cat)
    elif(cat=="UHD 4K TV"):
        p=Tv.objects.filter(subcategory=cat)
    elif(cat=="SMART TV"):
        p=Tv.objects.filter(subcategory=cat)
    elif(cat=="LED TV"):
        p=Tv.objects.filter(subcategory=cat)
    elif(cat=="IRON"):
        p=Iron.objects.all()
    elif(cat=="HOME THEATER"):
        p=HomeTheater.objects.all()
    elif(cat=="TOWER THEATER"):
        p=TowerTheater.objects.all()
    elif(cat=="FAN"):
        return HttpResponseRedirect('/comingsoon/')
        ''' p=Fan.objects.all() '''
    elif(cat=="AIR CONDITIONER"):
        return HttpResponseRedirect('/comingsoon/')
        ''' p=AirConditioner.objects.all() '''
    elif(cat=="AIR COOLER"):
      p=AirCooler.objects.all()
    elif(cat=="REFRIGERATOR"):
      p=Refrigerator.objects.all()
    elif(cat=="WASHING MACHINES"):
        return HttpResponseRedirect('/comingsoon/')
        ''' p=WashingMachine.objects.all() '''
    elif(cat=="ATTA CHAKKI"):
      p=AttaChakki.objects.all()
    elif(cat=="JUICER MIXER"):
      p=JuicerMixer.objects.all()
    elif(cat=="JUICER MIXER GRINDER"):
      p=JuicerMixerGrinder.objects.all()
    elif(cat=="HOT PLATE"):
      p=HotPlate.objects.all()
    else:
        pass
    return render(request, "shop.html",{

                        "Product":p})




def productDetails(request,scat,num):
    if(scat=="IRON"):
        p=Iron.objects.get(id=num)
    elif(scat=="REFRIGERATOR"):
        p=Refrigerator.objects.get(id=num)
    elif(scat=="TV"):
        p=Tv.objects.get(id=num)
    elif(scat=="HOT PLATE"):
        p=HotPlate.objects.get(id=num)
    elif(scat=="JUICER MIXER"):
        p=JuicerMixer.objects.get(id=num)
    elif(scat=="JUICER MIXER GRINDER"):
        p=JuicerMixerGrinder.objects.get(id=num)
    elif(scat=="HOME THEATER"):
        p=HomeTheater.objects.get(id=num)
    elif(scat=="TOWER THEATER"):
        p=TowerTheater.objects.get(id=num)
    elif(scat=="AIR COOLER"):
        p=AirCooler.objects.get(id=num)
    elif(scat=="ATTA CHAKKI"):
        p=AttaChakki.objects.get(id=num)
    elif(scat=="OLED TV"):
        p=Tv.objects.get(id=num)

    if (request.method == "POST"):
        try:
            c = Cart()
            b = Buyer.objects.get(uname=request.user)
            c.buyer = b
            c.quantity = int(request.POST.get('q'))
            if (scat == "IRON"):
                c.iron = Iron.objects.get(id=num)
                c.total = c.iron.finalPrice * c.quantity
            elif (scat == "REFRIGERATOR"):
                c.refrigerator = Refrigerator.objects.get(id=num)
                c.total = c.refrigerator.finalPrice * c.quantity
            elif (scat == "TV"):
                c.tv = Tv.objects.get(id=num)
                c.total = c.tv.finalPrice * c.quantity
            elif (scat == "HOT PLATE"):
                c.hotplate = HotPlate.objects.get(id=num)
                c.total = c.hotplate.finalPrice * c.quantity
            elif (scat == "JUICER MIXER"):
                c.juicerMixer = JuicerMixer.objects.get(id=num)
                c.total = c.juicerMixer.finalPrice * c.quantity
            elif (scat == "JUICER MIXER GRINDER"):
                c.juicerMixerGrinder = JuicerMixerGrinder.objects.get(id=num)
                c.total = c.juicerMixerGrinder.finalPrice * c.quantity
            elif (scat == "HOME THEATER"):
                c.homeTheater = HomeTheater.objects.get(id=num)
                c.total = c.homeTheater.finalPrice * c.quantity
            elif (scat == "TOWER THEATER"):
                c.towerTheater = TowerTheater.objects.get(id=num)
                c.total = c.towerTheater.finalPrice * c.quantity
            elif (scat == "AIR COOLER"):
                c.airCooler = AirCooler.objects.get(id=num)
                c.total = c.airCooler.finalPrice * c.quantity
            elif (scat == "ATTA CHAKKI"):
                c.attaChakki = AttaChakki.objects.get(id=num)
                c.total = c.attaChakki.finalPrice * c.quantity
            elif (scat == "OLED TV"):
                c.tv = Tv.objects.get(id=num)
                c.total = c.tv.finalPrice * c.quantity

            c.save()
            return HttpResponseRedirect('/cart/')
        except:
            return HttpResponseRedirect('/login/')

    return render(request, "product-single.html",
                  {
                      "Product":p,
                  })

@login_required(login_url='/login/')
def wishlistDetails(request,scat,num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')

    user = Buyer.objects.get(uname=request.user)
    w=Wishlist()
    if (scat == "IRON"):
        w.iron = Iron.objects.get(id=num)
    elif (scat == "REFRIGERATOR"):
        w.refrigerator = Refrigerator.objects.get(id=num)
    elif (scat == "TV"):
        w.tv = Tv.objects.get(id=num)
    elif (scat == "HOT PLATE"):
        w.hotplate = HotPlate.objects.get(id=num)
    elif (scat == "JUICER MIXER"):
        w.juicerMixer = JuicerMixer.objects.get(id=num)
    elif (scat == "JUICER MIXER GRINDER"):
        w.juicerMixerGrinder = JuicerMixerGrinder.objects.get(id=num)
    elif (scat == "HOME THEATER"):
        w.homeTheater = HomeTheater.objects.get(id=num)
    elif (scat == "TOWER THEATER"):
        w.towerTheater = TowerTheater.objects.get(id=num)
    elif (scat == "AIR COOLER"):
        w.airCooler = AirCooler.objects.get(id=num)
    elif (scat == "ATTA CHAKKI"):
        w.attaChakki = AttaChakki.objects.get(id=num)
    elif (scat == "OLED TV"):
        w.tv = Tv.objects.get(id=num)
    w.user=user
    w.save()
    return HttpResponseRedirect('/wishlist/')

@login_required(login_url='/login/')
def wishlist(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')

    user = Buyer.objects.get(uname=request.user)
    wish = Wishlist.objects.filter(user=user)
    return render(request,"wishlist.html",{
                             "Wish":wish,})

@login_required(login_url='/login/')
def wishlistDelete(request,num):
    wish=Wishlist.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlist/')


@login_required(login_url='/login/')
def cartDetails(request):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')

    b=Buyer.objects.get(uname=request.user)
    cart=Cart.objects.filter(buyer=b)
    subtotal=0
    for i in cart:
        subtotal+=i.total
    if(subtotal<70000):
        delivery=2500
    else:
        delivery=0
    finalAmount=subtotal+delivery
    return render(request, "cart.html",{
                            "Cart":cart,
                            "Sub":subtotal,
                            "Delivery":delivery,
                            "Final":finalAmount})


@login_required(login_url='/login/')
def deletecart(request,num):
    cart=Cart.objects.get(id=num)
    cart.delete()
    return HttpResponseRedirect('/cart/')