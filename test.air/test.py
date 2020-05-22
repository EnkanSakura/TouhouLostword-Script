# -*- encoding=utf8 -*-

from airtest.core.api import *

auto_setup(__file__)

while not exists(Template(r"tpl1589988798775.png", threshold=0.8, record_pos=(0.275, -0.195), resolution=(2244, 1080))):
    sleep(2)
touch([1574, 256])  #选择关卡
sleep(6)
touch([1882, 935])  #点击出发
sleep(20)
while not(exists(Template(r"tpl1590128884316.png", threshold=0.8, record_pos=(0.275, -0.195), resolution=(2244, 1080)))):  #判断是否进入关卡，保留
    sleep(2)

touch([2082, 799])  #打开技能栏
sleep(0.8)  #等待打开技能栏**
touch([557, 874])   #点击角色1的1技能
sleep(0.6)  #等待技能信息出现**
touch([1420, 825])  #点击决定
sleep(0.6)  #等待技能信息消失**
touch([706, 874])   #点击角色1的2技能
sleep(0.6)  #等待技能信息出现**
touch([1420, 825])  #点击决定
sleep(0.6)  #等待技能信息消失**
touch([2080, 799])  #关闭技能栏
sleep(0.8)  #等待关闭技能栏**

touch([1987, 608], times=3) #graze
sleep(0.3)  #缓冲时间**
touch([1858, 860])  #boost
sleep(0.3)  #缓冲时间**

touch([347, 709])   #打开符卡栏
sleep(0.8)  #等待打开符卡栏**
touch([1753, 326])  #使用5号符卡
sleep(1.0)  #等待符卡选中动画结束**
sleep(15)   #等待战斗动画

while not(exists(Template(r"tpl1590129319715.png", record_pos=(0.0, -0.142), resolution=(2244, 1080)))):    #判断是否进入结算，保留
    sleep(2)
touch([746, 401], times=5)  #点击屏幕空位
sleep(5)    #等待回到选关菜单
