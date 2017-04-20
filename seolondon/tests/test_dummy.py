# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
    The test in this file will serve no purpose but
    test the testing pipeline works

"""

import unittest


class TestDummy(unittest.TestCase):

    def test_dummy(self):
        # One equals one, test passed!
        self.assertEqual(1, 1)
