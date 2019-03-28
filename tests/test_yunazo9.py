# -*- coding: utf-8 -*-
"""Test for yunazo story 08.
"""
import unittest

from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story9.story import story, ep1, ep2, ep3
from yunazo.story9.story import charas, stages, items, words, daytimes


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: story yunazo 9 ****")

    def setUp(self):
        ma = Master('test yunazo9')
        self.story = story()
        self.ep1 = ep1(ma)
        self.ep2 = ep2(ma)
        self.ep3 = ep3(ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        yusha, orga = charas("yusha"), charas("orga")
        self.assertTrue(testtools.has_basic_infos(self, self.story, yusha, orga))

    def test_has_outline_infos(self):
        yusha, panna = charas("yusha"), charas("panna")
        wyusha = words("yusha")
        childhood = daytimes("childhood")
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            yusha.talk(about=wyusha),
            panna.wonder(about=wyusha),
            yusha.talk(about=childhood),
            yusha.teach(wyusha, to=panna),
            ))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

