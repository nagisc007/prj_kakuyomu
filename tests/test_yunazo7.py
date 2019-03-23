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
from yunazo.story7.story import dream_syndrome, wall_memo
from yunazo.story7.story import visit_day


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
            Yusha().know("村の噂",obj=vila),
            Yusha().visit("",obj=vila),
            Yusha().wake(),
            ))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        self.ma = Master('test')
        self.ep1 = ep_intro(self.ma, Yusha(), Panna(), Crades(), Emile(),
                noardo(), visit_day())
        self.ep2 = ep_in_dream(self.ma, Yusha(), Emile(), Panna(), Crades(),
                dream_syndrome(), wall_memo(),
                noardo(), visit_day())
        self.ep3 = ep_out_dream(self.ma, Yusha(), Emile(), Panna(), Crades(),
                dream_syndrome(),
                noardo(), visit_day())

    def test_ep1_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep1))

    def test_ep2_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep2))

    def test_ep3_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep3))

    def test_ep1_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep1,
            Yusha(), Emile()))

    def test_ep2_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep2,
            Yusha(), Emile()))

    def test_ep3_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep3,
            Emile(), Yusha()))

    def test_ep1_has_outline_infos(self):
        vila = noardo()
        self.assertTrue(testtools.has_outline_infos(self, self.ep1,
            Yusha().investigate("", vila),
            Yusha().know("村の噂", vila),
            Yusha().visit("", vila),
            Panna().sleep(),
            ))

    def test_ep2_has_outline_infos(self):
        dreamsyn = dream_syndrome()
        memo = wall_memo()
        self.assertTrue(testtools.has_outline_infos(self, self.ep2,
            Yusha().solve("", dreamsyn),
            Panna().sleep(),
            Yusha().read("", memo),
            Yusha().sleep(),
            ))

    def test_ep3_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep3,
            Emile().wake("", Yusha()),
            Yusha().sleep(),
            Emile().hear("解除方法", Crades()),
            Emile().kiss("", Yusha())
            ))
