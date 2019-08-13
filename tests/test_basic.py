from context import meta
import unittest


class BasicTest(unittest.TestCase):

    def test_ismeta(self):
        assert meta.ismeta([
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"]) is True, "Metahuman"
        assert meta.ismeta([
            "ATGCGA",
            "CCGTGC",
            "TTATCT",
            "AGAACG",
            "CGCCTA",
            "TCACTG"]) is False, "Human"


if __name__ == '__main__':
    unittest.main()
