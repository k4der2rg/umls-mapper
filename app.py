import streamlit as st
from umls.constants import vocab_list
from umls.client import UMLSClient
import pandas as pd

with st.sidebar:
    umls_api_key = st.text_input("UMLS API Key", key="umls_api_key", type="password")
    "[Get an UMLS API key](https://uts.nlm.nih.gov/uts/login)"
    "[View the source code](https://github.com/k4der2rg/umls-mapper)"
    "[![Open in GitHub](https://github.com/codespaces/badge.svg)](https://github.com/k4der2rg/umls-mapper)"

st.title("🔗 Terminology Mapping")
st.caption("🚀 A terminology mapper engine powered by UMLS ontology")
st.session_state["messages"] = [{"role": "assistant", "content": "Please enter the term you want to map and select to which terminology you want to map to?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

with st.form("my_form"):
    text = st.text_area("")
    targetVocab_text = st.selectbox("Select a state", vocab_list.values()).strip()
    submitted = st.form_submit_button("Submit")

    if not umls_api_key:
        st.info("Please add your UMLS API key to continue.")
    elif submitted:
        print(text)
        targetVocab = [k for k, v in vocab_list.items() if v == targetVocab_text][0]
        umls_client = UMLSClient(umls_api_key)
        cui_list = umls_client.get_cui_list(text)
        cui = cui_list[0]['ui']
        atoms = umls_client.get_atoms_list(cui,targetVocab)
        #sourceVocab = atoms[0]['rootSource']
        #sourceCode = atoms[0]['code']
        #mappings = umls_client.get_mapping(sourceCode,sourceVocab,targetVocab)
        print("------------------------")
        if len(atoms) == 0:
            st.info("No mappings found, try again with another terminology!")
        else:
            mappings_df = pd.DataFrame.from_dict(atoms)
            #mappings_df.rename(columns={'rootSource': 'Vocabulary ID'}, inplace=True)

            vocab_list_df = pd.DataFrame.from_dict(vocab_list, orient='index').reset_index()
            vocab_list_df.columns = ['Vocabulary ID','Vocabulary Name']

            results = pd.merge(mappings_df, vocab_list_df, how="inner", on=['Vocabulary ID', 'Vocabulary ID'])
            st.dataframe(results)
        

