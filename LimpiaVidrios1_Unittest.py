import unittest
from LimpiaVidrios1 import LimpiaVidrios

class TestLimpiaVidrios(unittest.TestCase):
    def test_limpia_vidrios(self):
        self.assertEqual(LimpiaVidrios(),True)

if __name__ == '__main__':
    unittest.main()