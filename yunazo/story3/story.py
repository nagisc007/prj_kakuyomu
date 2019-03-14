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
from common import RentalPony
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
            yusha.result("{}の捜索依頼を受けた".format(panna.name)),
            )


def ep_in_forest(forest, day, yusha, panna, pony):
    '''Middle episode.
    '''
    return (
            day.look("日が傾き、夜になる"),
            forest.look("月明かりが照らす森"),
            forest.look("その泉の前"),
            panna.think("王子来ないやん"),
            panna.look("裾の長い白銀のドレス姿"),
            )


def ep_truth(forest, day, yusha, panna, pony):
    '''End episode.
    '''
    return (
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
    # daytimes
    day = MeetDay()

    return ep_intro(house, day, yusha, panna, manderine)\
            + ep_in_forest(forest, day, yusha, panna, pony)\
            + ep_truth(forest, day, yusha, panna, pony)


def main():
    '''main.
    '''
    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

