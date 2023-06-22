from django.shortcuts import render
from django.http import HttpResponse
from .models import steregistration,studentfer
#-------------------------------------
# Create your views here.
def studentpage(request):
    return render(request,'studentpage.html')
def sindex(request):
    return render(request,'studentindex.html')
def studentpage2(request):
    return render(request,'studentpage2.html')
def student_registration(request):
    return render(request,'student_registration.html')
#-----------------------------------------------------
def sregistration(request):
    return render(request,'sregistration.html')
#student registration insertion operation
#view for student registration check
def sregistrationcheck(request):
    sid=request.GET["id"]
    spass=request.GET["pass"]
    fname=request.GET["first"]
    lname=request.GET["last"]
    saddress=request.GET["address"]
    squalification=request.GET["qualification"]
    sage=request.GET["age"]
    smobile=request.GET["mobile"]
    semail=request.GET["email"]
    data=steregistration.objects.filter(stdid=sid)
    # to display error
    if(len(data)>0):
        return render(request,"serror.html")
    else:
        #insertion in database(object colling)
        inser=steregistration()
        #--------------------------
        inser.stdid=sid
        inser.password=spass
        inser.first_name=fname
        inser.last_name=lname
        inser.address=saddress
        inser.qualification=squalification
        inser.age=sage
        inser.mobile=smobile
        inser.email=semail
        #for savedata after insertion
        inser.save()
        #---------------------------
        return render(request,"sregistrationsuccess.html")
#-----------------------------------------------------
def slogin(request):
    return render(request,'slogin.html')
def logincheck(request):
    lsid=request.POST["suid"]
    lspass=request.POST["supass"]
    #select * from tablename where stdid=sid
    #data=idfetchs.objects.filter(idno=cid)
    data=steregistration.objects.filter(stdid=lsid,password=lspass)
    if (len(data)>0):
        return render(request,'studentpage2.html')
    else:
        return render(request,'errorpage.html')
#------------------------------------------------------
def studentregistration(request):
    return render(request,'studentregistration.html')
#----------------------------------------------------------------------
#student registration fetching 
def studentregistrationfetch(request):
    return render(request,'studentregistrationfetch.html')
#idcard fetch retriveing data from database
def studentsregfetch(request):
    studid=request.POST["sid"]
    studedata=steregistration.objects.filter(stdid=studid)
    if(len(studedata)>0):
        return render(request,'sturegistratiofetchsuccess.html',{"studelist":studedata})
    else:
       return render(request,'errorpage.html')
#-------------------------------------------------------------------------
#views for delete student id
def deletedata(request):
    return render(request,'deletstudentid.html')
#views for delete checking operation
def deletecheck(request):
    sid=request.POST["id"]
    if(len(steregistration.objects.filter(stdid=sid))>0):
        data=steregistration.objects.filter(stdid=sid).delete()
        return render(request,"deletesuccess.html")
    else:
        return render(request,"errorpage.html")
#--------------------------------------------------
def updateforms(request):
    return render(request,"updatestudent.html")
#student updation 
def dataupdate(request):
    if request.method=="POST":
         stdid=request.POST['sid']
         data=request.POST['select']
         if(data=="name"):
            return render(request,"updatename.html",{"studentid":stdid})
         elif(data=="fathername"):
            return render(request,"updatefathername.html",{"studentid":stdid})
         elif(data=="age"):
            return render(request,"updateage.html",{"studentid":stdid})
         elif(data=="role"):
            return render(request,"updaterole.html",{"studentid":stdid})
         elif(data=="qualification"):
            return render(request,"updatequalification.html",{"studentid":stdid})
         elif(data=="address"):
            return render(request,"updateaddress.html",{"studentid":stdid})
         elif(data=="mobile"):
            return render(request,"updatemobile.html",{"studentid":stdid})
         elif(data=="email"):
            return render(request,"updateemail.html",{"studentid":stdid})
         elif(data=="password"):
            return render(request,"updatepassword.html",{"studentid":stdid})
    else:
        return render(request,'updatestudent.html')
