from django.urls import path
from . import views
#----------------------------
#create urls here
app_name='employee'
urlpatterns=[
      path('employeepage/',views.employeepage,name='employee page'),
      path('employeeindex/',views.employeeindex,name='employeeindex'),
      #-------------------------------------------------------------
      #employee login
      path('employeelogin/',views.employeelogin,name='employeelogin'),
      path('loginemployeecheck1/',views.loginemployeecheck1),
      #------------------------------------------------------------
      path('eregistration/',views.eregistration,name='eregistration'),
      path('emregistrationcheck/',views.emregistrationcheck),
      #employee registration fetch 
      path('employeeregistrationfetch/',views.employeeregistrationfetch,name='employeeregistrationfetch'),
      path('employeeregfetch/',views.employeeregfetch),
      path('hello/',views.hello,name='hello'),
      #urls for delete student id
      path('deleteemployeedata/',views.deleteemployeedata,name='deleteemployeedata'),
      path('deleteemployeecheck/',views.deleteemployeecheck),
      #urls for update
      path('updateemployeeforms/',views.updateemployeeforms,name='updateemployeeforms'),
      path('updateemployeecheck/',views.updateemployeecheck),
      #-----------------------------------------------------------------
      path('eupdateagecheck/',views.eupdateagecheck),
      path('eupdatenamecheck/',views.eupdatenamecheck),
      path('eupdateaddresscheck/',views.eupdateaddresscheck),
      path('eupdatequalificationcheck/',views.eupdatequalificationcheck),
      path('eupdatemobilecheck/',views.eupdatemobilecheck),
      path('eupdateemailcheck/',views.eupdateemailcheck),
      path('eupdatepasswordcheck/',views.eupdatepasswordcheck),
      path('eupdateworkrolecheck/',views.eupdateworkrolecheck),
      path('eupdatefathernamecheck/',views.eupdatefathernamecheck),
      #----------------------------------------------------------
      #student profile for student page
      path('studentprofile/',views.sprofile,name='studentprofile'),
      path('sprofilecheck/',views.sprofilecheck),
      path('sprofilefetch/',views.sprofilefetch,name='sprofilefetch'),
      path('sprofilefetchsuccess/',views.sprofilefetchsuccess),
      path('sperformance/',views.sperformance,name='sperformance'),
      path('sperformancecheck/',views.sperformancecheck),
      path('studentperformance/',views.studentperformance,name='studentperformance'),
      path('studentperformancecheck/',views.studentperformancecheck),
      #student profile for administration page
      path('stprofilefetch/',views.stprofilefetch,name='stprofilefetch'),
      path('stprofilefetchsuccess/',views.stprofilefetchsuccess),
      #----------------------------------------------------------------
      #logout
      path('logout/',views.log1,name='logout'),
    ]
