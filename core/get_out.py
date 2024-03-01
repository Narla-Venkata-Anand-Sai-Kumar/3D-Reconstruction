from gradio_client import Client
from IPython.display import clear_output
def get_ot(first_key):
  client = Client("ashawkey/LGM")
  result = client.predict(
  		first_key,
  		"",
  		"",
  		5,
  		100,
  		0,
  		api_name="/process"
  )
  clear_output()
  return client
