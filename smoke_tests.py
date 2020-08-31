from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from assertions_search_tests import AssertionsSearchTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(AssertionsSearchTest)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)