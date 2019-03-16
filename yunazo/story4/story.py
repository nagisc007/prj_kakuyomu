# -*- coding: utf-8 -*-
"""Story building as Yunazo-story4.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('common')

from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Story, Episode, Scene
from storybuilder.builder.tools import story_builded

from common import Yusha, Panna, Crades, Emile
from common import OldLibrary
from common import DancingBook
from common import ResearchDay


class ScFrontLibrary(Scene):
    def __init__(self):
        super().__init__("図書館前")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                day.look("秋のこと"),
                lib.look("古い遺跡の入り口"),
                yusha.think("調査依頼"),
                panna.tell("かび臭そう"),
                )

class ScInLibrary(Scene):
    def __init__(self):
        super().__init__("図書館内にて")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                lib.look("内部は全て煉瓦造り"),
                day.look("今日中にやりたい"),
                yusha.think("意外と頑丈そうだ"),
                panna.go("どんどん奥に進む"),
                )

class ScOldBooks(Scene):
    def __init__(self):
        super().__init__("紙の本たち")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                lib.look("本を収める棚はかびている"),
                day.look("{}が暇そうにしている".format(panna.name)),
                yusha.acquire("古い本"),
                panna.ask("これ何の本"),
                )

class ScDancingMen(Scene):
    def __init__(self):
        super().__init__("踊る人形たち")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                lib.look("壁は崩れそう"),
                day.look(""),
                )

class ScPaperExpensive(Scene):
    def __init__(self):
        super().__init__("紙は高価だった")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                lib.look("壁が濡れている"),
                day.look("随分と時間が経った"),
                )

class ScDancingGirl(Scene):
    def __init__(self):
        super().__init__("踊る少女")
        lib = OldLibrary()
        day = ResearchDay()
        yusha = Yusha()
        panna = Panna()
        crades = Crades()
        emile = Emile()
        self.commit(
                lib.look("ひっそりと佇む"),
                day.look("外は夕暮れていた"),
                yusha.go("外に向かう"),
                panna.go("{}を追いかける".format(yusha.name)),
                )


class EpIntro(Episode):
    def __init__(self):
        super().__init__("古代図書館")
        self.commit(
                ScFrontLibrary(),
                ScInLibrary())


class EpDancingMen(Episode):
    def __init__(self):
        super().__init__("踊る人形")
        self.commit(
                ScOldBooks(),
                ScDancingMen())


class EpPaperTruth(Episode):
    def __init__(self):
        super().__init__("紙の真実")
        self.commit(
                ScPaperExpensive(),
                ScDancingGirl())


class StoryYunazo4(Story):
    def __init__(self):
        TITLE = "勇者は冒険より紙とペンと踊る人形の謎解きをしたい"
        super().__init__(TITLE)
        self.commit(
                EpIntro(),
                EpDancingMen(),
                EpPaperTruth()
                )


def main(is_debug=True):
    '''main function.
    '''
    FILE_NAME = 'yunazo4'
    TITLE = "勇者は冒険より紙とペンと踊る人形の謎解きをしたい"
    
    story = StoryYunazo4()

    story_builded(TITLE, story, FILE_NAME, is_debug=is_debug)

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())

