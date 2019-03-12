# -*- coding: utf-8 -*-
"""Common data for yunazo series.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.base import Person, Stage, Item, DayTime


# define characters
class Yusha(Person):
    def __init__(self):
        super().__init__("勇者", 18, "male", "勇者", "謎解き好きな勇者")


class Panna(Person):
    def __init__(self):
        super().__init__("パンナ", 16, "female", "武闘家", "能天気な少女")


class Crades(Person):
    def __init__(self):
        super().__init__("クラデス", 76, "male", "僧侶", "自称かつて大神官候補の助平爺")


class Emile(Person):
    def __init__(self):
        super().__init__("エミール", 20, "female", "魔法剣士", "謎多き仮面の女性")


class InnOwner(Person):
    def __init__(self):
        super().__init__("宿の店主", 45, "male", "宿の店主", "宿の主。気苦労から窶れている")


class Klone(Person):
    def __init__(self):
        super().__init__("クローネ", 78, "male", "時計技師", "村随一の時計職人")


# define stages
class ClocVila(Stage):
    def __init__(self):
        super().__init__("クロク村", "山間にある寒村")


class Inn(Stage):
    def __init__(self):
        super().__init__("村の宿", "村唯一の宿。しょぼい")


class VigilanteOffice(Stage):
    def __init__(self):
        super().__init__("自警団事務所", "自警団の事務所")


# define items
class OwlClock(Item):
    def __init__(self):
        super().__init__("フクロウ時計", "フクロウの姿をした時計")


# define daytimes
class OneDay(DayTime):
    def __init__(self):
        super().__init__("ある日", mon=3, day=5, hour=11)


class AfterDay(DayTime):
    def __init__(self):
        super().__init__("後日", mon=3, day=15, hour=15)

