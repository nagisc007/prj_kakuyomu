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
        - Who:
        - Whom:
        - When:
        - Where:
        - Why:
        - How:
        - Resutl:
    """
    def setUp(self):
        self.ep = EpIntro()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))


class EpisodeTest_dancingmen(unittest.TestCase):
    """Test episode of intro.
    * outline
        - Who:
        - Whom:
        - When:
        - Where:
        - Why:
        - How:
        - Resutl:
    """
    def setUp(self):
        self.ep = EpDancingMen()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))


class EpisodeTest_papertruth(unittest.TestCase):
    """Test episode of intro.
    * outline
        - Who:
        - Whom:
        - When:
        - Where:
        - Why:
        - How:
        - Resutl:
    """
    def setUp(self):
        self.ep = EpPaperTruth()

    def test_is_structed_scenes(self):
        self.assertTrue(is_episode_structed_scenes(self, self.ep))


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
