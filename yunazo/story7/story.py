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

# items

# words

# daytimes

# episodes
def ep_intro(ma: Master):
    return ma.story(
            )

def ep_in_dream(ma: Master):
    return ma.story(
            )

def ep_out_dream(ma: Master):
    return ma.story(
            )


# story
def story():
    ma = Master("yunazo7")

    return ma.story(
            ma.title("勇者は冒険より夢中病の謎解きをしたい"),
            ep_intro(ma),
            ep_in_dream(ma),
            ep_out_dream(ma),
            )


def main():
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
