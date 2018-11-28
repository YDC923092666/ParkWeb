from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^accounts/login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),

    #修改密码
    url(r'^changepassword/$', views.ChangePassword, name='changepassword'),

    #主页
    url(r'^$', views.Index, name='index'),
    url(r'^index/getindextable1/$', views.GetIndexTable1, name='getindextable1'),
    url(r'^index/getindextable2/$', views.GetIndexTable2, name='getindextable2'),
    url(r'^index/getindextable3/$', views.GetIndexTable3, name='getindextable3'),
    url(r'^index/getindextable4/$', views.GetIndexTable4, name='getindextable4'),
    url(r'^index/getindextable5/$', views.GetIndexTable5, name='getindextable5'),
    url(r'^index/getindextable6/$', views.GetIndexTable6, name='getindextable6'),
    url(r'^index/gettable1detailinfo/$', views.GetTable1DetailInfo, name='gettable1detailinfo'),
    url(r'^index/gettable3detailinfo/$', views.GetTable3DetailInfo, name='gettable3detailinfo'),
    url(r'^index/gettable5detailinfo/$', views.GetTable5DetailInfo, name='gettable5detailinfo'),

    #我的片区
    url(r'^myarea/$', views.MyArea, name='myarea'),
    url(r'^myarea/myareashoufeiyuan/$', views.MyAreaShoufeiyuan, name='myshoufeiyuan'),

    #停车场管理
    url(r'^mypark/$', views.MyAreaPark, name='mypark'),
    url(r'^getmyparktable/$', views.MyAreaGetParkTable, name='getmyparktable'),
    url(r'^mypark/addpark/$', views.MyAreaAddPark, name='addpark'),
    url(r'^mypark/editpark/$', views.MyAreaEditPark, name='editpark'),
    url(r'^mypark/deletepark/$', views.MyAreaDeletePark, name='deletepark'),

    #硬件管理
    url(r'^myhardwarepos/$', views.MyHardwarePOS, name='myhardwarepos'),
    url(r'^getmyhardwarepostable/$', views.GetMyHardwarePosTable, name='getmyhardwarepostable'),
    url(r'^myhardwarepos/addpos/$', views.MyHardwareAddPOS, name='addpos'),
    url(r'^myhardwarepos/editpos/$', views.MyHardwareEditPOS, name='editpos'),
    url(r'^myhardwarepos/deletepos/$', views.MyHardwareDeletePOS, name='deletepos'),
    url(r'^myhardwarepos/searchpos/$', views.MyHardwareSearchPOS, name='searchpos'),
    url(r'^myhardwarepos/checkposid/$', views.MyHardwareCheckPOSID, name='checkposid'), # 查重ID
    url(r'^myhardwarepos/checkpossn/$', views.MyHardwareCheckPOSSN, name='checkpossn'), # 查重SN

    url(r'^myhardwaresim/$', views.MyHardwareSIM, name='myhardwaresim'),
    url(r'^getmyhardwaresimtable/$', views.GetMyHardwareSIMTable, name='getmyhardwaresimtable'),
    url(r'^myhardwaresim/addsim/$', views.MyHardwareAddSIM, name='addsim'),
    url(r'^myhardwaresim/editsim/$', views.MyHardwareEditSIM, name='editsim'),
    url(r'^myhardwaresim/deletesim/$', views.MyHardwareDeleteSIM, name='deletesim'),
    url(r'^myhardwaresim/checkiccid/$', views.MyHardwareCheckICCID, name='checkiccid'), # 查重ICCID



    #我的审核
    url(r'^myreview/$', views.MyReview, name='myreview'),
    url(r'^myreview/getberthtable/$', views.MyReviewGetBerthTable, name='GetBerthTable'),
    url(r'^myreview/getberthtable/nopass/$', views.MyReviewTaBle1NoPass, name='nopass'),
    url(r'^myreview/getberthtable/pass/$', views.MyReviewTaBle1Pass, name='pass'),
    url(r'^myreview/getmantable/$', views.MyReviewGetManTable, name='getmantable'),
    url(r'^myreview/getmantable/nopass/$', views.MyReviewTaBle2NoPass, name='myareashoufeiyuannopass'),
    url(r'^myreview/getmantable/pass/$', views.MyReviewTaBle2Pass, name='myareashoufeiyuanpass'),
    url(r'^myreview/getparktable/$', views.MyReviewGetParkTable, name='getparktable'),
    url(r'^myreview/getparkntable/nopass/$', views.MyReviewTaBle3NoPass, name='myareaparknopass'),
    url(r'^myreview/getparktable/pass/$', views.MyReviewTaBle3Pass, name='myareaparkpass'),
]
