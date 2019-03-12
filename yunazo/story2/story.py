# -*- coding: utf-8 -*-
"""Story building as Yunazo-story2.
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
from common import Yusha, Panna, Crades, Emile, Badac, TH_Tanaka
from common import DondahlTown, BadacCave, BadacSecretRoom
from common import BadacMap, BadacPics, BadacCaveDoor
from common import TreasureDay


# episodes
def ep_intro(cave, tday, yusha, panna, emile, tanaka, bmap, bdoor):
    '''Intro story.
    '''
    return (
            cave.look("ごく普通の洞窟内"),
            tday.look("外は午前だが、ここは薄暗い"),
            yusha.act("宝の地図の謎解き", Behavior.REQUEST),
            yusha.act("{}から{}".format(tanaka.name, bmap.name), Behavior.GET),
            yusha.tell("何もない"),
            panna.tell("何もない"),
            yusha.must("宝を見つける"),
            yusha.want("地図の謎を解く"),
            panna.tell("{}に書いてあるんでしょ？".format(bmap.name)),
            cave.look("一番奥に扉が一つだけある"),
            bdoor.look("小さな扉が裏側にある"),
            panna.act("{}を開ける".format(bdoor.name)),
            cave.look("表の方で音がする"),
            emile.act("表の入り口", Behavior.CHECK),
            emile.tell("入り口が閉じられていた"),
            yusha.result("洞窟に閉じ込められる"),
            )


def ep_incave(cave, tday, yusha, emile, panna, bmap):
    '''In cave story.
    '''
    return (
            cave.look("他には出入り口がない"),
            tday.look("大した時間が経っていない"),
            yusha.result("隠し部屋を発見する"),
            )


def ep_treasure(secroom, tday, yusha, panna, emile, bpics):
    '''His treasure.
    '''
    return (
            secroom.look("そこは隠し部屋"),
            bpics.look("絵が沢山散らばっている"),
            secroom.look("絵以外には特に何もない"),
            yusha.result("二番目が本当は一番だったと理解する"),
            )


# main story
def story():
    '''Story builded.
    '''
    # characters
    yusha = Yusha()
    panna = Panna()
    emile = Emile()
    tanaka = TH_Tanaka()
    # stages
    cave = BadacCave()
    secroom = BadacSecretRoom()
    # items
    bmap = BadacMap()
    bpics = BadacPics()
    bdoor = BadacCaveDoor()
    # daytimes
    tday = TreasureDay()

    return ep_intro(cave, tday, yusha, panna, emile, tanaka, bmap, bdoor)\
            + ep_incave(cave, tday, yusha, panna, emile, bmap)\
            + ep_treasure(secroom, tday, yusha, panna, emile, bpics)


def main(is_debug=True):
    '''main method.
    '''
    STORY_FILE = 'yunazo2'

    mystory = story()

    # output to the console
    output(mystory, is_debug=is_debug)

    # output to a markdown
    output_md(mystory, STORY_FILE, is_debug=is_debug)

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())
