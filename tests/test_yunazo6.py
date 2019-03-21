# -*- coding: utf-8 -*-
"""Test for yunazo story 06
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story6.story import story
from yunazo.story6.story import ep_intro, ep_competition, ep_realflavor
from yunazo.story6.story import Yusha, Emile


class StoryTest(unittest.TestCase):
    """Test the story.
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo 06 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            Yusha(), Emile()))

    def test_has_outline_infos(self):
        #self.assertTrue(testtools.has_outline_infos())
        pass

