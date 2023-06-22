from django.shortcuts import render
from django.http import HttpResponse
from .models import employeeregistration,empselary2,studentfees,idcardgenerate,adminregistration,emprofile
#-------------------------------------
# Create your views here.
def administrationpage(request):
    return render(request,'administrationpage.html')
def deletstudentid(request):
    return render(request,'deletstudentid.html')
#--------------------------------------------------
#views for delete admin id
def deleteadminpage(request):
    return render(request,'deleteadmin.html')
#views for delete checking operation
def deleteadmincheck(request):
    adid=request.POST["id"]
    if(len(adminregistration.objects.filter(admin_id=adid))>0):
        data=adminregistration.objects.filter(admin_id=adid).delete()
        return render(request,"deletesuccess.html")
    else:
        return render(request,"errorpage.html")
#--------------------------------------------
def deletemployeeid(request):
    return render(request,'deletemployeeid.html')
def updatestudent(request):
    return render(request,'updatestudent.html')
def updateemployee(request):
    return render(request,'updateemployee.html')
def updateadminpage(request):
    return render(request,'updateadmin.html')
#--------------------------------------------
#employee selary 
def employeeselary(request):
    return render(request,'employeeselary.html')
#view for student registration checkz(insertion)
def employeeselarycheck(request):
    eid=request.POST["id"]
    ename=request.POST["name"]
    eaddress=request.POST["address"]
    edate=request.POST["date"]
    emonthely=request.POST["monthely"]
    etotal=request.POST["total"]
    egiven=request.POST["given"]
    eremaning=request.POST["remaning"]
    ework=request.POST["work"]
    data=empselary2.objects.filter(employee_id=eid)
    # to display error
    if(len(data)>0):
        return render(request,"employeeselaryerror.html")
    else:
        #insertion in database(object colling)
        einser=empselary2()
        #--------------------------
        einser.employee_id=eid
        einser.employee_name=ename
        einser.employee_address=eaddress
        einser.date=edate
        einser.employee_monthely_income=emonthely
        einser.employee_total_income=etotal
        einser.employee_given_income=egiven
        einser.employee_remaning_income=eremaning
        einser.employee_role=ework
        #for savedata after insertion
        einser.save()
        #---------------------------
        return render(request,"employeeselarysuccess.html")
#employee selary retriveing data from database
def employeeselaryfetch(request):
    emid=request.POST["userid"]
    da=empselary2.objects.filter(employee_id=emid)
    if(len(da)>0):
        return render(request,'employeeselarysuccesspage.html',{"selarylist":da})
    else:
       return render(request,'errorpage.html')
#-------------------------------------------------------
#update employee selary 
#--------------------------------------------------
def updateemployeeselaryforms(request):
    return render(request,"updateemployeeselary.html")
#student updation 
def updateemployeeselarycheck(request):
    if request.method=="POST":
         eid=request.POST['employeid']
         datas=request.POST['employeeselect']
         if(datas=="name"):
            return render(request,"updateselaryname.html",{"employeeid":eid})
         elif(datas=="address"):
            return render(request,"updateselaryaddress.html",{"employeeid":eid})
         elif(datas=="date"):
            return render(request,"updateselarydate.html",{"employeeid":eid})
         elif(datas=="monthely_income"):
            return render(request,"updateselarymonthely.html",{"employeeid":eid})
         elif(datas=="total_income"):
            return render(request,"updateselarytotal.html",{"employeeid":eid})
         elif(datas=="given_income"):
            return render(request,"updateselarygiven.html",{"employeeid":eid})
         elif(datas=="remaning_income"):
            return render(request,"updateselaryremaning.html",{"employeeid":eid})
         elif(datas=="role"):
            return render(request,"updateselaryrole.html",{"employeeid":eid})
    else:
        return render(request,'updateemployeeselary.html')
