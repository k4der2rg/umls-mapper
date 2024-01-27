def format_cui_results(data):
    """
    Formats the get_cui_list results data from UMLS API for better readability.
    :param data: The raw data from UMLS API response.
    :return: Formatted data.
    """
    formatted_data = []
    for item in data['result'].get('results', []):
        formatted_data.append({
            'ui': item.get('ui'),
            'rootSource': item.get('rootSource'),
            'name': item.get('name'),
            'uri': item.get('uri'),
            })
    return formatted_data

def format_atom_results(data):
    """
    Formats the get_atoms_list results data from UMLS API for better readability.
    :param data: The raw data from UMLS API response.
    :return: Formatted data.
    """
    formatted_data = []
    for item in data['result']:
        formatted_data.append({
            'ui': item.get('ui'),
            'Vocabulary ID': item.get('rootSource'),
            'Term': item.get('name'),
            'Code': item.get('code').split("/")[-1],
            'Type': item.get('termType')
            })
    return formatted_data



def format_mapping_results(data):
    """
    Formats the get_mapping results data from UMLS API for better readability.
    :param data: The raw data from UMLS API response.
    :return: Formatted data.
    """
    formatted_data = []
    for item in data['result']:
        formatted_data.append({
            'Code': item.get('ui'),
            'Vocabulary ID': item.get('rootSource'),
            'Term': item.get('name'),
            })
    return formatted_data

