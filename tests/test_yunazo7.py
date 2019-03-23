# -*- coding: utf-8 -*-
"""Test for yunazo story 06
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story7.story import story
from yunazo.story7.story import ep_intro, ep_in_dream, ep_out_dream
from yunazo.story7.story import Yusha, Panna, Crades, Emile
from yunazo.story7.story import noardo


class StoryTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: story yunazo 7 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            Yusha(), Emile()))

    def test_has_outline_infos(self):
        vila = noardo()
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha().search("",obj=vila),
            Yusha().know("",obj=vila),
            Yusha().visit("",obj=vila),
            Yusha().wake(),
            ))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        self.ma = Master('test')
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_in_dream(self.ma)
        self.ep3 = ep_out_dream(self.ma)

    def test_ep1_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep1))

    def test_ep2_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep2))

    def test_ep3_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep3))

    def test_ep1_has_basic_infos(self):
        pass

    def test_ep2_has_basic_infos(self):
        pass

    def test_ep3_has_basic_infos(self):
        pass

    def test_ep1_has_outline_infos(self):
        pass

    def test_ep2_has_outline_infos(self):
        pass

    def test_ep3_has_outline_infos(self):
        pass
