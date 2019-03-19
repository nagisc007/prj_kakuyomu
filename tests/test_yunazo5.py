# -*- coding: utf-8 -*-
"""Test for yunazo story 05
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
from storybuilder.builder.testtools import is_all_actions
from storybuilder.builder.testtools import has_basic_infos
from storybuilder.builder.testtools import has_outline_infos

from yunazo.story5.story import story
from yunazo.story5.story import intro
from yunazo.story5.story import strange_oldman
from yunazo.story5.story import real_criminal


class StoryTest(unittest.TestCase):
    """Test story.
    * outline
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo5 ****")

    def setUp(self):
        pass


class EpisodeTest(unittest.TestCase):
    """Test episodes.
    * outline of Intro
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    * outline of Strange oldman
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    * outline of Real criminal
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    """
    def setUp(self):
        pass

