# -*- coding: utf-8 -*-
"""Test for yunazo story 08.
"""
import unittest

from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story8.story import story
from yunazo.story8.story import ep_intro, ep_maou, ep_festa
from yunazo.story8.story import Yusha, Panna, Crades, Emile
from yunazo.story8.story import boy_ordy, mam_ordy, dad_ordy, vila_people, vila_child, vila_sailor
from yunazo.story8.story import zibonga_vila, ordy_home
from yunazo.story8.story import devils_fes, real_tale, broken_sword, yusha_mark
from yunazo.story8.story import past_day, before_day, fes_day

class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: story yunazo 8 ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, Yusha(), Panna()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Yusha().hear(devils_fes()),
            Yusha().want(devils_fes(), info="知る"),
            Yusha().investigate(zibonga_vila()),
            Yusha().know(zibonga_vila(), info="魔王が救った"),
            ))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodesTest(unittest.TestCase):

    def setUp(self):
        ma = Master('test yunazo8')
        self.ep1 = ep_intro(ma, Yusha(), Panna(), Crades(), Emile(), boy_ordy(),
                vila_child(), vila_sailor(),
                devils_fes(), zibonga_vila(), before_day())
        self.ep2 = ep_maou(ma, Yusha(), Panna(), Crades(), Emile(), boy_ordy(),
                mam_ordy(), dad_ordy(), vila_sailor(),
                devils_fes(), real_tale(), broken_sword(), yusha_mark(),
                zibonga_vila(), ordy_home(), before_day(), past_day())
        self.ep3 = ep_festa(ma, Yusha(), Panna(), Crades(), Emile(), boy_ordy(),
                vila_people(), mam_ordy(),
                devils_fes(), real_tale(), broken_sword(), yusha_mark(),
                zibonga_vila(), fes_day(), past_day())

    def test_episodes_has_basic_infos(self):
        data_set = [
                ("ep1", self.ep1, Yusha(), boy_ordy()),
                ("ep2", self.ep2, Yusha(), boy_ordy()),
                ("ep3", self.ep3, Yusha(), boy_ordy()),
                ]
        for title, ep, hero, rival in data_set:
            with self.subTest(title=title, ep=ep, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, ep, hero, rival))

    def test_episodes_has_outline_infos(self):
        data_set = [
                ("ep1", self.ep1,
                    Yusha().investigate(devils_fes()),
                    Yusha().hear(devils_fes()),
                    Yusha().visit(zibonga_vila()),
                    Yusha().meet(boy_ordy()),
                    ),
                ("ep2", self.ep2,
                    Yusha().hear(boy_ordy(), info="祭り"),
                    boy_ordy().know(devils_fes()),
                    Yusha().teach(boy_ordy(),info= "勇者"),
                    boy_ordy().teach(past_day()),
                    ),
                ("ep3", self.ep3,
                    boy_ordy().rescue(Yusha()),
                    Yusha().catch(vila_people()).ps(),
                    boy_ordy().talk(real_tale()),
                    Yusha().rescue(boy_ordy()).ps(),
                    ),
                ]
        for title, ep, what, why, how, result in data_set:
            with self.subTest(title=title, ep=ep, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, ep,
                    what, why, how, result))
