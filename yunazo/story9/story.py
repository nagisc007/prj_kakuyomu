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

from common import p_yusha, p_panna, p_crades, p_emile


# characters
def charas(name):
    return {
            "yusha": p_yusha(),
            "panna": p_panna(),
            "crades": p_crades(),
            "emile": p_emile(),
            "young": Person("ゆうしゃ", 8, "male", "少年", "ぼく", "勇者オルガの息子としていじめられる"),
            "orga": Person("オルガ", 46, "male", "元勇者", "俺", "失踪した勇者の父親"),
            "rodas": Person("ロダス", 56, "male", "僧侶", "わし", "大神官を目指して修行の旅をする男"),
            "mam": Person("勇者の母", 42, "female", "母親", "私", "勇者の母親"),
            }[name]

# stages
def stages(name):
    return {
            "arial": Stage("アリアル", "勇者の生まれ故郷"),
            "ship": Stage("船上", "ジボンガから帰る途中"),
            }[name]

# items
def items(name):
    return {
            "crest": Item("勇者の紋章", "掌サイズのブローチ。勇者の紋が刻まれている。"),
            }[name]

# words
def words(name):
    return {
            "yusha": Word("勇者という言葉", "かつては勇み足な者、の意味だった"),
            }[name]

# daytimes
def daytimes(name):
    return {
            "current": DayTime("現在", 4, year=1019),
            "childhood": DayTime("幼い頃", 4, year=1009),
            }[name]


# episodes
def ep1(ma: Master):
    return ma.story("episode 1",
            )

def ep2(ma: Master):
    return ma.story("episode 2",
            )

def ep3(ma: Master):
    return ma.story("episode 3",
            )


# story
def story():
    ma = Master('Yunazo 09')
    yusha, panna, orga, young = charas("yusha"), charas("panna"), charas("orga"), charas("young")
    arial, ship = stages("arial"), stages("ship")
    wyusha = words("yusha")
    childhood, current = daytimes("childhood"), daytimes("current")
    return ma.story("勇者は冒険より勇者誕生の謎解きをしたい",
            ep1(ma),
            ep2(ma),
            ep3(ma),
            current.explain("春と呼ばれる季節"),
            ship.explain("穏やかな船上"),
            yusha.think(info="考え込む"),
            panna.ask(yusha, info="悩み"),
            yusha.talk(about=wyusha),
            panna.wonder(about=wyusha),
            yusha.talk(about=childhood),
            yusha.remember(childhood),
            childhood.explain("今から十年も前の話"),
            arial.explain(of=orga, info="生まれた町"),
            orga.explain(of=yusha, info="父親だった"),
            yusha.teach(wyusha, to=panna),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
