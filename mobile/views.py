from django.shortcuts import render,redirect
from .models import Product,Order,Carts
from .forms import CreateProductForm
from .forms import UserRegistrationForm,LoginForm,OrderForm,CartForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,admin_only



# Create your views here.
def base(request):
    return render(request,"mobile/base.html")



#LIST
@login_required
def list_mobiles(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

#CREATE

@admin_only
def add_product(request):
    form=CreateProductForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("base")
    return render(request,"mobile/createmobile.html",context)


#VIEW Details of Mobile
def get_mobile_object(id):
    return Product.objects.get(id=id)
@login_required
def mobile_detail(request,id):
    mobile=get_mobile_object(id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)

#DELETE

@admin_only
def mobile_delete(request,id):
    mobile = get_mobile_object(id)
    mobile.delete()
    return redirect("base")

#UPDATE

@admin_only
def update(request,id):
    mobile = get_mobile_object(id)
    context = {}
    form=CreateProductForm(instance=mobile)
    context["form"]=form
    if request.method=="POST":
        form=CreateProductForm(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("base")
    return render(request,"mobile/modileupdate.html",context)


#REGISTRATION
def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
    return render(request,"mobile/registration.html",context)


#LOGIN
def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"mobile/base.html")
    return render(request,"mobile/login.html",context)

#LOGOUT
def signout(request):
    logout(request)
    return redirect("userlogin")

#ORDER
@login_required
def item_order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base")
        else:
            context["form"]=form
            return render(request, "mobile/ordereditem.html", context)
    return render(request,"mobile/ordereditem.html",context)


#MY ORDERS
@login_required
def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)

#CANCEL ORDER
@login_required
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status='cancelled'
    order.save()
    return redirect("vieworder")


#ADD TO CART
@login_required
def add_to_cart(request,id):
    product = get_mobile_object(id)
    form = CartForm(initial={'user': request.user, 'product': product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"] = form
            return render(request, "mobile/mobiledetail.html", context)
    return render(request, "mobile/cartitem.html", context)


#VIEW CART
@login_required
def view_cart(request):
    cart_items=Carts.objects.filter(user=request.user)
    context={}
    context["cart_items"]=cart_items
    return render(request,"mobile/viewcart.html",context)


#REMOVE FROM CART
@login_required
def remove_cart_item(request,id):
    carts = Carts.objects.get(id=id)
    carts.delete()
    return redirect("viewcart")


# BUY FROM CART
def cart_order(request,id):
    carts=Carts.objects.get(id=id)
    form=OrderForm(initial={'user':request.user,'product':carts.product})
    context={}
    context['form']=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            remove_cart_item(request,id)
            return redirect("viewcart")
        else:
            context["form"]=form
            return render(request,"mobile/ordereditem.html",context)
    return render(request, "mobile/ordereditem.html", context)