from django.urls import path
from . import views
#----------------------------
#create urls here
app_name='student'
urlpatterns=[
    path('studentpage/',views.studentpage,name='studentpage'),
    path('studentindex/',views.sindex,name='studentindex'),
    path('studentpage2/',views.studentpage2,name='studentpage2'),
    #student registration
    path('studentregistration/',views.student_registration,name='studentregistration'),
    path('sregistration/',views.sregistration,name='sregistration'),
    path('sregistrationcheck/',views.sregistrationcheck),
    #login
    path('slogin/',views.slogin,name='slogin'),
    path('logincheck/',views.logincheck),
    path('studentregistration1/',views.studentregistration,name='studentregistration'),
    #student registration fetch 
    path('studentregistrationfetch/',views.studentregistrationfetch,name='studentregistrationfetch'),
    path('studentsregfetch/',views.studentsregfetch),
    #urls for delete student id
    path('deletedata/',views.deletedata,name='deletedata'),
    path('deletecheck/',views.deletecheck),
    #urls for student update
    path('updatepage/',views.dataupdate,name='updatepage'),
    path('supdatecheck/',views.supdatecheck),
    path('updateforms/',views.updateforms,name='updateforms'),
    #-----------------------------------------------------------------
    path('supdatenamecheck/',views.supdatenamecheck),
    path('supdateaddresscheck/',views.supdateaddresscheck),
    path('supdatequalificationcheck/',views.supdatequalificationcheck),
    path('supdatemobilecheck/',views.supdatemobilecheck),
    path('supdateemailcheck/',views.supdateemailcheck),
    path('supdatepasswordcheck/',views.supdatepasswordcheck),
    #------------------------------------------------------------------
    #student performance 
    #--------for student-----
    path('sperf/',views.sperf,name='sperf'),
    path('sperfcheck/',views.sperfcheck),
    path('sperformancefetch/',views.sperformancefetch,name='sperformancefetch'),
    path('sperformancefetchsuccess/',views.sperformancefetchsuccess),
    #-----------for admin--------
    path('sperformancefetch1/',views.sperformancefetch1,name='sperformancefetch1'),
    path('sperformancefetch1success/',views.sperformancefetch1success),
    #----------------------------------------------------------------
    path('logout/',views.log,name='logout'),
    ]
