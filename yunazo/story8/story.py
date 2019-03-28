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

def vila_child():
    return Person("村の子供", 10, "male", "子供")

def vila_sailor():
    return Person("渡し守", 58, "male", "船乗り", "おら")

# stages
def zibonga_vila():
    return Stage("ジボンガ", "魔王を崇めている集落")

def ordy_home():
    return Stage("オルディの家", "板と布を重ねた粗末な家")


# items
def broken_sword():
    return Item("折れた剣", "オルディが持っている父の形見。実は魔王の持っていた勇者の剣")


# words
def devils_fes():
    return Word("魔王祭", "魔王を崇める祭。今年で三周年")

def real_tale():
    return Word("真実の話", "三年前に魔王が助けたという話の真実")

def yusha_mark():
    return Word("勇者の印", "勇者に関係するものに刻印されている紋章")

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
        child: Person, sailor: Person,
        fes: Word,
        vila: Stage,
        day: DayTime):
    return ma.story("魔王を崇める村",
            ma.scene("村訪問",
                vila.explain("海に囲まれた小さな島国"),
                day.explain("春と呼ばれる季節"),
                day.explain("その最初の日に祭りが行われる"),
                sailor.talk(yusha, info="ようこそ"),
                yusha.visit(vila, info="仲間と共に"),
                panna.visit(vila),
                crades.visit(vila),
                emile.visit(vila),
                panna.explain("小柄な金髪少女"),
                panna.dress(info="ぴっちりした黒のハーフパンツ"),
                panna.ask(fes),
                crades.explain("白い顎髭に分厚い白眉"),
                crades.explain("大きな水晶のついた杖を持つ"),
                emile.explain("全身を甲冑で固め、兜で顔が見えない"),
                yusha.hear(fes),
                yusha.talk(fes),
                yusha.want(fes, info="知る"),
                vila.explain("粗末な木造の家が並ぶ"),
                ),
            ma.scene("嫌われの勇者",
                vila.explain("中央広場"),
                yusha.investigate(fes),
                yusha.investigate(vila),
                child.hate(yusha),
                child.throw(yusha, info="石"),
                child.know(yusha, info="勇者である").set_flag(yusha.name),
                yusha.wonder(child, info="自分を知っていたこと"),
                ),
            ma.scene("勇者好きの少年",
                ordy.angry(child),
                ordy.talk(child, info="勇者が本当の英雄なんだぞ"),
                ordy.talk(child, info="特別な子").ps().set_flag(ordy.name),
                yusha.meet(ordy),
                ordy.know(yusha, info="勇者"),
                ordy.glad(yusha, info="出会えて"),
                ordy.invite(yusha, info="自分の家"),
                ),
            )

def ep_maou(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        ordy: Person, mam: Person, dad: Person, sailor: Person,
        fes: Word, tale: Word, sword: Item, mark: Word,
        vila: Stage, home: Stage,
        day: DayTime, pday: DayTime):
    return ma.story("魔王と勇者",
            ma.scene("魔王に救われた村",
                day.explain("夕闇が落ちてきた"),
                home.explain("風雨をなんとかしのげる程度の粗末の木造家屋"),
                mam.glad(yusha),
                mam.explain("荒れた髪にシミの多い肌"),
                mam.explain("疲れた目尻"),
                sword.explain("部屋の片隅に柄だけの剣"),
                ordy.talk(sword, info="父親の形見").set_flag(sword.name),
                yusha.think(ordy, info="貧しい"),
                ordy.talk(yusha, info="勇者"),
                yusha.hear(ordy, info="祭り"),
                ordy.know(fes),
                ordy.want(yusha),
                yusha.ask(ordy, info="自分を勇者と知っている理由"),
                crades.talk(mark).set_flag(mark.name),
                ordy.reply(yusha, info="{}から聞いた".format(sailor.name)).set_deflag(yusha.name),
                ),
            ma.scene("三年前の話",
                yusha.teach(ordy, info="勇者"),
                ordy.teach(pday),
                ordy.talk(pday, info="村が津波で壊滅状態に"),
                ordy.teach(dad, info="その津波で亡くなる").set_flag(tale.name),
                yusha.know(dad, info="三年前に亡くなる"),
                ordy.talk(pday, info="村を襲う勇者を魔王が退治した"),
                ordy.hear(dad, info="魔王が本当は勇者だと"),
                yusha.know(vila, info="魔王が救った"),
                ),
            ma.scene("裏切りの夜",
                yusha.eat(),
                ordy.sleep(),
                mam.talk(pday, info="以来この村は魔王軍から襲われない"),
                yusha.sleep(),
                mam.whisper(yusha, info="ごめんなさい"),
                ),
            )

def ep_festa(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile, ordy: Person,
        people: Person, mam: Person,
        fes: Word, tale: Word, sword: Item, mark: Word,
        vila: Stage,
        day: DayTime, pday: DayTime):
    return ma.story("魔王の謎",
            ma.scene("捕まる勇者",
                day.explain("祭りの朝だった"),
                yusha.wake(),
                vila.explain("中央の広場で"),
                yusha.bind(),
                yusha.catch(people).ps(),
                mam.talk(yusha, info="勇者に夫は殺された").set_deflag(tale.name),
                people.speak(info="勇者たちを殺せ"),
                ),
            ma.scene("少年の勇気",
                ordy.rescue(yusha),
                ordy.help(panna, info="勇者の仲間は助けた"),
                panna.talk(crades, info="自分が村人から勇者を助け出す"),
                ordy.tell("魔王はそんなこと望んでない"),
                ordy.talk(people, info="本当のこと"),
                ordy.talk(tale).set_deflag(ordy.name),
                ),
            ma.scene("魔王の真実",
                ordy.talk(pday),
                ordy.attack(info="強盗").ps(),
                ordy.rescue(info="魔王に").ps(),
                ordy.talk(people, info="魔王が自分は昔勇者だったと語った"),
                ordy.teach(info="魔王はかつて勇者だった"),
                ordy.talk(sword, info="本当は魔王の持ち物だった").set_deflag(sword.name),
                crades.talk().set_deflag(mark.name),
                yusha.rescue(ordy).ps(),
                ),
            )

# story
def story():
    ma = Master('yunazo 08')
    yusha, panna, crades, emile = Yusha(), Panna(), Crades(), Emile()
    ordy, mam, dad = boy_ordy(), mam_ordy(), dad_ordy()
    people, child, sailor = vila_people(), vila_child(), vila_sailor()
    vila, home = zibonga_vila(), ordy_home()
    sword = broken_sword()
    fes, tale, mark = devils_fes(), real_tale(), yusha_mark()
    pday, bday, fday = past_day(), before_day(), fes_day()
    return ma.story("勇者は冒険より三周年魔王祭の謎解きをしたい",
            ep_intro(ma, yusha, panna, crades, emile, ordy,
                child, sailor,
                fes, vila, bday),
            ep_maou(ma, yusha, panna, crades, emile, ordy,
                mam, dad, sailor,
                fes, tale, sword, mark,
                vila, home, bday, pday),
            ep_festa(ma, yusha, panna, crades, emile, ordy,
                people, mam,
                fes, tale, sword, mark,
                vila, fday, pday),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
