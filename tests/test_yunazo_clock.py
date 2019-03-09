# -*- coding: utf-8 -*-
"""Test for story of yu-nazo1
"""
import unittest

from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime

from yunazo_clock.story import Yusha, Panna, Crades, Emile, InnOwner
from yunazo_clock.story import ClocVila, Inn
from yunazo_clock.story import OwlClock
from yunazo_clock.story import OneDay
from yunazo_clock.story import story
from yunazo_clock.story import ep_intro
from yunazo_clock.story import ep_mystery
from yunazo_clock.story import ep_resolve

from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info


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
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))

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

    def test_story_in_the_reason(self):
        for a in self.acts:
            if "家賃" in a.action:
                break
        else:
            raise AssertionError("Reason was a mismatch!")

    def test_story_has_howto(self):
        for a in self.acts:
            if "丸一日" in a.action: break
        else:
            raise AssertionError("Howto was a mismatch!")

    def test_story_has_the_result(self):
        for a in self.acts:
            if "鳩時計" in a.action:
                break
        else:
            raise AssertionError("Result was a mismatch!")


class EpisodeTest_intro(unittest.TestCase):
    """Test episode of intro.

    * フクロウ時計
        - 主人公（勇者）はいるか
        - パンナはいるか
        - 同じ部屋に二人きりか
        - フクロウ時計はあるか
        - フクロウ時計は鳴っていないか
        - 二人は遅刻しているか
    """

    def setUp(self):
        self.acts = ep_intro(
                Inn(), ClocVila(), OneDay(), Yusha(), Panna(), OwlClock(),
                )

    def test_intro_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_intro_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))

    def test_intro_has_chara_descs(self):
        '''人物描写
        '''
        pass

    def test_intro_has_stage_descs(self):
        '''場面描写
        '''
        pass

    def test_intro_has_daytime_descs(self):
        '''時節描写
        '''
        pass

class EpisodeTest_mystery(unittest.TestCase):
    """Test episode of mystery

    * フクロウ時計の謎
        - なぜ他の二人は起こしにこないのか
    """

    def setUp(self):
        self.acts = ep_mystery(
                Inn(), OneDay(), Yusha(), Panna(),
                )

    def test_mystery_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_mystery_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))


class EpisodeTest_resolve(unittest.TestCase):
    """Test episode of resolve

    * フクロウ時計はなかった
        - フクロウ時計の正体への言及
        - 二人が起こしにこないことの説明
    """

    def setUp(self):
        self.acts = ep_resolve(
                Inn(), OneDay(), Yusha(), Panna(), InnOwner(), OwlClock(),
                )

    def test_resolve_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_resolve_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Yusha(), Panna()))

