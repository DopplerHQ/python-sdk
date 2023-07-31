from pprint import pprint
from dopplersdk import DopplerSDK

DOPPLERSDK_BEARER_TOKEN = ""

sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)

results = sdk.projects.list()

pprint(vars(results))
