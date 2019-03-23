# -*- coding: utf-8 -*-
"""The story program for yunazo story 07.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.base import Stage, Item, DayTime, Word, Master
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story

from common import Yusha, Panna, Crades, Emile


# characters

# stages
def noardo():
    return Stage("ノアルド", "全員が眠る村")

# items
def wall_memo():
    return Item("壁のメモ", "壁にびっしり書かれた謎の文字")


# words
def dream_syndrome():
    return Word("夢中病", "何かに夢中になりそのまま夢の中にいついてしまう謎の病")

# daytimes
def visit_day():
    return DayTime("訪問日", 10, 11, 1018)


# episodes
def ep_intro(ma: Master,
        yusha: Yusha, panna: Panna, crades: Crades, emile: Emile,
        vila: Stage,
        day: DayTime):
    return ma.story(
            vila.explain("そこは全員が眠る村だった"),
            day.explain("小春日和の午後"),
            yusha.visit("", obj=vila),
            yusha.investigate("", vila),
            yusha.know("村の噂",obj=vila),
            yusha.search("",obj=vila),
            panna.visit("",obj=vila),
            crades.visit("",obj=vila),
            emile.visit("",obj=vila),
            vila.explain("全員本当に眠っている"),
            panna.sleep(),
            crades.sleep(),
            )

def ep_in_dream(ma: Master,
        yusha: Yusha, emile: Emile, panna: Panna, crades: Crades,
        dreamsyn: Word, memo: Item,
        vila: Stage,
        day: DayTime):
    return ma.story(
            panna.sleep(),
            crades.sleep(),
            yusha.leave("二人", emile),
            yusha.solve("", dreamsyn),
            vila.explain("村の教会を訪れる"),
            memo.explain("地下室の壁にびっしり書かれている"),
            yusha.read("", memo),
            day.explain("いつの間にか夕闇に"),
            emile.ask("夢中になるもの", yusha),
            yusha.reply("謎解き", emile),
            yusha.talk("謎解き"),
            yusha.dream("幼い頃のこと"),
            yusha.sleep(),
            )

def ep_out_dream(ma: Master,
        yusha: Yusha, emile: Emile, panna: Panna, crades: Crades,
        dreamsyn: Word,
        vila: Stage,
        day: DayTime):
    return ma.story(
            day.explain("まだ村に来て一時間と経っていない"),
            day.explain("外は明るい"),
            vila.explain("宿屋のベッドの上に運んだ"),
            panna.talk("眠ったまま",obj=yusha),
            yusha.sleep(),
            emile.wake("", yusha),
            emile.hear("解除方法", crades),
            crades.teach("{}の解除方法".format(dreamsyn.name)),
            dreamsyn.explain("その人物に夢中な人からのキスにより解除"),
            panna.kiss("",obj=yusha),
            emile.kiss("",obj=yusha),
            yusha.wake(),
            )


# story
def story():
    ma = Master("yunazo7")
    yusha, panna, crades, emile = Yusha(), Panna(), Crades(), Emile()
    vila = noardo()
    memo = wall_memo()
    dreamsyn = dream_syndrome()
    vday = visit_day()

    return ma.story(
            ma.title("勇者は冒険より夢中病の謎解きをしたい"),
            ep_intro(ma, yusha, panna, crades, emile,
                vila, vday),
            ep_in_dream(ma, yusha, emile, panna, crades,
                dreamsyn, memo,
                vila, vday),
            ep_out_dream(ma, yusha, emile, panna, crades,
                dreamsyn,
                vila, vday),
            )


def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
