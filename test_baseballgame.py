from unittest import TestCase
from baseballgame import Baseball

class BaseballTest(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Baseball()
    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_exception_when_input_length_is_unmatched(self):
        with self.assertRaises(TypeError):
            self.game.guess("12")
