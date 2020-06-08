# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def still_alive():
    graze()
    boost(2)
    shoot(2)
    sleep(8.0)

def enter_stage():
    try:
        stage=wait(Template(r"tpl1589961687670.png", threshold=0.85, record_pos=(0.206, 0.032), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return True
        else:
            return False
    
    
    touch(stage)  #选择关卡
    sleep(8.0)
    touch([1840, 929])  #出发
    sleep(15.0)

def normal_battle():
    #妖梦     uu
    skill()
    useskill(1, 1)  #uu1技能
    skill()
    change()
    skill()
    useskill(1, 1)  #妖梦1技能
    useskill(1, 2)  #妖梦2技能
    skill()
    graze(3)
    boost(2)
    spellcard(5)    #妖梦2p3g卫星
    sleep(15.0)       
    
    touch([1119, 263])
    touch([1064, 377], times=6)
#

for i in range(100):
    if exists(Template(r"tpl1591000677796.png", threshold=0.7, record_pos=(0.288, -0.193), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1591000677796.png", threshold=0.7, record_pos=(0.288, -0.193), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        continue
    else:
        normal_battle()
        try:
            wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
        except TargetNotFoundError:
            if not(inte_fail()):
                still_alive()
            try:
                wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
            except TargetNotFoundError:
                run_away()
    
#     Template(r"tpl1591000858316.png", threshold=0.7, record_pos=(0.283, -0.196), resolution=(2244, 1080))
