# -*- coding: utf-8 -*-
"""Story that Yusha like a mystery than an adventure.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime
from storybuilder.builder.tools import output, output_md


# define characters
class Yusha(Person):
    def __init__(self):
        super().__init__("勇者", 18, "male", "勇者")


class Panna(Person):
    def __init__(self):
        super().__init__("パンナ", 16, "female", "武闘家")


class Crades(Person):
    def __init__(self):
        super().__init__("クラデス", 76, "male", "僧侶")


class Emile(Person):
    def __init__(self):
        super().__init__("エミール", 20, "female", "魔法剣士")


class InnOwner(Person):
    def __init__(self):
        super().__init__("宿の店主", 45, "male", "宿の店主")


# define stages
class ClocVila(Stage):
    def __init__(self):
        super().__init__("クロク村", "山間にある寒村")


class Inn(Stage):
    def __init__(self):
        super().__init__("村の宿", "村唯一の宿。しょぼい")


# define items
class OwlClock(Item):
    def __init__(self):
        super().__init__("フクロウ時計", "フクロウの姿をした時計")


# define daytimes
class OneDay(DayTime):
    def __init__(self):
        super().__init__("ある日", mon=3, hour=10)


# episodes
def ep_intro(inn, vila, oneday, yusha, panna, oclock):
    '''Intro story.
    '''
    return (
            Title("フクロウ時計"),
            Must(yusha, "持ち金が少ない"),
            Done(yusha, "家賃を安くする交渉"),
            oneday.desc("既にすっかり日が昇ってしまっていた"),
            inn.desc("村唯一の宿で、しかも部屋が埋まっているという"),
            inn.desc("そこで仕方なく、一人部屋に二人押し込められたという訳だ"),
            vila.desc("ここが山間の寂れた村だということ"),
            yusha.think("それを忘れてしまうような安眠だった"),
            panna.tell("なあなあ、{}。まだ眠るん？　結局朝ご飯食べ損ねたやん".format(yusha.name)),
            yusha.act("目覚める"),
            yusha.tell("それで{}はアレが鳴くのを聞けたのか？".format(panna.name)),
            panna.tell("ううん"),
            yusha.think("アレとは棚の上に飾られた{}のことだ".format(oclock.name)),
            yusha.tell("宿の主と約束したからな。何故{}が鳴かなくなってしまったのか。その謎を解けば家賃を半額にしてくれると".format(oclock.name)),
            )


def ep_mystery(inn, oneday, yusha, panna):
    '''Mystery story.
    '''
    return (
            Title("鳴かないフクロウ"),
            Must(yusha, "フクロウ時計の謎を解く"),
            Done(yusha, "{}に謎はないと言った".format(panna.name)),
            oneday.desc("ぼんやりとした日差しが差し込んでいた"),
            inn.desc("床も天井も随分と古くなっている"),
            yusha.tell("謎なんか最初からなかったのさ"),
            panna.tell("どゆこと？"),
            )


def ep_resolve(inn, oneday, yusha, panna, owner, oclock):
    '''Resolve story.
    '''
    return (
            Title("そして鳥は動き出す"),
            Must(yusha, "事件解決"),
            Done(yusha, "再び眠りに就いた"),
            oneday.desc("まだ夕方にはなっていない"),
            inn.desc("部屋の中には空気がわだかまっていた"),
            panna.tell("それで何が分かったの？"),
            yusha.tell("結局何も起こっていない、ということさ"),
            yusha.tell("丸一日観察してみたが、一度として鳴かなかった"),
            yusha.tell("これはね、どこからどう見ても鳩時計なんだよ"),
            owner.tell("じゃあどうして鳴かないんで？"),
            yusha.tell("簡単なことだ。壊れているんだよ"),
            yusha.tell("あなたが貰ってきた時にはまだ正常に動いていたが、ここを見てくれ"),
            yusha.act("{}の下を見せた".format(oclock.name)),
            owner.tell("それが？"),
            yusha.tell("ここに微弱な魔法力を出す魔石がある。おそらくはそれに寿命がきたんだ。これを新しいものと取り替えれば、動き出す可能性もある"),
            )

# main story
def story():
    '''Story builded.

    Returns:
        tuple:obj:`Act`: the tuple of story actions object.
    '''
    # characters
    yusha = Yusha()
    panna = Panna()
    crades = Crades()
    emile = Emile()
    owner = InnOwner()
    # stages
    vila = ClocVila()
    inn = Inn()
    # items
    oclock = OwlClock()
    # daytimes
    oneday = OneDay()

    # episodes
    episodes = \
            ep_intro(inn, vila, oneday, yusha, panna, oclock) +\
            ep_mystery(inn, oneday, yusha, panna) +\
            ep_resolve(inn, oneday, yusha, panna, owner, oclock)

    return episodes


def main(is_debug=True):
    '''
    Returns:
        True: if completed the process to build and output a story.
    '''
    STORY_FILE = 'yunazo1'

    mystory = story()
    # output
    output(mystory, is_debug=is_debug)
    # output to markdown
    output_md(mystory, STORY_FILE, is_debug=is_debug)

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

