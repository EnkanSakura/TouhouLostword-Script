# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *

Watered = False
stage_pic = Template(r"tpl1595556252557.png", threshold=0.9, record_pos=(0.206, -0.054), resolution=(2244, 1080))
boss = Template(r"tpl1595556629593.png", threshold=0.8, record_pos=(-0.329, -0.2), resolution=(2244, 1080))
group=[
    Template(r"tpl1595556306417.png", threshold=0.9, record_pos=(-0.037, 0.189), resolution=(2244, 1080)),
    Template(r"tpl1595556326285.png", threshold=0.9, record_pos=(-0.037, 0.189), resolution=(2244, 1080)),
    Template(r"tpl1595556341359.png", threshold=0.9, record_pos=(-0.037, 0.188), resolution=(2244, 1080))
]
next_group = [1397, 638]
pre_group = [220, 640]


def enter_stage():
    global group
    global stage_pic
    global Watered
    try:
        stage_pos = wait(stage_pic, timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
    else:
        touch(stage_pos)
        sleep(7.0)
    if Watered:
        if exists(group[0]):
            touch(next_group)
        elif exists(group[1]):
            touch(next_group)
        elif exists(group[2]):
            touch(pre_group, times=2)
        else:
            return False
        Watered = False
        sleep(2.0)
    touch([1840, 929])  #出发
    sleep(20.0)
    return True

def normal_battle():
    #妖梦/UUZ/蓝
#     skill()
#     useskill(1, 1)  #1技能
#     useskill(1, 2)  #2技能
#     skill()
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
    if exists(boss):
        normal_battle()
        continue
    else:
        if water():
            Watered = True
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
 

