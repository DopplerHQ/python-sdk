

# DopplerSDK Python SDK 1.0.1
A Python SDK for DopplerSDK. 



- API version: 1.0.1
- SDK version: 1.0.1

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [Dependencies](#dependencies)
- [Authentication](#authentication)
    - [Bearer Authentication](#bearer-authentication)
- [API Endpoint Services](#api-endpoint-services)
- [API Models](#api-models)
- [Testing](#testing)
- [Configuration](#configuration)
- [Sample Usage](#sample-usage)

## Requirements

Building the API client library requires:
- Python ^3.9 installed.

## Installation

Make sure you have installed the needed dependencies.

```bash
pip install -r requirements.txt
```

If you want to install this library instead of embedding it locally, run this command.

```bash
python -m pip install -e src/
```

### Dependencies

This SDK uses the following dependencies:
- requests 2.28.1
- http-exceptions 0.2.10
- pytest 7.1.2
- responses 0.21.0

## Authentication

To see whether an endpoint needs a specific type of authentication check the endpoint's documentation.

### Bearer Authentication
The DopplerSDK API uses bearer tokens as a form of authentication.

The bearer token can be set either for the entire sdk: 

```
sdk = DopplerSDK()
sdk.set_bearer_token('YOUR_BEARER_TOKEN')
```
Or per endpoint:
```
sdk = DopplerSDK()
sdk.projects.set_bearer_token('YOUR_BEARER_TOKEN')
```

## API Endpoint Services

All URIs are relative to https://api.doppler.com.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Projects](./services/README.MD#projects)|
|[Secrets](./services/README.MD#secrets)|
|[ConfigLogs](./services/README.MD#configlogs)|
|[Environments](./services/README.MD#environments)|
|[Configs](./services/README.MD#configs)|
|[ActivityLogs](./services/README.MD#activitylogs)|
|[V3](./services/README.MD#v3)|
|[ServiceTokens](./services/README.MD#servicetokens)|
|[DynamicSecrets](./services/README.MD#dynamicsecrets)|
|[Integrations](./services/README.MD#integrations)|
|[Syncs](./services/README.MD#syncs)|

## API Models
[A list documenting all API models for this SDK](./models/README.MD#dopplersdk-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py" 
```

## Configuration

Your SDK may require some configuration changes.


This API is configured to use a security token for authorization. You should edit `sample.py` and paste your own token in place of **YOUR_PERSONAL_TOKEN**.

## Sample Usage

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''

sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)

results = sdk.projects.list()

pprint(vars(results))
```

Inside this directory is `sample.py`. It's a simple, "hello, world" level program to demonstrate this SDK. Run it with `python3 -m sample`.

To see what other functions this SDK is capable of, look inside `src/services/*.py`.





