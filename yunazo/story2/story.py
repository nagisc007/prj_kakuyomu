# -*- coding: utf-8 -*-
"""Story building as Yunazo-story2.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.acttypes import Behavior
from storybuilder.builder.base import Title 
from storybuilder.builder.tools import output, output_md

# import data
from common import Yusha, Panna, Crades, Emile, Badac, TH_Tanaka, DondahlChief, Brenda
from common import DondahlTown, BadacCave, BadacSecretRoom
from common import BadacMap, BadacPics, BadacCaveDoor, BadacShelf, BadacMemo
from common import TreasureDay


# episodes
def ep_intro(cave, tday, yusha, panna, emile, tanaka, chief, bmap, bdoor):
    '''Intro story.
    '''
    return (
            cave.look("ごく普通の洞窟内"),
            tday.look("外は午前だが、ここは薄暗い"),
            yusha.act("宝の地図の謎解き", Behavior.REQUEST),
            yusha.act("{}から{}".format(tanaka.name, bmap.name), Behavior.GET),
            chief.tell("命日までに遺品を見つけたい"),
            yusha.tell("{}に頼まれたんだ".format(chief.name)),
            yusha.think("依頼を達成したい"),
            yusha.must("宝を見つける"),
            yusha.want("地図の謎を解く"),
            yusha.tell("この地図に鍵がある"),
            yusha.look("右の前髪が少し立っている"),
            panna.look("金髪の小柄な少女"),
            panna.tell("{}に書いてあるんでしょ？".format(bmap.name)),
            emile.act("黙って二人のあとをついてくる", Behavior.MOVE),
            emile.look("濃いブロンドの長い髪"),
            emile.look("重そうな鎧と仮面で素顔が隠れている"),
            yusha.act("一番奥まで進む", Behavior.GO),
            cave.look("一番奥に扉が一つだけある"),
            yusha.act("裏側の扉を見つける", Behavior.FIND),
            bdoor.look("小さな扉が裏側にある"),
            panna.act("{}を開ける".format(bdoor.name)),
            yusha.tell("{}を注意".format(panna.name)),
            cave.look("表の方で音がする"),
            yusha.act("頭を抱える"),
            emile.act("姿が見えない", Behavior.VANISH),
            emile.act("表の入り口", Behavior.CHECK),
            emile.act("戻ってきた", Behavior.RETURN),
            emile.tell("入り口が閉じられていた"),
            yusha.act("入り口を確認", Behavior.CHECK),
            yusha.tell("閉じ込められたな"),
            yusha.result("洞窟に閉じ込められる"),
            )


def ep_incave(cave, tday, yusha, panna, emile, bmap):
    '''In cave story.
    '''
    return (
            cave.look("他には出入り口がない"),
            tday.look("大した時間が経っていない"),
            yusha.tell("結局他に入り口はなかった"),
            yusha.think("閉じ込められたようだ"),
            panna.act("壁を叩いて回る"),
            panna.tell("お腹すいた"),
            emile.tell("乾パンなら持っているぞ"),
            panna.act("乾パンを食べる"),
            yusha.must("出入り口を探す"),
            panna.tell("適当に壁壊せば"),
            yusha.tell("無理だな"),
            panna.act("壁を叩く"),
            cave.look("固く、何か魔法コーティングしてある様子"),
            yusha.tell("この地図の謎を解くしかないな"),
            yusha.act("地図を見る", Behavior.CHECK),
            bmap.look("二番目の扉は開けてはならない、と書かれている"),
            yusha.act("一番目の扉の奥を調べる", Behavior.SEARCH),
            yusha.tell("{}にここを破戒しろと".format(panna.name)),
            panna.tell("文句"),
            panna.act("壁を殴る"),
            cave.look("壁が動いた"),
            yusha.tell("それがスライド式ドアなんだ"),
            yusha.result("隠し部屋が現れた"),
            )


def ep_treasure(secroom, tday, yusha, panna, emile, badac, brenda, bmap, bpics, shelf, memo):
    '''His treasure.
    '''
    return (
            secroom.look("そこは隠し部屋"),
            tday.look("まだ昼にはなっていない"),
            bpics.look("絵が沢山散らばっている"),
            secroom.look("絵以外には特に何もない"),
            yusha.must("この中から遺品を探す"),
            yusha.think("この中に依頼された遺品がある"),
            panna.tell("この絵へたっぴ"),
            yusha.tell("探すぞ"),
            secroom.look("絵しかない"),
            emile.tell("この女性"),
            bpics.look("どれも女性の肖像画"),
            yusha.tell("{}に{}の妻のことを尋ねる".format(emile.name, badac.name)),
            emile.tell("{}の妻には似ていない".format(badac.name)),
            emile.tell("美人で有名だった"),
            emile.tell("ただ{}の家に使用人がいて、その女に似ている気がする".format(badac.name)),
            yusha.tell("地図の文言を復唱する"),
            bmap.look("二番目は開いてはならない"),
            yusha.think("二番目について"),
            panna.act("{}の二番目を開ける".format(shelf.name), Behavior.OPEN),
            shelf.look("二番目に当てた手紙がある"),
            memo.look("{}を二番目といつも呼んでいたことの謝罪が書いてある".format(brenda.name)),
            yusha.think("二番目が本当は一番だった"),
            emile.tell("二番目が一番だったんじゃ、と言おうとする"),
            yusha.tell("{}に黙っておくようにと".format(emile.name)),
            panna.think("？"),
            yusha.result("不器用な絵が遺品だった"),
            )


# main story
def story():
    '''Story builded.
    '''
    # characters
    yusha = Yusha()
    panna = Panna()
    emile = Emile()
    tanaka = TH_Tanaka()
    chief = DondahlChief()
    badac = Badac()
    brenda = Brenda()
    # stages
    cave = BadacCave()
    secroom = BadacSecretRoom()
    # items
    bmap = BadacMap()
    bpics = BadacPics()
    bdoor = BadacCaveDoor()
    shelf = BadacShelf()
    memo = BadacMemo()
    # daytimes
    tday = TreasureDay()

    return ep_intro(cave, tday, yusha, panna, emile, tanaka, chief, bmap, bdoor)\
            + ep_incave(cave, tday, yusha, panna, emile, bmap)\
            + ep_treasure(secroom, tday, yusha, panna, emile, badac, brenda, bmap, bpics, shelf, memo)


def main(is_debug=True):
    '''main method.
    '''
    STORY_FILE = 'yunazo2'

    mystory = story()

    # output to the console
    output(mystory, is_debug=is_debug)

    # output to a markdown
    output_md(mystory, STORY_FILE, is_debug=is_debug)

    return True


if __name__ == '__main__':
    import sys
    sys.exit(main())
