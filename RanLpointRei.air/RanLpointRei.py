# -*- encoding=utf8 -*-
__author__ = "落子w"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def enter_stage():
    try:
        stage=wait(Template(r"tpl1590989609826.png", record_pos=(0.205, -0.115), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
    
    touch(stage)
    sleep(7.0)
    touch([1840, 929])  #出发
    sleep(20.0)
    return True

def normal_battle():
#     global battle_times
    #蓝
    skill()
    useskill(1, 1)  #1技能
    useskill(1, 2)  #2技能
    skill()
    graze(2)
    boost(1)
    spellcard(1)    #1p2g橙
    sleep(14.0)
    while not(exists(Template(r"tpl1590845971210.png", record_pos=(0.3, -0.197), resolution=(2244, 1080)))):
        sleep(2.0)
    graze(1)
    spellcard(2)    #0p1g鬼
    sleep(14.0)
    while not(exists(Template(r"tpl1590845971210.png", record_pos=(0.3, -0.197), resolution=(2244, 1080)))):
        sleep(2.0)
    boost(2)
    graze(1)
    spellcard(3)    #2p1g橙
    sleep(14.0)
    
    try:
        wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=10, interval=3)
    except TargetNotFoundError:
        if inte_fail():
            sleep(7.0)
            return
        else:
            still_alive()
            try:
                wait(Template(r"../tpl1589526575394.png", record_pos=(0.0, -0.141), resolution=(2244, 1080)), timeout=10, interval=3)
            except TargetNotFoundError:
                if inte_fail():
                    sleep(7.0)
                    return
                else:    
                    run_away()
    
    touch([1119, 263])
    touch([1064, 377], times=6)
    
def still_alive():
    boost(1)
    shoot(2)
    
    
auto_setup(__file__)

while(True):
    if exists(Template(r"tpl1590845971210.png", record_pos=(0.3, -0.197), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1590845971210.png", record_pos=(0.3, -0.197), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        continue
    else:
        normal_battle()

    