# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import yunazo test
import test_yunazo_clock
import test_yunazo_2nd
import test_yunazo_forest

def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

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
    suite.addTest(unittest.makeSuite(test_yunazo_forest.StoryTest))
    suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_intro))
    suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_in_forest))
    suite.addTest(unittest.makeSuite(test_yunazo_forest.EpisodeTest_truth))

    return suite
