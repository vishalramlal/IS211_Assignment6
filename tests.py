#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assignment 6 Part 1

import sys
#sys.path.append("")
import unittest
import conversions

class Testconversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertEqual(conversions.convertCelsiusToKelvin(40), 313.15)
        print("Test passed! 40C is equal to 313.15K")
        self.assertAlmostEquals(conversions.convertCelsiusToKelvin(-50), 223.15)
        print("Test passed! -50C is equal to 223.15K")
        self.assertEqual(conversions.convertCelsiusToKelvin(0), 273.15)
        print("Test passed! 0C is equal to 273.15K")
        self.assertEqual(conversions.convertCelsiusToKelvin(1668), 1941.15)
        print("Test passed! 1668C is equal to 1941.15K")
        self.assertEqual(conversions.convertCelsiusToKelvin(37), 310.15)
        print("Test passed! 37C is equal to 310.15K")
        
    def test_convertCelsiusToFahrenheit(self):
        self.assertEqual(conversions.convertCelsiusToFahrenheit(0.0), 32.0)
        print("Test passed! 0C is equal to 32F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(-50), -58)
        print("Test passed! -50C is equal to -58F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(10), 50)
        print("Test passed! 10C is equal to 50F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(5), 41)
        print("Test passed! 5C is equal to 23F")
        self.assertEqual(conversions.convertCelsiusToFahrenheit(200), 392)
        print("Test passed! 200C is equal to 392F")
        
    def test_convertFahrenheitToCelsius(self):
        self.assertEqual(conversions.convertFahrenheitToCelsius(0), -17.78)
        print("Test passed! 0F is equal to -17.78C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(50), 10)
        print("Test passed! 50F is equal to 10C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(212), 100)
        print("Test passed! 212F is equal to 100C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(130), 54.44)
        print("Test passed! 130F is equal to 54.44C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(-40), -40)
        print("Test passed! -40F is equal to -40C")
        
    def test_convertFahrenheitToKelvin(self):
        self.assertEqual(conversions.convertFahrenheitToKelvin(110), 316.48)
        print("Test passed! 30F is equal to 272.04K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(-20), 244.26)
        print("Test passed! -20F is equal to 244.26K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(1000), 810.93)
        print("Test passed! 1000F is equal to 810.93K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(-459.67), 0)
        print("Test passed! -459.67F is equal to 0K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(100), 310.93)
        print("Test passed! 100F is equal to 310.93K")
        
    def test_convertKelvinToFahrenheit(self):
        self.assertEqual(conversions.convertKelvinToFahrenheit(200), -99.67)
        print("Test passed! 200K is equal to -99.67F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(50), -369.67)
        print("Test passed! 10K is equal to -441.67F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(1000), 1340.33)
        print("Test passed! 1000K is equal to 1340.33F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(500), 440.33)
        print("Test passed! 500K is equal to 440.33F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(260), 8.33)
        print("Test passed! 260K is equal to 8.33F")
        
    def test_convertKelvinToCelsius(self):
        self.assertEqual(conversions.convertKelvinToCelsius(150), -123.15)
        print("Test passed! 150K is equal to -123.15C")
        self.assertEqual(conversions.convertKelvinToCelsius(270), -3.15)
        print("Test passed! 270K is equal to -3.15C")
        self.assertEqual(conversions.convertKelvinToCelsius(400), 126.85)
        print("Test passed! 400K is equal to 126.85C")
        self.assertEqual(conversions.convertKelvinToCelsius(600), 326.85)
        print("Test passed! 600K is equal to 326.85C")
        self.assertEqual(conversions.convertKelvinToCelsius(90), -183.15)
        print("Test passed! 90K is equal to -183.15C")

        
if __name__ == "__main__":
    unittest.main()



# In[ ]:




