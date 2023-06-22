from django.urls import path
from . import views
#----------------------------
#create urls here
app_name='administration'
urlpatterns=[
    path('administrationpage/',views.administrationpage,name='administrationpage'),
    path('deletstudentid/',views.deletstudentid,name='deletstudentid'),
    #---------------------------------------------------
    #delete admin data
    path('deleteadmin/',views.deleteadminpage,name='deleteadmin'),
    path('deleteadmincheck/',views.deleteadmincheck),
    #-------------------------------------------
    path('deleteemployeeid/',views.deletemployeeid,name='deletemployeeid'),
    #---------------------------------------------------------------------
    #urls for delete student fees id
    path('deletefees/',views.deletefees,name='deletefees'),
    path('deletefeescheck/',views.deletefeescheck),
    #-------------------------------------------
    #urls for update
    path('updateadminforms/',views.updateadminforms,name='updateadminforms'),
    path('updateadmincheck/',views.updateadmincheck),
    #-----------------------------------------------------
    #employee selary fetch
    path('employeeselary/',views.employeeselary,name='employeeselary'),
    path('employeeselarycheck/',views.employeeselarycheck),
    path('employeeselaryfetch/',views.employeeselaryfetch),
    #-------------------------------------------------------
    #urls for update employee selary
    path('updateemployeeselaryforms/',views.updateemployeeselaryforms,name='updateemployeeselaryforms'),
    path('updateemployeeselarycheck/',views.updateemployeeselarycheck),
    #-----------------------------------------------------------------
    path('eupdateselarydatecheck/',views.eupdateselarydatecheck),
    path('eupdateselarynamecheck/',views.eupdateselarynamecheck),
    path('eupdateselaryaddresscheck/',views.eupdateselaryaddresscheck),
    path('eupdateselarymonthelycheck/',views.eupdateselarymonthelycheck),
    path('eupdateselarytotalcheck/',views.eupdateselarytotalcheck),
    path('eupdateselarygivencheck/',views.eupdateselarygivencheck),
    path('updateselaryremaningcheck/',views.eupdateselaryremaningcheck),
    path('eupdateselaryrolecheck/',views.eupdateselaryrolecheck),
    #----------------------------------------------------------
    #urls for delete employee selary id
    path('deleteselary/',views.deleteselary,name='deleteselary'),
    path('deleteselarycheck/',views.deleteselarycheck),
    #-------------------------------------------
    #employee profile insertion
    path('employeeprofile/',views.eprofile,name='employeeprofile'),
    path('employeeprofilecheck/',views.eprofilecheck),
    #employee profile fetch
    path('eprofilefetch/',views.eprofilefetch,name='eprofilefetch'),
    path('eprofilefetchsuccess/',views.eprofilefetchsuccess),
    #employee profilefetch for adminpage
    path('empprofilefetch/',views.emplprofilefetch,name='empprofilefetch'),
    path('emplprofilefetchsuccess/',views.emplprofilefetchsuccess),
    #--------------------------------------------------------
    #student fees 
    path('studentfees/',views.studentsfees,name='studentfees'),
    path('studentfeescheck/',views.studentfeescheck),
    path('studentfeesretrivedata/',views.studentfeesretrivedata),
    #student fees update 
    path('updatestudentfeesforms/',views.updatestudentfeesforms,name='updatestudentfeesforms'),
    path('dataupdatecheck/',views.dataupdatecheck),
    path('updatefeesnamecheck/',views.updatefeesnamecheck),
    path('feesaddress/',views.feesaddress),
    path('feescourse/',views.feescourse),
    path('feesadmitiondate/',views.feesadmitiondate),
    path('feestotal/',views.feestotal),
    path('feesgivan/',views.feesgivan),
    path('feesremaning/',views.feesremaning),
    path('feescourseduration/',views.feescourseduration),
    #-----------------------------------------------------------
    #idcard form 
    path('idcardform/',views.idcardform,name='idcardform'),
    path('idcardcheck/',views.idcardcheck),
    path('idcardfetchdata/',views.idcardfetchdata),
    #-------------------------------------------------------
    path('sregistration/',views.sturegistration,name='sregistration'),
    #--------------------------------------------------------
    #employee registration
    path('eregistration/',views.empregistration,name='eregistration'),
    path('empregistrationcheck/',views.empregistrationcheck),
    #---------------------------------------------------------
    #admin registration url
    path('adminregistration/',views.admregistration,name='adminregistration'),
    path('adminregistrationcheck/',views.adminregistrationcheck),
    #--------------------------------------------------------------------------
    path('studentfeesretrive/',views.studentfeesretrive,name='studentfeesretrive'),
    path('idcardfetch/',views.idcardfetch,name='idcardfetch'),
    path('employeeselaryretrive/',views.employeeselaryretrive,name='employeeselaryretrive'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('employeeprofile/',views.employeeprofile,name='employeeprofile'),
    path('studentregistrationfetch/',views.studentregistrationfetch,name='studentregistrationfetch'),
    path('enquarifetch/',views.enquarifetch,name='enquarifetch'),
    #--------------------------------------------------------------
    #employee registration fetch 
    path('employeeregistrationfetch/',views.employeeregistrationfetch,name='employeeregistrationfetch'),
    #------------------------------------------------------------------
    #logout page
    path('logout/',views.log,name='logout'),
    #------------------------------------------------------------------
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('companyname/',views.companyname,name='companyname'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('main/',views.main,name='main'),
    path('adminindex/',views.adminindexpage,name='adminindex'),
    #-----------------------------------------------------------------
    path('aupdateagecheck/',views.aupdateagecheck),
    path('aupdatenamecheck/',views.aupdatenamecheck),
    path('aupdateaddresscheck/',views.aupdateaddresscheck),
    path('aupdatequalificationcheck/',views.aupdatequalificationcheck),
    path('aupdatemobilecheck/',views.aupdatemobilecheck),
    path('aupdateemailcheck/',views.aupdateemailcheck),
    path('aupdatepasswordcheck/',views.aupdatepasswordcheck),
    path('aupdateworkrolecheck/',views.aupdateworkrolecheck),
    path('aupdatefathernamecheck/',views.aupdatefathernamecheck),
    ]

