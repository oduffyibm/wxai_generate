import requests
import os
from dotenv import find_dotenv, load_dotenv
from ibm_cloud_sdk_core import IAMTokenManager

location = find_dotenv()
load_dotenv(location)

api_key =os.getenv('api_key')
project_id = os.getenv('project_id')

url = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-28"

body = {
	"parameters": {
		"decoding_method": "sample",
		"max_new_tokens": 200,
		"min_new_tokens": 50,
		"random_seed": 111,
		"temperature": 1.14,
		"top_k": 50,
		"top_p": 1,
		"repetition_penalty": 2
	},
	"model_id": "google/flan-t5-xxl",
	"project_id": project_id,
	"moderations": {
		"hap": {
			"input": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			},
			"output": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			}
		},
		"pii": {
			"input": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			},
			"output": {
				"enabled": True,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": True
				}
			}
		}
	}
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer " + access_token
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()