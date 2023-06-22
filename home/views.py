from django.shortcuts import render
from django.http import HttpResponse
from .models import idfetch,enquari1,idgenerate1

# Create your views here.
#-------------------------
def homepage(request):
    return render(request,'homepage.html')
#-------------------------
#login page
def logins(request):
    return render(request,'loginpage.html')
#---------------------------------
def studentspage(request):
    return render(request,'studentpage.html')
def about(request):
    return render(request,'about.html')
def contect(request):
    return render(request,'contect.html')
def course1(request):
    return render(request,'course1.html')
def course(request):
    return render(request,'course.html')
def gellary(request):
    return render(request,'gellary.html')
def ourtrainer(request):
    return render(request,'ourtrainer.html')
def service(request):
    return render(request,'service.html')
#service for employeepage
def service1(request):
    return render(request,'service1.html')
#-----------------------------------------
def constructions(request):
    return render(request,'construction.html')
def landdeling(request):
    return render(request,'landdeling.html')
#employee field
def ergistation(request):
    return render(request,'ergistation.html')
def emplogin(request):
    return render(request,'emplogin.html')
#------------------------------------------
#-----------------------------------------------
#views for id card generating
def idform(request):
    return render(request,'idform.html')
#view for student registration check(insertion)
def idformcheck(request):
    uidcard=request.POST["idcard"]
    uname=request.POST["name"]
    ipass=request.POST["pass"]
    ufname=request.POST["father"]
    uaddress=request.POST["address"]
    umobile=request.POST["mobile"]
    uqualification=request.POST["qualification"]
    uemail=request.POST["email"]
    ugender=request.POST["gender"]
    uage=request.POST["age"]
    usession=request.POST["session"]
    uselect=request.POST["select"]
    sdata=idgenerate1.objects.filter(idcard_number=uidcard)
    # to display error
    if(len(sdata)>0):
        return render(request,"employeeselaryerror.html")
    else:
        #insertion in database(object colling)
        uinser=idgenerate1()
        #--------------------------
        uinser.idcard_number=uidcard
        uinser.user_password=ipass
        uinser.name=uname
        uinser.father_name=ufname
        uinser.address=uaddress
        uinser.mobile=umobile
        uinser.email=uemail
        uinser.qualification=uqualification
        uinser.gender=ugender
        uinser.age=uage
        uinser.session=usession
        uinser.role=uselect
        #for savedata after insertion
        uinser.save()
        #---------------------------
        return render(request,"employeeselarysuccess.html")
#--------------------------------------------------------
#views for id form 
def idformfetch(request):
    return render(request,'idformfetch.html')
#idcard fetch retriveing data from database
def idformfetchdata(request):
    iddata=request.POST["idcard"]
    uspass=request.POST["upass"]
    carddata=idgenerate1.objects.filter(idcard_number=iddata,user_password=uspass)
    if(len(carddata)>0):
        return render(request,'idformfetchsuccess.html',{"idlist":carddata})
    else:
       return render(request,'errorpage.html')
#--------------------------------------------------
#update idcard details
def updateidcardforms(request):
    return render(request,"updateidcard.html")
#student updation 
def idcardupdatecheck(request):
    if request.method=="POST":
         userid=request.POST['uid']
         data=request.POST['uselect']
         if(data=="name"):
            return render(request,"updateidname.html",{"usersid":userid})
         elif(data=="father_name"):
            return render(request,"updateidfathername.html",{"usersid":userid})
         elif(data=="age"):
            return render(request,"updateidage.html",{"usersid":userid})
         elif(data=="role"):
            return render(request,"updateidrole.html",{"usersid":userid})
         elif(data=="qualification"):
            return render(request,"updateidqualification.html",{"usersid":userid})
         elif(data=="address"):
            return render(request,"updateidaddress.html",{"usersid":userid})
         elif(data=="mobile"):
            return render(request,"updateidmobile.html",{"usersid":userid})
         elif(data=="email"):
            return render(request,"updateidemail.html",{"usersid":userid})
         elif(data=="gender"):
            return render(request,"updateidgender.html",{"usersid":userid})
         elif(data=="session"):
            return render(request,"updateidsession.html",{"usersid":userid})
         elif(data=="password"):
            return render(request,"updateidpassword.html",{"usersid":userid})
    else:
        return render(request,'updateidcard.html')
