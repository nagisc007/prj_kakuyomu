# -*- coding: utf-8 -*-
"""Test for yunazo story 05
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story5.story import story
from yunazo.story5.story import intro
from yunazo.story5.story import strange_oldman
from yunazo.story5.story import real_criminal

from yunazo.story5.story import Yusha, Panna, Crades, Claire, PoliceChief
from yunazo.story5.story import Donston
from yunazo.story5.story import MagicBall
from yunazo.story5.story import Today


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
        print("\n**** story of yunazo5 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, Yusha(), Crades()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha().dispel("容疑"),
            Yusha().believe("やっていない"),
            Yusha().tell("真犯人を見つける"),
            Claire().confess("継ぎたくない")
            ))


class EpisodeTest(unittest.TestCase):
    """Test episodes.
    * outline of Intro
        - Who: 勇者
        - Whom: パンナ
        - When: 六月の午後
        - Where: 競馬で有名な町ドンストン
        - What: 事件解決を依頼された
        - Why: 突然店が消えたという謎に興味を持った
        - How: 実際に訪れる
        - Result: 容疑者クラデスに出会う
    * outline of Strange oldman
        - Who: 勇者
        - Whom: クラデス
        - When: 継続
        - Where: 継続
        - What: 消失の謎を解く
        - Why: クラデスが自分でやったと言っている
        - How: 関係者に事情聴取をする
        - Result: クラデスの魔法が元凶だった
    * outline of Real criminal
        - Who: 勇者
        - Whom: クラデス
        - When: 継続
        - Where: 消えた靴屋の前
        - What: 事件の犯人を見つける
        - Why: 真犯人の兇行を止めるため
        - How: 真犯人の行為を暴く
        - Result: クラデスがパーティに加わる
    """
    def setUp(self):
        self.ma = Master("test")
        self.intro = intro(self.ma, Yusha(), Panna(), Crades(), Donston(), Today())
        self.oldman = strange_oldman(self.ma, Yusha(), Panna(), Crades(), Claire(),
                PoliceChief(), Donston(), MagicBall(), Today())
        self.criminal = real_criminal(self.ma, Yusha(), Panna(), Crades(), Claire(),
                Donston(), Today())

    def test_intro_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.intro, Yusha(), Panna()))

    def test_intro_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.intro,
            Yusha().must("事件解決"),
            Yusha().feel("謎に興味"),
            Yusha().visit(Donston().name),
            Yusha().meet(Crades().name)))

    def test_oldman_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.oldman, Yusha(), Crades()))

    def test_oldman_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.oldman,
            Yusha().tell("謎を解く"),
            Crades().talk("自分でやった"),
            Yusha().hear("関係者"),
            Crades().talk("自分の魔法が原因")))

    def test_crimnal_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.criminal, Yusha(), Crades()))

    def test_criminal_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.criminal,
            Yusha().tell("犯人を見つける"),
            Yusha().explain("本当の殺人を起こさせない"),
            Yusha().talk("事件の真相"),
            Crades().talk("パーティに入る")))

