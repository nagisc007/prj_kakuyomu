# -*- coding: utf-8 -*-
"""Test for yunazo story3.
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

from yunazo.common import Yusha, Panna, Manderine
from yunazo.common import WaroneHouse, SilverForest
from yunazo.common import RentalPony
from yunazo.common import MeetDay

from yunazo.story3.story import story
from yunazo.story3.story import ep_intro
from yunazo.story3.story import ep_in_forest
from yunazo.story3.story import ep_truth


class StoryTest(unittest.TestCase):
    """Test story.
    * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 二人がパーティを組む前（二年前）
        - Where: 白馬の王子伝説のある森
        - What: 家出したパンナを連れ戻す
        - Why: 渡航費を稼ぐ
        - How: 家出娘捜索依頼を受ける
        - Result: パンナが勇者とパーティを組む
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo3 ****")

    def setUp(self):
        self.acts = story()

    def test_story_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_basic_info(self):
        self.assertTrue(checked_has_basic_info(
            self, self.acts, Yusha(), Panna(), "渡航費", "捜索依頼"
            ))


class EpisodeTest_intro(unittest.TestCase):
    """Test episode of intro.
     * Outline
        - Who: 勇者
        - Whom: マンデリン
        - When: 二人が出会う前（二年前）
        - Where: ワローン邸の応接間
        - What: 渡航費を稼ぐ
        - Why: 金がない
        - How: 捜索依頼を引き受ける
        - Result: 捜索依頼を引き受けた
    """
    def setUp(self):
        self.acts = ep_intro(
                WaroneHouse(), MeetDay(), Yusha(), Panna(), Manderine()
                )

    def test_intro_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_basic_info(self):
        self.assertTrue(checked_has_basic_info(
            self, self.acts, Yusha(), Manderine(), "渡航費", "捜索依頼"
            ))


class EpisodeTest_in_forest(unittest.TestCase):
    """Test episode of in forest.
     * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 捜索依頼を受けた日の夜
        - Where: 白銀の湖畔
        - What: パンナを見つける
        - Why: 捜索依頼された
        - How: 説得する
        - Result: パンナは白銀の王子が現れるまで帰らない
    """
    def setUp(self):
        self.acts = ep_in_forest(
                SilverForest(), MeetDay(), Yusha(), Panna(), RentalPony()
                )

    def test_intro_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_basic_info(self):
        self.assertTrue(checked_has_basic_info(
            self, self.acts, Yusha(), Panna(), "捜索依頼", "説得"
            ))


class EpisodeTest_truth(unittest.TestCase):
    """Test episode of truth.
     * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: パンナを見つけて以降
        - Where: 白銀の湖畔
        - What: パンナを連れて帰る
        - Why: 捜索依頼を受けた
        - How: 白銀の王子の謎を解く
        - Result: パンナは勇者とパーティを組んだ
    """
    def setUp(self):
        self.acts = ep_truth(
                SilverForest(), MeetDay(), Yusha(), Panna(), RentalPony()
                )

    def test_intro_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_basic_info(self):
        self.assertTrue(checked_has_basic_info(
            self, self.acts, Yusha(), Panna(), "依頼", "謎を解く"
            ))

