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
from yunazo.story6.story import Yusha, Panna, Crades, Emile, Conny
from yunazo.story6.story import NachansTown, TownBar
from yunazo.story6.story import HotDok
from yunazo.story6.story import BeforeDay, CompeDay


class StoryTest(unittest.TestCase):
    """Test the story.
    """
    @classmethod
    def setUpClass(cls):
        print("\n**** story of yunazo 06 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            Yusha(), Emile()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha().investigate("大会での不正疑惑"),
            Yusha().accept("大会調査依頼"),
            Yusha().let("{}を大会参加".format(Panna().name)), # how
            Emile().eat("本物の{}".format(HotDok().name)), # result
            ))

class EpisodeTest(unittest.TestCase):
    """Test episodes.
    """
    def setUp(self):
        self.ma = Master("test master")
        self.ep_intro = ep_intro(self.ma,
                Yusha(), Panna(), Crades(), Emile(), Conny(),
                NachansTown(), BeforeDay(), HotDok())
        self.ep_compe = ep_competition(self.ma,
                Yusha(), Panna(), Crades(), Emile(),
                NachansTown(), TownBar(), BeforeDay(), CompeDay())
        self.ep_flavor = ep_realflavor(self.ma,
                Yusha(), Panna(), Crades(), Emile(),
                NachansTown(), CompeDay(), HotDok())

    def test_intro_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep_intro,
            Yusha(), Panna()))

    def test_intro_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep_intro,
            Yusha().investigate("大会での不正疑惑"),
            Yusha().accept("大会調査依頼"),
            Yusha().visit(NachansTown().name),
            Yusha().see("{}の悲しげな様".format(Emile().name)),
            ))

    def test_compe_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep_compe,
            Yusha(), Emile()))

    def test_compe_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep_compe,
            Yusha().release("{}を大会から".format(Emile().name)),
            Yusha().think("{}が気になる".format(Emile().name)),
            Yusha().investigate(Emile().name),
            Yusha().know("呪いの所為"),
            ))

    def test_flavor_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep_flavor,
            Yusha(), Emile()))

    def test_flavor_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep_flavor,
            Yusha().must("{}の呪いを解く".format(Emile().name)),
            Yusha().think("{}を助けるべき".format(Emile().name)),
            Yusha().confess("{}の素顔が美しい".format(Emile().name)),
            Emile().tell("美味しい"),
            ))

