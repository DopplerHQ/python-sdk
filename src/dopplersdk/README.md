# DopplerSDK Python SDK 1.1.0
A Python SDK for DopplerSDK.



- API version: 1.1.0
- SDK version: 1.1.0

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
- [DopplerSDK Services](#dopplersdk-services)

## Installation
```bash
pip install doppler-sdk
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
The DopplerSDK API uses bearer tokens as a form of authentication.You can set the bearer token when initializing the SDK through the constructor: 

```py
sdk = DopplerSDK('YOUR_BEARER_TOKEN')
```

Or through the `set_bearer_token` method:
```py
sdk = DopplerSDK()
sdk.set_bearer_token('YOUR_BEARER_TOKEN')
```

You can also set it for each service individually:
```py
sdk = DopplerSDK()
sdk.projects.set_bearer_token('YOUR_BEARER_TOKEN')
```

## API Endpoint Services

All URIs are relative to https://api.doppler.com.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Projects](./services/README.md#projects)|
|[Environments](./services/README.md#environments)|
|[Configs](./services/README.md#configs)|
|[Secrets](./services/README.md#secrets)|
|[ConfigLogs](./services/README.md#configlogs)|
|[V3](./services/README.md#v3)|
|[ActivityLogs](./services/README.md#activitylogs)|
|[ServiceTokens](./services/README.md#servicetokens)|
|[DynamicSecrets](./services/README.md#dynamicsecrets)|
|[Integrations](./services/README.md#integrations)|
|[Syncs](./services/README.md#syncs)|
|[TrustedIps](./services/README.md#trustedips)|
|[WorkplaceRoles](./services/README.md#workplaceroles)|
|[ProjectRoles](./services/README.md#projectroles)|
|[ProjectMembers](./services/README.md#projectmembers)|
|[Invites](./services/README.md#invites)|
|[ServiceAccounts](./services/README.md#serviceaccounts)|
|[Groups](./services/README.md#groups)|

## API Models
[A list documenting all API models for this SDK](./models/README.md#dopplersdk-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py" 
```

## Sample Usage

```py
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''

sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)

results = sdk.projects.list()

pprint(vars(results))
```


# DopplerSDK Services
A list of all services and services methods.
- Services

    - [Projects](#projects)

    - [Environments](#environments)

    - [Configs](#configs)

    - [Secrets](#secrets)

    - [ConfigLogs](#configlogs)

    - [V3](#v3)

    - [ActivityLogs](#activitylogs)

    - [ServiceTokens](#servicetokens)

    - [DynamicSecrets](#dynamicsecrets)

    - [Integrations](#integrations)

    - [Syncs](#syncs)

    - [TrustedIps](#trustedips)

    - [WorkplaceRoles](#workplaceroles)

    - [ProjectRoles](#projectroles)

    - [ProjectMembers](#projectmembers)

    - [Invites](#invites)

    - [ServiceAccounts](#serviceaccounts)

    - [Groups](#groups)
- [All Methods](#all-methods)


## Projects

| Method    | Description|
| :-------- | :----------| 
| [update](#update) | Update |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [create](#create) | Create |
| [list](#list) | List |


## Environments

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [rename](#rename) | Rename |


## Configs

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [update](#update) | Update |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [clone](#clone) | Clone |
| [lock](#lock) | Lock |
| [unlock](#unlock) | Unlock |


## Secrets

| Method    | Description|
| :-------- | :----------| 
| [update](#update) | Update |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [download](#download) | Download |
| [names](#names) | List Names |
| [update_note](#update_note) | Update Note |


## ConfigLogs

| Method    | Description|
| :-------- | :----------| 
| [list](#list) | List |
| [get](#get) | Retrieve |
| [rollback](#rollback) | Rollback |


## V3

| Method    | Description|
| :-------- | :----------| 
| [me](#me) | Me |


## ActivityLogs

| Method    | Description|
| :-------- | :----------| 
| [list](#list) | List |
| [retrieve](#retrieve) | Retrieve |


## ServiceTokens

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [delete](#delete) | Delete |


## DynamicSecrets

| Method    | Description|
| :-------- | :----------| 
| [issue_lease](#issue_lease) | Issue Lease |
| [revoke_lease](#revoke_lease) | Revoke Lease |


## Integrations

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [update](#update) | Update |


## Syncs

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |


## TrustedIps

| Method    | Description|
| :-------- | :----------| 
| [add](#add) | Add |
| [list](#list) | List |
| [delete](#delete) | Delete |


## WorkplaceRoles

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [list_permissions](#list_permissions) | List Permissions |
| [get](#get) | Retrieve |
| [update](#update) | Update |
| [delete](#delete) | Delete |


## ProjectRoles

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [update](#update) | Update |
| [delete](#delete) | Delete |
| [list_permissions](#list_permissions) | List Permissions |


## ProjectMembers

| Method    | Description|
| :-------- | :----------| 
| [add](#add) | Add |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [update](#update) | Update |
| [delete](#delete) | Delete |


## Invites

| Method    | Description|
| :-------- | :----------| 
| [list](#list) | List |


## ServiceAccounts

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [update](#update) | Update |
| [delete](#delete) | Delete |


## Groups

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [get](#get) | Retrieve |
| [update](#update) | Update |
| [delete](#delete) | Delete |
| [add_member](#add_member) | Add Member |
| [delete_member](#delete_member) | Delete Member |




## All Methods


### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/projects/project

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.projects.update(request_input = request_body)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/projects/project

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.projects.get(project = 'PROJECT_NAME')

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/projects/project

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DeleteRequest](/src/dopplersdk/models/README.md#deleterequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.projects.delete(request_input = request_body)

pprint(vars(results))

```

### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/projects

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.projects.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/projects

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | int | Optional | Page number |
| per_page | int | Optional | Items per page |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.projects.list(
	page = 1,
	per_page = 20
)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/environments

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.environments.create(
	request_input = request_body,
	project = 'project'
)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/environments

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.environments.list(project = 'project')

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/environments/environment

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| environment | str | Required | The environment's slug |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.environments.get(
	project = 'project',
	environment = 'environment'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/environments/environment

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| environment | str | Required | The environment's slug |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.environments.delete(
	project = 'project',
	environment = 'environment'
)

pprint(vars(results))

```

### **rename**
Rename
- HTTP Method: PUT
- Endpoint: /v3/environments/environment

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| environment | str | Required | The environment's slug |
| request_input | [RenameRequest](/src/dopplersdk/models/README.md#renamerequest) | Optional | Request body. |

**Return Type**

[RenameResponse](/src/dopplersdk/models/README.md#renameresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'name': 'name',
	'slug': 'slug'
}
results = sdk.environments.rename(
	request_input = request_body,
	project = 'project',
	environment = 'environment'
)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.configs.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/configs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| environment | str | Optional | (optional) the environment from which to list configs |
| page | int | Optional | Page number |
| per_page | int | Optional | Items per page |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.configs.list(
	project = 'project',
	environment = 'Environment slug',
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/configs/config

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.configs.update(request_input = request_body)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/configs/config

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.configs.get(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DeleteRequest](/src/dopplersdk/models/README.md#deleterequest) | Optional | Request body. |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.configs.delete(request_input = request_body)

pprint(vars(results))

```

### **clone**
Clone
- HTTP Method: POST
- Endpoint: /v3/configs/config/clone

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CloneRequest](/src/dopplersdk/models/README.md#clonerequest) | Optional | Request body. |

**Return Type**

[CloneResponse](/src/dopplersdk/models/README.md#cloneresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'name': 'NEW_CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.clone(request_input = request_body)

pprint(vars(results))

```

### **lock**
Lock
- HTTP Method: POST
- Endpoint: /v3/configs/config/lock

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [LockRequest](/src/dopplersdk/models/README.md#lockrequest) | Optional | Request body. |

**Return Type**

[LockResponse](/src/dopplersdk/models/README.md#lockresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.lock(request_input = request_body)

pprint(vars(results))

```

### **unlock**
Unlock
- HTTP Method: POST
- Endpoint: /v3/configs/config/unlock

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UnlockRequest](/src/dopplersdk/models/README.md#unlockrequest) | Optional | Request body. |

**Return Type**

[UnlockResponse](/src/dopplersdk/models/README.md#unlockresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.unlock(request_input = request_body)

pprint(vars(results))

```


### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.secrets.update(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| accepts | str | Optional | Available options are: **application/json**, **text/plain** |
| include_dynamic_secrets | bool | Optional | Whether or not to issue leases and include dynamic secret values for the config |
| dynamic_secrets_ttl_sec | int | Optional | The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes). |
| secrets | str | Optional | A comma-separated list of secrets to include in the response |
| include_managed_secrets | bool | Optional | Whether to include Doppler's auto-generated (managed) secrets |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.list(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	accepts = 'application/json',
	include_dynamic_secrets = True,
	dynamic_secrets_ttl_sec = 18119642,
	secrets = 'secrets',
	include_managed_secrets = True
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/configs/config/secret

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| name | str | Required | Name of the secret. |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.get(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	name = 'SECRET_NAME'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/secret

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| name | str | Required | Name of the secret. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.delete(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	name = 'SECRET_NAME'
)

pprint(vars(results))

```

### **download**
Download
- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets/download

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. Not required if using a Service Token. |
| config | str | Required | Name of the config object. Not required if using a Service Token. |
| format | [Format](/src/dopplersdk/models/README.md#format) | Optional |  |
| name_transformer | [NameTransformer](/src/dopplersdk/models/README.md#nametransformer) | Optional | Transform secret names to a different case |
| include_dynamic_secrets | bool | Optional | Whether or not to issue leases and include dynamic secret values for the config |
| dynamic_secrets_ttl_sec | int | Optional | The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes). |

**Return Type**

[DownloadResponse](/src/dopplersdk/models/README.md#downloadresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.download(
	project = 'project',
	config = 'config',
	format = 'json',
	name_transformer = 'dotnet-env',
	include_dynamic_secrets = True,
	dynamic_secrets_ttl_sec = 1800
)

pprint(vars(results))

```

### **names**
List Names
- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets/names

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| include_dynamic_secrets | bool | Optional | Whether or not to issue leases and include dynamic secret values for the config |
| include_managed_secrets | bool | Optional | Whether to include Doppler's auto-generated (managed) secrets |

**Return Type**

[NamesResponse](/src/dopplersdk/models/README.md#namesresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.names(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	include_dynamic_secrets = True,
	include_managed_secrets = True
)

pprint(vars(results))

```

### **update_note**
Update Note
- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets/note

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UpdateNoteRequest](/src/dopplersdk/models/README.md#updatenoterequest) | Optional | Request body. |

**Return Type**

[UpdateNoteResponse](/src/dopplersdk/models/README.md#updatenoteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'note': 'note',
	'project': 'PROJECT_NAME',
	'secret': 'secret'
}
results = sdk.secrets.update_note(request_input = request_body)

pprint(vars(results))

```


### **list**
List
- HTTP Method: GET
- Endpoint: /v3/configs/config/logs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| page | int | Optional | Page number |
| per_page | int | Optional | Items per page |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.config_logs.list(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/configs/config/logs/log

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| log | str | Required | Unique identifier for the log object. |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.config_logs.get(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	log = 'LOG_ID'
)

pprint(vars(results))

```

### **rollback**
Rollback
- HTTP Method: POST
- Endpoint: /v3/configs/config/logs/log/rollback

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| log | str | Required | Unique identifier for the log object. |

**Return Type**

[RollbackResponse](/src/dopplersdk/models/README.md#rollbackresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.config_logs.rollback(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	log = 'LOG_ID'
)

pprint(vars(results))

```


### **me**
Me
- HTTP Method: GET
- Endpoint: /v3/me

**Parameters**

This method has no parameters.

**Return Type**

[MeResponse](/src/dopplersdk/models/README.md#meresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.v_3.me()

pprint(vars(results))

```


### **list**
List
- HTTP Method: GET
- Endpoint: /v3/logs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | str | Optional | Page number |
| per_page | int | Optional | Items per page |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.activity_logs.list(
	page = '1',
	per_page = 20
)

pprint(vars(results))

```

### **retrieve**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/logs/log

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| log | str | Required | Unique identifier for the log object. |

**Return Type**

[RetrieveResponse](/src/dopplersdk/models/README.md#retrieveresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.activity_logs.retrieve(log = 'LOG_ID')

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs/config/tokens

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.service_tokens.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/configs/config/tokens

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.service_tokens.list(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/tokens/token

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DeleteRequest](/src/dopplersdk/models/README.md#deleterequest) | Optional | Request body. |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.service_tokens.delete(request_input = request_body)

pprint(vars(results))

```


### **issue_lease**
Issue Lease
- HTTP Method: POST
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [IssueLeaseRequest](/src/dopplersdk/models/README.md#issueleaserequest) | Optional | Request body. |

**Return Type**

[IssueLeaseResponse](/src/dopplersdk/models/README.md#issueleaseresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'config',
	'dynamic_secret': 'dynamic_secret',
	'project': 'project',
	'ttl_sec': 66643403
}
results = sdk.dynamic_secrets.issue_lease(request_input = request_body)

pprint(vars(results))

```

### **revoke_lease**
Revoke Lease
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [RevokeLeaseRequest](/src/dopplersdk/models/README.md#revokeleaserequest) | Optional | Request body. |

**Return Type**

[RevokeLeaseResponse](/src/dopplersdk/models/README.md#revokeleaseresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'config': 'config',
	'dynamic_secret': 'dynamic_secret',
	'project': 'project',
	'slug': 'slug'
}
results = sdk.dynamic_secrets.revoke_lease(request_input = request_body)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/integrations

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.integrations.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/integrations

**Parameters**

This method has no parameters.

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.integrations.list()

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/integrations/integration

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration | str | Required | The integration slug |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.integrations.get(integration = 'integration')

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/integrations/integration

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration | str | Required | The slug of the integration to delete |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.integrations.delete(integration = 'integration')

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PUT
- Endpoint: /v3/integrations/integration

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration | str | Required | The slug of the integration to update |
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.integrations.update(
	request_input = request_body,
	integration = 'integration'
)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs/config/syncs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project slug |
| config | str | Required | The config slug |
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.syncs.create(
	request_input = request_body,
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/configs/config/syncs/sync

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project slug |
| config | str | Required | The config slug |
| sync | str | Required | The sync slug |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.syncs.get(
	project = 'project',
	config = 'config',
	sync = 'sync'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/syncs/sync

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project slug |
| config | str | Required | The config slug |
| sync | str | Required | The sync slug |
| delete_from_target | bool | Required | Whether or not to delete the synced data from the target integration |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.syncs.delete(
	project = 'project',
	config = 'config',
	sync = 'sync',
	delete_from_target = True
)

pprint(vars(results))

```


### **add**
Add
- HTTP Method: POST
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |
| request_input | [AddRequest](/src/dopplersdk/models/README.md#addrequest) | Optional | Request body. |

**Return Type**

[AddResponse](/src/dopplersdk/models/README.md#addresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'environments': ["laboris","incididunt esse Duis aute aliquip"],
	'role': 'role',
	'slug': 'slug',
	'type_': 'service_account'
}
results = sdk.trusted_ips.add(
	request_input = request_body,
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.trusted_ips.list(
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |
| request_input | [DeleteRequest](/src/dopplersdk/models/README.md#deleterequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.trusted_ips.delete(
	request_input = request_body,
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/workplace/roles

**Parameters**

This method has no parameters.

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.create()

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/workplace/roles

**Parameters**

This method has no parameters.

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.list()

pprint(vars(results))

```

### **list_permissions**
List Permissions
- HTTP Method: GET
- Endpoint: /v3/workplace/permissions

**Parameters**

This method has no parameters.

**Return Type**

[ListPermissionsResponse](/src/dopplersdk/models/README.md#listpermissionsresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.list_permissions()

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/workplace/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.get(role = 'role')

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PATCH
- Endpoint: /v3/workplace/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.update(role = 'role')

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/workplace/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.workplace_roles.delete(role = 'role')

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/projects/roles

**Parameters**

This method has no parameters.

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.create()

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/projects/roles

**Parameters**

This method has no parameters.

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.list()

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/projects/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.get(role = 'role')

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PATCH
- Endpoint: /v3/projects/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.update(role = 'role')

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/projects/roles/role/{role}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| role | str | Required | The role's unique identifier |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.delete(role = 'role')

pprint(vars(results))

```

### **list_permissions**
List Permissions
- HTTP Method: GET
- Endpoint: /v3/projects/permissions

**Parameters**

This method has no parameters.

**Return Type**

[ListPermissionsResponse](/src/dopplersdk/models/README.md#listpermissionsresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_roles.list_permissions()

pprint(vars(results))

```


### **add**
Add
- HTTP Method: POST
- Endpoint: /v3/projects/project/members

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Project slug |
| request_input | [AddRequest](/src/dopplersdk/models/README.md#addrequest) | Optional | Request body. |

**Return Type**

[AddResponse](/src/dopplersdk/models/README.md#addresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'environments': ["cillum","occaecat ipsum consectetur amet"],
	'role': 'role',
	'slug': 'slug',
	'type_': 'workplace_user'
}
results = sdk.project_members.add(
	request_input = request_body,
	project = 'project'
)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/projects/project/members

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Project slug |
| page | int | Optional |  |
| per_page | int | Optional |  |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_members.list(
	project = 'project',
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/projects/project/members/member/{type}/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Project slug |
| type | [Type](/src/dopplersdk/models/README.md#type) | Required |  |
| slug | str | Required | Member's slug |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_members.get(
	project = 'project',
	type = 'workplace_user',
	slug = 'slug'
)

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PATCH
- Endpoint: /v3/projects/project/members/member/{type}/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| type | [Type](/src/dopplersdk/models/README.md#type) | Required |  |
| slug | str | Required | Member's slug |
| project | str | Required | Project slug |
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.project_members.update(
	request_input = request_body,
	type = 'workplace_user',
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/projects/project/members/member/{type}/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| type | [Type](/src/dopplersdk/models/README.md#type) | Required |  |
| slug | str | Required | Member's slug |
| project | str | Required | Project slug |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.project_members.delete(
	type = 'workplace_user',
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```


### **list**
List
- HTTP Method: GET
- Endpoint: /v3/workplace/invites

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | int | Optional |  |
| per_page | int | Optional |  |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.invites.list(
	page = 1,
	per_page = 20
)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/workplace/service_accounts

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.service_accounts.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | int | Optional |  |
| per_page | int | Optional |  |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.service_accounts.list(
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts/service_account/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | Slug of the service account |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.service_accounts.get(slug = 'slug')

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PATCH
- Endpoint: /v3/workplace/service_accounts/service_account/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | Slug of the service account |
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.service_accounts.update(
	request_input = request_body,
	slug = 'slug'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/workplace/service_accounts/service_account/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | Slug of the service account |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.service_accounts.delete(slug = 'slug')

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/workplace/groups

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateRequest](/src/dopplersdk/models/README.md#createrequest) | Optional | Request body. |

**Return Type**

[CreateResponse](/src/dopplersdk/models/README.md#createresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.groups.create(request_input = request_body)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/workplace/groups

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | int | Optional |  |
| per_page | int | Optional |  |

**Return Type**

[ListResponse](/src/dopplersdk/models/README.md#listresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.groups.list(
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/workplace/groups/group/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The group's slug |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.groups.get(slug = 'slug')

pprint(vars(results))

```

### **update**
Update
- HTTP Method: PATCH
- Endpoint: /v3/workplace/groups/group/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The group's slug |
| request_input | [UpdateRequest](/src/dopplersdk/models/README.md#updaterequest) | Optional | Request body. |

**Return Type**

[UpdateResponse](/src/dopplersdk/models/README.md#updateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'default_project_role': 'default_project_role',
	'name': 'name'
}
results = sdk.groups.update(
	request_input = request_body,
	slug = 'slug'
)

pprint(vars(results))

```

### **delete**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/workplace/groups/group/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The group's slug |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.groups.delete(slug = 'slug')

pprint(vars(results))

```

### **add_member**
Add Member
- HTTP Method: POST
- Endpoint: /v3/workplace/groups/group/{slug}/members

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The group's slug |
| request_input | [AddMemberRequest](/src/dopplersdk/models/README.md#addmemberrequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
request_body = {
	'slug': 'slug',
	'type_': 'workplace_user'
}
results = sdk.groups.add_member(
	request_input = request_body,
	slug = 'slug'
)

pprint(vars(results))

```

### **delete_member**
Delete Member
- HTTP Method: DELETE
- Endpoint: /v3/workplace/groups/group/{slug}/members/{type}/{member_slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The group's slug |
| type | [Type](/src/dopplersdk/models/README.md#type) | Required |  |
| member_slug | str | Required | The member's slug |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.groups.delete_member(
	slug = 'slug',
	type = 'workplace_user',
	member_slug = 'member_slug'
)

pprint(vars(results))

```