#view for update check
#-----------------------------------------------------------------------------
###############################################################################
def supdatecheck(request):
    sids=request.POST["sid"]
    stuage=request.POST["sage"]
    if(len(steregistration.objects.filter(stdid=sids))>0):
        data=steregistration.objects.filter(stdid=sids).update(age=stuage)
        return render(request,"updatesuccess.html",{"AGE":stuage,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def supdatenamecheck(request):
    sidn=request.POST["sid"]
    stufirst=request.POST["first"]
    stulast=request.POST["last"]
    if(len(steregistration.objects.filter(stdid=sidn))>0):
        data=steregistration.objects.filter(stdid=sidn).update(first_name=stufirst,last_name=stulast)
        return render(request,"updatenamesuccess.html",{"FIRST":stufirst,"LAST":stulast,"SID":sidn})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def supdateaddresscheck(request):
    sids=request.POST["sid"]
    stuaddress=request.POST["saddress"]
    if(len(steregistration.objects.filter(stdid=sids))>0):
        data=steregistration.objects.filter(stdid=sids).update(address=stuaddress)
        return render(request,"updateaddresssuccess.html",{"ADDRESS":stuaddress,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def supdatequalificationcheck(request):
    sidq=request.POST["sid"]
    stuquali=request.POST["quli"]
    if(len(steregistration.objects.filter(stdid=sidq))>0):
        data=steregistration.objects.filter(stdid=sidq).update(qualification=stuquali)
        return render(request,"updatequalificationsuccess.html",{"QUALIFICATION":stuquali,"SID":sidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def supdatemobilecheck(request):
    sids=request.POST["sid"]
    stumobile=request.POST["smobile"]
    if(len(steregistration.objects.filter(stdid=sids))>0):
        data=steregistration.objects.filter(stdid=sids).update(mobile=stumobile)
        return render(request,"updatemobilesuccess.html",{"MOBILE":stumobile,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def supdateemailcheck(request):
    sidq=request.POST["sid"]
    stuemail=request.POST["semail"]
    if(len(steregistration.objects.filter(stdid=sidq))>0):
        data=steregistration.objects.filter(stdid=sidq).update(email=stuemail)
        return render(request,"updateemailsuccess.html",{"EMAIL":stuemail,"SID":sidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def supdatepasswordcheck(request):
    sids=request.POST["sid"]
    stupassword=request.POST["spass"]
    if(len(steregistration.objects.filter(stdid=sids))>0):
        data=steregistration.objects.filter(stdid=sids).update(password=stupassword)
        return render(request,"updatepasswordsuccess.html",{"PASSWORD":stupassword,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#student profile insertion
def sperf(request):
    return render(request,'studenperformance.html')
def sperfcheck(request):
    srolln=request.POST["roll"]
    sname=request.POST["name"]
    sfname=request.POST["father"]
    saddress=request.POST["address"]
    squalification=request.POST["qualification"]
    sage=request.POST["age"]
    smobile=request.POST["mobile"]
    semail=request.POST["email"]
    sfmarks=request.POST["fmarks"]
    sobtain=request.POST["obtain"]
    sgrad=request.POST["grad"]
    sper=request.POST["per"]
    sattendance=request.POST["attend"]
    sstype=request.POST["stype"]
    sperformance=request.POST["performance"]
    simg=request.FILES["imgs"]
    data=studentfer.objects.filter(stdudeid=srolln)
    # to display error
    if(len(data)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        inser=studentfer()
        #--------------------------
        inser.stdudeid=srolln
        inser.name=sname
        inser.father_name=sfname
        inser.address=saddress
        inser.qualification=squalification
        inser.age=sage
        inser.mobile=smobile
        inser.email=semail
        inser.fullmarks=sfmarks
        inser.obtaindmarks=sobtain
        inser.grad=sgrad
        inser.percentage=sper
        inser.attendance=sattendance
        inser.studenttype=sstype
        inser.performance=sperformance
        inser.studeimage=simg
        #for savedata after insertion
        inser.save()
        #---------------------------
        return render(request,"sregistrationsuccess.html")
#student profile fetch for studentpage
def sperformancefetch(request):
    return render(request,"studenperformancefetch.html")
def sperformancefetchsuccess(request):
    idstuden=request.POST['studenid']
    data=studentfer.objects.filter(stdudeid=idstuden)
    if(len(data)>0):
        return render(request,"studenperformancefetchsuccess.html",{"profile":data})
    else:
        return render(request,"")
#student profile fetch for admin page
def sperformancefetch1(request):
    return render(request,"studentperformancefetch1.html")
def sperformancefetch1success(request):
    idstuden=request.POST['studenid']
    data=studentfer.objects.filter(stdudeid=idstuden)
    if(len(data)>0):
        return render(request,"studentperformancefetch1success.html",{"profile":data})
    else:
        return render(request,"")
#--------------------------------------------------------
def log(request):
    request.session["username"]=""
    return render(request,'homepage.html')