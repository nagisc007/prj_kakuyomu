# -*- coding: utf-8 -*-
"""Test for yunazo story 08.
"""
import unittest

from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story8.story import story
from yunazo.story8.story import ep_intro, ep_maou, ep_festa
from yunazo.story8.story import Yusha, Panna, Crades, Emile
from yunazo.story8.story import boy_ordy
from yunazo.story8.story import zibonga_vila
from yunazo.story8.story import devils_fes
from yunazo.story8.story import past_day, before_day, fes_day

class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: story yunazo 8 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, Yusha(), Panna()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha().hear(devils_fes()),
            Yusha().want(devils_fes(), "知る"),
            Yusha().investigate(zibonga_vila()),
            Yusha().know(zibonga_vila(), "魔王が救った"),
            ))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodesTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_episodes_has_basic_infos(self):
        # for p1, p2, p3 in tables:
        # with self.subTest(param1=p1,param2=p2...)
        # self.assertEqual()
        pass

    def test_episodes_has_outline_infos(self):
        pass
