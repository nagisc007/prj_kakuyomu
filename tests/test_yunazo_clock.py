# -*- coding: utf-8 -*-
"""Test for story of yu-nazo1
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

from yunazo.common import Yusha, Panna, InnOwner
from yunazo.common import ClocVila, Inn
from yunazo.common import OwlClock
from yunazo.common import OneDay
from yunazo.story1 import story
from yunazo.story1 import ep_intro
from yunazo.story1 import ep_mystery
from yunazo.story1 import ep_resolve


class StoryTest(unittest.TestCase):
    """Test story.

    * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 遅い朝
        - Where: クロク村唯一宿
        - What: フクロウ時計が鳴かくなった謎を解く
        - Why: 家賃を安くするため（店主の依頼）
        - How: 丸一日フクロウ時計と過ごす
        - Result: フクロウ時計ではなく壊れた不細工な鳩時計だった
    """

    def setUp(self):
        self.acts = story()

    def test_story_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_has_basic_infos(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "家賃", "丸一日")
                )

    def test_story_in_the_time(self):
        for a in self.acts:
            if isinstance(a.subject, DayTime) and "すっかり日が昇って" in a.action:
                break
        else:
            raise AssertionError("DayTime was a mismatch!")

    def test_story_in_the_place(self):
        for a in self.acts:
            if isinstance(a.subject, Stage) and "唯一の宿" in a.action:
                break
        else:
            raise AssertionError("Stage was a mismatch!")

    def test_story_outline_reason(self):
        for a in self.acts:
            if "家賃" in a.action:
                break
        else:
            raise AssertionError("Reason was a mismatch!")

    def test_story_outline_process(self):
        for a in self.acts:
            if "丸一日" in a.action: break
        else:
            raise AssertionError("Process was a mismatch!")

    def test_story_outline_result(self):
        for a in self.acts:
            if "鳩時計" in a.action:
                break
        else:
            raise AssertionError("Result was a mismatch!")


class EpisodeTest_intro(unittest.TestCase):
    """Test episode of intro.

    * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 昼前
        - Where: 宿の個室（一人部屋に二人）
        - What: フクロウ時計が鳴かなくなった謎を解く
        - Why: 家賃を半額にする為
        - How: 一日観察する
        - Result: フクロウ時計は鳴かなかった
    * Advanced
        - 勇者とは何か？
        - 勇者の外見描写
        - パンナの外見描写
        - パーティの簡易紹介
        - 宿の部屋の描写
        - 季節の描写
        - 村の簡易説明
        - クロク村は時計職人の村である
    """

    def setUp(self):
        self.acts = ep_intro(
                Inn(), ClocVila(), OneDay(), Yusha(), Panna(), OwlClock(),
                )

    def test_intro_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_has_basic_infos(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "家賃", "半額")
                )

    def test_intro_outline_reason(self):
        for a in self.acts:
            if "家賃" in a.action and "半額" in a.action: break
        else:
            raise AssertionError("Reason was a mismatch!")

    def test_intro_outline_process(self):
        for a in self.acts:
            if "一日" in a.action and "見張" in a.action: break
        else:
            raise AssertionError("Process was a mismatch!")

    def test_intro_outline_result(self):
        for a in self.acts:
            if "鳴かなかった" in a.action: break
        else:
            raise AssertionError("Result was a mismatch!")

    def test_intro_has_yusha_desc(self):
        for a in self.acts:
            if isinstance(a.subject, Yusha) and a.act_type is ActType.DESC: break
        else:
            raise AssertionError("Yusha's description not exists!")

    def test_intro_has_panna_desc(self):
        for a in self.acts:
            if isinstance(a.subject, Panna) and a.act_type is ActType.DESC: break
        else:
            raise AssertionError("Panna's description not exists!")

    def test_intro_has_stage_descs(self):
        pass

    def test_intro_has_daytime_descs(self):
        pass

class EpisodeTest_mystery(unittest.TestCase):
    """Test episode of mystery

    * Outline
        - Who: 勇者
        - Whom: パンナ
        - When: 継続
        - Where: 継続
        - What: フクロウ時計が鳴かなくなった理由を解明する
        - Why: 家賃を半額にしたい（金があまりない）
        - How: 店主に事情聴取する
        - Result: 別の部屋のフクロウ時計が鳴いた
    """

    def setUp(self):
        self.acts = ep_mystery(
                Inn(), OneDay(), Yusha(), Panna(), InnOwner(), OwlClock(),
                )

    def test_mystery_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_mystery_has_basic_infos(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "家賃", "謎")
                )

    def test_mystery_outline_reason(self):
        for a in self.acts:
            if "家賃" in a.action and "半額" in a.action: break
        else:
            raise AssertionError("Reason was a mismatch!")

    def test_mystery_outline_process(self):
        for a in self.acts:
            if isinstance(a.subject, InnOwner): break
        else:
            raise AssertionError("Process was a mismatch (owner not exists)!")
        for a in self.acts:
            if isinstance(a.subject, Yusha) and "聞かせて" in a.action: break 
        else:
            raise AssertionError("Process was a mismatch!")

    def test_mystery_outline_result(self):
        for a in self.acts:
            if isinstance(a.subject, OwlClock) and "別の部屋" in a.action: break
        else:
            raise AssertionError("Result was a mismatch!")

class EpisodeTest_resolve(unittest.TestCase):
    """Test episode of resolve

    * Outline
        - Who: 勇者
        - Whom: 店主
        - When: 昼前から昼
        - Where: 宿の中、村
        - What: 店主にフクロウ時計が鳴かない理由を説明する
        - Why: 謎が解けたので
        - How: フクロウ時計を分解して見せる
        - Result: 村で一斉に鳩時計が鳴いた
    """

    def setUp(self):
        self.acts = ep_resolve(
                Inn(), OneDay(), Yusha(), Panna(), InnOwner(), OwlClock(),
                )

    def test_resolve_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_resolve_has_basic_infos(self):
        self.assertTrue(
                checked_has_basic_info(self,
                    self.acts, Yusha(), Panna(),
                    "解", "分解")
                )

    def test_resolve_outline_reason(self):
        for a in self.acts:
            if "謎" in a.action and "解" in a.action: break
        else:
            raise AssertionError("Reason was a mismatch!")

    def test_resolve_outline_process(self):
        for a in self.acts:
            if "分解" in a.action: break
        else:
            raise AssertionError("Process was a mismatch!")

    def tset_resolve_outline_result(self):
        for a in self.acts:
            if "一斉" in a.action and "鳴" in a.action: break
        else:
            raise AssertionError("Result was a mismatch!")

