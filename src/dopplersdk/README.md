# DopplerSDK Python SDK 1.2.0
A Python SDK for DopplerSDK.



- API version: 1.2.0
- SDK version: 1.2.0

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [Dependencies](#dependencies)
- [Authentication](#authentication)
    - [Access Token Authentication](#bearer-authentication)
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

### Access Token Authentication
The DopplerSDK API uses bearer tokens as a form of authentication.You can set the bearer token when initializing the SDK through the constructor: 

```py
sdk = DopplerSDK('YOUR_BEARER_TOKEN')
```

Or through the `set_access_token` method:
```py
sdk = DopplerSDK()
sdk.set_access_token('YOUR_BEARER_TOKEN')
```

You can also set it for each service individually:
```py
sdk = DopplerSDK()
sdk.projects.set_access_token('YOUR_BEARER_TOKEN')
```

## API Endpoint Services

All URIs are relative to https://api.doppler.com.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Projects](./services/README.md#projects)|
|[Secrets](./services/README.md#secrets)|
|[ConfigLogs](./services/README.md#configlogs)|
|[Environments](./services/README.md#environments)|
|[Configs](./services/README.md#configs)|
|[ActivityLogs](./services/README.md#activitylogs)|
|[Workplace](./services/README.md#workplace)|
|[ServiceTokens](./services/README.md#servicetokens)|
|[Audit](./services/README.md#audit)|
|[DynamicSecrets](./services/README.md#dynamicsecrets)|
|[Auth](./services/README.md#auth)|
|[Integrations](./services/README.md#integrations)|
|[Syncs](./services/README.md#syncs)|
|[WorkplaceRoles](./services/README.md#workplaceroles)|
|[ProjectRoles](./services/README.md#projectroles)|
|[ProjectMembers](./services/README.md#projectmembers)|
|[Invites](./services/README.md#invites)|
|[ServiceAccounts](./services/README.md#serviceaccounts)|
|[Groups](./services/README.md#groups)|
|[Users](./services/README.md#users)|

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
DOPPLERSDK_ACCESS_TOKEN = ''

sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)

results = sdk.projects.list()

pprint(vars(results))
```


# DopplerSDK Services
A list of all services and services methods.
- Services

    - [Projects](#projects)

    - [Secrets](#secrets)

    - [ConfigLogs](#configlogs)

    - [Environments](#environments)

    - [Configs](#configs)

    - [ActivityLogs](#activitylogs)

    - [Workplace](#workplace)

    - [ServiceTokens](#servicetokens)

    - [Audit](#audit)

    - [DynamicSecrets](#dynamicsecrets)

    - [Auth](#auth)

    - [Integrations](#integrations)

    - [Syncs](#syncs)

    - [WorkplaceRoles](#workplaceroles)

    - [ProjectRoles](#projectroles)

    - [ProjectMembers](#projectmembers)

    - [Invites](#invites)

    - [ServiceAccounts](#serviceaccounts)

    - [Groups](#groups)

    - [Users](#users)
- [All Methods](#all-methods)


## Projects

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [update](#update) | Update |
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |


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


## Environments

| Method    | Description|
| :-------- | :----------| 
| [get](#get) | Retrieve |
| [delete](#delete) | Delete |
| [rename](#rename) | Rename |
| [create](#create) | Create |
| [list](#list) | List |


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
| [add_trusted_ip](#add_trusted_ip) | Add |
| [list_trusted_ips](#list_trusted_ips) | List |
| [delete_trusted_ip](#delete_trusted_ip) | Delete |


## ActivityLogs

| Method    | Description|
| :-------- | :----------| 
| [retrieve](#retrieve) | Retrieve |
| [list](#list) | List |


## Workplace

| Method    | Description|
| :-------- | :----------| 
| [update](#update) | Update |
| [get](#get) | Retrieve |


## ServiceTokens

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [delete](#delete) | Delete |


## Audit

| Method    | Description|
| :-------- | :----------| 
| [get_user](#get_user) | Workplace User |


## DynamicSecrets

| Method    | Description|
| :-------- | :----------| 
| [issue_lease](#issue_lease) | Issue Lease |
| [revoke_lease](#revoke_lease) | Revoke Lease |


## Auth

| Method    | Description|
| :-------- | :----------| 
| [revoke](#revoke) | Revoke |
| [me](#me) | Me |


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


## Users

| Method    | Description|
| :-------- | :----------| 
| [list](#list) | List |
| [get](#get) | Retrieve |




## All Methods


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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'description': 'PROJECT_DESCRIPTION',
	'name': 'PROJECT_NAME'
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.projects.list(
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/projects/project

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ProjectsUpdateRequest](/src/dopplersdk/models/README.md#projectsupdaterequest) | Optional | Request body. |

**Return Type**

[ProjectsUpdateResponse](/src/dopplersdk/models/README.md#projectsupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'description': 'PROJECT_DESCRIPTION',
	'name': 'PROJECT_NEW_NAME',
	'project': 'PROJECT_NAME'
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

[ProjectsGetResponse](/src/dopplersdk/models/README.md#projectsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {'project': 'PROJECT_NAME'}
results = sdk.projects.delete(request_input = request_body)

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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME',
	'secrets': {"ALGOLIA":"N9TOPUCTO","DATABASE":"${USER}@aws.dynamodb.com:9876","STRIPE":"sk_test_9YxLnoLDdvOPn2dfjBVPB"}
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

[SecretsListResponse](/src/dopplersdk/models/README.md#secretslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.secrets.list(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	accepts = 'application/json',
	include_dynamic_secrets = True,
	dynamic_secrets_ttl_sec = -92040823,
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

[SecretsGetResponse](/src/dopplersdk/models/README.md#secretsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.secrets.download(
	project = 'project',
	config = 'config',
	format = 'json',
	name_transformer = 'lower-snake',
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ConfigLogsListResponse](/src/dopplersdk/models/README.md#configlogslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.config_logs.rollback(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	log = 'LOG_ID'
)

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

[EnvironmentsGetResponse](/src/dopplersdk/models/README.md#environmentsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
- Endpoint: /v3/environments

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | The project's name |
| request_input | [EnvironmentsCreateRequest](/src/dopplersdk/models/README.md#environmentscreaterequest) | Optional | Request body. |

**Return Type**

[EnvironmentsCreateResponse](/src/dopplersdk/models/README.md#environmentscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'slug': 'slug'
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

[EnvironmentsListResponse](/src/dopplersdk/models/README.md#environmentslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.environments.list(project = 'project')

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ConfigsCreateRequest](/src/dopplersdk/models/README.md#configscreaterequest) | Optional | Request body. |

**Return Type**

[ConfigsCreateResponse](/src/dopplersdk/models/README.md#configscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'environment': 'ENVIRONMENT_ID',
	'name': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
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

[ConfigsListResponse](/src/dopplersdk/models/README.md#configslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ConfigsUpdateRequest](/src/dopplersdk/models/README.md#configsupdaterequest) | Optional | Request body. |

**Return Type**

[ConfigsUpdateResponse](/src/dopplersdk/models/README.md#configsupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'name': 'CONFIG_NEW_NAME',
	'project': 'PROJECT_NAME'
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

[ConfigsGetResponse](/src/dopplersdk/models/README.md#configsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ConfigsDeleteRequest](/src/dopplersdk/models/README.md#configsdeleterequest) | Optional | Request body. |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.unlock(request_input = request_body)

pprint(vars(results))

```

### **add_trusted_ip**
Add
- HTTP Method: POST
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |
| request_input | [AddTrustedIpRequest](/src/dopplersdk/models/README.md#addtrustediprequest) | Optional | Request body. |

**Return Type**

[AddTrustedIpResponse](/src/dopplersdk/models/README.md#addtrustedipresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.configs.add_trusted_ip(
	request_input = request_body,
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```

### **list_trusted_ips**
List
- HTTP Method: GET
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |

**Return Type**

[ListTrustedIpsResponse](/src/dopplersdk/models/README.md#listtrustedipsresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.configs.list_trusted_ips(
	project = 'project',
	config = 'config'
)

pprint(vars(results))

```

### **delete_trusted_ip**
Delete
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required |  |
| config | str | Required |  |
| request_input | [DeleteTrustedIpRequest](/src/dopplersdk/models/README.md#deletetrustediprequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {'ip': 'ip'}
results = sdk.configs.delete_trusted_ip(
	request_input = request_body,
	project = 'project',
	config = 'config'
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.activity_logs.retrieve(log = 'LOG_ID')

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

[ActivityLogsListResponse](/src/dopplersdk/models/README.md#activitylogslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.activity_logs.list(
	page = '1',
	per_page = 20
)

pprint(vars(results))

```


### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/workplace

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [WorkplaceUpdateRequest](/src/dopplersdk/models/README.md#workplaceupdaterequest) | Optional | Request body. |

**Return Type**

[WorkplaceUpdateResponse](/src/dopplersdk/models/README.md#workplaceupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'billing_email': 'billing_email',
	'name': 'name',
	'security_email': 'security_email'
}
results = sdk.workplace.update(request_input = request_body)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/workplace

**Parameters**

This method has no parameters.

**Return Type**

[WorkplaceGetResponse](/src/dopplersdk/models/README.md#workplacegetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.workplace.get()

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs/config/tokens

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ServiceTokensCreateRequest](/src/dopplersdk/models/README.md#servicetokenscreaterequest) | Optional | Request body. |

**Return Type**

[ServiceTokensCreateResponse](/src/dopplersdk/models/README.md#servicetokenscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'access': 'read',
	'config': 'CONFIG_NAME',
	'expire_at': '1929-12-26T01:25:38.0Z',
	'name': 'TOKEN_NAME',
	'project': 'PROJECT_NAME'
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

[ServiceTokensListResponse](/src/dopplersdk/models/README.md#servicetokenslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ServiceTokensDeleteRequest](/src/dopplersdk/models/README.md#servicetokensdeleterequest) | Optional | Request body. |

**Return Type**

[DeleteResponse](/src/dopplersdk/models/README.md#deleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME',
	'slug': 'TOKEN_SLUG',
	'token': 'TOKEN_VALUE'
}
results = sdk.service_tokens.delete(request_input = request_body)

pprint(vars(results))

```


### **get_user**
Workplace User
- HTTP Method: GET
- Endpoint: /v3/workplace/users/{workplace_user_id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| workplace_user_id | str | Required | The ID of the workplace user |
| settings | bool | Optional | If true, the api will return more information if the user has e.g. SAML enabled and/or Multi Factor Auth enabled |

**Return Type**

[GetUserResponse](/src/dopplersdk/models/README.md#getuserresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.audit.get_user(
	workplace_user_id = 'workplace_user_id',
	settings = True
)

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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'config',
	'dynamic_secret': 'dynamic_secret',
	'project': 'project',
	'ttl_sec': -58145692
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'config': 'config',
	'dynamic_secret': 'dynamic_secret',
	'project': 'project',
	'slug': 'slug'
}
results = sdk.dynamic_secrets.revoke_lease(request_input = request_body)

pprint(vars(results))

```


### **revoke**
Revoke
- HTTP Method: POST
- Endpoint: /v3/auth/revoke

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [RevokeRequest](/src/dopplersdk/models/README.md#revokerequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {'token': 'token'}
results = sdk.auth.revoke(request_input = request_body)

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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.auth.me()

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/integrations

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [IntegrationsCreateRequest](/src/dopplersdk/models/README.md#integrationscreaterequest) | Optional | Request body. |

**Return Type**

[IntegrationsCreateResponse](/src/dopplersdk/models/README.md#integrationscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'data': {},
	'name': 'name',
	'type_': 'type'
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

[IntegrationsListResponse](/src/dopplersdk/models/README.md#integrationslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[IntegrationsGetResponse](/src/dopplersdk/models/README.md#integrationsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[IntegrationsDeleteResponse](/src/dopplersdk/models/README.md#integrationsdeleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [IntegrationsUpdateRequest](/src/dopplersdk/models/README.md#integrationsupdaterequest) | Optional | Request body. |

**Return Type**

[IntegrationsUpdateResponse](/src/dopplersdk/models/README.md#integrationsupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'data': 'data',
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
| request_input | [SyncsCreateRequest](/src/dopplersdk/models/README.md#syncscreaterequest) | Optional | Request body. |

**Return Type**

[SyncsCreateResponse](/src/dopplersdk/models/README.md#syncscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'data': {},
	'import_option': 'none',
	'integration': 'integration'
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

[SyncsGetResponse](/src/dopplersdk/models/README.md#syncsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[SyncsDeleteResponse](/src/dopplersdk/models/README.md#syncsdeleteresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.syncs.delete(
	project = 'project',
	config = 'config',
	sync = 'sync',
	delete_from_target = True
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

[WorkplaceRolesCreateResponse](/src/dopplersdk/models/README.md#workplacerolescreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[WorkplaceRolesListResponse](/src/dopplersdk/models/README.md#workplaceroleslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[WorkplaceRolesGetResponse](/src/dopplersdk/models/README.md#workplacerolesgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[WorkplaceRolesUpdateResponse](/src/dopplersdk/models/README.md#workplacerolesupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectRolesCreateResponse](/src/dopplersdk/models/README.md#projectrolescreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectRolesListResponse](/src/dopplersdk/models/README.md#projectroleslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectRolesGetResponse](/src/dopplersdk/models/README.md#projectrolesgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectRolesUpdateResponse](/src/dopplersdk/models/README.md#projectrolesupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectRolesListPermissionsResponse](/src/dopplersdk/models/README.md#projectroleslistpermissionsresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'environments': ["do ut occaecat","mollit sit"],
	'role': 'role',
	'slug': 'slug',
	'type_': 'group'
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

[ProjectMembersListResponse](/src/dopplersdk/models/README.md#projectmemberslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ProjectMembersGetResponse](/src/dopplersdk/models/README.md#projectmembersgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ProjectMembersUpdateRequest](/src/dopplersdk/models/README.md#projectmembersupdaterequest) | Optional | Request body. |

**Return Type**

[ProjectMembersUpdateResponse](/src/dopplersdk/models/README.md#projectmembersupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'environments': ["cillum","ad voluptate"],
	'role': 'role'
}
results = sdk.project_members.update(
	request_input = request_body,
	type = 'group',
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.project_members.delete(
	type = 'service_account',
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

[InvitesListResponse](/src/dopplersdk/models/README.md#inviteslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ServiceAccountsCreateRequest](/src/dopplersdk/models/README.md#serviceaccountscreaterequest) | Optional | Request body. |

**Return Type**

[ServiceAccountsCreateResponse](/src/dopplersdk/models/README.md#serviceaccountscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'workplace_role': {"identifier":"identifier","permissions":["Excepteur pariatur","et ut tempor voluptate"]}
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

[ServiceAccountsListResponse](/src/dopplersdk/models/README.md#serviceaccountslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[ServiceAccountsGetResponse](/src/dopplersdk/models/README.md#serviceaccountsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [ServiceAccountsUpdateRequest](/src/dopplersdk/models/README.md#serviceaccountsupdaterequest) | Optional | Request body. |

**Return Type**

[ServiceAccountsUpdateResponse](/src/dopplersdk/models/README.md#serviceaccountsupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'workplace_role': {"identifier":"identifier","permissions":["sunt Lorem reprehenderit","adipisicing"]}
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [GroupsCreateRequest](/src/dopplersdk/models/README.md#groupscreaterequest) | Optional | Request body. |

**Return Type**

[GroupsCreateResponse](/src/dopplersdk/models/README.md#groupscreateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[GroupsListResponse](/src/dopplersdk/models/README.md#groupslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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

[GroupsGetResponse](/src/dopplersdk/models/README.md#groupsgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| request_input | [GroupsUpdateRequest](/src/dopplersdk/models/README.md#groupsupdaterequest) | Optional | Request body. |

**Return Type**

[GroupsUpdateResponse](/src/dopplersdk/models/README.md#groupsupdateresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
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
| type | [GroupsType](/src/dopplersdk/models/README.md#groupstype) | Required |  |
| member_slug | str | Required | The member's slug |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.groups.delete_member(
	slug = 'slug',
	type = 'workplace_user',
	member_slug = 'member_slug'
)

pprint(vars(results))

```


### **list**
List
- HTTP Method: GET
- Endpoint: /v3/workplace/users

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| page | int | Optional | The page of users to fetch |

**Return Type**

[UsersListResponse](/src/dopplersdk/models/README.md#userslistresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.users.list(page = 1)

pprint(vars(results))

```

### **get**
Retrieve
- HTTP Method: GET
- Endpoint: /v3/workplace/users/{slug}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| slug | str | Required | The slug of the workplace user |

**Return Type**

[UsersGetResponse](/src/dopplersdk/models/README.md#usersgetresponse) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.users.get(slug = 'slug')

pprint(vars(results))

```






