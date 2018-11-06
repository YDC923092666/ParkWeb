# -*- coding: utf-8 -*
from django.db import models


#用户和片区的对应关系
class UserInfo(models.Model):
    areaname = models.CharField(max_length=100,default="停车公司")
    user = models.ForeignKey('auth.User')
    area = models.ForeignKey('Area')

    def __str__(self):
        return self.areaname

    class Meta:
        verbose_name = "用户和片区的对应关系"
        verbose_name_plural = verbose_name

# 待审核泊位数
class Berth(models.Model):
    class1 = models.IntegerField(default=0) #一类区总泊位数
    class2 = models.IntegerField(default=0)
    class3 = models.IntegerField(default=0)
    parkingLotNumber = models.IntegerField(default=0) #停车场泊位数
    controlclass1 = models.IntegerField(default=0) #一类区在管泊位数
    controlclass2 = models.IntegerField(default=0)
    controlclass3 = models.IntegerField(default=0)
    diciInclass1 = models.IntegerField(default=0)
    diciInclass2 = models.IntegerField(default=0)
    diciInclass3 = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    createUser = models.ForeignKey('auth.User')
    area = models.ForeignKey('Area')

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "待审核泊位数"
        verbose_name_plural = verbose_name
        ordering = ['createTime']
        permissions = (
            ('can_review', '是否可以审核'),
        )

# 发布泊位数
class ShowBerth(models.Model):
    class1 = models.IntegerField(default=0) #一类区泊位总数
    class2 = models.IntegerField(default=0)
    class3 = models.IntegerField(default=0)
    inRoadTotalNumber = models.IntegerField(default=0) #占道泊位总数
    parkingLotNumber = models.IntegerField(default=0) #停车场泊位总数
    controlclass1 = models.IntegerField(default=0)  # 一类区在管泊位数
    controlclass2 = models.IntegerField(default=0)
    controlclass3 = models.IntegerField(default=0)
    controlTotalNumber = models.IntegerField(default=0) #在管泊位总数
    remainclass1 = models.IntegerField(default=0) #未管一类区泊位总数
    remainclass2 = models.IntegerField(default=0)
    remainclass3 = models.IntegerField(default=0)
    remainTotalNumber = models.IntegerField(default=0)  #未管泊位总数
    diciInclass1 = models.IntegerField(default=0)
    diciInclass2 = models.IntegerField(default=0)
    diciInclass3 = models.IntegerField(default=0)
    diciTotalNumber = models.IntegerField(default=0) #地磁总数
    createTime = models.DateTimeField()
    createUser = models.ForeignKey('auth.User',related_name="createUser")
    passTime = models.DateTimeField(null=True,blank=True)
    passUser = models.ForeignKey('auth.User',related_name="passUser")
    area = models.ForeignKey('Area')
    isLastest = models.BooleanField(default=False)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "发布泊位数"
        verbose_name_plural = verbose_name
        ordering = ['createTime']

# 片区
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "片区"
        verbose_name_plural = verbose_name
        permissions = (
            ('can_edit', '是否可以编辑片区信息'),
        )

#收费员数
class Shoufeiyuan(models.Model):
    maninclass1 = models.IntegerField(default=0)
    maninclass2 = models.IntegerField(default=0)
    maninclass3 = models.IntegerField(default=0)
    manTotalNumber = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    createUser = models.ForeignKey('auth.User', related_name="createShoufeiyuanUser")
    passTime = models.DateTimeField(null=True, blank=True)
    passUser = models.ForeignKey('auth.User', related_name="passShoufeiyuanUser",null=True, blank=True)
    isPassed = models.BooleanField(default=False)
    isLastest = models.BooleanField(default=False)
    area = models.ForeignKey('Area')

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "待审核收费员数"
        verbose_name_plural = verbose_name

# 停车场
class Park(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    fibre = models.IntegerField(default=0)
    cameraBrand = models.CharField(max_length=100) #摄像头品牌
    wentongcameraNumber = models.IntegerField(default=0)
    jieshuncameraNumber = models.IntegerField(default=0)
    ketuocameraNumber = models.IntegerField(default=0)
    explain = models.CharField(max_length=200, null=True, blank=True) #说明
    isInSystem = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, null=True, blank=True) #未接入原因
    LEDNumber = models.IntegerField(default=0)
    daozhaNumber = models.IntegerField(default=0)
    daozhaBrand = models.CharField(max_length=100) #道闸品牌
    stationNumber = models.IntegerField(default=0) #岗亭数量
    computerNumber = models.IntegerField(default=0) #收费电脑数量
    jiankongNumber = models.IntegerField(default=0) #监控探头数量
    createTime = models.DateTimeField(auto_now_add=True)
    createUser = models.ForeignKey('auth.User', related_name="createParkUser")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "停车场"
        verbose_name_plural = verbose_name
        permissions = (
            ('can_edit_park', '是否可以编辑停车场信息'),
        )
