from django.shortcuts import render
from .models import Userreg,Login,Category,Subcategory,Design,Craftcategory,Craftsubcategory,Craft,Designcart,Craftcart
from datetime import date
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
 try:
    m=Login.objects.get(username=request.POST['email'],password=request.POST['password'])
    if m.status == 1:
        request.session['user']=m.username
        data = Design.objects.all()
        data1 = Craft.objects.all()
        return render(request, 'uhome.html', {'f': data,'c':data1})
    elif m.status==0:
        return render(request, 'adminhome.html')
    elif m.status==5:
        return render(request, 'work.html')
    elif m.status==2:
        return render(request, 'designerhome.html')
    elif m.status==3:
        return render(request, 'crafterhome.html')
    elif m.status==6:
        return render(request, 'work.html')
    else:
        return render(request,'login.html',{'error':"didnt match"})
 except:
        return render(request,'login.html',{'error':"invalid username or password"})
def out(request):
    data=request.session['user']
    return render(request,'login.html',{'data':data})
def ureg(request):
    return render(request,'ureg.html')
def reg(request):
    fname=request.POST['fname']
    lname = request.POST['lname']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    data=Userreg(fname=fname,lname=lname,address=address,phone=phone,email=email)
    data.save()
    data1=Login(username=email,password=password,status=1)
    data1.save()
    return render(request,'login.html')
def uhome(request):
    data = Design.objects.all()
    return render(request, 'uhome.html', {'s': data})
def viewprofile(request):
    user=request.session['user']
    data=Userreg.objects.filter(email=user)
    return render(request,'viewprofile.html',{'data':data})
def adminhome(request):
    return render(request,'adminhome.html')
def pending(request):
    return render(request,'pending.html')
def designerhome(request):
    return render(request,'designerhome.html')
def crafterhome(request):
    return render(request,'crafterhome.html')
def show(request):
    return render(request,'show.html')
def category(request):
    return render(request,'category.html')
def cate(request):
    ctype = request.POST['ctype']
    description = request.POST['description']
    data2 = Category(ctype=ctype, description=description)
    data2.save()
    return render(request,'designerhome.html')
def subcategory(request):
    return render(request,'subcategory.html')
def subcatego(request):
    cate = request.POST['cate']
    sub = request.POST['sub']
    tdata = Subcategory(cate=cate, sub=sub)
    tdata.save()
    return render(request,'designerhome.html')
def adddesign(request):
    return render(request,'adddesign.html')
def abc(request):
    ddesign = request.POST['ddesign']
    subdesign = request.POST['subdesign']
    proname = request.POST['proname']
    prodis = request.POST['prodis']
    price = request.POST['price']
    shipping = request.POST['shipping']
    photo = request.FILES['file']
    photo1 = request.FILES['file1']
    photo2 = request.FILES['file2']
    poc=date.today()
    data3 = Design(ddesign=ddesign,subdesign=subdesign,proname=proname,prodis=prodis,price=price,shipping=shipping,photo=photo,photo1=photo1,photo2=photo2,poc=poc)
    data3.save()
    return render(request,'designerhome.html')
def ccategory(request):
    return render(request,'craftcate.html')
def cgory(request):
    crafttype = request.POST['crafttype']
    craftdescription = request.POST['craftdescription']
    data4 = Craftcategory(crafttype=crafttype, craftdescription=craftdescription)
    data4.save()
    return render(request,'crafterhome.html')
def craftsubcate(request):
    return render(request,'craftsubcate.html')
def craftsubcatego(request):
    craftstype = request.POST['craftstype']
    craftsubtype= request.POST['craftsubtype']
    data5 = Craftsubcategory(craftstype=craftstype, craftsubtype=craftsubtype)
    data5.save()
    return render(request,'crafterhome.html')
def addcraft(request):
    return render(request,'addcraft.html')
def craft(request):
    print("heloooooo")
    craft = request.POST['craft']
    subcraft = request.POST['subcraft']
    craftname = request.POST['craftname']
    craftdis = request.POST['craftdis']
    cprice = request.POST['cprice']
    cshipping = request.POST['cshipping']
    cphoto = request.FILES['file']
    cphoto1 = request.FILES['file1']
    cphoto2 = request.FILES['file2']
    cpoc=date.today()
    data3 = Craft(craft=craft,subcraft=subcraft,craftname=craftname,craftdis=craftdis,cprice=cprice,cshipping=cshipping,cphoto=cphoto,cphoto1=cphoto1,cphoto2=cphoto2,cpoc=cpoc)
    data3.save()
    return render(request,'crafterhome.html')
def viewcraft(request):
    data=Craft.objects.all()
    return render(request,'viewcraft.html',{'d':data})
def viewdesign(request):
    data=Design.objects.all()
    return render(request,'viewdesign.html',{'f':data})
def showu(request):
    data = Login.objects.filter(status=1)
    return render(request,'showu.html',{'d':data})
def viewuser(request):
    id = request.POST['id']
    data1 = Userreg.objects.filter(email=id)
    return render(request,'viewuser.html',{'f':data1})
def showd(request):
    data = Login.objects.filter(status=2)
    return render(request,'showd.html',{'d':data})
def viewdesigner(request):
    id = request.POST['id']
    data1 = Userreg.objects.filter(email=id)
    return render(request,'viewdesigner.html',{'f':data1})
def showc(request):
    data = Login.objects.filter(status=3)
    return render(request,'showc.html',{'d':data})
