import myvalidator

def test_lengthscheck():
    # Test case 1: Check if the length of the string is equal to nums
    result = myvalidator.lengthscheck("hello", 5, 1)
    if result != True:
        print("Test case 1 failed: expected True, got", result)

    # Test case 2: Check if the length of the string is greater than or equal to nums
    result = myvalidator.lengthscheck("hello", 4, 2)
    if result != True:
        print("Test case 2 failed: expected True, got", result)

    # Test case 3: Check if the length of the string is less than or equal to nums
    result = myvalidator.lengthscheck("hello", 6, 3)
    if result != True:
        print("Test case 3 failed: expected True, got", result)

# Run the tests
test_lengthscheck()