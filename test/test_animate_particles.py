import unittest

from animate_particles import animate


class TestAnimate(unittest.TestCase):
    def test_0(self):
        output = animate("..R....", 2)
        self.assertEqual(output, ["..X....", "....X..", "......X", "......."])

    def test_1(self):
        output = animate("RR..LRL", 3)
        self.assertEqual(output, ["XX..XXX", ".X.XX..", "X.....X", "......."])

    def test_2(self):
        output = animate("LRLR.LRLR", 2)
        self.assertEqual(
            output,
            [
                "XXXX.XXXX",
                "X..X.X..X",
                ".X.X.X.X.",
                ".X.....X.",
                ".........",
            ],
        )

    def test_3(self):
        output = animate("RLRLRLRLRL", 10)
        self.assertEqual(output, ["XXXXXXXXXX", ".........."])
