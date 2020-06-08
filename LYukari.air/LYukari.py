# -*- encoding=utf8 -*-
__author__ = "落子w"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-

__author__ = "落子w"

import sys
sys.path.append("..")
from battle import *


def still_alive():
    graze()
    boost(1)
    shoot(2)
    sleep(8)

def normal_battle():
    skill()
    useskill(1, 1)
    skill()
    change()
    skill()
    useskill(1, 1)
    useskill(1, 2)
    skill()
    graze(3)
    boost(2)
    spellcard(5)
    sleep(15.0)
    
    try:
        battle_end = wait(Template(r"tpl1589458986628.png", record_pos=(-0.003, -0.141), resolution=(2244, 1080)), timeout=6, interval=2)
    except TargetNotFoundError:
        still_alive()
        try:
            wait(Template(r"tpl1589458986628.png", record_pos=(-0.003, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
        except TargetNotFoundError:
            run_away()
            sleep(10.0)
            return False
    else:
        touch(battle_end)
        return True
        
def enter_stage():
    try:
        stage = wait(Template(r"tpl1591584800196.png", threshold=0.8, record_pos=(0.206, -0.107), resolution=(2244, 1080)), timeout=10, interval=3)
    except TargetNotFoundError:
        run_away()
        return
    
    touch(stage)
    sleep(8.0)
    touch([1849, 940])  #出发
    sleep(20.0)

    
while(True):
    
    if exists(Template(r"tpl1591585447576.png", threshold=0.75, record_pos=(0.354, -0.187), resolution=(2244, 1080))):
        normal_battle()
    try:
        again = wait(Template(r"tpl1591584772117.png", record_pos=(-0.328, 0.197), resolution=(2244, 1080)), timeout=5, interval=2)
    except TargetNotFoundError:
        enter_stage()
    else:
        touch(again)
        sleep(10.0)
    



    