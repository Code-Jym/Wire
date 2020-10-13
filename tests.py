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
    
    def testReplace(self):
        """
        Tests Wire.replace()
        Tests with:
        - Wire.replace(old, new, count=1)
        - Wire.replace(old, new, count=2)
        - Wire.replace(old, new, count=None)
        """
        wire = Wire("Testing 1 2 3 Testing 1 2 3")
        wire = wire.replace("Testing", "Success", count=1)
        self.assertEqual(wire, "Success 1 2 3 Testing 1 2 3")

        wire = Wire("Testing 1 2 3 Testing 1 2 3 Testing")
        wire = wire.replace("Testing", "Success", count=2)
        self.assertEqual(wire, "Success 1 2 3 Success 1 2 3 Testing")

        wire = Wire("Testing Testing Testing 1 2 3 Testing")
        wire = wire.replace("Testing", "Success", count=None)
        self.assertEqual(wire, "Success Success Success 1 2 3 Success")
    
    def testFormat(self):
        """
        Tests Wire.format()
        """
        var = "Test"
        wire = Wire("This is a {}").format(var)
        self.assertEqual(wire, "This is a Test")
    
    def testSwap(self):
        """
        Tests Wire.swap()
        """
        wire = Wire("Test")
        wire = wire.swap(0, 3)
        self.assertEqual(wire, "tesT")
    
    def testForEach(self):
        """
        Tests Wire.forEach()
        """
        wire = Wire("test")
        print("\n")
        print("Testing Wire.forEach()")
        wire = wire.forEach(print)
        self.assertEqual(wire, [None, None, None, None])
    
    def testSort(self):
        """
        Tests Wire.sort
        """
        wire = Wire("bacd")
        wire = wire.sort()
        self.assertEqual(wire, "abcd")
    

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
    
    def testGetItem(self):
        wire = Wire("Test")
        self.assertEqual(wire[0], "T")
        self.assertEqual(wire["T"], 0)

    def testSetItem(self):
        wire = Wire("Test")
        wire["T"] = 3
        self.assertEqual(str(wire), "tesT")
        wire[0] = "J"
        self.assertEqual(str(wire), "JesT")
    
    def testLoop(self):
        wire = Wire("Test")
        print("\n")
        for i in wire:
            print(i)
        self.assertEqual(1, 1) # Pass
    

if __name__ == "__main__":
    main()