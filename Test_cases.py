#Add the necessary files to file 
import unittest 
import searchAlgor

"""
- "result" is the outcome of importing from the searchAlgor file, then identifying the function
- putting the parameters of (which key to find, range or list to find key in)
- last line is putting the parameters of (index of which the key was in, the supposed answer of index of key)
"""

class Test_Linear_Search(unittest.TestCase):

    def test_small_range(self):
        result = searchAlgor.LinearSearchAlgor(2, range(1, 3)) 
        self.assertEqual(result, 1) 

    def test_large_range(self):
        result = searchAlgor.LinearSearchAlgor(88, range(23, 125))
        self.assertEqual(result,65)
    
    def test_key_not_found(self):
        result = searchAlgor.LinearSearchAlgor(67, range(78, 170))
        self.assertEqual(result, None)

class Test_Binary_Search(unittest.TestCase):

    def test_small_range(self):
        list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 20, low, high)
        self.assertEqual(result, 5)

    def test_large_range(self):
        list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 45, 67, 89, 94, 101, 120, 495, 283, 596, 294, 300, 319, 314, 3, 6, 8]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 596, low, high)
        self.assertEqual(result, 32)

    def test_no_key_found(self):  
        list = [45, 684, 283, 749, 8, 10, 293]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 1, low, high)
        self.assertEqual(result, None)

if __name__=='__main__':
    unittest.main()
