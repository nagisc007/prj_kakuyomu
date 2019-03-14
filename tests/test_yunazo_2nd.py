# -*- coding: utf-8 -*-
"""Test for yunazo story2.
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

from yunazo.common import Yusha, Panna, Crades, Emile, Badac, TH_Tanaka, DondahlChief, Brenda
from yunazo.common import BadacCave, DondahlTown, BadacSecretRoom
from yunazo.common import BadacMap, BadacPics, BadacCaveDoor, BadacShelf, BadacMemo
from yunazo.common import TreasureDay
from yunazo.story2.story import story
from yunazo.story2.story import ep_intro
from yunazo.story2.story import ep_incave
from yunazo.story2.story import ep_treasure


class StoryTest(unittest.TestCase):
    """Test story.
    """

    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo2 ****")

    def setUp(self):
        self.acts = story()

    def test_story_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "謎を解く", "地図"))

    def test_has_looks_of_yusha(self):
        self.assertTrue(_checked_has_the_looks_desc(self.acts, Yusha()))

    def test_has_looks_of_panna(self):
        self.assertTrue(_checked_has_the_looks_desc(self.acts, Panna()))

    def test_has_looks_of_emile(self):
        self.assertTrue(_checked_has_the_looks_desc(self.acts, Emile()))

    def test_has_looks_of_cave(self):
        self.assertTrue(_checked_has_the_looks_desc(self.acts, BadacCave()))


class EpisodeTest_intro(unittest.TestCase):
    """Test episode intro.
    * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 天才発明家の命日前日
        - Where: 天才の宝があるという洞窟
        - What: 洞窟に隠された遺品を見つける
        - Why: 依頼された
        - How: 地図の謎を解く
        - Result: 洞窟に閉じ込められた
    """
    def setUp(self):
        self.acts = ep_intro(BadacCave(), TreasureDay(),
                Yusha(), Panna(), Emile(), TH_Tanaka(), DondahlChief(),
                BadacMap(), BadacCaveDoor(),
                )

    def test_intro_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "頼", "地図")
                )

    def test_intro_result(self):
        for a in self.acts:
            if a.behavior is Behavior.RESULT and "洞窟に閉じ込" in a.action:
                break
        else:
            self.fail("Result is a mismatch!")


class EpisodeTest_incave(unittest.TestCase):
    """Test episode incave.
     * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 継続（閉じ込められた後）
        - Where: 洞窟内
        - What: 洞窟から出る
        - Why: 閉じ込められた
        - How: 地図の謎を解く
        - Result: 隠し部屋が現れた
    """
    def setUp(self):
        self.acts = ep_incave(BadacCave(), TreasureDay(),
                Yusha(), Panna(), Emile(),
                BadacMap(),
                )

    def test_incave_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_incave_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "閉じ込め", "地図の謎")
            )

    def test_incave_result(self):
        for a in self.acts:
            if a.behavior is Behavior.RESULT and "隠し部屋" in a.action and "現" in a.action:
                break
        else:
            self.fail("Result is a mismatch!")


class EpisodeTest_treasure(unittest.TestCase):
    """Test episode treasure.
     * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 継続（隠し部屋突入後）
        - Where: 隠し部屋
        - What: 遺品を探す
        - Why: 依頼を達成する
        - How: 部屋を探す
        - Result: 不器用な絵が遺品だった
    """
    def setUp(self):
        self.acts = ep_treasure(BadacCave(), TreasureDay(),
                Yusha(), Panna(), Emile(), Badac(), Brenda(),
                BadacMap(), BadacPics(), BadacShelf(), BadacMemo(),
                )

    def test_treasure_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_treasure_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "依頼", "探")
                )

    def test_treasure_result(self):
        for a in self.acts:
            if a.behavior is Behavior.RESULT and "不器用な絵" in a.action:
                break
        else:
            self.fail("Result is a mismatch!")


def _checked_has_the_looks_desc(acts, subject):
    for a in acts:
        if a.subject.name == subject.name and a.behavior is Behavior.LOOK:
            return True
    else:
        return False

