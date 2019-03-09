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
        super().__init__("ある日")


# episodes
def ep_intro(inn, oneday, yusha, panna):
    '''Intro story.
    '''
    return (
            Must(yusha, "冒険に出掛ける"),
            oneday.desc("既に昼を過ぎていた"),
            panna.tell("大変だよ！"),
            yusha.act("目覚める"),
            Done(yusha, "目覚めた"),
            )


def ep_resolve(inn, oneday, yusha, panna):
    '''Resolve story.
    '''
    return (
            Must(yusha, "事件解決"),
            Done(yusha, "再び眠りに就いた"),
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
    # stages
    vila = ClocVila()
    inn = Inn()
    # items
    oclock = OwlClock()
    # daytimes
    oneday = OneDay()

    # episodes
    episodes = \
            ep_intro(inn, oneday, yusha, panna) +\
            ep_resolve(inn, oneday, yusha, panna)

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

