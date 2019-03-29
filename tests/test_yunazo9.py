# -*- coding: utf-8 -*-
"""Test for yunazo story 08.
"""
import unittest

from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from yunazo.story9.story import story, ep1, ep2, ep3
from yunazo.story9.story import charas, stages, items, words, daytimes


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: story yunazo 9 ****")

    def setUp(self):
        ma = Master('test yunazo9')
        yusha, panna, orga, young = charas("yusha"), charas("panna"), charas("orga"), charas("young")
        arial, ship = stages("arial"), stages("ship")
        wyusha = words("yusha")
        childhood, current = daytimes("childhood"), daytimes("current")
        self.story = story()
        self.ep1 = ep1(ma)
        self.ep2 = ep2(ma)
        self.ep3 = ep3(ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        data_set = [
                ("story", self.story, charas("yusha"), charas("panna")),
                ("ep1", self.ep1, charas("yusha"), charas("panna")),
                ("ep2", self.ep2, charas("young"), charas("orga")),
                ("ep3", self.ep3, charas("young"), charas("orga")),
                ]
        for title, body, hero, rival in data_set:
            with self.subTest(title=title, body=body, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, body, hero, rival))

    def test_has_outline_infos(self):
        yusha, panna, orga, young = charas("yusha"), charas("panna"), charas("orga"), charas("young")
        mam, children = charas("mam"), charas("children")
        ymark = items("mark")
        wyusha, yworry = words("yusha"), words("worry")
        childhood = daytimes("childhood")
        data_set = [
                ("story", self.story,
                    yusha.talk(about=wyusha),
                    panna.wonder(about=wyusha),
                    yusha.talk(about=childhood, to=panna),
                    yusha.teach(wyusha, to=panna),
                    ),
                ("ep1", self.ep1,
                    panna.know(of=yworry),
                    yusha.worry(info="何か"),
                    panna.ask(about=yworry, info="直接"),
                    yusha.talk(about=childhood, to=panna),
                    ),
                ("ep2", self.ep2,
                    yusha.be(info="誕生"),
                    mam.do(yusha, info="産んだ"),
                    mam.marry(orga),
                    yusha.hate(frm=children).ps(),
                    ),
                ("ep3", self.ep3,
                    yusha.become(wyusha),
                    yusha.hate(frm=children).ps().non(),
                    yusha.find(ymark),
                    yusha.have(ymark),
                    ),
                ]
        for title, body, what, why, how, result in data_set:
            with self.subTest(title=title, body=body, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, body, what, why, how, result))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

