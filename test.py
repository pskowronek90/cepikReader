import unittest
import requests
from cepikRegions import regionCode
from cepikTransform import transformVehiclesData

class CepikTests(unittest.TestCase):
    def test_regionCode(self):
        self.assertEqual(regionCode("DOLNOŚLĄSKIE"), "02")

    
    def test_transformVehiclesData(self):
        goodCall = requests.get("https://api.cepik.gov.pl//pojazdy?wojewodztwo=30&data-od=20200101&data-do=20200331")
        self.assertEqual(goodCall.status_code, 200)

        badCall = requests.get("https://api.cepik.gov.pl//pojazdy?wojewodztwo=??&data-od=20200101&data-do=20200331")
        self.assertEqual(badCall.status_code, 400)



if __name__ == '__main__':
    unittest.main()