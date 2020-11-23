import count_vowels
import unittest

class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        string = "aeiou"
        only_unique_letters = set(string)
        result = count_vowels.get_vowels(string)
        self.assertEqual(result[0], 5)
        for vowel in only_unique_letters:
            self.assertEqual(result[1].get(vowel, None), 1)
    
    def test_buzz(self):
        string = "aaeeiioouu"
        only_unique_letters = set(string)
        result = count_vowels.get_vowels(string)
        self.assertEqual(result[0], 10)
        for vowel in only_unique_letters:
            self.assertEqual(result[1].get(vowel, None), 2)

    def test_fizzbuzz(self):
        string = "aaaeeeiiiooouuu"
        only_unique_letters = set(string)
        result = count_vowels.get_vowels(string)
        self.assertEqual(result[0], 15)
        for vowel in only_unique_letters:
            self.assertEqual(result[1].get(vowel, None), 3)
    
if __name__ == '__main__':
    unittest.main()