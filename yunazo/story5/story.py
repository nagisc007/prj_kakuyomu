# -*- coding: utf-8 -*-
"""Story program for yunazo story 05.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Stage, Item, DayTime, Word, Master
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story

from common import Yusha, Panna, Crades


# characters
class Claire(Person):
    def __init__(self):
        super().__init__("クレア", 20, "female", "靴屋の娘", "あたし", "事件の真犯人")


class PoliceChief(Person):
    def __init__(self):
        super().__init__("警官", 36, "male", "警官", note="町の警官")


class LePoir(Person):
    def __init__(self):
        super().__init__("ル・ポワ", 55, "male", "探偵", "私", "グレート島で名を馳せる名探偵")


# stages
class Donston(Stage):
    def __init__(self):
        super().__init__("ドンストン", "グレート島中北部の町。競馬で有名。")

# items
class MagicBall(Stage):
    def __init__(self):
        super().__init__("魔法玉", "異次元に飛ばす魔力を詰めた玉")

# words
class MagiNet(Word):
    def __init__(self):
        super().__init__("魔導ネット", "魔術により")


# days
class Today(DayTime):
    def __init__(self):
        super().__init__("逮捕日", 6, 10, 1018, 15, "クラデスと出会った日")

class FirstDay(DayTime):
    def __init__(self):
        super().__init__("第一の事件日", 6, 1, 1018)

class SecondDay(DayTime):
    def __init__(self):
        super().__init__("第二の事件日", 6, 5, 1018)

class ThirdDay(DayTime):
    def __init__(self):
        super().__init__("第三の事件日", 6, 9, 1018)


def intro(ma: Master):
    return ma.story(
            ma.title("イントロ"),
            )

def strange_oldman(ma: Master):
    return ma.story(
            ma.title("奇妙な老人"),
            )

def real_criminal(ma: Master):
    return ma.story(
            ma.title("真犯人"),
            )

def story():
    '''Create a story object.
    '''
    ma = Master("Yunazo5")
    yusha, panna, crades = Yusha(), Panna(), Crades()
    claire, poli, lepoir = Claire(), PoliceChief(), LePoir()
    town = Donston()
    ball = MagicBall()
    net = MagiNet()
    day = Today()

    return ma.story(
            ma.title("勇者は冒険よりＡＢＣ商店消失の謎解きをしたい"),
            intro(ma),
            strange_oldman(ma),
            real_criminal(ma),
            day.explain("六月の湿気が多い午後"),
            town.explain("競馬で有名な町"),
            yusha.come(town.name),
            panna.come(town.name),
            town.explain("中央広場で騒ぎ"),
            yusha.go("広場"),
            poli.catch(crades.name),
            crades.tell("何もしとらん"),
            poli.explain("{}が事件の重要参考人".format(crades.name)),
            lepoir.talk("事件について"),
            claire.tell("突然店が消えたんです"),
            lepoir.talk("数日前から連続して商店が消えたのだ"),
            yusha.dispel("{}の容疑".format(crades.name)),
            yusha.believe("{}はやっていない".format(crades.name)),
            # 信じてる根拠
            yusha.talk("犯人を見つける"),
            lepoir.laugh(""),
            yusha.hear("それぞれの事情"),
            crades.talk("ずっと飲んだくれていた"),
            claire.talk("最近は何でも魔導ネットを使うから商売にならない"),
            yusha.tell("真犯人を見つける"),
            yusha.search("消失場所"),
            yusha.go("店があった場所"),
            town.explain("地面から綺麗に区切られたように消えている"),
            panna.tell("まるで魔法みたい"),
            yusha.ask("どんな店だったか"),
            claire.talk("汚い店で、大嫌いだったと文句"),
            claire.confess("店を継ぎたくない"),
            )

def main():
    '''main function.
    '''
    build_to_story(story())

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

