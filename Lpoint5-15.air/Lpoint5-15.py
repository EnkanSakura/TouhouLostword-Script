# -*- encoding=utf8 -*-
__author__ = "落子w"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-

import sys
sys.path.append("..")
from airtest.core.api import *
from battle import *


def enter_stage():
    try:
        wait(Template(r"tpl1590049791070.png", record_pos=(0.213, -0.11), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        run_away()
        if item_detail():
            touch([121, 48])    #返回
            return False
        else:
            return True
        
    touch([1589, 480])
    sleep(7.0)
    touch([1840, 929])  #出发
    sleep(20.0)

def normal_battle():
    #妖梦
    skill()
    useskill(1, 1)  #1技能
    useskill(1, 2)  #2技能
    skill()
    graze(1)
    boost(1)
    spellcard(2)    #1p1g未来
    sleep(14.0)
    while not(exists(Template(r"tpl1590049993151.png", record_pos=(0.275, -0.197), resolution=(2244, 1080)))):
        sleep(2.0)
    graze(3)
    boost(2)
    spellcard(4)    #2p3g未来
    sleep(14.0)
    while not(exists(Template(r"tpl1590049993151.png", record_pos=(0.275, -0.197), resolution=(2244, 1080)))):
        sleep(2.0)
    boost(2)
    spellcard(5)    #2p0g卫星
    sleep(14.0)
    
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
    
    sleep(30)
#

auto_setup(__file__)

for i in range(100):
    if exists(Template(r"tpl1590049993151.png", threshold=0.8, record_pos=(0.275, -0.197), resolution=(2244, 1080))):
        normal_battle()
        continue
            
    if not(enter_stage()):
        continue
            
    try:
        wait(Template(r"tpl1590049993151.png", threshold=0.8, record_pos=(0.275, -0.197), resolution=(2244, 1080)), timeout=10)
    except TargetNotFoundError:
        continue
    else:
        normal_battle()
