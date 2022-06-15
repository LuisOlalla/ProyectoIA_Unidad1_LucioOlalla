import unittest


from LimpiaVidrios1 import LimpiaVidrios

class TestLimpiaVidrios(unittest.TestCase):
    
    
    def testLimpiaVidrios(self):
      
        
        self.assertTrue(LimpiaVidrios,{'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0', 'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '1'})
        
        self.assertNotEqual(LimpiaVidrios,{'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0', 'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '1', 'Ventana 7': '1'})
        
        


if __name__ == "__main__":
    unittest.main()
    
    




