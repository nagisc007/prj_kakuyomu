# -*- coding: utf-8 -*-
"""Common data for yunazo series.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.base import Stage, Item, DayTime
from storybuilder.builder.person import Person


# define characters
## main
class Yusha(Person):
    def __init__(self):
        super().__init__("勇者", 18, "male", "勇者", "僕", "謎解き好きな勇者")


class Panna(Person):
    def __init__(self):
        super().__init__("パンナ", 16, "female", "武闘家", "ウチ", "能天気な少女")


class Crades(Person):
    def __init__(self):
        super().__init__("クラデス", 76, "male", "僧侶", "わし", "自称かつて大神官候補の助平爺")


class Emile(Person):
    def __init__(self):
        super().__init__("エミール", 20, "female", "魔法剣士", "私", "謎多き仮面の女性")

## story1
class InnOwner(Person):
    def __init__(self):
        super().__init__("宿の店主", 45, "male", "宿の店主", "わたし", "宿の主。気苦労から窶れている")


class Klone(Person):
    def __init__(self):
        super().__init__("クローネ", 78, "male", "時計技師", "儂", "村随一の時計職人")


## story2
class Badac(Person):
    def __init__(self):
        super().__init__("バダック", 80, "male", "発明家", "私", "稀代の天才発明家")


class TH_Tanaka(Person):
    def __init__(self):
        super().__init__("アンラッキィ田中", 35, "male", "トレジャーハンター", "オレ", "何かと不幸な星の下に生まれた男")


class DondahlChief(Person):
    def __init__(self):
        super().__init__("ドンダール村長", 67, "male", "村長", "私", "前髪の薄い中肉の男性")


class Brenda(Person):
    def __init__(self):
        super().__init__("ブレンダ", 56, "female", "使用人", info="バダック付の使用人")

## story3
class Manderine(Person):
    def __init__(self):
        super().__init__("マンデリン", 66, "male", "執事", "私", "ワローン家に代々使える執事の家系")


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

## story3
class WaroneHouse(Stage):
    def __init__(self):
        super().__init__("ワローン邸", "ワローン家の豪邸")


class SilverForest(Stage):
    def __init__(self):
        super().__init__("白銀の森", "白銀の馬に乗った王子に出会える伝説がある")


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

## story3
class RentalPony(Item):
    def __init__(self):
        super().__init__("ポニィ", "トンハイの街で勇者が借りたポニィ")


class TabooBook(Item):
    def __init__(self):
        super().__init__("禁忌の本", "倉庫に所蔵されていた読んではならない本")


# define daytimes
## story1
class OneDay(DayTime):
    def __init__(self):
        super().__init__("ある日", mon=3, day=5, year=1019, hour=11)


class AfterDay(DayTime):
    def __init__(self):
        super().__init__("後日", mon=3, day=15, year=1019, hour=15)

## story2
class TreasureDay(DayTime):
    def __init__(self):
        super().__init__("宝物日和", mon=5, day=5, year=1019, hour=10, info="バロックの命日の数日前")

## story3
class MeetDay(DayTime):
    def __init__(self):
        super().__init__("パンナと出会った日", mon=9, day=20, year=1017, info="勇者とパンナが出会った日。二年前")

