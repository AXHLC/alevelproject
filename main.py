# testing
from myvalidator import TheValidation
import unittest

# -------------------Unittests-------------------
# running unittests.py from main.py
# Load all tests from unittests.py
test_suite = unittest.TestLoader().loadTestsFromName('unittests')
# Run the tests
unittest.TextTestRunner().run(test_suite)
# -------------------------------------------------
