import sys
import unittest
from test_pipeline import TestPipeline

def test_suite():
    """Run the unit tests."""
    suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    suite.addTest(test_loader.loadTestsFromTestCase(TestPipeline))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite())

    # Exit with non-zero code if any test failed
    if not result.wasSuccessful():
        sys.exit(1)
