# -*- coding: utf-8 -*-
"""Story that Yusha like a mystery than an adventure.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Title 
from storybuilder.builder.tools import output, output_md

# import data
from common import Yusha, Panna, InnOwner
from common import ClocVila, Inn
from common import OwlClock
from common import OneDay


# episodes
def ep_intro(inn, vila, oneday, yusha, panna, oclock):
    '''Intro story.
    '''
    return (
            Title("フクロウ時計"),
            oneday.look("既にすっかり日が昇ってしまっていた"),
            inn.look("村唯一の宿で、しかも部屋が埋まっているという"),
            inn.look("そこで仕方なく、一人部屋に二人押し込められたという訳だ"),
            vila.look("ここが山間の寂れた村だということ"),
            yusha.want("家賃を安くすませる"),
            yusha.think("それを忘れてしまうような安眠だった"),
            panna.tell("なあなあ、{}。まだ眠るん？　結局朝ご飯食べ損ねたやん".format(yusha.name)),
            panna.look("小柄で肩までの金髪が跳ね返っている"),
            yusha.look("右の前髪がつんと天井を向いている"),
            yusha.act("目覚める", Behavior.WAKE),
            yusha.look("本当に一日ずっと起きて見張っていたのか？"),
            panna.look("昨日からずっと夜通し起きてたよ。なんで勇者はさっさと寝ちゃったの。せっかく二人きりになれたのにさ"),
            yusha.tell("それで{}はアレが鳴くのを聞けたのか？".format(panna.name)),
            panna.tell("ううん"),
            yusha.tell("本当に一度も鳴かなかったのか？"),
            panna.tell("うん"),
            yusha.think("アレとは棚の上に飾られた{}のことだ".format(oclock.name)),
            yusha.tell("宿の主と約束したからな。何故{}が鳴かなくなってしまったのか。その謎を解けば家賃を半額にしてくれると".format(oclock.name)),
            yusha.result("{}に店主を呼ぶよう頼む".format(panna.name)),
            )


def ep_mystery(inn, oneday, yusha, panna, owner, oclock):
    '''Mystery story.
    '''
    return (
            Title("鳴かないフクロウ"),
            oneday.look("ぼんやりとした日差しが差し込んでいた"),
            inn.look("床も天井も随分と古くなっている"),
            yusha.must("フクロウ時計の謎を解く"),
            yusha.think("家賃を安くしたい"),
            yusha.tell("謎なんか最初からなかったのさ"),
            panna.tell("どゆこと？"),
            yusha.tell("家賃を半額にしてもらわないと、手持ちのお金が足りないんだよ"),
            owner.act("部屋に入ってくる", Behavior.COME),
            yusha.tell("すみません。少し聞かせてもらえませんか。"),
            oneday.look("その時だった"),
            oclock.look("別の部屋で{}が鳴いた".format(oclock.name)),
            yusha.result("店主に解いた謎を披露する"),
            )


def ep_resolve(inn, oneday, yusha, panna, owner, oclock):
    '''Resolve story.
    '''
    return (
            Title("そして鳥は動き出す"),
            oneday.look("まだ夕方にはなっていない"),
            inn.look("部屋の中には空気がわだかまっていた"),
            yusha.want("家賃を半額にする"),
            yusha.think("謎が解けた"),
            yusha.tell("謎は既に解けていたんだよ"),
            panna.tell("それで何が分かったの？"),
            yusha.tell("結局何も起こっていない、ということさ"),
            yusha.tell("丸一日観察してみたが、一度として鳴かなかった"),
            yusha.tell("これはね、どこからどう見ても鳩時計なんだよ"),
            owner.tell("じゃあどうして鳴かないんで？"),
            yusha.tell("簡単なことだ。壊れているんだよ"),
            yusha.tell("あなたが貰ってきた時にはまだ正常に動いていたが、ここを見てくれ"),
            yusha.act("{}の下を分解して見せた".format(oclock.name)),
            owner.tell("それが？"),
            yusha.tell("ここに微弱な魔法力を出す魔石がある。おそらくはそれに寿命がきたんだ。これを新しいものと取り替えれば、動き出す可能性もある"),
            oclock.look("村で一斉に鳩時計が鳴き出した"),
            yusha.result("謎を解いた"),
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
            ep_mystery(inn, oneday, yusha, panna, owner, oclock) +\
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

