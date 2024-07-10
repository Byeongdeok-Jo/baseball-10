from unittest import TestCase
from baseballgame import Baseball

class BaseballTest(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Baseball()
    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
