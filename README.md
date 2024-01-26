# 🎈 Terminology Mapper

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://symmetrical-spork-4qw5gxqxqgghjqj9.github.dev/)

Starter code for Medical Terminology Mapper build ontop of UMLS ontology.

## Overview of the App

This app showcases a collection of usecase for Mapping medical terminology.

Current examples include:

- Terminology mapper: Takes text or code and return list of mappings
- Maper from Code: Maps code to list of codes from a source to target terminology



### Get a UMLS API key

You can get your own UMLS API key by following the following instructions:

1. Go to https://uts.nlm.nih.gov/uts/login.
2. Create an account and fill your informations
2. Go to your profile and find your API KEY after validation.


## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Terminology\ Mapping.py
```
