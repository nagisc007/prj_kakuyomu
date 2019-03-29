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
            "children": Person("町の子供たち", 10, "male", "子供"),
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
            "mark": Item("勇者の痣", "背中に現れた紋章に似た痣"),
            }[name]

# words
def words(name):
    return {
            "yusha": Word("勇者という言葉", "かつては勇み足な者、の意味だった"),
            "worry": Word("勇者の心配事"),
            }[name]

# daytimes
def daytimes(name):
    return {
            "current": DayTime("現在", 4, year=1019),
            "childhood": DayTime("幼い頃", 4, year=1009),
            }[name]


# episodes
def ep1(ma: Master):
    yusha, panna = charas("yusha"), charas("panna")
    ship = stages("ship")
    wyusha, yworry = words("yusha"), words("worry")
    current, childhood = daytimes("current"), daytimes("childhood")
    return ma.story("episode 1",
            current.explain("春と呼ばれる季節"),
            ship.explain("穏やかな船上"),
            yusha.think(info="考え込む"),
            panna.know(of=yworry),
            yusha.worry(info="何か"),
            panna.ask(about=yworry, info="直接"),
            yusha.talk(about=wyusha),
            panna.wonder(wyusha),
            yusha.talk(about=childhood, to=panna),
            yusha.remember(childhood),
            )

def ep2(ma: Master):
    yusha, orga, young = charas("yusha"), charas("orga"), charas("young")
    mam, children = charas("mam"), charas("children")
    arial = stages("arial")
    current, childhood = daytimes("current"), daytimes("childhood")
    return ma.story("episode 2",
            childhood.explain("もう10年も前のこと"),
            arial.explain("生まれ故郷"),
            arial.explain(of=orga, info="生まれた町"),
            young.explain("そこで生まれた", at=arial),
            yusha.be(info="誕生"),
            mam.do(yusha, info="産んだ"),
            mam.marry(orga),
            orga.glad(young, info="誕生を"),
            orga.vanish(),
            yusha.hate(frm=children).ps(),
            )

def ep3(ma: Master):
    yusha, panna, orga = charas("yusha"), charas("panna"), charas("orga")
    young, children = charas("young"), charas("children")
    arial = stages("arial")
    wyusha, ymark = words("yusha"), items("mark")
    current, childhood = daytimes("current"), daytimes("childhood")
    return ma.story("episode 3",
            childhood.explain("ある日だった"),
            orga.talk(info="英雄になった").ps(),
            arial.explain("彼の噂が伝わる"),
            young.think(ymark),
            yusha.become(wyusha),
            yusha.hate(frm=children).ps().non(),
            yusha.find(ymark),
            yusha.have(ymark),
            current.explain("現代に戻る"),
            yusha.teach(wyusha, to=panna),
            )


# story
def story():
    ma = Master('Yunazo 09')
    return ma.story("勇者は冒険より勇者誕生の謎解きをしたい",
            ep1(ma),
            ep2(ma),
            ep3(ma),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
