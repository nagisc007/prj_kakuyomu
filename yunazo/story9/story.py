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
    return ma.story("episode 1",
            )

def ep2(ma: Master):
    return ma.story("episode 2",
            )

def ep3(ma: Master):
    return ma.story("episode 3",
            )


# story
def story():
    ma = Master('Yunazo 09')
    return ma.story("勇者は冒険より勇者誕生の謎解きをしたい",
            )

# main
def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
