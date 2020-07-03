# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


stage_pic = Template(r"tpl1592891651875.png", record_pos=(0.205, -0.132), resolution=(2244, 1080))
groupA = Template(r"tpl1593664257940.png", threshold=0.9, record_pos=(-0.143, 0.215), resolution=(2244, 1080))
groupB = Template(r"tpl1593664352558.png", threshold=0.9, record_pos=(-0.143, 0.215), resolution=(2244, 1080))
A2B_times = 1


def enter_stage():
    try:
        stage_pos = wait(stage_pic, timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
    touch(stage_pos)
    sleep(7.0)
    if Watered:
        if exists(groupA):
            touch([1392, 642], times=A2B_times)
        elif exists(groupB):
            touch([208, 633], times=A2B_times)
        else:
            return False
    touch([1840, 929])  #出发
    sleep(20.0)
    return True

def normal_battle():
    #妖梦/UUZ
    skill()
    useskill(1, 1)  #1技能
    useskill(1, 2)  #2技能
    skill()
    graze(3)
    boost(1)
    spellcard(5)    #1p3gLW
    sleep(15.0)
    
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=10, interval=3)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
            return
        else:
            run_away()
    touch([1976, 950])


auto_setup(__file__)
while(True):
    if exists(Template(r"tpl1592891418830.png", threshold=0.8, record_pos=(-0.322, -0.198), resolution=(2244, 1080))):
        normal_battle()
        continue
    else:
        if water():
            touch([900, 875])   #Template(r"tpl1593663414826.png", record_pos=(-0.095, 0.16), resolution=(2244, 1080))
            touch([1985, 959])  #Template(r"../tpl1592892121177.png", record_pos=(0.377, 0.194), resolution=(2244, 1080))
            enter_stage()
            continue
    try:
        again=wait(Template(r"../tpl1592891989347.png", threshold=0.9, record_pos=(-0.393, 0.195), resolution=(2244, 1080)), timeout=5, interval=2)
    except TargetNotFoundError:
        enter_stage()
    else:
        touch(again)
        sleep(14.0)
 

