import unittest

def fonction(string,ending):
    return string.endswith(ending)  

class Exo2Test(unittest.TestCase):

    def test_true_cases(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for string, ending in fixed_tests_True:
            self.assertEqual(fonction(string, ending),True)
    
    
    def test_false_cases(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for string, ending in fixed_tests_False:
            self.assertEqual(fonction(string, ending),False)


if __name__ == '__main__':
    unittest.main()
    