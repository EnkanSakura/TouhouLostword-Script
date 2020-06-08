# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def enter_stage():
    try:
        wait(Template(r"tpl1589939051943.png", record_pos=(0.204, -0.118), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return True
        else:
            return False
    
    touch([1565, 253])
    sleep(5.0)
#     sleep(3.0)  #模拟器
    touch([1840, 929])  #出发
    sleep(15.0)

def normal_battle():
    #妖梦
    #魔理沙
    #蓝
    skill()
    useskill(2, 1)  #魔理沙1技能
    useskill(2, 2)  #魔理沙2技能
    useskill(3, 1)  #蓝1技能
    skill()
    graze()
    boost()
    spellcard(2)    #妖梦1p1g未来
    graze()
    spellcard(1)    #魔理沙0p1g魔炮
    graze()
    boost()
    spellcard(1)    #蓝1p1g橙
    sleep(15.0)
    while not(exists(Template(r"tpl1589939713081.png", threshold=0.85, record_pos=(0.154, -0.047), resolution=(2244, 1080)))):
        sleep(4.0)
    sleep(1.0)
    skill()
    useskill(1, 2)  #妖梦2技能
    skill()
    graze()
    boost()
    spellcard(4)    #妖梦1p1g未来
    graze()
    boost()
    spellcard(3)    #魔理沙1p1g魔炮
    graze()
    boost()
    spellcard(3)    #蓝1p1g橙
    sleep(15.0)
    while not(exists(Template(r"tpl1589939713081.png", threshold=0.85, record_pos=(0.154, -0.047), resolution=(2244, 1080)))):
        sleep(4.0)
    sleep(1.0)
    skill()
    useskill(1, 1)  #妖梦1技能
    skill()
    boost(2)
    graze(2)
    spellcard(5)    #妖梦2p2g卫星
    shoot(2)        #空过
    shoot(2)        #空过
    sleep(15)
    
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

for i in range(100):
    if exists(Template(r"tpl1589939713081.png", threshold=0.85, record_pos=(0.154, -0.047), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1589939713081.png", threshold=0.85, record_pos=(0.154, -0.047), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        null
    else:
        normal_battle()
    
