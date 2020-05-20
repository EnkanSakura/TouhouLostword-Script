# -*- encoding=utf8 -*-

import sys
sys.path.append("..")
from airtest.core.api import *
from battle import *


def still_alive():
    graze()
    boost(3)
    shoot(2)
    graze()
    shoot(2)
    graze()
    shoot(2)
    sleep(8)


for i in range(100):
    try:
        wait(Template(r"tpl1589456783866.png", record_pos=(0.203, -0.117), resolution=(2244, 1080)))
    except TargetNotFoundError:
        run_away()
        continue
    touch([1607, 234])
    sleep(5.0)
    touch([1849, 940])  #出发
    sleep(20.0)
    #魔理沙    妖梦
    #咲夜      姆q
    #莉莉白
    skill()
    useskill(1, 2)  #魔2技能
    skill()
    change()    #魔换妖梦
    skill()
    useskill(1, 2)  #妖梦2技能
    skill()
    spellcard(1)    #妖梦0p冥想
    change()    #xx换姆q
    graze()
    boost()
    spellcard(1)    #姆q1p1g月符
    graze()
    boost()
    spellcard(1)    #莉莉白1p1g春符
    sleep(18.0)
    wait(Template(r"tpl1589458748891.png", record_pos=(0.114, 0.111), resolution=(2244, 1080)),timeout=10)
    skill()
    useskill(1, 1)  #妖梦1技能
    skill()
    graze(3)
    boost(3)
    spellcard(3)    #妖梦3p3g冥想
    graze()
    boost()
    shoot(2)    #姆q1p1g集中
    graze()
    boost()
    shoot(2)    #莉莉白1p1g集中
    sleep(22)
    
    try:    #万一两波没打死
        wait(Template(r"tpl1589458986628.png", record_pos=(-0.003, -0.141), resolution=(2244, 1080)), timeout=6, interval=2)
    except TargetNotFoundError:
        still_alive()   #补三个集中
        try:    #万一三波还没打死
            wait(Template(r"tpl1589458986628.png", record_pos=(-0.003, -0.141), resolution=(2244, 1080)), timeout=5, interval=2)
        except TargetNotFoundError:
            run_away()      #还没打死就跑吧
            continue
        
    touch([1119, 263])
    touch([1064, 377], times=6)



    