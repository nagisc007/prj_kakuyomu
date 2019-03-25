# -*- coding: utf-8 -*-
"""The story program for yunazo 8.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.base import Master, Stage, Item, DayTime, Word
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story

from common import Yusha, Panna, Crades, Emile


# characters
def boy_ordy():
    return Person("オルディ", 12, "male", "少年", "おれ", "勇者に憧れる少年")


# stages
def zibonga_vila():
    return Stage("ジボンガ", "魔王を崇めている集落")


# items


# words
def devils_fes():
    return Word("魔王祭", "魔王を崇める祭。今年で三周年")


# daytimes
def past_day():
    return DayTime("魔王の日", 4, 1, 1016, note="魔王により村が救われた日。三年前")

def before_day():
    return DayTime("祭り前日", 3, 31, 1019)

def fes_day():
    return DayTime("祭りの日", 4, 1, 1019)


# episodes
def ep_intro(ma: Master):
    return ma.story("魔王を崇める村",
            )

def ep_maou(ma: Master):
    return ma.story("魔王と勇者",
            )

def ep_festa(ma: Master):
    return ma.story("魔王の謎",
            )

# story
def story():
    ma = Master('yunazo 08')
    yusha, panna, crades, emile = Yusha(), Panna(), Crades(), Emile()
    ordy = boy_ordy()
    vila = zibonga_vila()
    fes = devils_fes()
    pday, bday, fday = past_day(), before_day(), fes_day()
    return ma.story("勇者は冒険より三周年魔王祭の謎解きをしたい",
            ep_intro(ma),
            ep_maou(ma),
            ep_festa(ma),
            bday.explain("祭りの前日"),
            vila.explain("行われている", fes),
            yusha.visit(vila, "仲間と共に"),
            panna.visit(vila),
            yusha.hear(fes),
            yusha.want(fes, "知る"),
            yusha.investigate(vila),
            yusha.know(vila, info="魔王が救った"),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
