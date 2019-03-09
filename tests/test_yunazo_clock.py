# -*- coding: utf-8 -*-
"""Test for story of yu-nazo1
"""
import unittest

from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime

from yunazo_clock.story import Yusha, Panna, Crades, Emile
from yunazo_clock.story import ClocVila, Inn
from yunazo_clock.story import OwlClock
from yunazo_clock.story import OneDay
from yunazo_clock.story import story
from yunazo_clock.story import ep_intro
from yunazo_clock.story import ep_resolve

from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info


class StoryTest(unittest.TestCase):

    def setUp(self):
        self.acts = story()

    def test_story_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))


class EpisodeTest_intro(unittest.TestCase):

    def setUp(self):
        self.acts = ep_intro(
                Inn(), OneDay(), Yusha(), Panna()
                )

    def test_intro_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))


class EpisodeTest_resolve(unittest.TestCase):

    def setUp(self):
        self.acts = ep_resolve(
                Inn(), OneDay(), Yusha(), Panna()
                )

    def test_resolve_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_resolve_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))

