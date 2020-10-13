"""
This is where I test all the functions for Wire to make
sure they work exactly as they were supposed to
"""

from wire import Wire
from unittest import TestCase, main

class TestExtraWireFunctions(TestCase):
    def testGetDiff(self):

        """
        Tests Wire.getDiff() 
        """

        wire = Wire("Test")
        wire = wire.getDiff("TESTING")
        self.assertEqual(wire, 7)
    
    def testRemoveDuplicate(self):

        """
        Tests Wire.removeDuplicate() 
        Tests with:
        - inOrder=True, caseSensitive=True
        - inOrder=False, caseSensitive=True
        - inOrder=True, caseSensitive=False
        - inOrder=False, caseSensitive=False
        """

        wire = Wire("Tester")
        wire = wire.removeDuplicate(inOrder=True)
        self.assertEqual(wire, "Testr")

        wire = Wire("Tester")
        wire = wire.removeDuplicate(inOrder=False)
        singles = ""
        for letter in list(wire):
            # This is a tricky bit of code here (don't let it confuse you)
            # What it does is it asserts that the letter is not in singles
            # which is defined before the for loop, if things go well
            # and an AssertionError is not made, then that letter is then added to singles
            # If there is a duplicate letter, then AssertionError would be made.
            self.assertNotIn(letter, singles)
            singles += letter
        
        wire = Wire("Tester")
        wire = wire.removeDuplicate(caseSensitive=False)
        singles = ""
        for letter in list(wire):
            # Same as above
            self.assertNotIn(letter.lower(), singles)
            singles += letter
        
        wire = Wire("Tester")
        wire = wire.removeDuplicate(inOrder=False, caseSensitive=False)

class TestWireDunderFunctions(TestCase):

    def testMul(self):
        wire = Wire("Test")
        self.assertEqual((wire * 2), ("TestTest"))
    
    def testAdd(self):
        wire = Wire("Test")
        self.assertEqual((wire + "ing"), "Testing")

    def testDiv(self):
        wire = Wire("TesthiTesthi")
        self.assertEqual((wire / "hi"), "TestTest")
    
    def testSub(self):
        wire = Wire("hiTesthiTest")
        self.assertEqual((wire - "hi"), "TesthiTest")

    def testLen(self):
        wire = Wire("Test")
        self.assertEqual(len(wire), 4)
    

if __name__ == "__main__":
    main()