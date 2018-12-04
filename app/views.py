from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from app.forms import LoginForm
from app.models import Berth,Area,UserInfo,ShowBerth,Shoufeiyuan, Park, POS, SIM

from datetime import datetime
import json
import os

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #验证用户名和密码
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                result = 'success'
            else:
                result = 'failed'
        else:
            result = 'error'
        return HttpResponse(result)
    elif request.method == 'GET':
        form = LoginForm(request.GET)
        return render(request, 'login.html', {'form': form})

@login_required()
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required()
def ChangePassword(request):
    if request.method == 'GET':
        return render(request,'changepassword.html',locals())
    elif request.method == 'POST':
        username = request.user.username
        newPassword = request.POST.get('newpassword')
        user = User.objects.get(username=username)
        user.set_password(newPassword)
        user.save()
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def Index(request):
    if request.method == 'GET':
        return render(request,'index.html',locals())

@login_required()
def GetIndexTable1(request):
    if request.method == 'GET':
        li = list(ShowBerth.objects.filter(isLastest=True).\
                  values('area__name','class1','class2','class3','inRoadTotalNumber','parkingLotNumber','controlclass1',
                         'controlclass2','controlclass3','remainclass1','remainclass2','remainclass3')
                  .order_by('area_id'))
        all_li = Berth.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def GetIndexTable2(request):
    if request.method == 'GET':
        li = list(ShowBerth.objects.filter(isLastest=True).\
            values('inRoadTotalNumber','controlTotalNumber','remainTotalNumber','parkingLotNumber','area__name').order_by('area_id'))
        all_li = Berth.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def GetIndexTable3(request):
    if request.method == 'GET':
        li = list(ShowBerth.objects.filter(isLastest=True).\
                  values('diciInclass1','diciInclass2','diciInclass3','area__name','diciTotalNumber').order_by('area_id'))
        all_li = Berth.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def GetIndexTable4(request):
    if request.method == 'GET':
        allcount1 = 0 # 直营泊位总数
        li2 = []
        try:
            li1 = list(ShowBerth.objects.filter(isLastest=True).exclude(area__name__contains='俊成').values())
            for i in li1:
                allcount1 += int(i['inRoadTotalNumber'])
        except:
            allcount1=None
        try:
            allcount2= ShowBerth.objects.filter(isLastest=True,area__name__contains='俊成').values()[0]['inRoadTotalNumber']
        except:
            allcount2=None
        if(allcount1):
            dic1={'type': '直营','allcount': allcount1}
            li2.append(dic1)
        if(allcount2):
            dic2={'type': '俊成','allcount': allcount2}
            li2.append(dic2)
        count = len(li2)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li2
        }
        return JsonResponse(data)

@login_required()
def GetIndexTable5(request):
    if request.method == 'GET':
        li = list(Shoufeiyuan.objects.filter(isPassed=True,isLastest=True).\
                  values('maninclass1','maninclass2','maninclass3','area__name','manTotalNumber').order_by('area_id'))
        all_li = Berth.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def GetIndexTable6(request):
    if request.method == 'GET':
        page = int(request.GET.get('page'))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit - 1
        if start < 0:
            start = 0
        end = page * limit
        li = list(Park.objects.all().values()[start:end])
        all_li = Park.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def GetTable1DetailInfo(request):
    if request.method == 'GET':
        area=request.GET.get('area__name')
        data = ShowBerth.objects.filter(isLastest=True,area__name=area).\
            values('area__name','createTime','createUser__username','passUser__username','passTime')
        return render(request,'index_showtabledetailinfo.html',locals())

@login_required()
def GetTable3DetailInfo(request):
    if request.method == 'GET':
        area=request.GET.get('area__name')
        data = ShowBerth.objects.filter(isLastest=True,area__name=area).\
            values('area__name','createTime','createUser__username','passUser__username','passTime')
        return render(request,'index_showtabledetailinfo.html',locals())

