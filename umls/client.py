import requests 
from .utils import *

class UMLSClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_cui_list(self, string):
        """ 
        Returns an orderded list of most relevent CUI that correspond to the code or term passed. 
        :param string: Any term or code in the UMLS. 
        :return: Formatted list of cui. 
        """

        try:
            if not self.api_key:
                raise Exception('Client is not authenticated')
            url = 'https://uts-ws.nlm.nih.gov/search/current'
            params = {'apiKey': self.api_key, 'string': string}
            response = requests.get(url, params=params)
            return format_cui_results(response.json())
        except Exception as e:
            # Handle exceptions (e.g., connection errors, timeouts)
            return str(e)
        
    def get_info_cui(self, cui):
        """ 
        Returns informatoins related to the a concept unique indentifier in UMLS. 
        :param cui: UMLS concept unique indentifier. 
        :return: Formatted object of information. 
        """

        try:
            if not self.api_key:
                raise Exception('Client is not authenticated')
            url = 'https://uts-ws.nlm.nih.gov/rest/content/current/CUI/' + cui
            params = {'apiKey': self.api_key}
            response = requests.get(url, params=params)
            return response.json()['result']
        except Exception as e:
            # Handle exceptions (e.g., connection errors, timeouts)
            return str(e)
        
    def get_mapping(self, code ,sourceVocabId, targetVocabId):
        """ 
        Returns an list of the mapping of CUI in the vocabulary vocab. 
        :param code: UMLS concept unique indentifier. 
        :param sourceVocabId: Source vocavulary identifier from the UMLS ontology 
        :param targetVocabId: Target vocavulary identifier from the UMLS ontology
        :return: Formatted list of mappings. 
        """

        try:
            if not self.api_key:
                raise Exception('Client is not authenticated')
            url = 'https://uts-ws.nlm.nih.gov/rest/crosswalk/current/source' +'/'+ sourceVocabId +'/'+ code
            params = {'apiKey': self.api_key, 'targetSource': targetVocabId}

            response = requests.get(url, params=params)

            cuis_list = format_mapping_results(response.json())
            return cuis_list
        except Exception as e:
            # Handle exceptions (e.g., connection errors, timeouts)
            return str(e)
        
    def get_atoms_list(self, cui ,VocabId, lang = 'ENG'):
        """ 
        Returns an list of the mapping of CUI in the vocabulary vocab. 
        :param code: UMLS concept unique indentifier. 
        :param sourceVocabId: Source vocavulary identifier from the UMLS ontology 
        :param targetVocabId: Target vocavulary identifier from the UMLS ontology
        :return: Formatted list of mappings. 
        """

        try:
            if not self.api_key:
                raise Exception('Client is not authenticated')
            url = 'https://uts-ws.nlm.nih.gov/rest/content/2023AB/CUI/'+ cui +'/atoms'
            params = {'apiKey': self.api_key, 'language':lang, 'sabs': VocabId}

            response = requests.get(url, params=params)
            if response.status_code == 404:
                return []
                #error_message = handle_api_error(response)
                #raise Exception(error_message)
            else:
                atoms_list = format_atom_results(response.json())
                return atoms_list
        except Exception as e:
            # Handle exceptions (e.g., connection errors, timeouts)
            return str(e)