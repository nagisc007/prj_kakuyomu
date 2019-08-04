# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import yunazo test
#import test_yunazo_clock
#import test_yunazo_2nd
#import test_yunazo_forest
#import test_yunazo_dance
#import test_yunazo5
#import test_yunazo6
#import test_yunazo7
#import test_yunazo8
#import test_yunazo9
import test_loli


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        # sneaker contests
        unittest.makeSuite(test_loli.StoryTest),
        ))
    # story1
    #suite.addTest(unittest.makeSuite(test_yunazo_clock.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_intro))
    #suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_mystery))
    #suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_resolve))

    # story2
    #suite.addTest(unittest.makeSuite(test_yunazo_2nd.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo_2nd.EpisodeTest_intro))
    #suite.addTest(unittest.makeSuite(test_yunazo_2nd.EpisodeTest_incave))
    #suite.addTest(unittest.makeSuite(test_yunazo_2nd.EpisodeTest_treasure))

    # story3
    #suite.addTest(unittest.makeSuite(test_yunazo_forest.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_intro))
    #suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_in_forest))
    #suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_truth))

    # story4
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.EpisodeTest_intro))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.EpisodeTest_dancingmen))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.EpisodeTest_papertruth))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_dancinggirl))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_dancingmen))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_frontlib))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_in_lib))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_oldbooks))
    #suite.addTest(unittest.makeSuite(test_yunazo_dance.SceneTest_paperexpensive))

    # story5
    #suite.addTest(unittest.makeSuite(test_yunazo5.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo5.EpisodeTest))

    # story6
    #suite.addTest(unittest.makeSuite(test_yunazo6.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo6.EpisodeTest))

    # story7
    #suite.addTest(unittest.makeSuite(test_yunazo7.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo7.EpisodeTest))

    # story 8
    #suite.addTest(unittest.makeSuite(test_yunazo8.StoryTest))
    #suite.addTest(unittest.makeSuite(test_yunazo8.EpisodesTest))

    # story 9
    #suite.addTest(unittest.makeSuite(test_yunazo9.StoryTest))

    return suite
