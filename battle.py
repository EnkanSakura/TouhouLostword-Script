from airtest.core.api import *

Watered = False	#两滴水标记

def graze(t=1): #擦蛋，t为graze次数
    touch([1972, 605],times=t)
    sleep(0.6)

def boost(t=1): #爆发，t为boost次数
    touch([1853, 863],times=t)
    sleep(0.6)

def change():   #换人
    touch([1931, 101])
    sleep(3.0)
    
def spellcard(no):  #符卡，no为卡的序号
    touch([360, 706])
    sleep(0.8)
    if no == 1:
        touch([604, 571])
    elif no == 2:
        touch([857, 466])
    elif no == 3:
        touch([1165, 343])
    elif no == 4:
        touch([1477, 334])
    else:
        touch([1762, 379])
    sleep(2.0)

def skill():    #打开/关闭技能面板
    touch([2075, 790])
    sleep(0.7)

def useskill(r, s): #使用技能，r为角色次序，s为技能次序
    if r == 1:
        if s == 1:
            touch([556, 881])
        elif s == 2:
            touch([688, 890])
        else:
            touch([688, 890])
    elif r == 2:
        if s == 1:
            touch([1076, 877])
        elif s== 2:
            touch([1219, 888])
        else:
            touch([1354, 877])
    else:
        if s == 1:
            touch([1593, 890])
        elif s == 2:
            touch([1733, 881])
        else:
            touch([1862, 879])
    sleep(0.2)
    touch([1416, 831])
    sleep(0.3)

def shoot(s):   #弹幕，s为扩散1或集中2
    if s == 1:
        touch([761, 888])
    else:
        touch([1381, 877])
    sleep(0.4)

def run_away(): #离开战斗（逃げるだよ）
    touch([1193, 38])
    sleep(0.3)
    touch([1886, 967])
    sleep(0.3)
    touch([1328, 751])
    sleep(1.2)

def inte_fail():    #网络异常
    if exists(Template(r"../tpl1589532705892.png", record_pos=(-0.001, 0.0), resolution=(2244, 1080))):
        touch([1323, 750])
        return True
    return False

def item_detail():  #点到物品详细
    if exists(Template(r"../tpl1589627182286.png", record_pos=(-0.001, -0.111), resolution=(2244, 1080))):
        touch([1122, 762])
        return True
    return False

def water():	#再 起 不 能
    global Watered
    if exists(Template(r"../tpl1591760727159.png", record_pos=(-0.003, 0.037), resolution=(2244, 1080))):
        Watered = True
        return True
    return False

