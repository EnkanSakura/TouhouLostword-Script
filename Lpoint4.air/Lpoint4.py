# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *

def still_alive():
    boost(1)
    shoot(2)
    sleep(8)

def enter_stage():
    try:
        wait(Template(r"tpl1590026492003.png", record_pos=(0.203, -0.125), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
        else:
            return True
        
    touch([1576, 255])
    sleep(5.0)
    touch([1840, 929])  #出发
    sleep(20.0)

def normal_battle():
    #妖梦
    skill()
    useskill(1, 2)  #2技能
    skill()
    graze()
    boost()
    spellcard(1)    #1p1g冥想
    sleep(13.0)
    while not(exists(Template(r"tpl1590026624724.png", record_pos=(-0.294, -0.2), resolution=(2244, 1080)))):
        sleep(2.0)
    graze()
    spellcard(2)    #0p1g未来
    sleep(13.0)
    while not(exists(Template(r"tpl1590026624724.png", record_pos=(-0.294, -0.2), resolution=(2244, 1080)))):
        sleep(2.0)
    graze()
    boost()
    spellcard(3)    #1p1g冥想
    sleep(13.0)
    while not(exists(Template(r"tpl1590026624724.png", record_pos=(-0.294, -0.2), resolution=(2244, 1080)))):
        sleep(2.0)
    skill()
    useskill(1, 1)  #1技能
    skill()
    graze()
    boost(3)
    spellcard(5)    #3p1g卫星
    sleep(13.0)
    
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=10, interval=3)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
            return
        else:
            still_alive()
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
            return
        else:
            still_alive()
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
            return
        else:
            run_away
            return
    
    touch([1119, 263])
    touch([1064, 377], times=6)
#

auto_setup(__file__)

for i in range(100):
    if exists(Template(r"tpl1590026624724.png", record_pos=(-0.294, -0.2), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1590026624724.png", record_pos=(-0.294, -0.2), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        continue
    else:
        normal_battle()
