# DopplerSDK Services
A list of all services and services methods.
- Services

    - [Projects](#projects)

    - [Secrets](#secrets)

    - [ConfigLogs](#configlogs)

    - [Environments](#environments)

    - [Configs](#configs)

    - [ActivityLogs](#activitylogs)

    - [V3](#v3)

    - [ServiceTokens](#servicetokens)

    - [DynamicSecrets](#dynamicsecrets)

    - [Integrations](#integrations)

    - [Syncs](#syncs)
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
| [download](#download) | Download |
| [list_names](#listnames) | List |
| [update_note](#updatenote) | Note |


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


## ActivityLogs

| Method    | Description|
| :-------- | :----------| 
| [retrieve](#retrieve) | Retrieve |
| [list](#list) | List |


## V3

| Method    | Description|
| :-------- | :----------| 
| [me](#me) | Me |


## ServiceTokens

| Method    | Description|
| :-------- | :----------| 
| [create](#create) | Create |
| [list](#list) | List |
| [delete](#delete) | Delete |


## DynamicSecrets

| Method    | Description|
| :-------- | :----------| 
| [issue_lease](#issuelease) | Issue Lease |
| [revoke_lease](#revokelease) | Revoke Lease |


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




## All Methods


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/projects

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ProjectsCreateRequest](../models/README.MD#projectscreaterequest) | Optional | Request body. |

**Return Type**

[ProjectsCreate200Response](../models/README.MD#projectscreate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'description': 'PROJECT_DESCRIPTION',
	'name': 'PROJECT_NAME'
}
results = sdk.projects.create(request_body=input)

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

[ProjectsList200Response](../models/README.MD#projectslist200response) 

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

### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/projects/project

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ProjectsUpdateRequest](../models/README.MD#projectsupdaterequest) | Optional | Request body. |

**Return Type**

[ProjectsUpdate200Response](../models/README.MD#projectsupdate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'description': 'PROJECT_DESCRIPTION',
	'name': 'PROJECT_NEW_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.projects.update(request_body=input)

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

[ProjectsGet200Response](../models/README.MD#projectsget200response) 

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
| request_input | [ProjectsDeleteRequest](../models/README.MD#projectsdeleterequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {'project': 'PROJECT_NAME'}
results = sdk.projects.delete(request_body=input)

pprint(vars(results))

```


### **update**
Update
- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [SecretsUpdateRequest](../models/README.MD#secretsupdaterequest) | Optional | Request body. |

**Return Type**

[SecretsUpdate200Response](../models/README.MD#secretsupdate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME',
	'secrets': {"ALGOLIA":"N9TOPUCTO","DATABASE":"${USER}@aws.dynamodb.com:9876","STRIPE":"sk_test_9YxLnoLDdvOPn2dfjBVPB"}
}
results = sdk.secrets.update(request_body=input)

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

Returns a dict object.

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
	dynamic_secrets_ttl_sec = 50843607,
	secrets = 'eu anim nulla commodo reprehenderit',
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

[SecretsGet200Response](../models/README.MD#secretsget200response) 

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

### **download**
Download
- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets/download

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| project | str | Required | Unique identifier for the project object. Not required if using a Service Token. |
| config | str | Required | Name of the config object. Not required if using a Service Token. |
| format | str | Optional |  |
| name_transformer | str | Optional | Transform secret names to a different case |
| include_dynamic_secrets | bool | Optional | Whether or not to issue leases and include dynamic secret values for the config |
| dynamic_secrets_ttl_sec | int | Optional | The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes). |

**Return Type**

[SecretsDownload200Response](../models/README.MD#secretsdownload200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.download(
	project = 'proident minim dolor officia',
	config = 'Ut Duis',
	format = 'json',
	name_transformer = 'camel',
	include_dynamic_secrets = True,
	dynamic_secrets_ttl_sec = 1800
)

pprint(vars(results))

```

### **list_names**
List
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

[SecretsListNames200Response](../models/README.MD#secretslistnames200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.secrets.list_names(
	project = 'PROJECT_NAME',
	config = 'CONFIG_NAME',
	include_dynamic_secrets = True,
	include_managed_secrets = True
)

pprint(vars(results))

```

### **update_note**
Note
- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets/note

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [SecretsUpdateNoteRequest](../models/README.MD#secretsupdatenoterequest) | Optional | Request body. |

**Return Type**

[SecretsUpdateNote200Response](../models/README.MD#secretsupdatenote200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'note': 'minim',
	'project': 'PROJECT_NAME',
	'secret': 'id aliqua'
}
results = sdk.secrets.update_note(request_body=input)

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

[ConfigLogsList200Response](../models/README.MD#configlogslist200response) 

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

[ConfigLogsGet200Response](../models/README.MD#configlogsget200response) 

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

[ConfigLogsRollback200Response](../models/README.MD#configlogsrollback200response) 

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

[EnvironmentsGet200Response](../models/README.MD#environmentsget200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.environments.get(
	project = 'ut est aliqua quis reprehenderit',
	environment = 'quis tempor'
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
	project = 'fugiat velit consequat',
	environment = 'magna fugiat aliquip est esse'
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
| request_input | [EnvironmentsRenameRequest](../models/README.MD#environmentsrenamerequest) | Optional | Request body. |

**Return Type**

[EnvironmentsRename200Response](../models/README.MD#environmentsrename200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'name': 'sed in',
	'slug': 'dolore deserunt magna'
}
results = sdk.environments.rename(
	request_body=input,
	project = 'culpa occaecat commodo',
	environment = 'veniam consectetur aliqua cupidatat occaecat'
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
| request_input | [EnvironmentsCreateRequest](../models/README.MD#environmentscreaterequest) | Optional | Request body. |

**Return Type**

[EnvironmentsCreate200Response](../models/README.MD#environmentscreate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'name': 'Ut irure veniam cillum sit',
	'slug': 'nostrud non ex'
}
results = sdk.environments.create(
	request_body=input,
	project = 'dolor veniam minim'
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

[EnvironmentsList200Response](../models/README.MD#environmentslist200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.environments.list(project = 'pariatur')

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ConfigsCreateRequest](../models/README.MD#configscreaterequest) | Optional | Request body. |

**Return Type**

[ConfigsCreate200Response](../models/README.MD#configscreate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'environment': 'ENVIRONMENT_ID',
	'name': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.create(request_body=input)

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

[ConfigsList200Response](../models/README.MD#configslist200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.configs.list(
	project = 'sint ut amet qui irure',
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
| request_input | [ConfigsUpdateRequest](../models/README.MD#configsupdaterequest) | Optional | Request body. |

**Return Type**

[ConfigsUpdate200Response](../models/README.MD#configsupdate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'name': 'CONFIG_NEW_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.update(request_body=input)

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

[ConfigsGet200Response](../models/README.MD#configsget200response) 

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
| request_input | [ConfigsDeleteRequest](../models/README.MD#configsdeleterequest) | Optional | Request body. |

**Return Type**

[ConfigsDelete200Response](../models/README.MD#configsdelete200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.delete(request_body=input)

pprint(vars(results))

```

### **clone**
Clone
- HTTP Method: POST
- Endpoint: /v3/configs/config/clone

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ConfigsCloneRequest](../models/README.MD#configsclonerequest) | Optional | Request body. |

**Return Type**

[ConfigsClone200Response](../models/README.MD#configsclone200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'name': 'NEW_CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.clone(request_body=input)

pprint(vars(results))

```

### **lock**
Lock
- HTTP Method: POST
- Endpoint: /v3/configs/config/lock

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ConfigsLockRequest](../models/README.MD#configslockrequest) | Optional | Request body. |

**Return Type**

[ConfigsLock200Response](../models/README.MD#configslock200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.lock(request_body=input)

pprint(vars(results))

```

### **unlock**
Unlock
- HTTP Method: POST
- Endpoint: /v3/configs/config/unlock

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ConfigsUnlockRequest](../models/README.MD#configsunlockrequest) | Optional | Request body. |

**Return Type**

[ConfigsUnlock200Response](../models/README.MD#configsunlock200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.configs.unlock(request_body=input)

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

[ActivityLogsRetrieve200Response](../models/README.MD#activitylogsretrieve200response) 

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

[ActivityLogsList200Response](../models/README.MD#activitylogslist200response) 

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


### **me**
Me
- HTTP Method: GET
- Endpoint: /v3/me

**Parameters**

This method has no parameters.

**Return Type**

[V3Me200Response](../models/README.MD#v3me200response) 

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


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/configs/config/tokens

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ServiceTokensCreateRequest](../models/README.MD#servicetokenscreaterequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'access': 'read',
	'config': 'CONFIG_NAME',
	'expire_at': '1917-09-21T23:46:58.0Z',
	'name': 'TOKEN_NAME',
	'project': 'PROJECT_NAME'
}
results = sdk.service_tokens.create(request_body=input)

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

Returns a dict object.

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
| request_input | [ServiceTokensDeleteRequest](../models/README.MD#servicetokensdeleterequest) | Optional | Request body. |

**Return Type**

[ServiceTokensDelete200Response](../models/README.MD#servicetokensdelete200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME',
	'slug': 'TOKEN_SLUG',
	'token': 'TOKEN_VALUE'
}
results = sdk.service_tokens.delete(request_body=input)

pprint(vars(results))

```


### **issue_lease**
Issue Lease
- HTTP Method: POST
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DynamicSecretsIssueLeaseRequest](../models/README.MD#dynamicsecretsissueleaserequest) | Optional | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'esse exercitation cillum amet Ut',
	'dynamic_secret': 'eu reprehenderit occaecat',
	'project': 'velit deserunt culpa ipsum',
	'ttl_sec': 53005069
}
results = sdk.dynamic_secrets.issue_lease(request_body=input)

pprint(vars(results))

```

### **revoke_lease**
Revoke Lease
- HTTP Method: DELETE
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DynamicSecretsRevokeLeaseRequest](../models/README.MD#dynamicsecretsrevokeleaserequest) | Optional | Request body. |

**Return Type**

[DynamicSecretsRevokeLease200Response](../models/README.MD#dynamicsecretsrevokelease200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'config': 'dolore reprehenderit dolor culpa ipsum',
	'dynamic_secret': 'consequat nostrud dolore ex',
	'project': 'ut Duis consectetur',
	'slug': 'qui amet'
}
results = sdk.dynamic_secrets.revoke_lease(request_body=input)

pprint(vars(results))

```


### **create**
Create
- HTTP Method: POST
- Endpoint: /v3/integrations

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [IntegrationsCreateRequest](../models/README.MD#integrationscreaterequest) | Optional | Request body. |

**Return Type**

[IntegrationsCreate200Response](../models/README.MD#integrationscreate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'data': {},
	'name': 'do elit',
	'type': 'non mollit'
}
results = sdk.integrations.create(request_body=input)

pprint(vars(results))

```

### **list**
List
- HTTP Method: GET
- Endpoint: /v3/integrations

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

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

[IntegrationsGet200Response](../models/README.MD#integrationsget200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.integrations.get(integration = 'ea adipisicing consectetur')

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

[IntegrationsDelete200Response](../models/README.MD#integrationsdelete200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.integrations.delete(integration = 'sint cillum velit')

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
| request_input | [IntegrationsUpdateRequest](../models/README.MD#integrationsupdaterequest) | Optional | Request body. |

**Return Type**

[IntegrationsUpdate200Response](../models/README.MD#integrationsupdate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'data': 'qui fugiat',
	'name': 'magna sunt ullamco'
}
results = sdk.integrations.update(
	request_body=input,
	integration = 'consequat anim et'
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
| request_input | [SyncsCreateRequest](../models/README.MD#syncscreaterequest) | Optional | Request body. |

**Return Type**

[SyncsCreate200Response](../models/README.MD#syncscreate200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
input = {
	'data': {},
	'import_option': 'none',
	'integration': 'nulla nisi dolore commodo'
}
results = sdk.syncs.create(
	request_body=input,
	project = 'amet in mollit occaecat',
	config = 'dolore eu id voluptate'
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

[SyncsGet200Response](../models/README.MD#syncsget200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.syncs.get(
	project = 'nostrud aute',
	config = 'officia est sed veniam tempor',
	sync = 'sit minim sunt id fugiat'
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

[SyncsDelete200Response](../models/README.MD#syncsdelete200response) 

**Example Usage Code Snippet**
```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_BEARER_TOKEN = ''  
sdk = DopplerSDK()
sdk.set_bearer_token(DOPPLERSDK_BEARER_TOKEN)
results = sdk.syncs.delete(
	project = 'ea veniam',
	config = 'laboris',
	sync = 'fugiat magna ex esse deserunt',
	delete_from_target = True
)

pprint(vars(results))

```




