from pprint import pprint
from dopplersdk import DopplerSDK

DOPPLERSDK_ACCESS_TOKEN = ""

sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)

results = sdk.projects.list()

pprint(vars(results))
