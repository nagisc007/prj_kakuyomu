# -*- coding: utf-8 -*-
"""Test for yunazo story4.
"""
import unittest

from storybuilder.builder.acttypes import ActType, Behavior
from storybuilder.builder.base import Stage, DayTime
from storybuilder.builder.testtools import is_episode_structed_scenes
from storybuilder.builder.testtools import is_scene_structed_acts
from storybuilder.builder.testtools import is_story_structed_episodes
from storybuilder.builder.testtools import has_scene_basic_infos
from storybuilder.builder.testtools import has_episode_outline_infos

from yunazo.common import Yusha, Panna, Crades, Emile
from yunazo.common import OldLibrary
from yunazo.common import DancingBook
from yunazo.common import ResearchDay

from yunazo.story4.story import StoryYunazo4
from yunazo.story4.story import EpIntro
from yunazo.story4.story import EpDancingMen
from yunazo.story4.story import EpPaperTruth
from yunazo.story4.story import ScDancingGirl
from yunazo.story4.story import ScDancingMen
from yunazo.story4.story import ScFrontLibrary
from yunazo.story4.story import ScInLibrary
from yunazo.story4.story import ScOldBooks
from yunazo.story4.story import ScPaperExpensive


class StoryTest(unittest.TestCase):
    """Test story.
    * outline
        - Who:
        - Whom:
        - When:
        - Where:
        - Why:
        - How:
        - Resutl:
    """
    @classmethod
    def setUpClass(cls):
        print("**** story of yunazo4 ****")

    def setUp(self):
        self.story = StoryYunazo4()

    def test_is_structed_episodes(self):
        self.assertTrue(is_story_structed_episodes(self, self.story))


class EpisodeTest_intro(unittest.TestCase):
    """Test episode of intro.
    * outline
        - Who: 勇者
        - Whom: パンナ
        - When: 秋
        - Where: 遺跡
        - What: 遺跡調査を行う
        - Why: 遺跡調査を依頼された
        - How: 実際に入ってみる
        - Resutl: 中には本があった
    """
    def setUp(self):
        self.ep = EpIntro()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))

    def test_has_basic_infos(self):
        self.assertTrue(
            has_episode_outline_infos(self, self.ep,
                "遺跡", "依頼", "入る", "本があった"))


class EpisodeTest_dancingmen(unittest.TestCase):
    """Test episode of intro.
    * outline
        - Who: 勇者
        - Whom: パンナ
        - When: 遺跡に入った後
        - Where: 遺跡内部
        - What: 本を調べる
        - Why: 本が怪しい
        - How: 実際に手に取る
        - Resutl: 踊る人形文字が描かれていた
    """
    def setUp(self):
        self.ep = EpDancingMen()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))

    def test_has_basic_infos(self):
        self.assertTrue(
            has_episode_outline_infos(self, self.ep,
                "調査", "本", "手に取る", "踊る人形"))


class EpisodeTest_papertruth(unittest.TestCase):
    """Test episode of intro.
    * outline
        - Who: 勇者
        - Whom: パンナ
        - When: 本を調べてから少し経った
        - Where: 遺跡内部
        - What: 遺跡の謎を解く
        - Why: 本の謎に気づいた
        - How: パンナを踊らせる
        - Resutl: 踊りを記録しようとした男の苦闘の後だった
    """
    def setUp(self):
        self.ep = EpPaperTruth()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))

    def test_has_basic_infos(self):
        self.assertTrue(
            has_episode_outline_infos(self, self.ep,
                "謎", "気づく", "踊らせる", "記録"))


class SceneTest_dancinggirl(unittest.TestCase):

    def setUp(self):
        self.sc = ScDancingGirl()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))


class SceneTest_dancingmen(unittest.TestCase):

    def setUp(self):
        self.sc = ScDancingMen()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))


class SceneTest_frontlib(unittest.TestCase):

    def setUp(self):
        self.sc = ScFrontLibrary()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))


class SceneTest_in_lib(unittest.TestCase):

    def setUp(self):
        self.sc = ScInLibrary()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))


class SceneTest_oldbooks(unittest.TestCase):

    def setUp(self):
        self.sc = ScOldBooks()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))


class SceneTest_paperexpensive(unittest.TestCase):

    def setUp(self):
        self.sc = ScPaperExpensive()

    def test_is_structed_actions(self):
        self.assertTrue(is_scene_structed_acts(self, self.sc))
