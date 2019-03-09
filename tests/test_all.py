# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import yunazo test
import test_yunazo_clock

def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    # add each tests
    suite.addTest(unittest.makeSuite(test_yunazo_clock.StoryTest))
    suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_intro))
    suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_mystery))
    suite.addTest(unittest.makeSuite(test_yunazo_clock.EpisodeTest_resolve))

    return suite