#view for selary update check
def eupdateselarydatecheck(request):
    eids=request.POST["eid"]
    emdate=request.POST["edate"]
    if(len(empselary2.objects.filter(employee_id=eids))>0):
        data=empselary2.objects.filter(employee_id=eids).update(date=emdate)
        return render(request,"updatesdatesuccess.html",{"DATE":emdate,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateselarynamecheck(request):
    eidn=request.POST["eid"]
    emname=request.POST["ename"]
    if(len(empselary2.objects.filter(employee_id=eidn))>0):
        data=empselary2.objects.filter(employee_id=eidn).update(employee_name=emname)
        return render(request,"updatesnamesuccess.html",{"NAME":emname,"SID":eidn})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateselaryaddresscheck(request):
    eids=request.POST["eid"]
    emaddress=request.POST["eaddress"]
    if(len(empselary2.objects.filter(employee_id=eids))>0):
        data=empselary2.objects.filter(employee_id=eids).update(employee_address=emaddress)
        return render(request,"updatesaddresssuccess.html",{"ADDRESS":emaddress,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateselarymonthelycheck(request):
    eidq=request.POST["eid"]
    emmonthely=request.POST["emonthely"]
    if(len(empselary2.objects.filter(employee_id=eidq))>0):
        data=empselary2.objects.filter(employee_id=eidq).update(employee_monthely_income=emmonthely)
        return render(request,"updatesmonthelysuccess.html",{"MONTHELY":emmonthely,"SID":eidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def eupdateselarytotalcheck(request):
    eids=request.POST["eid"]
    emetotal=request.POST["etotal"]
    if(len(empselary2.objects.filter(employee_id=eids))>0):
        data=empselary2.objects.filter(employee_id=eids).update(employee_total_income=emetotal)
        return render(request,"updatestotalsuccess.html",{"TOTAL":emetotal,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateselarygivencheck(request):
    eidq=request.POST["eid"]
    emgiven=request.POST["egiven"]
    if(len(empselary2.objects.filter(employee_id=eidq))>0):
        data=empselary2.objects.filter(employee_id=eidq).update(employee_given_income=emgiven)
        return render(request,"updatesgivensuccess.html",{"GIVEN":emgiven,"SID":eidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def eupdateselaryremaningcheck(request):
    eids=request.POST["eid"]
    emremaning=request.POST["eremaning"]
    if(len(empselary2.objects.filter(employee_id=eids))>0):
        data=empselary2.objects.filter(employee_id=eids).update(employee_remaning_income=emremaning)
        return render(request,"updatesremaningsuccess.html",{"REMANING":emremaning,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def eupdateselaryrolecheck(request):
    eids=request.POST["eid"]
    emrole=request.POST["erole"]
    if(len(empselary2.objects.filter(employee_id=eids))>0):
        data=empselary2.objects.filter(employee_id=eids).update(employee_role=emrole)
        return render(request,"updatesrolesuccess.html",{"ROLE":emrole,"SID":eids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#views for delete employee selary id
def deleteselary(request):
    return render(request,'deleteemployeeselarypage.html')
#views for delete checking operation
def deleteselarycheck(request):
    eid=request.POST["emid"]
    if(len(empselary2.objects.filter(employee_id=eid))>0):
        data=empselary2.objects.filter(employee_id=eid).delete()
        return render(request,"deleteemployeeselarysuccess.html")
    else:
        return render(request,"errorpage.html")

#views for student fees 
def studentsfees(request):
    return render(request,'studentfees.html')
#view for student registration check(insertion)
def studentfeescheck(request):
    stid=request.POST["id"]
    sname=request.POST["name"]
    saddress=request.POST["address"]
    sdate=request.POST["date"]
    scourse=request.POST["course"]
    stotal=request.POST["total"]
    sgiven=request.POST["given"]
    sremaning=request.POST["remaning"]
    sduration=request.POST["duration"]
    sdata=studentfees.objects.filter(studid=stid)
    # to display error
    if(len(sdata)>0):
        return render(request,"employeeselaryerror.html")
    else:
        #insertion in database(object colling)
        sinser=studentfees()
        #--------------------------
        sinser.studid=stid
        sinser.student_name=sname
        sinser.student_address=saddress
        sinser.admision_date=sdate
        sinser.student_course=scourse
        sinser.total_fees=stotal
        sinser.given_fees=sgiven
        sinser.remaning_fees=sremaning
        sinser.course_duration=sduration
        #for savedata after insertion
        sinser.save()
        #---------------------------
        return render(request,"employeeselarysuccess.html")
#student fees retriveing data from database
def studentfeesretrivedata(request):
    ids=request.POST["sid"]
    b=studentfees.objects.filter(studid=ids)
    if(len(b)>0):
        return render(request,'studentfeessuccess.html',{"studentdata":b})
    else:
       return render(request,'errorpage.html')
#----student update fees-----------------------
def updatestudentfeesforms(request):
    return render(request,"updatestudentfees.html")
#student updation 
def dataupdatecheck(request):
    if request.method=="POST":
         stdid=request.POST['sid']
         data=request.POST['select']
         if(data=="name"):
            return render(request,"updatestdfeesname.html",{"studentid":stdid})
         elif(data=="address"):
            return render(request,"updatefeesaddress.html",{"studentid":stdid})
         elif(data=="course"):
            return render(request,"updatefeescourse.html",{"studentid":stdid})
         elif(data=="admition_date"):
            return render(request,"updatefeesadmition.html",{"studentid":stdid})
         elif(data=="total_fees"):
            return render(request,"updatefeestotal.html",{"studentid":stdid})
         elif(data=="givan_fees"):
            return render(request,"updatefeesgiven.html",{"studentid":stdid})
         elif(data=="remaning_fees"):
            return render(request,"updatefeesremaning.html",{"studentid":stdid})
         elif(data=="course_duration"):
            return render(request,"updatefeesduration.html",{"studentid":stdid})
    else:
        return render(request,'updatestudent.html')
#view for update check fetch
#name 
#-----------------------------------------------------------
def updatefeesnamecheck(request):
    sidn=request.POST["sid"]
    stuname=request.POST["sname"]
    if(len(studentfees.objects.filter(studid=sidn))>0):
        data=studentfees.objects.filter(studid=sidn).update(student_name=stuname)
        return render(request,"updatefeesnamesuccess.html",{"NAME":stuname,"SID":sidn})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#address
def feesaddress(request):
    sids=request.POST["sid"]
    stuaddress=request.POST["saddress"]
    if(len(studentfees.objects.filter(studid=sids))>0):
        data=studentfees.objects.filter(studid=sids).update(student_address=stuaddress)
        return render(request,"updatefeesaddresssuccess.html",{"ADDRESS":stuaddress,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#course
def feescourse(request):
    sidq=request.POST["sid"]
    ucourse=request.POST["course"]
    if(len(studentfees.objects.filter(studid=sidq))>0):
        data=studentfees.objects.filter(studid=sidq).update(student_course=ucourse)
        return render(request,"updatefeescoursesuccess.html",{"COURSE":ucourse,"SID":sidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
#admition data
def feesadmitiondate(request):
    sids=request.POST["sid"]
    uadmitiondate=request.POST["admitiondate"]
    if(len(studentfees.objects.filter(studid=sids))>0):
        data=studentfees.objects.filter(studid=sids).update(admision_date=uadmitiondate)
        return render(request,"updatefeesadmitiondatesuccess.html",{"ADMITIONDATE":uadmitiondate,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
#total fees
def feestotal(request):
    sidq=request.POST["sid"]
    utotal=request.POST["total"]
    if(len(studentfees.objects.filter(studid=sidq))>0):
        data=studentfees.objects.filter(studid=sidq).update(total_fees=utotal)
        return render(request,"updatefeestotalsuccess.html",{"TOTALFEES":utotal,"SID":sidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
#givan fees
def feesgivan(request):
    sids=request.POST["sid"]
    ugiven=request.POST["given"]
    if(len(studentfees.objects.filter(studid=sids))>0):
        data=studentfees.objects.filter(studid=sids).update(given_fees=ugiven)
        return render(request,"updatefeesgivensuccess.html",{"GIVENFEES":ugiven,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
#remaning fees
def feesremaning(request):
    sids=request.POST["sid"]
    uremaning=request.POST["remaning"]
    if(len(studentfees.objects.filter(studid=sids))>0):
        data=studentfees.objects.filter(studid=sids).update(remaning_fees=uremaning)
        return render(request,"updatefeesremaningsuccess.html",{"REMANINGFEES":uremaning,"SID":sids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
#course duration
def feescourseduration(request):
    sids=request.POST["sid"]
    uduration=request.POST["cduration"]
    if(len(studentfees.objects.filter(studid=sids))>0):
        data=studentfees.objects.filter(studid=sids).update(course_duration=uduration)
        return render(request,"updatefeesdurationsuccess.html",{"DURATION":uduration,"SID":sids})
    else:
        return render(request,"updateerror.html")        
#-----------------------------------------------
#delet student fees id 
#views for delete student id
def deletefees(request):
    return render(request,'deletefeesid.html')
#views for delete checking operation
def deletefeescheck(request):
    sid=request.POST["id"]
    if(len(studentfees.objects.filter(studid=sid))>0):
        data=studentfees.objects.filter(studid=sid).delete()
        return render(request,"deletesuccesspage.html")
    else:
        return render(request,"errorpage.html")
#views for id card generating
def idcardform(request):
    return render(request,'idcardform.html')
#view for student registration check(insertion)
def idcardcheck(request):
    uidcard=request.POST["idcard"]
    uname=request.POST["name"]
    ufname=request.POST["father"]
    uaddress=request.POST["address"]
    umobile=request.POST["mobile"]
    uqualification=request.POST["qualification"]
    uemail=request.POST["email"]
    ugender=request.POST["gender"]
    uage=request.POST["age"]
    usession=request.POST["session"]
    uselect=request.POST["select"]
    sdata=idcardgenerate.objects.filter(idcard_number=uidcard)
    # to display error
    if(len(sdata)>0):
        return render(request,"employeeselaryerror.html")
    else:
        #insertion in database(object colling)
        uinser=idcardgenerate()
        #--------------------------
        uinser.idcard_number=uidcard
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
#idcard fetch retriveing data from database
def idcardfetchdata(request):
    iddata=request.POST["idcard"]
    carddata=idcardgenerate.objects.filter(idcard_number=iddata)
    if(len(carddata)>0):
        return render(request,'idcardfetchsuccess.html',{"idlist":carddata})
    else:
       return render(request,'errorpage.html')
#--------------------------------------------------
def studentfeesretrive(request):
    return render(request,'studentfeesretrive.html')
def employeeselaryretrive(request):
    return render(request,'employeeselaryretrive.html')
def idcardfetch(request):
    return render(request,'idcardfetch.html')
def studentprofile(request):
    return render(request,'studentprofile.html')
def employeeprofile(request):
    return render(request,'employeeprofile.html')
def studentregistrationfetch(request):
    return render(request,'studentregistrationfetch.html')
def enquarifetch(request):
    return render(request,'enquarifetch.html')
def sturegistration(request):
    return render(request,'sregistration.html')
#------------------------------------------------
#views for admin registration
def admregistration(request):
    return render(request,'aregistration.html')
#view for admin registration check
def adminregistrationcheck(request):
    aid=request.POST["id"]
    apass=request.POST["pass"]
    arole=request.POST["role"]
    aname=request.POST["name"]
    afname=request.POST["father"]
    aaddress=request.POST["address"]
    aqualification=request.POST["qualification"]
    aage=request.POST["age"]
    amobile=request.POST["mobile"]
    aemail=request.POST["email"]
    data=adminregistration.objects.filter(admin_id=aid)
    # to display error
    if(len(data)>0):
        return render(request,"employeeerror.html")
    else:
        #insertion in database(object colling)
        ainser=adminregistration()
        #--------------------------
        ainser.admin_id=aid
        ainser.password=apass
        ainser.admin_name=aname
        ainser.father_name=afname
        ainser.address=aaddress
        ainser.qualification=aqualification
        ainser.age=aage
        ainser.mobile=amobile
        ainser.email=aemail
        ainser.workrole=arole
        #for savedata after insertion
        ainser.save()
        #---------------------------
        return render(request,"empregistrationsuccess.html")
#-----------------------------------------------
def empregistration(request):
    return render(request,'eregistration.html')
#student registration insertion operation
#view for student registration check
def empregistrationcheck(request):
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
    # data=employeeregistration.objects.filter(stdid=sid)
    data=employeeregistration.objects.filter(stdid=eid)
    # to display error
    if(len(data)>0):
        return render(request,"employeeerror.html")
    else:
        #insertion in database(object colling)
        inser=employeeregistration()
        #--------------------------
        inser.stdid=eid
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
        return render(request,"empregistrationsuccess.html")

#----------------------------------------------
def log(request):
    request.session["username"]=""
    return render(request,'homepage.html')
#------------------------------------------------
def employeeregistrationfetch(request):
    return render(request,'employeeregistrationfetch.html')
def adminlogout(request):
    return render(request,'adminlogout.html')
def adminpage(request):
    return render(request,'adminpage.html')
def companyname(request):
    return render(request,'companyname.html')
def dashboard(request):
    return render(request,'dashboard.html')
def main(request):
    return render(request,'main.html')
def adminindexpage(request):
    return render(request,'adminindex.html')
#----------------------------------------------------
#employee profile 
def eprofile(request):
    return render(request,'employeeprofile1.html')
def eprofilecheck(request):
    eroll=request.POST["roll"]
    ename=request.POST["name"]
    efname=request.POST["father"]
    eaddress=request.POST["address"]
    equalification=request.POST["qualification"]
    eage=request.POST["age"]
    emobile=request.POST["mobile"]
    eemail=request.POST["email"]
    etsubject=request.POST["subjects"]
    epresenting=request.POST["emplpresenting"]
    eperform=request.POST["emplperformance"]
    eimg=request.FILES["imgemp"]
    data=emprofile.objects.filter(employees_id=eroll)
    # to display error
    if(len(data)>0):
        return render(request,"emperror.html")
    else:
        #insertion in database(object colling)
        einser=emprofile()
        #--------------------------
        einser.employees_id=eroll
        einser.employee_name=ename
        einser.father_name=efname
        einser.address=eaddress
        einser.qualification=equalification
        einser.age=eage
        einser.mobile=emobile
        einser.email_id=eemail
        einser.teaching_subject=etsubject
        einser.presinting=epresenting
        einser.performance=eperform
        einser.emplimage=eimg
        #for savedata after insertion
        einser.save()
        #---------------------------
        return render(request,"eregistrationsuccess.html")
#employee profile fetch
def eprofilefetch(request):
    return render(request,"employeeprofilefetch.html")
def eprofilefetchsuccess(request):
    idempl=request.POST['emplid']
    data=emprofile.objects.filter(employees_id=idempl)
    if(len(data)>0):
        return render(request,"employeeprofilefetchsuccess.html",{"profile":data})
    else:
        return render(request,"")
#for employeefetch for adminpage
def emplprofilefetch(request):
    return render(request,"empprofilefetch.html")
def emplprofilefetchsuccess(request):
    idempl=request.POST['emplid']
    data=emprofile.objects.filter(employees_id=idempl)
    if(len(data)>0):
        return render(request,"empprofilefetchsuccess.html",{"profile":data})
    else:
        return render(request,"")
#----------------------------------------------------
def updateadminforms(request):
    return render(request,"updateadmin.html")
#student updation 
def updateadmincheck(request):
    if request.method=="POST":
         admid=request.POST['adminsid']
         adatas=request.POST['adminselect']
         if(adatas=="name"):
            return render(request,"admupdatename.html",{"adminsid":admid})
         elif(adatas=="fathername"):
            return render(request,"admupdatefathername.html",{"adminsid":admid})
         elif(adatas=="age"):
            return render(request,"admupdateage.html",{"adminsid":admid})
         elif(adatas=="role"):
            return render(request,"admupdaterole.html",{"adminsid":admid})
         elif(adatas=="qualification"):
            return render(request,"admupdatequalification.html",{"adminsid":admid})
         elif(adatas=="address"):
            return render(request,"admupdateaddress.html",{"adminsid":admid})
         elif(adatas=="mobile"):
            return render(request,"admupdatemobile.html",{"adminsid":admid})
         elif(adatas=="email"):
            return render(request,"admupdateemail.html",{"adminsid":admid})
         elif(adatas=="password"):
            return render(request,"admupdatepassword.html",{"adminsid":admid})
    else:
        return render(request,'updateadmin.html')
#view for update check
#-----------------------------------------------------------------------------
###############################################################################
def aupdateagecheck(request):
    aids=request.POST["aid"]
    adage=request.POST["aage"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(age=adage)
        return render(request,"updateaagesuccess.html",{"AGE":adage,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdatenamecheck(request):
    aidn=request.POST["aid"]
    adname=request.POST["aname"]
    if(len(adminregistration.objects.filter(admin_id=aidn))>0):
        data=adminregistration.objects.filter(admin_id=aidn).update(admin_name=adname)
        return render(request,"updateanamesuccess.html",{"NAME":adname,"SID":aidn})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdateaddresscheck(request):
    aids=request.POST["aid"]
    adaddress=request.POST["aaddress"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(address=adaddress)
        return render(request,"updateaaddresssuccess.html",{"ADDRESS":adaddress,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdatequalificationcheck(request):
    aidq=request.POST["aid"]
    adquali=request.POST["aqualification"]
    if(len(adminregistration.objects.filter(admin_id=aidq))>0):
        data=adminregistration.objects.filter(admin_id=aidq).update(qualification=adquali)
        return render(request,"updateaqualificationsuccess.html",{"QUALIFICATION":adquali,"SID":aidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def aupdatemobilecheck(request):
    aids=request.POST["aid"]
    admobile=request.POST["amobile"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(mobile=admobile)
        return render(request,"updateamobilesuccess.html",{"MOBILE":admobile,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdateemailcheck(request):
    aidq=request.POST["aid"]
    ademail=request.POST["aemail"]
    if(len(adminregistration.objects.filter(admin_id=aidq))>0):
        data=adminregistration.objects.filter(admin_id=aidq).update(email=ademail)
        return render(request,"updateaemailsuccess.html",{"EMAIL":ademail,"SID":aidq})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------------
def aupdatepasswordcheck(request):
    aids=request.POST["aid"]
    adpassword=request.POST["apass"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(password=adpassword)
        return render(request,"updateapasswordsuccess.html",{"PASSWORD":adpassword,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdateworkrolecheck(request):
    aids=request.POST["aid"]
    adrole=request.POST["arole"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(workrole=adrole)
        return render(request,"updatearolesuccess.html",{"PASSWORD":adrole,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
def aupdatefathernamecheck(request):
    aids=request.POST["aid"]
    adfname=request.POST["afname"]
    if(len(adminregistration.objects.filter(admin_id=aids))>0):
        data=adminregistration.objects.filter(admin_id=aids).update(father_name=adfname)
        return render(request,"updateafathernamesuccess.html",{"FATHER":adfname,"SID":aids})
    else:
        return render(request,"updateerror.html")
#-----------------------------------------------------------
