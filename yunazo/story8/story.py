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

def mam_ordy():
    return Person("オルディ母", 30, "female", "機織り", "わたし")

def dad_ordy():
    return Person("オルディ父", 28, "male", "漁師", "俺", "三年前に亡くなる")

def vila_people():
    return Person("村人", 30, "male", "村の人間")


# stages
def zibonga_vila():
    return Stage("ジボンガ", "魔王を崇めている集落")

def ordy_home():
    return Stage("オルディの家", "板と布を重ねた粗末な家")


# items


# words
def devils_fes():
    return Word("魔王祭", "魔王を崇める祭。今年で三周年")

def real_tale():
    return Word("真実の話", "三年前に魔王が助けたという話の真実")

# daytimes
def past_day():
    return DayTime("三年前", 4, 1, 1016, note="魔王により村が救われた日。三年前")

def before_day():
    return DayTime("祭り前日", 3, 31, 1019)

def fes_day():
    return DayTime("祭りの日", 4, 1, 1019)


# episodes
def ep_intro(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile, ordy: Person,
        fes: Word,
        vila: Stage,
        day: DayTime):
    return ma.story("魔王を崇める村",
            day.explain("祭りの前日"),
            vila.explain("行われている", fes),
            yusha.visit(vila, "仲間と共に"),
            panna.visit(vila),
            yusha.hear(fes),
            yusha.want(fes, "知る"),
            yusha.investigate(fes),
            yusha.investigate(vila),
            yusha.meet(ordy),
            ordy.glad(yusha, "出会えて"),
            ordy.invite(yusha, "自分の家"),
            )

def ep_maou(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        ordy: Person, mam: Person, dad: Person,
        fes: Word,
        vila: Stage, home: Stage,
        day: DayTime, pday: DayTime):
    return ma.story("魔王と勇者",
            day.explain("夕闇が落ちてきた"),
            home.explain("風雨をなんとかしのげる程度の粗末の木造家屋"),
            yusha.think(ordy, "貧しい"),
            ordy.talk(yusha, "勇者"),
            yusha.hear(ordy, "祭り"),
            ordy.know(fes),
            ordy.want(yusha),
            yusha.teach(ordy, "勇者"),
            ordy.teach(pday),
            yusha.know(dad, "三年前に亡くなる"),
            )

def ep_festa(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile, ordy: Person,
        people: Person,
        fes: Word, tale: Word,
        vila: Stage,
        day: DayTime):
    return ma.story("魔王の謎",
            yusha.know(vila, info="魔王が救った"),
            day.explain("祭りの朝だった"),
            yusha.wake(),
            vila.explain("中央の広場で"),
            yusha.bind(),
            yusha.catch(people).ps(),
            ordy.rescue(yusha),
            ordy.tell("魔王はそんなこと望んでない"),
            ordy.talk(tale),
            ordy.teach(info="魔王はかつて勇者だった"),
            yusha.rescue(ordy).ps(),
            )

# story
def story():
    ma = Master('yunazo 08')
    yusha, panna, crades, emile = Yusha(), Panna(), Crades(), Emile()
    ordy, mam, dad = boy_ordy(), mam_ordy(), dad_ordy()
    people = vila_people()
    vila, home = zibonga_vila(), ordy_home()
    fes, tale = devils_fes(), real_tale()
    pday, bday, fday = past_day(), before_day(), fes_day()
    return ma.story("勇者は冒険より三周年魔王祭の謎解きをしたい",
            ep_intro(ma, yusha, panna, crades, emile, ordy,
                fes, vila, bday),
            ep_maou(ma, yusha, panna, crades, emile, ordy,
                mam, dad,
                fes, vila, home, bday, pday),
            ep_festa(ma, yusha, panna, crades, emile, ordy,
                people,
                fes, tale, vila, fday),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
