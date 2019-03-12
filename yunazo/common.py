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
## main
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

## story1
class InnOwner(Person):
    def __init__(self):
        super().__init__("宿の店主", 45, "male", "宿の店主", "宿の主。気苦労から窶れている")


class Klone(Person):
    def __init__(self):
        super().__init__("クローネ", 78, "male", "時計技師", "村随一の時計職人")


## story2
class Badac(Person):
    def __init__(self):
        super().__init__("バダック", 80, "male", "発明家", "稀代の天才発明家")


class TH_Tanaka(Person):
    def __init__(self):
        super().__init__("アンラッキィ田中", 35, "male", "トレジャーハンター", "何かと不幸な星の下に生まれた男")


class DondahlChief(Person):
    def __init__(self):
        super().__init__("ドンダール村長", 67, "male", "村長", "前髪の薄い中肉の男性")


class Brenda(Person):
    def __init__(self):
        super().__init__("ブレンダ", 56, "female", "使用人", "バダック付の使用人")


# define stages
## story1
class ClocVila(Stage):
    def __init__(self):
        super().__init__("クロク村", "山間にある寒村")


class Inn(Stage):
    def __init__(self):
        super().__init__("村の宿", "村唯一の宿。しょぼい")


class VigilanteOffice(Stage):
    def __init__(self):
        super().__init__("自警団事務所", "自警団の事務所")

## story2
class DondahlTown(Stage):
    def __init__(self):
        super().__init__("ドンダール", "発明家バダックの生まれ故郷")


class BadacCave(Stage):
    def __init__(self):
        super().__init__("バダックの洞窟", "バダックが財宝を隠したと云われる洞窟")


class BadacSecretRoom(Stage):
    def __init__(self):
        super().__init__("バダックの隠し部屋", "バダックが財宝を隠した部屋")


# define items
## story1
class OwlClock(Item):
    def __init__(self):
        super().__init__("フクロウ時計", "フクロウの姿をした時計")


## story2
class BadacMap(Item):
    def __init__(self):
        super().__init__("バダックの地図", "バダックの財宝の在り処が書かれていると云われている地図")


class BadacPics(Item):
    def __init__(self):
        super().__init__("バダックの絵", "バダックによる絵だが歪な線で描かれた下手なもの")


class BadacCaveDoor(Item):
    def __init__(self):
        super().__init__("洞窟の扉", "バダックの洞窟内に唯一ある扉")


class BadacShelf(Item):
    def __init__(self):
        super().__init__("バダックの棚", "隠し部屋にあった引き出し付の棚")


class BadacMemo(Item):
    def __init__(self):
        super().__init__("バダックの手紙", "使用人に宛てた買い物メモ")


# define daytimes
## story1
class OneDay(DayTime):
    def __init__(self):
        super().__init__("ある日", mon=3, day=5, hour=11)


class AfterDay(DayTime):
    def __init__(self):
        super().__init__("後日", mon=3, day=15, hour=15)

## story2
class TreasureDay(DayTime):
    def __init__(self):
        super().__init__("宝物日和", mon=5, day=5, hour=10, explain="バロックの命日の数日前")

