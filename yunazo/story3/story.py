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
from common import Yusha, Panna, Crades, Emilee


# episodes
def ep_intro():
    '''Intro episode.
    '''
    return (
            )


def ep_middle():
    '''Middle episode.
    '''
    return (
            )


def ep_end():
    '''End episode.
    '''
    return (
            )


# main story
def story():
    '''Story builded.
    '''
    return ep_intro()\
            + ep_middle()\
            + ep_end()


def main():
    '''main.
    '''
    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

