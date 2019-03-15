# -*- coding: utf-8 -*-
"""Story building as Yunazo-story3.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

# import libs
from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Title 
from storybuilder.builder.tools import output, output_md

# import data
from common import Yusha, Panna, Manderine
from common import WaroneHouse, SilverForest
from common import RentalPony, TabooBook
from common import MeetDay

# episodes
def ep_intro(house, day, yusha, panna, manderine):
    '''Intro episode.
    '''
    return (
            day.look("まだ二人が出会う前のこと"),
            house.look("豪華な応接間"),
            yusha.check("財布の中身"),
            yusha.want("渡航費が稼ぎたい"),
            manderine.come("部屋に"),
            manderine.tell("大事なお嬢様がいなくなり捜索して欲しい"),
            manderine.talk("礼金の話"),
            yusha.ask("そのお嬢様とは？"),
            manderine.explain("{}のこと".format(panna.name)),
            yusha.result("{}の捜索依頼を受けた".format(panna.name)),
            )


def ep_in_forest(forest, day, yusha, panna, pony, book):
    '''Middle episode.
    '''
    return (
            day.look("日が傾き、夜になる"),
            forest.look("月明かりが照らす森"),
            forest.look("その泉の前"),
            panna.think("王子来ないやん"),
            panna.look("裾の長い白銀のドレス姿"),
            yusha.look("{}に乗っている".format(pony.name)),
            yusha.talk("自己紹介"),
            panna.tell("王子に会うまで帰らへん"),
            panna.explain("白銀の王子の伝説"),
            panna.talk("{}に書いてあった".format(book.name)),
            book.look("倉庫に眠っていた"),
            yusha.result("{}を説得する為に王子の謎を解く"),
            )


def ep_truth(forest, day, yusha, panna, pony, book):
    '''End episode.
    '''
    return (
            day.look("夜"),
            forest.look("湖畔が月明かりで輝く"),
            yusha.must("{}を連れて帰る".format(panna.name)),
            yusha.talk("白銀の馬の王子の伝説が生まれた事情"),
            panna.tell("なんで？"),
            yusha.tell("最初から王子なんていなかった"),
            yusha.tell("白銀の馬などいない"),
            yusha.explain("白銀は甲冑の色のことだ"),
            yusha.explain("川向こうから兵士が娘を拐いにきた"),
            yusha.tell("伝承が伝説に書き換えられたんだ"),
            panna.tell("でも自分にとっては{}が王子様だ".format(yusha.name)),
            yusha.result("{}がパーティに加わった")
            )


# main story
def story():
    '''Story builded.
    '''
    # characters
    yusha = Yusha()
    panna = Panna()
    manderine = Manderine()
    # stages
    house = WaroneHouse()
    forest = SilverForest()
    # items
    pony = RentalPony()
    book = TabooBook()
    # daytimes
    day = MeetDay()

    return ep_intro(house, day, yusha, panna, manderine)\
            + ep_in_forest(forest, day, yusha, panna, pony, book)\
            + ep_truth(forest, day, yusha, panna, pony, book)


def main(is_debug=True):
    '''main.
    '''
    STORY_FILE = 'yunazo3'

    mystory = story()

    # output to the console
    output(mystory, is_debug=is_debug)

    # output to a markdown
    output_md(mystory, STORY_FILE, is_debug=is_debug)

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

