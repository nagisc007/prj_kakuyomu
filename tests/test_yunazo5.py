# -*- coding: utf-8 -*-
"""Test for yunazo story 05
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
import storybuilder.builder.testtools as testtools

from yunazo.story5.story import story
from yunazo.story5.story import intro
from yunazo.story5.story import strange_oldman
from yunazo.story5.story import real_criminal

from yunazo.story5.story import Yusha, Panna, Crades, Claire
from yunazo.story5.story import Donston


class StoryTest(unittest.TestCase):
    """Test story.
    * outline
        - Who: 勇者
        - Whom: クラデス（容疑者）
        - When: 六月末（クラデスと出会う前）
        - Where: ドンストンの警察本部
        - What: クラデスの容疑を晴らす
        - Why: クラデスはやっていない
        - How: 真犯人を暴く
        - Result: 店を継ぎたくない息子の犯行だった
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo5 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, Yusha(), Crades()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha(), Behavior.DISPEL, "容疑",
            Yusha(), Behavior.BELIEVE, "やっていない",
            Yusha(), Behavior.TELL, "真犯人を見つける",
            Claire(), Behavior.CONFESS, "継ぎたくない")
            )


class EpisodeTest(unittest.TestCase):
    """Test episodes.
    * outline of Intro
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    * outline of Strange oldman
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    * outline of Real criminal
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

