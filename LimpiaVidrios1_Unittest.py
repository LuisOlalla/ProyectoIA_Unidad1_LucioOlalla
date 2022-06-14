import unittest
from LimpiaVidrios1 import LimpiaVidriosP

class TestLimpiaVidrios(unittest.TestCase):
    def test_LimpiaVidriosP(self):
        self.assertFalse(LimpiaVidriosP(), LimpiaVidriosP)

if __name__ == '__main__':
    unittest.main()