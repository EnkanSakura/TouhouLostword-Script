# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def still_alive():
    graze()
    boost()
    shoot(1)

def enter_stage():
    try:
        wait(Template(r"tpl1589961687670.png", record_pos=(0.206, 0.032), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return True
        else:
            return False
    
    
    touch([1590, 233])  #选择关卡
    sleep(5.0)
#     sleep(3.0)  #模拟器
    touch([1840, 929])  #出发
    sleep(15.0)

def normal_battle():
    #妖梦
    skill()
    useskill(1, 2)  #妖梦2技能
    skill()
    graze()
    spellcard(2)    #妖梦0p1g未来
    sleep(15.0)
            
    try:
        wait(Template(r"tpl1589961763403.png", threshold=0.75, record_pos=(-0.214, -0.021), resolution=(2244, 1080)), timeout=10, interval=3)
    except:
        null
    else:
        graze()
        boost()
        spellcard(4)    #妖梦1p1g未来
        
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
    except TargetNotFoundError:
        if not inte_fail():
            skill()
            useskill(1, 1)
            skill()
            graze(2)
            boost(3)
            spellcard(3)    #妖梦2p2g冥想
            sleep(15.0)
            
    
    touch([1119, 263])
    touch([1064, 377], times=6)
#

for i in range(100):
    if exists(Template(r"tpl1589961763403.png", threshold=0.75, record_pos=(-0.214, -0.021), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1589961763403.png", threshold=0.75, record_pos=(-0.214, -0.021), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        null
    else:
        normal_battle()
    
