# doppler-sdk

Doppler's SDK provides convenient access to the Doppler API from applications written in Python.

- API version: 3
- SDK version: 1.0.0

## Installation

```sh
pip install --upgrade doppler-sdk
```

## Usage

```python
from pprint import pprint
from doppler-sdk import DopplerSDK

doppler = DopplerSDK()
doppler.set_bearer_token("dp.xx.yyy")

results = doppler.projects.list()

pprint(vars(results))
```

## Reference Docs

[A list of all services and service methods](./src/dopplersdk/services/README.MD)
