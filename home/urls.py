from django.urls import path
from . import views
# create urls
app_name='home'
urlpatterns=[
      path('homepage/',views.homepage,name='homepage'),
      #login page
      path('loginpage/',views.logins,name='loginpage'),
      #-------------------idcard form------------------- 
      path('idform/',views.idform,name='idform'),
      path('idformcheck/',views.idformcheck),
      path('idformfetch/',views.idformfetch,name='idformfetch'),
      path('idformfetchdata/',views.idformfetchdata),
      #update idcard form
      path('updateidcardforms/',views.updateidcardforms,name='updateidcardforms'),
      path('idcardupdatecheck/',views.idcardupdatecheck),
      #-----------
      path('idpdateagecheck/',views.idpdateagecheck),
      path('idpdatenamecheck/',views.idpdatenamecheck),
      path('idupdatefathernamecheck/',views.idupdatefathernamecheck),
      path('idupdateaddresscheck/',views.idupdateaddresscheck),
      path('idupdatequalificationcheck/',views.idupdatequalificationcheck),
      path('idupdatemobilecheck/',views.idupdatemobilecheck),
      path('idupdateemailcheck/',views.idupdateemailcheck),
      path('idupdatepasswordcheck/',views.idupdatepasswordcheck),
      path('idupdategendercheck/',views.idupdategendercheck),
      path('idupdatesessioncheck/',views.idupdatesessioncheck),
      path('idupdaterolecheck/',views.idupdaterolecheck),
      #delete idcard details
      path('deleteiddata/',views.deleteiddata,name='deleteiddata'),
      path('deleteidcheck/',views.deleteidcheck),
    #---------------------------------------------------------
    #-------------------------------------------------------
      path('idcheck/',views.idcheck),
      #--------------------------------------
      #enquari data
      path('enquaricheck/',views.enquaricheck),
      #enquari fetch 
      path('enquarifetch/',views.enquarifetch,name='enquarifetch'),
      path('enquarifetchdata/',views.enquarifetchdata),  
      #---------------------------------------------------
      path('studentpage/',views.studentspage,name='studentpage'),
      path('about/',views.about,name='about'),
      path('contect/',views.contect,name='contect'),
      path('course/',views.course,name='course'),
      path('course1/',views.course1,name='course1'),
      path('gellary/',views.gellary,name='gellary'),
      path('ourtrainer/',views.ourtrainer,name='ourtrainer'),
      path('service/',views.service,name='service'),
      #urls for employeepage
      path('service1/',views.service1,name='service1'),
      #for homepage
      path('landdeling/',views.landdeling,name='landdeling'),
      path('construction/',views.constructions,name='construction'),
      #employee page
      path('emplogin/',views.emplogin,name='emplogin'),
      path('ergistation/',views.ergistation,name='ergistation')
      ]
