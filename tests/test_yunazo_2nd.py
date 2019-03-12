# -*- coding: utf-8 -*-
"""Test for yunazo story2.
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

from yunazo.common import Yusha, Panna, Crades, Emile, Badac, TH_Tanaka
from yunazo.common import BadacCave, DondahlTown, BadacSecretRoom
from yunazo.common import BadacMap, BadacPics
from yunazo.common import TreasureDay
from yunazo.story2.story import story
from yunazo.story2.story import ep_intro
from yunazo.story2.story import ep_incave
from yunazo.story2.story import ep_treasure


class StoryTest(unittest.TestCase):
    """Test story.
    """
    def setUp(self):
        self.acts = story()

    def test_story_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "謎を解く", "地図"))


class EpisodeTest_intro(unittest.TestCase):
    """Test episode intro.
    """
    def setUp(self):
        pass

    def test_intro_actions(self):
        pass

    def test_intro_basic_info(self):
        pass


class EpisodeTest_incave(unittest.TestCase):
    """Test episode incave.
    """
    def setUp(self):
        pass

    def test_incave_actions(self):
        pass

    def test_incave_basic_info(self):
        pass


class EpisodeTest_treasure(unittest.TestCase):
    """Test episode treasure.
    """
    def setUp(self):
        pass

    def test_treasure_actions(self):
        pass

    def test_treasure_basic_info(self):
        pass


