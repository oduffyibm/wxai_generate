from ibm_watsonx_ai import Credentials, APIClient
import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference



def main():
    envloc = find_dotenv()
    load_dotenv(envloc)

    credentials = Credentials(
        #url = os.getenv('url'),
        #api_key = os.getenv('api_key'),
        url = st.secrets['url'],
        api_key = st.secrets['api_key']
    )

    project_id = 'cec51c53-de81-40d9-a95a-e252d28addb8'
    space_id = 'eb924898-995a-4ded-b299-ff34982b2cfc'
    client = APIClient(credentials, project_id = project_id)


        # Prepare input data

    input_data = {"Company": "JP Morgan & Chase"}
    
    params = {
        "decoding_method": "greedy",
        #"temperature": 1.0,
        "max_new_tokens": 200,
        "min_new_tokens": 100,
        "end_sequence": "."
    }

    model_id = "google/flan-ul2-20b"
    verify = False

    model = ModelInference(
    model_id=model_id,
    api_client=client,
    params=params,
    project_id=project_id,
    space_id=space_id,
    verify=verify,
    )

    War = st.text_input("War","War of the Roses")

    prompt = f"""
    Prompt: Generate five-sentence summary of {War}\. The summary should include the nations or groups involved in the war. 
    It should also include who
    won the war and why they won.

    Summary:

    """


    #print(model.generate(prompt))
    st.title("War summary")
    st.write(model.generate_text(prompt))



main()