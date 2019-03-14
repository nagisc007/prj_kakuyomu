# -*- coding: utf-8 -*-
"""Test for yunazo story3.
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

from yunazo.common import Yusha, Panna


class StoryTest(unittest.TestCase):
    """Test story.
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo3 ****")

    def setUp(self):
        pass

    def test_story_actions(self):
        pass

    def test_story_basic_info(self):
        pass


class EpisodeTest_intro(unittest.TestCase):
    """Test episode of intro.
     * Outline
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

    def test_intro_actions(self):
        pass

    def test_intro_basic_info(self):
        pass

