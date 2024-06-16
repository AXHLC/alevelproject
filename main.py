# testing
from myvalidator import TheValidation
import unittest

# -------------------MyValidator-------------------
# running myvalidator.py from main.py
validator = TheValidation()
x = validator.lengthscheck("daddy", 3, 3)
print(x)
# -------------------------------------------------

# -------------------Unittests-------------------
# running unittests.py from main.py
# Load all tests from unittests.py
test_suite = unittest.TestLoader().loadTestsFromName('unittests')
# Run the tests
unittest.TextTestRunner().run(test_suite)
# -------------------------------------------------