def viewcrafter(request):
    id = request.POST['id']
    data2 = Userreg.objects.filter(email=id)
    return render(request,'viewcrafter.html',{'f':data2})
def search(request):
    data = Design.objects.all()
    return render(request, 'search.html', {'s': data})
def sea(request):
    id=request.POST['id']
    data4 = Design.objects.filter(id=id)
    return render(request, 'search.html', {'s': data4})
def searchc(request):
    data = Craft.objects.all()
    return render(request, 'searchc.html', {'d': data})
def searc(request):
    id=request.POST['id']
    dat = Craft.objects.filter(id=id)
    return render(request, 'searchc.html', {'d': dat})
def view(request):
    id=request.POST['id']
    data1=Design.objects.filter(id=id)
    data=Craft.objects.filter(id=id)
    return render(request,'view.html',{'data1':data1,'data':data})
def viewdonly(request):
    id=request.POST['id']
    data1=Design.objects.filter(id=id)
    return render(request,'viewdonly.html',{'data1':data1})
def viewconly(request):
    id=request.POST['id']
    data1=Craft.objects.filter(id=id)
    return render(request,'viewconly.html',{'data':data1})
def vvsearch(request):
    return render(request,'viewsearch.html')
def viewsearch(request):
    n=request.POST['id']
    data1=Design.objects.filter(id=n)
    return render(request,'viewsearch.html',{'data1':data1})
def ccsearch(request):
    return render(request,'viewsearchc.html')
def viewsearchc(request):
    n=request.POST['id']
    data3=Craft.objects.filter(id=n)
    return render(request,'viewsearchc.html',{'data3':data3})
def editdesign(request):
    id=request.POST['id']
    data=Design.objects.get(id=id)
    return render(request, 'editdesign.html',{'data':data})
def update(request):
    id=request.POST['id']
    data=Design.objects.get(id=id)
    data.ddesign=request.POST['ddesign']
    data.subdesign = request.POST['subdesign']
    data.proname = request.POST['proname']
    data.prodis = request.POST['prodis']
    data.price = request.POST['price']
    data.shipping = request.POST['shipping']
    data.photo = request.FILES['file']
    data.photo1 = request.FILES['file']
    data.photo2 = request.FILES['file']
    data.save()
    data2=Design.objects.filter(id=id)
    return render(request, 'viewdesign.html',{'f':data2})
def editcraft(request):
    id=request.POST['id']
    data=Craft.objects.get(id=id)
    return render(request, 'editcraft.html',{'data':data})
def updated(request):
    id=request.POST['id']
    data=Craft.objects.get(id=id)
    data.craft=request.POST['craft']
    data.subcraft = request.POST['subcraft']
    data.craftname = request.POST['craftname']
    data.craftdis = request.POST['craftdis']
    data.cprice = request.POST['cprice']
    data.cshipping = request.POST['cshipping']
    data.cphoto = request.FILES['file']
    data.cphoto1 = request.FILES['file']
    data.cphoto2 = request.FILES['file']
    data.save()
    data3=Craft.objects.filter(id=id)
    return render(request, 'viewcraft.html',{'d':data3})
def reqde(request):
    id = request.session['user']
    Login.objects.filter(username=id).update(status=5)
    return render(request,'work.html')
def aprvede(request):
    data=Login.objects.filter(status=5)
    return render(request,'aprvede.html',{'d':data})
def approve(request):
    id=request.POST['id']
    Login.objects.filter(username=id).update(status=2)
    data = Login.objects.filter(status=5)
    return render(request, 'aprvede.html', {'d': data})
def reqcraft(request):
    id = request.session['user']
    Login.objects.filter(username=id).update(status=6)
    return render(request,'work.html')
def aprvecraft(request):
    data=Login.objects.filter(status=6)
    return render(request,'aprvecraft.html',{'d':data})
def approvecraft(request):
    id=request.POST['id']
    Login.objects.filter(username=id).update(status=3)
    data = Login.objects.filter(status=6)
    return render(request, 'aprvecraft.html', {'d': data})
def home1(request):
    data = Design.objects.all()
    data1 = Craft.objects.all()
    return render(request, 'uhome.html', {'f': data, 'c': data1})
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'login.html')
def cart1(request):
    id=request.POST['id']
    data3=Design.objects.get(id=id)

    user=request.session['user']
    data1=Userreg.objects.get(email=user)
    qty=request.POST['qty']
    size=request.POST['size']
    gtotal=int(qty)*int(data3.price)
    data2=Designcart(did=data3,qty=qty,gtotal=gtotal,size=size,status=0,user=user)
    data2.save()
    return render(request,'gocart.html',{'i':data3,'data1':data1,'data2':data2})
def gocart(request):
    return render(request,'gocart.html')
def cart2(request):
    id=request.POST['id']
    data=Craft.objects.get(id=id)
    user=request.session['user']
    data1=Userreg.objects.get(email=user)
    qty=request.POST['qty']
    gtotal=int(qty)*int(data.cprice)
    data2=Craftcart(cid=data,qty=qty,gtotal=gtotal,status=0,user=user)
    data2.save()
    return render(request,'gocartc.html',{'data':data,'data1':data1,'data2':data2})
def gocartc(request):
    return render(request,'gocartc.html')
def cartdetails(request):
    id=request.session['user']
    data=Designcart.objects.filter(user=id)
    data1 = Craftcart.objects.filter(user=id)
    return render(request,'cartdetails.html',{'data':data,'data1':data1})



