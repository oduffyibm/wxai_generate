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
    client = APIClient(credentials, space_id = space_id)


        # Prepare input data

    input_data = {"Company": "JP Morgan & Chase"}
    
    params = {
        "decoding_method": "sample",
        "temperature": 0.4,
        "max_new_tokens": 100
    }

    model_id = "google/flan-t5-xxl"
    verify = False

    model = ModelInference(
    model_id=model_id,
    api_client=client,
    params=params,
    project_id=project_id,
    space_id=space_id,
    verify=verify,
    )

    Company = st.text_input("Company Name","Walmart")

    prompt = f"""
    Generate a 5 sentence marketing message for a company with the given characteristics.

    Characteristics:

    Company - {Company}

    Offer includes - no fees, 2% interest rate, no minimum balance

    Tone - informative

    Response requested - click the link

    End date - July 15
    """


    #print(model.generate(prompt))
    st.title("Email Generation")
    st.write(model.generate_text(prompt))



main()