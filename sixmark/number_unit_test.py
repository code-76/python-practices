

import unittest
from testcase.test_extractor import TestNumberExtractor
from testcase.test_local_number_datasources import TestLocalNumberDataSources
from testcase.test_analytics import TestAnalytics
from testcase.test_remote_number_datasources import TestRemoteNumberDataSource

if __name__ == '__main__':
    """
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase('test_default_widget_size'))
        suite.addTest(WidgetTestCase('test_widget_resize'))
        return suite

        runner = unittest.TextTestRunner()
        runner.run(suite())
    """
    local_number_datasource_suite = unittest.TestLoader().loadTestsFromTestCase(TestLocalNumberDataSources)
    remote_number_datasource_suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoteNumberDataSource)
    analytics_suite = unittest.TestLoader().loadTestsFromTestCase(TestAnalytics)
    extractor_suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberExtractor)
    unittest.TextTestRunner(verbosity=2).run(local_number_datasource_suite)
    unittest.TextTestRunner(verbosity=2).run(remote_number_datasource_suite)
    unittest.TextTestRunner(verbosity=2).run(analytics_suite)
    unittest.TextTestRunner(verbosity=2).run(extractor_suite)