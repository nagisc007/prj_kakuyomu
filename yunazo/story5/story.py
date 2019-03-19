# -*- coding: utf-8 -*-
"""Story program for yunazo story 05.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Master
from storybuilder.builder.tools import build_to_story

from common import Yusha, Panna, Crades


def intro(ma: Master):
    return ma.story(
            ma.title("イントロ"),
            )

def strange_oldman(ma: Master):
    return ma.story(
            ma.title("奇妙な老人"),
            )

def real_criminal(ma: Master):
    return ma.story(
            ma.title("真犯人"),
            )

def story():
    '''Create a story object.
    '''
    ma = Master("Yunazo5")
    return ma.story(
            ma.title("勇者は冒険よりＡＢＣ商店消失の謎解きをしたい"),
            intro(ma),
            strange_oldman(ma),
            real_criminal(ma)
            )

def main():
    '''main function.
    '''
    build_to_story(story())

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

