import unittest
from umls.client import UMLSClient

class TestUMLSClient(unittest.TestCase):

    def test_get_cui(self):
        client = UMLSClient(api_key="api_key")
        response = client.get_cui_list("aspirin")
        # To be added

if __name__ == '__main__':
    unittest.main()
