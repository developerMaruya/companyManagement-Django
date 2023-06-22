from django.shortcuts import render
from django.http import HttpResponse
from .models import empregistration,stprofile1,stperformance
#-------------------------------------
# Create your views here.
def employeepage(request):
    return render(request,'employeepage.html')
# Create your views here.
def employeeindex(request):
    return render(request,'employeeindex.html')
#---------------------------------------------
#employee login
def employeelogin(request):
    return render(request,'employeelogin.html')
def loginemployeecheck1(request):
    eamid=request.POST["employeeid"]
    eampass=request.POST["employeepass"]
    data=empregistration.objects.filter(empid=eamid,password=eampass)
    if (len(data)>0):
        return render(request,'employeepage2.html')
    else:
        return render(request,'errorpage.html')
#----------------------------------------------
#student profile 
def sprofile(request):
    return render(request,'studentprofile.html')
def sprofilecheck(request):
    sroll=request.POST["roll"]
    sname=request.POST["name"]
    sfname=request.POST["father"]
    saddress=request.POST["address"]
    squalification=request.POST["qualification"]
    sage=request.POST["age"]
    smobile=request.POST["mobile"]
    semail=request.POST["email"]
    scourse1=request.POST["course1"]
    scourse2=request.POST["course2"]
    scourse3=request.POST["course3"]
    scourse4=request.POST["course4"]
    sfmarks=request.POST["fmarks"]
    sobtain=request.POST["obtain"]
    sgrad=request.POST["grad"]
    sper=request.POST["per"]
    stimg=request.FILES["imgstu"]
    data=stprofile1.objects.filter(student_id=sroll)
    # to display error
    if(len(data)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        inser=stprofile1()
        #--------------------------
        inser.student_id=sroll
        inser.student_name=sname
        inser.father_name=sfname
        inser.address=saddress
        inser.qualification=squalification
        inser.age=sage
        inser.mobile=smobile
        inser.email=semail
        inser.student_course1=scourse1
        inser.student_course2=scourse2
        inser.student_course3=scourse3
        inser.student_course4=scourse4
        inser.full_marks=sfmarks
        inser.obtaind_marks=sobtain
        inser.grad=sgrad
        inser.percentage=sper
        inser.stdimage=stimg
        #for savedata after insertion
        inser.save()
        #---------------------------
        return render(request,"eregistrationsuccess.html")
#profile fetch
def sprofilefetch(request):
    return render(request,"studentprofilefetch.html")
def sprofilefetchsuccess(request):
    idstu=request.POST['studid']
    data=stprofile1.objects.filter(student_id=idstu)
    if(len(data)>0):
        return render(request,"studentprofilefetchsuccess.html",{"profile":data})
    else:
        return render(request,"")
#profile fetch for administration page
#profile fetch
def stprofilefetch(request):
    return render(request,"studentprofilefetch1.html")
def stprofilefetchsuccess(request):
    idstud=request.POST['stuid']
    data=stprofile1.objects.filter(student_id=idstud)
    if(len(data)>0):
        return render(request,"studentprofilefetchsuccess1.html",{"profile":data})
    else:
        return render(request,"")
#--------------------------------------------------------
#student performance
def sperformance(request):
    return render(request,'studentperformance.html')
def sperformancecheck(request):
    stroll=request.POST["rolln"]
    stname=request.POST["name"]
    stfather_name=request.POST["fname"]
    staddress=request.POST["address"]
    stmobile=request.POST["mobile"]
    stfmarks=request.POST["fmarks"]
    stobtain=request.POST["obtain"]
    stgrad=request.POST["grad"]
    stper=request.POST["per"]
    stattendance=request.POST["attendance"]
    ststype=request.POST["stype"]
    stperformance=request.POST["performance"]
    stimage=request.FILES["studenimage"]
    data1=stperformance.objects.filter(student_id=stroll)
    # to display error
    if(len(data1)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        sinser=stperformance()
        #--------------------------
        sinser.student_id=stroll
        sinser.student_name=stname
        sinser.father_name=stfather_name
        sinser.address=staddress
        sinser.mobile=stmobile
        sinser.full_marks=stfmarks
        sinser.obtaind_marks=stobtain
        sinser.grad=stgrad
        sinser.percentage=stper
        sinser.attendance=stattendance
        sinser.student_type=ststype
        sinser.performance=stperformance
        sinser.studimage=stimage
        #for savedata after insertion
        sinser.save()
        #---------------------------
        return render(request,"eregistrationsuccess.html")
#--------------------------------------------------------
#students  performances
def studentperformance(request):
    return render(request,'studentperformance1.html')
def studentperformancecheck(request):
    studroll=request.POST["srollnumber"]
    studname=request.POST["sname"]
    studfather_name=request.POST["sfname"]
    studaddress=request.POST["saddress"]
    studmobile=request.POST["smobile"]
    studfmarks=request.POST["sfmarks"]
    studobtain=request.POST["sobtain"]
    studgrad=request.POST["sgrad"]
    studper=request.POST["sper"]
    studattendance=request.POST["sattendance"]
    studtype=request.POST["stype"]
    studperformance=request.POST["sperformance"]
    studimage=request.FILES["sstudenimage"]
    data1=studentperformance.objects.filter(studentsid=studroll)
    # to display error
    if(len(data1)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        sinser=studentperformance()
        #--------------------------
        sinser.studentsid=studroll
        sinser.student_name=studname
        sinser.father_name=studfather_name
        sinser.address=studaddress
        sinser.mobile=studmobile
        sinser.full_marks=studfmarks
        sinser.obtaind_marks=studobtain
        sinser.grad=studgrad
        sinser.percentage=studper
        sinser.attendance=studattendance
        sinser.student_type=studtype
        sinser.performance=studperformance
        sinser.studimage=studimage
        #for savedata after insertion
        sinser.save()
        #---------------------------
        return render(request,"eregistrationsuccess.html")
#--------------------------------------------------------
#----------------------------------------------
def eregistration(request):
    return render(request,'ergistation.html')
#student registration insertion operation
#view for student registration check
def emregistrationcheck(request):
    eid=request.GET["id"]
    epass=request.GET["pass"]
    erole=request.GET["role"]
    ename=request.GET["name"]
    efname=request.GET["father"]
    eaddress=request.GET["address"]
    equalification=request.GET["qualification"]
    eage=request.GET["age"]
    emobile=request.GET["mobile"]
    eemail=request.GET["email"]
    data=empregistration.objects.filter(empid=eid)
    # to display error
    if(len(data)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        inser=empregistration()
        #--------------------------
        inser.empid=eid
        inser.password=epass
        inser.emp_name=ename
        inser.father_name=efname
        inser.address=eaddress
        inser.qualification=equalification
        inser.age=eage
        inser.mobile=emobile
        inser.email=eemail
        inser.workrole=erole
        #for savedata after insertion
        inser.save()
        #---------------------------
        return render(request,"eregistrationsuccess.html")
#----------------------------------------------------------------------
#employee registration fetching 
def employeeregistrationfetch(request):
    return render(request,'employeeregistrationfetch.html')
#idcard fetch retriveing data from database
def employeeregfetch(request):
    emplid=request.POST["userid"]
    emplodata=empregistration.objects.filter(empid=emplid)
    if(len(emplodata)>0):
        return render(request,'emploregistratiofetchsuccess.html',{"emplolist":emplodata})
    else:
       return render(request,'errorpage.html')
#----------------------------------------------
def hello(request):
    return render(request,'hello.html')
#-------------------------------------------------------------------------
#views for delete employee id
def deleteemployeedata(request):
    return render(request,'deletemployeeid.html')
#views for delete checking operation
def deleteemployeecheck(request):
    emid=request.POST["eid"]
    if(len(empregistration.objects.filter(empid=emid))>0):
        data=empregistration.objects.filter(empid=emid).delete()
        return render(request,"deletesuccess.html")
    else:
        return render(request,"errorpage.html")
#--------------------------------------------------
def updateemployeeforms(request):
    return render(request,"updateemployee.html")
#student updation 
def updateemployeecheck(request):
    if request.method=="POST":
         eid=request.POST['employeid']
         datas=request.POST['employeeselect']
         if(datas=="name"):
            return render(request,"updateename.html",{"employeeid":eid})
         elif(datas=="fathername"):
            return render(request,"updateefathername.html",{"employeeid":eid})
         elif(datas=="age"):
            return render(request,"updateeage.html",{"employeeid":eid})
         elif(datas=="role"):
            return render(request,"updateerole.html",{"employeeid":eid})
         elif(datas=="qualification"):
            return render(request,"updateequalification.html",{"employeeid":eid})
         elif(datas=="address"):
            return render(request,"updateeaddress.html",{"employeeid":eid})
         elif(datas=="mobile"):
            return render(request,"updateemobile.html",{"employeeid":eid})
         elif(datas=="email"):
            return render(request,"updateeemail.html",{"employeeid":eid})
         elif(datas=="password"):
            return render(request,"updateepassword.html",{"employeeid":eid})
    else:
        return render(request,'updateemployee.html')
#view for update check
#-----------------------------------------------------------------------------
###############################################################################
def eupdateagecheck(request):
    eids=request.POST["eid"]
    emage=request.POST["eage"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(age=emage)
        return render(request,"updateeagesuccess.html",{"AGE":emage,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdatenamecheck(request):
    eidn=request.POST["eid"]
    emname=request.POST["ename"]
    if(len(empregistration.objects.filter(empid=eidn))>0):
        data=empregistration.objects.filter(empid=eidn).update(emp_name=emname)
        return render(request,"updateenamesuccess.html",{"NAME":emname,"SID":eidn})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateaddresscheck(request):
    eids=request.POST["eid"]
    emaddress=request.POST["eaddress"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(address=emaddress)
        return render(request,"updateeaddresssuccess.html",{"ADDRESS":emaddress,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdatequalificationcheck(request):
    eidq=request.POST["eid"]
    emquali=request.POST["equli"]
    if(len(empregistration.objects.filter(empid=eidq))>0):
        data=empregistration.objects.filter(empid=eidq).update(qualification=emquali)
        return render(request,"updateequalificationsuccess.html",{"QUALIFICATION":emquali,"SID":eidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def eupdatemobilecheck(request):
    eids=request.POST["eid"]
    emmobile=request.POST["emobile"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(mobile=emmobile)
        return render(request,"updateemobilesuccess.html",{"MOBILE":emmobile,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateemailcheck(request):
    eidq=request.POST["eid"]
    ememail=request.POST["eemail"]
    if(len(empregistration.objects.filter(empid=eidq))>0):
        data=empregistration.objects.filter(empid=eidq).update(email=ememail)
        return render(request,"updateeemailsuccess.html",{"EMAIL":ememail,"SID":eidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def eupdatepasswordcheck(request):
    eids=request.POST["eid"]
    empassword=request.POST["epass"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(password=empassword)
        return render(request,"updateepasswordsuccess.html",{"PASSWORD":empassword,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateworkrolecheck(request):
    eids=request.POST["eid"]
    emrole=request.POST["erole"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(workrole=emrole)
        return render(request,"updateerolesuccess.html",{"PASSWORD":emrole,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdatefathernamecheck(request):
    eids=request.POST["eid"]
    emfname=request.POST["efname"]
    if(len(empregistration.objects.filter(empid=eids))>0):
        data=empregistration.objects.filter(empid=eids).update(father_name=emfname)
        return render(request,"updateefathernamesuccess.html",{"FATHER":emfname,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#logout 
def log1(request):
    request.session["username"]=""
    return render(request,'homepage.html')