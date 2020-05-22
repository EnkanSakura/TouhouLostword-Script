# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def still_alive():
    graze()
    boost(2)
    spellcard(3)
    graze()
    shoot(2)
    sleep(8)

# def inte_fail():
#     if exists(Template(r"../tpl1589532705892.png", record_pos=(-0.001, 0.0), resolution=(2244, 1080))):
#         touch([1323, 750])
#         return True
#     return False

# def item_detail():
#     if exists(Template(r"../tpl1589627182286.png", record_pos=(-0.001, -0.111), resolution=(2244, 1080))):
#         touch([1122, 762])
#         return True
#     return False

def enter_stage():
    try:
        wait(Template(r"tpl1589607478947.png", record_pos=(0.206, -0.117), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
        else:
            return True
        
    touch([1518, 567])  #手机
#     touch([1565, 795])  #模拟器
    sleep(5.0)
#     sleep(3.0)  #模拟器
    touch([1840, 929])  #出发
    sleep(20.0)

def normal_battle():
    #妖梦     蹭经验
    #魔理沙   蹭经验
    skill()
    useskill(1, 1)  #妖梦1技能
    useskill(1, 2)  #妖梦2技能
    useskill(2, 1)  #魔理沙1技能
    useskill(2, 2)  #魔理沙2技能
    skill()
    graze(3)
    boost()
    spellcard(1)    #妖梦1p3g冥想
    graze()
    boost()
    spellcard(1)    #魔理沙1p1g魔炮
    sleep(10.0)
    
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=10, interval=3)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
        else:
            still_alive()
            try:
                wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
            except TargetNotFoundError:
                if not(inte_fail()):
                    still_alive()
    
    touch([1119, 263])
    touch([1064, 377], times=6)
#

swipe([1904, 192], [1957, 958])
sleep(0.2)
swipe([1959, 859], [1964, 204], duration=1.0)
swipe([1964, 204], [2100, 204], duration=0.1)
sleep(0.2)
for i in range(100):
    if exists(Template(r"tpl1589627876207.png", record_pos=(-0.202, -0.034), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1589627876207.png", record_pos=(-0.202, -0.034), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        null
    else:
        normal_battle()
    
    

    
    

