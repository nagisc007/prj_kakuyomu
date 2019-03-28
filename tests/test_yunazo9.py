# -*- coding: utf-8 -*-
"""Test for yunazo story 08.
"""
import unittest

from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story9.story import story, ep1, ep2, ep3


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
        pass

    def test_has_outline_infos(self):
        pass

    def test_followed_all_flags(self):
        pass

