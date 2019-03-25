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

# stages

# items

# words

# daytimes


# episodes
def ep1(ma: Master):
    return ma.story("ep1",
            )

def ep2(ma: Master):
    return ma.story("ep2",
            )

def ep3(ma: Master):
    return ma.story("ep3",
            )

# story
def story():
    ma = Master('yunazo 08')
    return ma.story("勇者は冒険より三周年魔王祭の謎解きをしたい",
            ep1(ma),
            ep2(ma),
            ep3(ma),
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
