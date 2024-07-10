from unittest import TestCase
from baseballgame import Baseball

class BaseballTest(TestCase):
    def test_exception_when_input_is_none(self):
        self.game = Baseball()
        with self.assertRaises(TypeError):
            self.game.guess(None)
