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
    text = st.text_area("Enter Code:")
    sourceVocab_text = st.selectbox("Select the source terminology", vocab_list.values()).strip()
    targetVocab_text = st.selectbox("Select the target terminology", vocab_list.values()).strip()
    submitted = st.form_submit_button("Submit")

    if not umls_api_key:
        st.info("Please add your UMLS API key to continue.")
    elif submitted:
        targetVocab = [k for k, v in vocab_list.items() if v == targetVocab_text][0]
        sourceVocab = [k for k, v in vocab_list.items() if v == sourceVocab_text][0]
        umls_client = UMLSClient(umls_api_key)
        cui_list = umls_client.get_cui_list(text,sourceVocab)
        if len(cui_list) == 0:
            st.info("Code \" "+ text + " \" not found in "+ sourceVocab_text +". Try again!", icon="ℹ️")
        else:
            cui = cui_list[0]['ui']
            mappings = umls_client.get_mapping(text,sourceVocab,targetVocab)
            if len(mappings) == 0:
                st.info("Mapping not found for \" "+ text + " \" in "+ targetVocab_text +". Try again!", icon="ℹ️")
            else:
                mappings_df = pd.DataFrame.from_dict(mappings)
                vocab_list_df = pd.DataFrame.from_dict(vocab_list, orient='index').reset_index()
                vocab_list_df.columns = ['Vocabulary ID','Vocabulary Name']

                results = pd.merge(mappings_df, vocab_list_df, how="inner", on=['Vocabulary ID', 'Vocabulary ID'])
                st.dataframe(results)
        