@login_required()
def GetTable5DetailInfo(request):
    if request.method == 'GET':
        area=request.GET.get('area__name')
        data = Shoufeiyuan.objects.filter(isPassed=True,isLastest=True,area__name=area).\
            values('area__name','createTime','createUser__username','passUser__username','passTime')
        return render(request,'index_showtabledetailinfo.html',locals())

@login_required()
@permission_required('app.can_edit')
def MyArea(request):
    if request.method == 'GET':
        username = request.user.username
        areainfo = UserInfo.objects.filter(user__username=username)
        area = areainfo.values('area__name')[0]['area__name']
        try:
            data = ShowBerth.objects.filter(area__name=area,isLastest=True)[0]
        except:
            data = []
        return render(request, 'myarea.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        areaid = UserInfo.objects.filter(user__username=username).values('area__id')[0]['area__id']
        area = Area.objects.get(id=areaid)
        class1 = int(request.POST.get('class1'))  # 一类区泊位总数
        class2 = int(request.POST.get('class2'))
        class3 = int(request.POST.get('class3'))
        controlclass1 = int(request.POST.get('controlclass1'))  # 一类区在管泊位数
        controlclass2 = int(request.POST.get('controlclass2'))
        controlclass3 = int(request.POST.get('controlclass3'))
        diciInclass1 = int(request.POST.get('diciInclass1'))
        diciInclass2 = int(request.POST.get('diciInclass2'))
        diciInclass3 = int(request.POST.get('diciInclass3'))

        if (request.POST.get('parkinglotnumber')):
            parkinglotnumber = int(request.POST.get('parkinglotnumber'))
        else:
            parkinglotnumber = 0

        Berth.objects.create(
            class1=class1,
            class2=class2,
            class3=class3,
            parkingLotNumber=parkinglotnumber,
            controlclass1=controlclass1,
            controlclass2=controlclass2,
            controlclass3=controlclass3,
            diciInclass1=diciInclass1,
            diciInclass2=diciInclass2,
            diciInclass3=diciInclass3,
            createUser=user,
            createTime=datetime.now,
            area=area
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
@permission_required('app.can_edit')
def MyAreaShoufeiyuan(request):
    if request.method == 'GET':
        username = request.user.username
        areainfo = UserInfo.objects.filter(user__username=username)
        area = areainfo.values('area__name')[0]['area__name']
        try:
            data = Shoufeiyuan.objects.filter(area__name=area,isPassed=True,isLastest=True)[0]
        except:
            data = []
        return render(request, 'myareashoufeiyuan.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        areaid = UserInfo.objects.filter(user__username=username).values('area__id')[0]['area__id']
        area = Area.objects.get(id=areaid)
        maninclass1 = int(request.POST.get('maninclass1'))
        maninclass2 = int(request.POST.get('maninclass2'))
        maninclass3 = int(request.POST.get('maninclass3'))
        manTotalNumber = maninclass1+maninclass2+maninclass3

        Shoufeiyuan.objects.create(
            maninclass1=maninclass1,
            maninclass2=maninclass2,
            maninclass3=maninclass3,
            manTotalNumber=manTotalNumber,
            createTime="",
            createUser=user,
            area=area
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
@permission_required('app.can_review')
def MyReview(request):
    if request.method == 'GET':
        return render(request, 'myreview.html', locals())

@login_required()
@permission_required('app.can_review')
def MyReviewGetBerthTable(request):
    if request.method == 'GET':
        li = list(Berth.objects.all().\
                  values('id','area__name','class1','class2','class3','parkingLotNumber',
                         'createTime','createUser__username','diciInclass1','diciInclass2','diciInclass3',
                         'controlclass1','controlclass2','controlclass3')\
                  .order_by('id'))
        all_li = Berth.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
@permission_required('app.can_review')
def MyReviewTaBle1NoPass(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Berth.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
@permission_required('app.can_review')
def MyReviewTaBle1Pass(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        berthinfo = Berth.objects.filter(id=id).values()[0]
        username = request.user.username
        passUser = User.objects.get(username=username)

        class1 = berthinfo['class1']
        class2 = berthinfo['class2']
        class3 = berthinfo['class3']
        inRoadTotalNumber = class1+class2+class3

        controlclass1 = berthinfo['controlclass1']
        controlclass2 = berthinfo['controlclass2']
        controlclass3 = berthinfo['controlclass3']
        controlTotalNumber = controlclass1 + controlclass2 + controlclass3

        remainclass1 = class1 - controlclass1
        remainclass2 = class2 - controlclass2
        remainclass3 = class3 - controlclass3
        remainTotalNumber = inRoadTotalNumber - controlTotalNumber

        diciInclass1 = berthinfo['diciInclass1']
        diciInclass2 = berthinfo['diciInclass2']
        diciInclass3 = berthinfo['diciInclass3']
        diciTotalNumber = diciInclass1+diciInclass2+diciInclass3

        parkingLotNumber = berthinfo['parkingLotNumber']

        area = Area.objects.filter(id=berthinfo['area_id'])[0]
        createUser = User.objects.filter(id=berthinfo['createUser_id'])[0]
        createTime = berthinfo['createTime']

        # 将这条审核信息从Berth表里删除
        Berth.objects.filter(id=id).delete()
        # 将原有isLastest为True的泊位信息的isLastest置为False，表示该信息已不再是最新，弃用
        ShowBerth.objects.filter(area=area,isLastest=True).update(isLastest=False)

        # 创建最新的泊位信息
        ShowBerth.objects.create(
            class1=class1,
            class2=class2,
            class3=class3,
            inRoadTotalNumber=inRoadTotalNumber,
            controlclass1=controlclass1,
            controlclass2=controlclass2,
            controlclass3=controlclass3,
            controlTotalNumber=controlTotalNumber,
            remainclass1=remainclass1,
            remainclass2=remainclass2,
            remainclass3=remainclass3,
            remainTotalNumber=remainTotalNumber,
            diciInclass1=diciInclass1,
            diciInclass2=diciInclass2,
            diciInclass3=diciInclass3,
            diciTotalNumber=diciTotalNumber,
            parkingLotNumber=parkingLotNumber,
            createTime=createTime,
            createUser=createUser,
            area=area,
            passUser=passUser,
            passTime=datetime.now(),
            isLastest=True
        )
        return HttpResponse("OK")

@login_required()
@permission_required('app.can_review')
def MyReviewGetManTable(request):
    if request.method == 'GET':
        li = list(Shoufeiyuan.objects.filter(isPassed=False).\
                  values('id','area__name','maninclass1','maninclass2','maninclass3',
                         'createTime','createUser__username')\
                  .order_by('id'))
        all_li = Shoufeiyuan.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
@permission_required('app.can_review')
def MyReviewTaBle2NoPass(request):
        id = request.POST.get('id')
        Shoufeiyuan.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
@permission_required('app.can_review')
def MyReviewTaBle2Pass(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        username = request.user.username
        passUser = User.objects.get(username=username)
        area_id = Shoufeiyuan.objects.filter(id=id).values('area__id')[0]['area__id']
        area = Area.objects.filter(id=area_id)

        # 将原有isLastest为True的泊位信息的isLastest置为False，表示该信息已不再是最新，弃用
        try:
            Shoufeiyuan.objects.filter(area=area, isLastest=True).update(isLastest=False)
        finally:
            Shoufeiyuan.objects.filter(id=id).update(
                passTime=datetime.now(),
                passUser=passUser,
                isPassed=True,
                isLastest=True,
            )
        return HttpResponse("OK")

@login_required()
def MyReviewGetParkTable(request):
    if request.method == 'GET':
        li = list(Park.objects.filter(isPassed=False).\
                  values('id','area__name','berthNumber','cameraNumber','createTime',
                         'createUser','createUser__username','inCount','isInSystem','name',
                         'outCount','reason')\
                  .order_by('id'))
        all_li = Park.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def MyReviewTaBle3NoPass(request):
        id = request.POST.get('id')
        Park.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
def MyReviewTaBle3Pass(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        username = request.user.username
        passUser = User.objects.get(username=username)

        Park.objects.filter(id=id).update(
            passTime=datetime.now(),
            passUser=passUser,
            isPassed=True,
        )
        return HttpResponse("OK")

@login_required()
@permission_required('app.can_edit_park')
def MyAreaPark(request):
    if request.method == 'GET':
        return render(request, 'myareapark.html', locals())

@login_required()
def MyAreaGetParkTable(request):
    if request.method == 'GET':
        page = int(request.GET.get('page'))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit - 1
        if start < 0:
            start = 0
        end = page * limit
        li = list(Park.objects.all().values().order_by('id')[start:end])
        all_li = Park.objects.all()
        count = len(all_li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': li
        }
        return JsonResponse(data)

@login_required()
def MyAreaAddPark(request):
    if request.method == 'GET':
        return render(request, 'myareapark_addmodal.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        createUser = User.objects.get(username=username)

        name = request.POST.get('name')
        company = request.POST.get('company')
        fibre = request.POST.get('fibre')
        cameraBrand = request.POST.get('cameraBrand')
        wentongcameraNumber = request.POST.get('wentongcameraNumber')
        jieshuncameraNumber = request.POST.get('jieshuncameraNumber')
        ketuocameraNumber = request.POST.get('ketuocameraNumber')
        explain = request.POST.get('explain')
        isInSystem = request.POST.get('isInSystem')
        reason = request.POST.get('reason')
        LEDNumber = request.POST.get('LEDNumber')
        daozhaBrand = request.POST.get('daozhaBrand')
        daozhaNumber = request.POST.get('daozhaNumber')
        stationNumber = request.POST.get('stationNumber')
        computerNumber = request.POST.get('computerNumber')
        jiankongNumber = request.POST.get('jiankongNumber')

        Park.objects.create(
            name=name,
            company=company,
            fibre=fibre,
            cameraBrand=cameraBrand,
            wentongcameraNumber=wentongcameraNumber,
            jieshuncameraNumber=jieshuncameraNumber,
            ketuocameraNumber=ketuocameraNumber,
            explain=explain,
            isInSystem=isInSystem,
            reason=reason,
            LEDNumber=LEDNumber,
            daozhaBrand=daozhaBrand,
            daozhaNumber=daozhaNumber,
            stationNumber=stationNumber,
            computerNumber=computerNumber,
            jiankongNumber=jiankongNumber,
            createTime='',
            createUser=createUser,
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyAreaEditPark(request):
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            data = Park.objects.filter(id=id)[0]
        except:
            data = []
        return render(request, 'myareapark_editmodal.html', locals())
    elif request.method == 'POST':  #点击模态框的确认修改按钮
        username = request.user.username
        createUser = User.objects.get(username=username)

        id = int(request.POST.get('id'))

        name = request.POST.get('name')
        company = request.POST.get('company')
        fibre = request.POST.get('fibre')
        cameraBrand = request.POST.get('cameraBrand')
        wentongcameraNumber = request.POST.get('wentongcameraNumber')
        jieshuncameraNumber = request.POST.get('jieshuncameraNumber')
        ketuocameraNumber = request.POST.get('ketuocameraNumber')
        explain = request.POST.get('explain')
        isInSystem = request.POST.get('isInSystem')
        reason = request.POST.get('reason')
        LEDNumber = request.POST.get('LEDNumber')
        daozhaBrand = request.POST.get('daozhaBrand')
        daozhaNumber = request.POST.get('daozhaNumber')
        stationNumber = request.POST.get('stationNumber')
        computerNumber = request.POST.get('computerNumber')
        jiankongNumber = request.POST.get('jiankongNumber')

        Park.objects.filter(id=id).update(
            name=name,
            company=company,
            fibre=fibre,
            cameraBrand=cameraBrand,
            wentongcameraNumber=wentongcameraNumber,
            jieshuncameraNumber=jieshuncameraNumber,
            ketuocameraNumber=ketuocameraNumber,
            explain=explain,
            isInSystem=isInSystem,
            reason=reason,
            LEDNumber=LEDNumber,
            daozhaBrand=daozhaBrand,
            daozhaNumber=daozhaNumber,
            stationNumber=stationNumber,
            computerNumber=computerNumber,
            jiankongNumber=jiankongNumber,
            createTime=datetime.now(),
            createUser=createUser,
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyAreaDeletePark(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Park.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
@permission_required('app.can_edit_hardware')
def MyHardwarePOS(request):
    if request.method == 'GET':
        return render(request, 'myhardware_pos.html', locals())


@login_required()
def GetMyHardwarePosTable(request):
    if request.method == 'GET':
        page = int(request.GET.get('page'))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit - 1
        if start < 0:
            start = 0
        end = page * limit

        # 查询条件，用于表格重载
        dic = {}
        status = request.GET.get('status')
        people = request.GET.get('people')
        POS_ID = request.GET.get('POS_ID')
        POS_SN = request.GET.get('POS_SN')
        POS_Model = request.GET.get('POS_Model')

        if status:
            dic['status'] = status
        if people:
            dic['people__contains'] = people
        if POS_ID:
            dic['POS_ID__contains'] = POS_ID
        if POS_SN:
            dic['POS_SN__contains'] = POS_SN
        if POS_Model:
            dic['POS_Model'] = POS_Model

        try:
            data = list(POS.objects.filter(**dic).values().order_by('id')[start:end])
            for i in data:
                for key, value in i.items():
                    if type(value) == bool and value:
                        i[key] = "有"
                    elif type(value) == bool and not value:
                        i[key] = "无"
        except:
            data = []

        li = list(POS.objects.all())
        count = len(li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': data
        }
        return JsonResponse(data)


@login_required()
def MyHardwareAddPOS(request):
    if request.method == 'GET':
        return render(request, 'myhardware_pos_addmodal.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        createUser = User.objects.get(username=username)

        status = request.POST.get('status')
        people = request.POST.get('people')
        POS_Model = request.POST.get('POS_Model')
        POS_ID = request.POST.get('POS_ID')
        POS_SN = request.POST.get('POS_SN')
        POS_Battery = request.POST.get('POS_Battery')
        POS_Charger = request.POST.get('POS_Charger')
        TF = request.POST.get('TF')
        printer = request.POST.get('printer')
        printer_Charger = request.POST.get('printer_Charger')
        remark = request.POST.get('remark')

        POS.objects.create(
            status=status,
            people=people,
            POS_Model=POS_Model,
            POS_ID=POS_ID,
            POS_SN=POS_SN,
            POS_Battery=POS_Battery,
            POS_Charger=POS_Charger,
            TF=TF,
            printer=printer,
            printer_Charger=printer_Charger,
            remark=remark,
            createUser=createUser,
            changeTime=''
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyHardwareEditPOS(request):
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            data = POS.objects.filter(id=id)[0]
        except:
            data = []
        return render(request, 'myhardware_pos_editmodal.html', locals())
    elif request.method == 'POST':  #点击模态框的确认修改按钮
        username = request.user.username
        createUser = User.objects.get(username=username)

        id = int(request.POST.get('id'))

        status = request.POST.get('status')
        people = request.POST.get('people')
        POS_Model = request.POST.get('POS_Model')
        POS_ID = request.POST.get('POS_ID')
        POS_SN = request.POST.get('POS_SN')
        POS_Battery = request.POST.get('POS_Battery')
        POS_Charger = request.POST.get('POS_Charger')
        TF = request.POST.get('TF')
        printer = request.POST.get('printer')
        printer_Charger = request.POST.get('printer_Charger')
        remark = request.POST.get('remark')

        POS.objects.filter(id=id).update(
            status=status,
            people=people,
            POS_Model=POS_Model,
            POS_ID=POS_ID,
            POS_SN=POS_SN,
            POS_Battery=POS_Battery,
            POS_Charger=POS_Charger,
            TF=TF,
            printer=printer,
            printer_Charger=printer_Charger,
            remark=remark,
            createUser=createUser,
            changeTime=datetime.now()
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyHardwareDeletePOS(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        POS.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
def MyHardwareSearchPOS(request):
    if request.method == 'GET':
        dic = {}
        status = request.GET.get('status')
        people = request.GET.get('people')
        POS_ID = request.GET.get('POS_ID')
        POS_SN = request.GET.get('POS_SN')

        if status:
            dic['status'] = status
        if people:
            dic['people__contains'] = people
        if POS_ID:
            dic['POS_ID__contains'] = POS_ID
        if POS_SN:
            dic['POS_SN__contains'] = POS_SN
        try:
            data = list(POS.objects.filter(**dic).values())
        except:
            data = []

        print(data)
        count = len(data)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': data
        }
        return JsonResponse(data)


@login_required()
def MyHardwareCheckPOSID(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        tmp = POS.objects.filter(POS_ID=data)
        if not tmp:
            result = "OK"
        else:
            result = 'NO'
        ret = {
            'result': result
        }
        return JsonResponse(ret)

@login_required()
def MyHardwareCheckPOSSN(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        tmp = POS.objects.filter(POS_SN=data)
        if not tmp:
            result = "OK"
        else:
            result = 'NO'
        ret = {
            'result': result
        }
        return JsonResponse(ret)

@login_required()
@permission_required('app.can_edit_hardware')
def MyHardwareSIM(request):
    if request.method == 'GET':
        return render(request, 'myhardware_sim.html', locals())


@login_required()
def GetMyHardwareSIMTable(request):
    if request.method == 'GET':
        page = int(request.GET.get('page'))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit - 1
        if start < 0:
            start = 0
        end = page * limit

        # 查询条件，用于表格重载
        dic = {}
        status = request.GET.get('status')
        people = request.GET.get('people')
        SIM_ICCID = request.GET.get('SIM_ICCID')
        SIM_Company = request.GET.get('SIM_Company')

        if status:
            dic['status'] = status
        if people:
            dic['people__contains'] = people
        if SIM_ICCID:
            dic['SIM_ICCID__contains'] = SIM_ICCID
        if SIM_Company:
            dic['SIM_Company__contains'] = SIM_Company

        try:
            data = list(SIM.objects.filter(**dic).values().order_by('id')[start:end])
        except:
            data = []

        li = list(SIM.objects.all())
        count = len(li)
        data = {
            'code': 0,
            'msg': "",
            'count': count,
            'data': data
        }
        return JsonResponse(data)

@login_required()
def MyHardwareAddSIM(request):
    if request.method == 'GET':
        return render(request, 'myhardware_sim_addmodal.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        createUser = User.objects.get(username=username)

        status = request.POST.get('status')
        people = request.POST.get('people')
        SIM_Company = request.POST.get('SIM_Company')
        SIM_ICCID = request.POST.get('SIM_ICCID')
        remark = request.POST.get('remark')

        SIM.objects.create(
            status=status,
            people=people,
            SIM_Company=SIM_Company,
            SIM_ICCID=SIM_ICCID,
            remark=remark,
            createUser=createUser,
            changeTime=''
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyHardwareEditSIM(request):
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            data = SIM.objects.filter(id=id)[0]
        except:
            data = []
        return render(request, 'myhardware_sim_editmodal.html', locals())
    elif request.method == 'POST':  #点击模态框的确认修改按钮
        username = request.user.username
        createUser = User.objects.get(username=username)

        id = int(request.POST.get('id'))

        status = request.POST.get('status')
        people = request.POST.get('people')
        SIM_Company = request.POST.get('SIM_Company')
        SIM_ICCID = request.POST.get('SIM_ICCID')
        remark = request.POST.get('remark')

        SIM.objects.filter(id=id).update(
            status=status,
            people=people,
            SIM_Company=SIM_Company,
            SIM_ICCID=SIM_ICCID,
            remark=remark,
            createUser=createUser,
            changeTime=datetime.now()
        )
        data = {
            'result': 'success'
        }
        return JsonResponse(data)

@login_required()
def MyHardwareDeleteSIM(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SIM.objects.filter(id=id).delete()
        return HttpResponse("OK")

@login_required()
def MyHardwareCheckICCID(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        tmp = SIM.objects.filter(SIM_ICCID=data)
        if not tmp:
            result = "OK"
        else:
            result = 'NO'
        ret = {
            'result': result
        }
        return JsonResponse(ret)