"""Run the test suite."""

import sys
import unittest

tests = ['process.math']

suite = unittest.TestSuite()

for test in tests:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

res = unittest.TextTestRunner().run(suite).wasSuccessful()
rc = (0 if res else 1)
sys.exit(rc)