#view for update check
#-----------------------------------------------------------------------------
###############################################################################
#update idcard age
def idpdateagecheck(request):
    sids=request.POST["uid"]
    stuage=request.POST["sage"]
    if(len(idgenerate1.objects.filter(idcard_number=sids))>0):
        data=idgenerate1.objects.filter(idcard_number=sids).update(age=stuage)
        return render(request,"updateidagesuccess.html",{"AGE":stuage,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#update idcard name
def idpdatenamecheck(request):
    sidn=request.POST["uid"]
    stufirst=request.POST["sname"]
    if(len(idgenerate1.objects.filter(idcard_number=sidn))>0):
        data=idgenerate1.objects.filter(idcard_number=sidn).update(name=stufirst)
        return render(request,"updateidnamesuccess.html",{"FIRST":stufirst,"SID":sidn})
    else:
        return render(request,"updateerror.html")
# update idcard father name
def idupdatefathernamecheck(request):
    sidf=request.POST["uid"]
    stufather=request.POST["sfathername"]
    if(len(idgenerate1.objects.filter(idcard_number=sidf))>0):
        data=idgenerate1.objects.filter(idcard_number=sidf).update(father_name=stufather)
        return render(request,"updateidfathernamesuccess.html",{"FATHER":stufather,"SID":sidf})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def idupdateaddresscheck(request):
    sidss=request.POST["uid"]
    stuaddress=request.POST["saddress"]
    if(len(idgenerate1.objects.filter(idcard_number=sidss))>0):
        data=idgenerate1.objects.filter(idcard_number=sidss).update(address=stuaddress)
        return render(request,"updateidaddresssuccess.html",{"ADDRESS":stuaddress,"SID":sidss})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def idupdatequalificationcheck(request):
    sidq=request.POST["uid"]
    stuquali=request.POST["squli"]
    if(len(idgenerate1.objects.filter(idcard_number=sidq))>0):
        data=idgenerate1.objects.filter(idcard_number=sidq).update(qualification=stuquali)
        return render(request,"updateidqualificationsuccess.html",{"QUALIFICATION":stuquali,"SID":sidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def idupdatemobilecheck(request):
    sidm=request.POST["uid"]
    stumobile=request.POST["smobile"]
    if(len(idgenerate1.objects.filter(idcard_number=sidm))>0):
        data=idgenerate1.objects.filter(idcard_number=sidm).update(mobile=stumobile)
        return render(request,"updateidmobilesuccess.html",{"MOBILE":stumobile,"SID":sidm})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def idupdateemailcheck(request):
    side=request.POST["uid"]
    stuemail=request.POST["semail"]
    if(len(idgenerate1.objects.filter(idcard_number=side))>0):
        data=idgenerate1.objects.filter(idcard_number=side).update(email=stuemail)
        return render(request,"updateidemailsuccess.html",{"EMAIL":stuemail,"SID":side})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def idupdatepasswordcheck(request):
    sidp=request.POST["uid"]
    stupassword=request.POST["spass"]
    if(len(idgenerate1.objects.filter(idcard_number=sidp))>0):
        data=idgenerate1.objects.filter(idcard_number=sidp).update(user_password=stupassword)
        return render(request,"updateidpasswordsuccess.html",{"PASSWORD":stupassword,"SID":sidp})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def idupdategendercheck(request):
    sidg=request.POST["uid"]
    stugender=request.POST["sgender"]
    if(len(idgenerate1.objects.filter(idcard_number=sidg))>0):
        data=idgenerate1.objects.filter(idcard_number=sidg).update(gender=stugender)
        return render(request,"updateidgendersuccess.html",{"GENDER":stugender,"SID":sidg})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def idupdatesessioncheck(request):
    sidse=request.POST["uid"]
    stusession=request.POST["ssession"]
    if(len(idgenerate1.objects.filter(idcard_number=sidse))>0):
        data=idgenerate1.objects.filter(idcard_number=sidse).update(session=stusession)
        return render(request,"updateidsessionsuccess.html",{"SESSION":stusession,"SID":sidse})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def idupdaterolecheck(request):
    sidr=request.POST["uid"]
    sturole=request.POST["srole"]
    if(len(idgenerate1.objects.filter(idcard_number=sidr))>0):
        data=idgenerate1.objects.filter(idcard_number=sidr).update(role=sturole)
        return render(request,"updateidrolesuccess.html",{"ROLE":sturole,"SID":sidr})
    else:
        return render(request,"updateerror.html")
#views for delete student id
def deleteiddata(request):
    return render(request,'deletuserid.html')
#views for delete checking operation
def deleteidcheck(request):
    deid=request.POST["did"]
    if(len(idgenerate1.objects.filter(idcard_number=deid))>0):
        data=idgenerate1.objects.filter(idcard_number=deid).delete()
        return render(request,"deleteidsuccess.html")
    else:
        return render(request,"errorpage.html")
#------------------------------------------
def idcheck(request):
    cid=request.GET["id"]
    userpass=request.GET["passw"]
    crole=request.GET["role"]
    #select * from tablename where stdid=sid
    #data=idfetchs.objects.filter(idno=cid)
    data=idgenerate1.objects.filter(idcard_number=cid,user_password=userpass,role=crole)
    if (len(data)>0):
        if(crole=="student"):
            return render(request,'studentindex.html')
        elif(crole=="employee"):
            return render(request,'employeepage.html')
        elif(crole=="admin"):
            return render(request,'adminindex.html')
        else:
            return render(request,'errorpage.html')
#------------------------------------------------------
#views for enquari data
def enquaricheck(request):
    enqname=request.POST["name"]
    enqaddress=request.POST["address"]
    enqmobile=request.POST["mobile"]
    enqemail=request.POST["email"]
    enqcourse=request.POST["course"]
    data=enquari1.objects.filter(mobile=enqmobile)
    # to display error
    if(len(data)>0):
        return render(request,"employeeselaryerror.html")
    else:
        #insertion in database(object colling)
        einser=enquari1()
        #--------------------------
        einser.name=enqname
        einser.address=enqaddress
        einser.mobile=enqmobile
        einser.email=enqemail
        einser.course=enqcourse
        #for savedata after insertion
        einser.save()
        #---------------------------
        return render(request,"employeeselarysuccess.html")
#enquari fetching data 
def enquarifetch(request):
    return render(request,'enquarifetch.html')
#idcard fetch retriveing data from database
def enquarifetchdata(request):
    enqricourse=request.POST["course"]
    enqudata=enquari1.objects.filter(course=enqricourse)
    if(len(enqudata)>0):
        return render(request,'enquarifetchsuccess.html',{"enquarilist":enqudata})
    else:
       return render(request,'errorpage.html')
        
        
