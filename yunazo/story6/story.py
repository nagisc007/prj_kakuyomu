# -*- coding: utf-8 -*-
"""Story program for yunazo story 06.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Stage, Item, DayTime, Word, Master
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story

from common import Yusha, Panna, Crades, Emile


# characters
class Conny(Person):
    def __init__(self):
        super().__init__("コニー", 54, "male", "大会委員")


# stages
class NachansTown(Stage):
    def __init__(self):
        super().__init__("ネーチャンス", "ホットドクで有名な町")

class TownBar(Stage):
    def __init__(self):
        super().__init__("酒場", "町の裏路地にある酒場")


# items
class HotDok(Item):
    def __init__(self):
        super().__init__("ホットドク", "厚切りパンで辛く味付けしたハムを挟んだもの")

# words
class Competition(Word):
    def __init__(self):
        super().__init__("早食い大会", "ホットドクの早食い大会")

    def prize(self):
        return "賞金10ガル"


# daytimes
class BeforeDay(DayTime):
    def __init__(self):
        super().__init__("大会前日", 7, 3, 1018)

class CompeDay(DayTime):
    def __init__(self):
        super().__init__("大会当日", 7, 4, 1018)


# episodes
def ep_intro(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        conny: Conny,
        town: NachansTown,
        day0: BeforeDay,
        hotdok: HotDok):
    return ma.story(
            ma.title("大会前夜"),
            day0.explain("大会前夜"),
            town.explain("{}で有名な町".format(hotdok.name)),
            yusha.investigate("大会での不正疑惑"),
            yusha.accept("大会調査依頼を{}から".format(conny.name)),
            yusha.let("{}を大会参加".format(panna.name)),
            panna.tell("いっぱい食べられるん？"),
            emile.explain("十戦無敗の仮面騎士"),
            yusha.visit(town.name),
            panna.visit(town.name),
            crades.visit(town.name),
            yusha.meet(emile.name),
            yusha.see("{}の悲しげな様".format(emile.name)),
            )

def ep_competition(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        town: NachansTown, bar: TownBar,
        day0: BeforeDay, day1: CompeDay):
    return ma.story(
            ma.title("大会当日"),
            day0.explain("日が落ちて夜が訪れる"),
            bar.explain("寂れた裏路地にあるバーだった"),
            emile.sad("悲しげな顔"),
            yusha.think("{}が気になる".format(emile.name)),
            yusha.investigate(emile.name),
            yusha.know("{}は無理やり協力させられている".format(emile.name)),
            yusha.release("{}を大会から".format(emile.name)),
            day1.explain("大会当日"),
            town.explain("会場は中央広場に設けられている"),
            emile.join("大会"),
            panna.join("大会"),
            crades.find("仮面騎士の呪い"),
            yusha.know("呪いの所為で{}は苦しんでいる".format(emile.name)),
            )

def ep_realflavor(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        town: NachansTown,
        day1: CompeDay,
        hotdok: HotDok):
    return ma.story(
            ma.title("本当の味"),
            day1.explain("試合開始から既に2分経過"),
            town.explain("会場は静まり返っている"),
            yusha.must("{}の呪いを解く".format(emile.name)),
            yusha.think("{}を助けるべき".format(emile.name)),
            crades.teach("呪いを解く方法"),
            yusha.confess("{}の素顔が美しい".format(emile.name)),
            emile.eat("本物の{}".format(hotdok.name)),
            emile.tell("美味しい"),
            )

# main story
def story():
    '''Define main story.
    '''
    ma = Master("Yunazo6")
    yusha, panna, crades, emile = Yusha(), Panna(), Crades(), Emile()
    conny = Conny()
    town, bar = NachansTown(), TownBar()
    hotdok = HotDok()
    day0, day1 = BeforeDay(), CompeDay()

    return ma.story(
            ma.title("勇者は冒険より大食い仮面騎士の謎解きをしたい"),
            ep_intro(ma,
                yusha, panna, crades, emile, conny, town, day0, hotdok),
            ep_competition(ma,
                yusha, panna, crades, emile, town, bar, day0, day1),
            ep_realflavor(ma,
                yusha, panna, crades, emile, town, day1, hotdok),
            )

def main():
    '''main.
    '''
    build_to_story(story())

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

