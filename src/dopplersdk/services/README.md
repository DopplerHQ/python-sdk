# DopplerSDK Services

A list of all services and services methods.

- Services

  - [Projects](#projects)

  - [Environments](#environments)

  - [Configs](#configs)

  - [ConfigLogs](#configlogs)

  - [Secrets](#secrets)

  - [Workplace](#workplace)

  - [ActivityLogs](#activitylogs)

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

  - [Get](#get)

  - [Retrieve](#retrieve)

  - [Webhooks](#webhooks)

  - [ServiceAccountTokens](#serviceaccounttokens)

- [All Methods](#all-methods)

## Projects

| Method            | Description |
| :---------------- | :---------- |
| [create](#create) | Create      |
| [list](#list)     | List        |
| [update](#update) | Update      |
| [get](#get)       | Retrieve    |
| [delete](#delete) | Delete      |

## Environments

| Method            | Description |
| :---------------- | :---------- |
| [create](#create) | Create      |
| [list](#list)     | List        |
| [get](#get)       | Retrieve    |
| [delete](#delete) | Delete      |
| [rename](#rename) | Rename      |

## Configs

| Method                                  | Description |
| :-------------------------------------- | :---------- |
| [update](#update)                       | Update      |
| [get](#get)                             | Retrieve    |
| [delete](#delete)                       | Delete      |
| [create](#create)                       | Create      |
| [list](#list)                           | List        |
| [unlock](#unlock)                       | Unlock      |
| [clone](#clone)                         | Clone       |
| [lock](#lock)                           | Lock        |
| [add_trusted_ip](#add_trusted_ip)       | Add         |
| [list_trusted_ips](#list_trusted_ips)   | List        |
| [delete_trusted_ip](#delete_trusted_ip) | Delete      |

## ConfigLogs

| Method                | Description |
| :-------------------- | :---------- |
| [get](#get)           | Retrieve    |
| [list](#list)         | List        |
| [rollback](#rollback) | Rollback    |

## Secrets

| Method                      | Description |
| :-------------------------- | :---------- |
| [update](#update)           | Update      |
| [list](#list)               | List        |
| [get](#get)                 | Retrieve    |
| [delete](#delete)           | Delete      |
| [download](#download)       | Download    |
| [update_note](#update_note) | Update Note |
| [names](#names)             | List Names  |

## Workplace

| Method            | Description |
| :---------------- | :---------- |
| [update](#update) | Update      |
| [get](#get)       | Retrieve    |

## ActivityLogs

| Method                | Description |
| :-------------------- | :---------- |
| [list](#list)         | List        |
| [retrieve](#retrieve) | Retrieve    |

## ServiceTokens

| Method            | Description |
| :---------------- | :---------- |
| [delete](#delete) | Delete      |
| [create](#create) | Create      |
| [list](#list)     | List        |

## Audit

| Method                | Description    |
| :-------------------- | :------------- |
| [get_user](#get_user) | Workplace User |

## DynamicSecrets

| Method                        | Description  |
| :---------------------------- | :----------- |
| [revoke_lease](#revoke_lease) | Revoke Lease |
| [issue_lease](#issue_lease)   | Issue Lease  |

## Auth

| Method            | Description |
| :---------------- | :---------- |
| [revoke](#revoke) | Revoke      |
| [me](#me)         | Me          |

## Integrations

| Method            | Description |
| :---------------- | :---------- |
| [get](#get)       | Retrieve    |
| [delete](#delete) | Delete      |
| [update](#update) | Update      |
| [create](#create) | Create      |
| [list](#list)     | List        |

## Syncs

| Method            | Description |
| :---------------- | :---------- |
| [create](#create) | Create      |
| [get](#get)       | Retrieve    |
| [delete](#delete) | Delete      |

## WorkplaceRoles

| Method                                | Description      |
| :------------------------------------ | :--------------- |
| [create](#create)                     | Create           |
| [list](#list)                         | List             |
| [get](#get)                           | Retrieve         |
| [update](#update)                     | Update           |
| [delete](#delete)                     | Delete           |
| [list_permissions](#list_permissions) | List Permissions |

## ProjectRoles

| Method                                | Description      |
| :------------------------------------ | :--------------- |
| [get](#get)                           | Retrieve         |
| [update](#update)                     | Update           |
| [delete](#delete)                     | Delete           |
| [create](#create)                     | Create           |
| [list](#list)                         | List             |
| [list_permissions](#list_permissions) | List Permissions |

## ProjectMembers

| Method            | Description |
| :---------------- | :---------- |
| [add](#add)       | Add         |
| [list](#list)     | List        |
| [get](#get)       | Retrieve    |
| [update](#update) | Update      |
| [delete](#delete) | Delete      |

## Invites

| Method        | Description |
| :------------ | :---------- |
| [list](#list) | List        |

## ServiceAccounts

| Method            | Description |
| :---------------- | :---------- |
| [get](#get)       | Retrieve    |
| [update](#update) | Update      |
| [delete](#delete) | Delete      |
| [create](#create) | Create      |
| [list](#list)     | List        |

## Groups

| Method                          | Description   |
| :------------------------------ | :------------ |
| [get](#get)                     | Retrieve      |
| [update](#update)               | Update        |
| [delete](#delete)               | Delete        |
| [create](#create)               | Create        |
| [list](#list)                   | List          |
| [delete_member](#delete_member) | Delete Member |
| [add_member](#add_member)       | Add Member    |

## Users

| Method        | Description |
| :------------ | :---------- |
| [list](#list) | List        |
| [get](#get)   | Retrieve    |

## Get

| Method              | Description |
| :------------------ | :---------- |
| [options](#options) | Get Options |

## Retrieve

| Method            | Description     |
| :---------------- | :-------------- |
| [member](#member) | Retrieve Member |

## Webhooks

| Method              | Description |
| :------------------ | :---------- |
| [add](#add)         | Add         |
| [list](#list)       | List        |
| [get](#get)         | Retrieve    |
| [update](#update)   | Update      |
| [delete](#delete)   | Delete      |
| [enable](#enable)   | Enable      |
| [disable](#disable) | Disable     |

## ServiceAccountTokens

| Method            | Description |
| :---------------- | :---------- |
| [create](#create) | Create      |
| [list](#list)     | List        |
| [get](#get)       | Retrieve    |
| [delete](#delete) | Delete      |

## All Methods

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/projects

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | Unique identifier for the project object. |

**Return Type**

[GetResponse](/src/dopplersdk/models/README.md#getresponse)

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
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/environments

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/environments/environment

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **update**

Update

- HTTP Method: POST
- Endpoint: /v3/configs/config

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/configs

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **unlock**

Unlock

- HTTP Method: POST
- Endpoint: /v3/configs/config/unlock

**Parameters**
| Name | Type| Required | Description |
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

### **clone**

Clone

- HTTP Method: POST
- Endpoint: /v3/configs/config/clone

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **add_trusted_ip**

Add

- HTTP Method: POST
- Endpoint: /v3/configs/config/trusted_ips

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | |
| config | str | Required | |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | |
| config | str | Required | |

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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | |
| config | str | Required | |
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

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/configs/config/logs/log

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | Unique identifier for the project object. |
| config | str | Required | Name of the config object. |
| log | str | Required | Unique identifier for the log object. |

**Return Type**

[ConfigLogsGetResponse](/src/dopplersdk/models/README.md#configlogsgetresponse)

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

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/configs/config/logs

**Parameters**
| Name | Type| Required | Description |
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

### **rollback**

Rollback

- HTTP Method: POST
- Endpoint: /v3/configs/config/logs/log/rollback

**Parameters**
| Name | Type| Required | Description |
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

### **update**

Update

- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [SecretsUpdateRequest](/src/dopplersdk/models/README.md#secretsupdaterequest) | Optional | Request body. |

**Return Type**

[SecretsUpdateResponse](/src/dopplersdk/models/README.md#secretsupdateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'change_requests': [{"name":"quis et","originalName":"Ut voluptate reprehenderit culpa","originalValue":"sed ex","originalVisibility":"do nisi exercitation","shouldConverge":true,"shouldDelete":true,"shouldPromote":false,"value":"laboris anim","visibility":"sit nostrud ut est consectetur"},{"name":"officia consectetur velit amet cupidatat","originalName":"consequat nostrud deserunt ut","originalValue":"eiusmod esse veniam commodo officia","originalVisibility":"cillum","shouldConverge":false,"shouldDelete":true,"shouldPromote":true,"value":"nulla Lorem in dolore","visibility":"in"}],
	'config': 'CONFIG_NAME',
	'project': 'PROJECT_NAME',
	'secrets': {}
}
results = sdk.secrets.update(request_input = request_body)

pprint(vars(results))

```

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets

**Parameters**
| Name | Type| Required | Description |
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
	dynamic_secrets_ttl_sec = -20553545,
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | Unique identifier for the project object. Not required if using a Service Token. |
| config | str | Required | Name of the config object. Not required if using a Service Token. |
| format | [Format](/src/dopplersdk/models/README.md#format) | Optional | |
| name_transformer | [NameTransformer](/src/dopplersdk/models/README.md#nametransformer) | Optional | Transform secret names to a different case |
| include_dynamic_secrets | bool | Optional | Whether or not to issue leases and include dynamic secret values for the config |
| dynamic_secrets_ttl_sec | int | Optional | The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes). |
| secrets | str | Optional | Comma-delimited list of secrets to include in the download. Defaults to all secrets if left unspecified. |

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
	name_transformer = 'camel',
	include_dynamic_secrets = True,
	dynamic_secrets_ttl_sec = 1800,
	secrets = 'secrets'
)

pprint(vars(results))

```

### **update_note**

Update Note

- HTTP Method: POST
- Endpoint: /v3/configs/config/secrets/note

**Parameters**
| Name | Type| Required | Description |
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
	'config': 'config',
	'note': 'YOUR_NOTE',
	'project': 'PROJECT_NAME',
	'secret': 'SECRET_NAME'
}
results = sdk.secrets.update_note(request_input = request_body)

pprint(vars(results))

```

### **names**

List Names

- HTTP Method: GET
- Endpoint: /v3/configs/config/secrets/names

**Parameters**
| Name | Type| Required | Description |
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

### **update**

Update

- HTTP Method: POST
- Endpoint: /v3/workplace

**Parameters**
| Name | Type| Required | Description |
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

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/logs

**Parameters**
| Name | Type| Required | Description |
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

### **retrieve**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/logs/log

**Parameters**
| Name | Type| Required | Description |
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

### **delete**

Delete

- HTTP Method: DELETE
- Endpoint: /v3/configs/config/tokens/token

**Parameters**
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/configs/config/tokens

**Parameters**
| Name | Type| Required | Description |
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
	'expire_at': '1898-12-29T20:03:18.0Z',
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
| Name | Type| Required | Description |
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

### **get_user**

Workplace User

- HTTP Method: GET
- Endpoint: /v3/workplace/users/{workplace_user_id}

**Parameters**
| Name | Type| Required | Description |
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

### **revoke_lease**

Revoke Lease

- HTTP Method: DELETE
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease

**Parameters**
| Name | Type| Required | Description |
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

### **issue_lease**

Issue Lease

- HTTP Method: POST
- Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases

**Parameters**
| Name | Type| Required | Description |
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
	'ttl_sec': 56600272
}
results = sdk.dynamic_secrets.issue_lease(request_input = request_body)

pprint(vars(results))

```

### **revoke**

Revoke

- HTTP Method: POST
- Endpoint: /v3/auth/revoke

**Parameters**
| Name | Type| Required | Description |
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

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/integrations/integration

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
- Endpoint: /v3/integrations

**Parameters**
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/configs/config/syncs

**Parameters**
| Name | Type| Required | Description |
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
	'await_initial_sync': True,
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [WorkplaceRolesCreateRequest](/src/dopplersdk/models/README.md#workplacerolescreaterequest) | Optional | Request body. |

**Return Type**

[WorkplaceRolesCreateResponse](/src/dopplersdk/models/README.md#workplacerolescreateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'permissions': ["aliqua do","ullamco Lorem sunt eu"]
}
results = sdk.workplace_roles.create(request_input = request_body)

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

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/workplace/roles/role/{role}

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| role | str | Required | The role's unique identifier, which is the initial name the role was given |
| request_input | [WorkplaceRolesUpdateRequest](/src/dopplersdk/models/README.md#workplacerolesupdaterequest) | Optional | Request body. |

**Return Type**

[WorkplaceRolesUpdateResponse](/src/dopplersdk/models/README.md#workplacerolesupdateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'permissions': ["Ut labore sunt in","veniam qui laborum nisi"]
}
results = sdk.workplace_roles.update(
	request_input = request_body,
	role = 'role'
)

pprint(vars(results))

```

### **delete**

Delete

- HTTP Method: DELETE
- Endpoint: /v3/workplace/roles/role/{role}

**Parameters**
| Name | Type| Required | Description |
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
- Endpoint: /v3/projects/roles/role/{role}

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| role | str | Required | The role's unique identifier |
| request_input | [ProjectRolesUpdateRequest](/src/dopplersdk/models/README.md#projectrolesupdaterequest) | Optional | Request body. |

**Return Type**

[ProjectRolesUpdateResponse](/src/dopplersdk/models/README.md#projectrolesupdateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'permissions': ["eiusmod tempor laboris id","dolore proident"]
}
results = sdk.project_roles.update(
	request_input = request_body,
	role = 'role'
)

pprint(vars(results))

```

### **delete**

Delete

- HTTP Method: DELETE
- Endpoint: /v3/projects/roles/role/{role}

**Parameters**
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/projects/roles

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| request_input | [ProjectRolesCreateRequest](/src/dopplersdk/models/README.md#projectrolescreaterequest) | Optional | Request body. |

**Return Type**

[ProjectRolesCreateResponse](/src/dopplersdk/models/README.md#projectrolescreateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'name': 'name',
	'permissions': ["velit reprehenderit ipsum","incididunt elit sint qui"]
}
results = sdk.project_roles.create(request_input = request_body)

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
| Name | Type| Required | Description |
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
	'environments': ["Excepteur mollit","magna eiusmod sunt enim"],
	'role': 'role',
	'slug': 'slug',
	'type_': 'service_account'
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | Project slug |
| page | int | Optional | |
| per_page | int | Optional | |

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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Required | Project slug |
| type\_ | [Type](/src/dopplersdk/models/README.md#type) | Required | |
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
	type_ = 'workplace_user',
	slug = 'slug'
)

pprint(vars(results))

```

### **update**

Update

- HTTP Method: PATCH
- Endpoint: /v3/projects/project/members/member/{type}/{slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| type\_ | [Type](/src/dopplersdk/models/README.md#type) | Required | |
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
	'environments': ["culpa","ut aliquip officia"],
	'role': 'role'
}
results = sdk.project_members.update(
	request_input = request_body,
	type_ = 'group',
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| type\_ | [Type](/src/dopplersdk/models/README.md#type) | Required | |
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
	type_ = 'service_account',
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| page | int | Optional | |
| per_page | int | Optional | |

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

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts/service_account/{slug}

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
	'workplace_role': {"identifier":"identifier","permissions":["nulla","dolore"]}
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
| Name | Type| Required | Description |
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
- Endpoint: /v3/workplace/service_accounts

**Parameters**
| Name | Type| Required | Description |
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
	'workplace_role': {"identifier":"identifier","permissions":["consectetur voluptate","ipsum cupidatat est qui"]}
}
results = sdk.service_accounts.create(request_input = request_body)

pprint(vars(results))

```

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| page | int | Optional | |
| per_page | int | Optional | |

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
- Endpoint: /v3/workplace/groups/group/{slug}

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
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

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/workplace/groups

**Parameters**
| Name | Type| Required | Description |
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
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| page | int | Optional | |
| per_page | int | Optional | |

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

### **delete_member**

Delete Member

- HTTP Method: DELETE
- Endpoint: /v3/workplace/groups/group/{slug}/members/{type}/{member_slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| slug | str | Required | The group's slug |
| type\_ | [GroupsType](/src/dopplersdk/models/README.md#groupstype) | Required | |
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
	type_ = 'workplace_user',
	member_slug = 'member_slug'
)

pprint(vars(results))

```

### **add_member**

Add Member

- HTTP Method: POST
- Endpoint: /v3/workplace/groups/group/{slug}/members

**Parameters**
| Name | Type| Required | Description |
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

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/workplace/users

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| page | int | Optional | The page of users to fetch |
| email | str | Optional | Filter results to only include the user with the provided email address |

**Return Type**

[UsersListResponse](/src/dopplersdk/models/README.md#userslistresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.users.list(
	page = 1,
	email = 'email'
)

pprint(vars(results))

```

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/workplace/users/{slug}

**Parameters**
| Name | Type| Required | Description |
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

### **options**

Get Options

- HTTP Method: GET
- Endpoint: /v3/integrations/integration/options

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| integration | str | Required | The integration slug |

**Return Type**

[OptionsResponse](/src/dopplersdk/models/README.md#optionsresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.get.options(integration = 'integration')

pprint(vars(results))

```

### **member**

Retrieve Member

- HTTP Method: GET
- Endpoint: /v3/workplace/groups/group/{group_slug}/members/{member_type}/{member_slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| group_slug | str | Required | The group's slug |
| member_type | [MemberType](/src/dopplersdk/models/README.md#membertype) | Required | |
| member_slug | str | Required | The member's slug |

**Return Type**

[MemberResponse](/src/dopplersdk/models/README.md#memberresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.retrieve.member(
	group_slug = 'group_slug',
	member_type = 'workplace_user',
	member_slug = 'member_slug'
)

pprint(vars(results))

```

### **add**

Add

- HTTP Method: POST
- Endpoint: /v3/webhooks

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |
| request_input | [WebhooksAddRequest](/src/dopplersdk/models/README.md#webhooksaddrequest) | Optional | Request body. |

**Return Type**

[WebhooksAddResponse](/src/dopplersdk/models/README.md#webhooksaddresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {}
results = sdk.webhooks.add(
	request_input = request_body,
	project = 'project'
)

pprint(vars(results))

```

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/webhooks

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |

**Return Type**

[WebhooksListResponse](/src/dopplersdk/models/README.md#webhookslistresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.webhooks.list(project = 'project')

pprint(vars(results))

```

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/webhooks/webhook/{slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| slug | str | Required | Webhook's slug |
| project | str | Optional | The project's name |

**Return Type**

[WebhooksGetResponse](/src/dopplersdk/models/README.md#webhooksgetresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.webhooks.get(
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **update**

Update

- HTTP Method: PATCH
- Endpoint: /v3/webhooks/webhook/{slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |
| slug | str | Required | Webhook's slug |
| request_input | [WebhooksUpdateRequest](/src/dopplersdk/models/README.md#webhooksupdaterequest) | Optional | Request body. |

**Return Type**

[WebhooksUpdateResponse](/src/dopplersdk/models/README.md#webhooksupdateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {}
results = sdk.webhooks.update(
	request_input = request_body,
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **delete**

Delete

- HTTP Method: DELETE
- Endpoint: /v3/webhooks/webhook/{slug}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |
| slug | str | Required | Webhook's slug |

**Return Type**

[WebhooksDeleteResponse](/src/dopplersdk/models/README.md#webhooksdeleteresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.webhooks.delete(
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **enable**

Enable

- HTTP Method: POST
- Endpoint: /v3/webhooks/webhook/{slug}/enable

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |
| slug | str | Required | Webhook's slug |

**Return Type**

[EnableResponse](/src/dopplersdk/models/README.md#enableresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.webhooks.enable(
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **disable**

Disable

- HTTP Method: POST
- Endpoint: /v3/webhooks/webhook/{slug}/disable

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| project | str | Optional | The project's name |
| slug | str | Required | Webhook's slug |

**Return Type**

[DisableResponse](/src/dopplersdk/models/README.md#disableresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.webhooks.disable(
	slug = 'slug',
	project = 'project'
)

pprint(vars(results))

```

### **create**

Create

- HTTP Method: POST
- Endpoint: /v3/workplace/service_accounts/service_account/{service_account}/tokens

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| service_account | str | Required | Slug of the service account |
| request_input | [ServiceAccountTokensCreateRequest](/src/dopplersdk/models/README.md#serviceaccounttokenscreaterequest) | Optional | Request body. |

**Return Type**

[ServiceAccountTokensCreateResponse](/src/dopplersdk/models/README.md#serviceaccounttokenscreateresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
request_body = {
	'expires_at': '1920-11-18T08:18:44.0Z',
	'name': 'name'
}
results = sdk.service_account_tokens.create(
	request_input = request_body,
	service_account = 'service_account'
)

pprint(vars(results))

```

### **list**

List

- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts/service_account/{service_account}/tokens

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| page | int | Optional | |
| per_page | int | Optional | |
| service_account | str | Required | Slug of the service account |

**Return Type**

[ServiceAccountTokensListResponse](/src/dopplersdk/models/README.md#serviceaccounttokenslistresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.service_account_tokens.list(
	service_account = 'service_account',
	page = 1,
	per_page = 20
)

pprint(vars(results))

```

### **get**

Retrieve

- HTTP Method: GET
- Endpoint: /v3/workplace/service_accounts/service_account/{service_account}/tokens/token/{api_token}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| service_account | str | Required | Slug of the service account |
| api_token | str | Required | Slug of the API token |

**Return Type**

[ServiceAccountTokensGetResponse](/src/dopplersdk/models/README.md#serviceaccounttokensgetresponse)

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.service_account_tokens.get(
	service_account = 'service_account',
	api_token = 'api_token'
)

pprint(vars(results))

```

### **delete**

Delete

- HTTP Method: DELETE
- Endpoint: /v3/workplace/service_accounts/service_account/{service_account}/tokens/token/{api_token}

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------| :----------|
| service_account | str | Required | Slug of the service account |
| api_token | str | Required | Slug of the API token |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**

```Python
from pprint import pprint
from dopplersdk import DopplerSDK
DOPPLERSDK_ACCESS_TOKEN = ''
sdk = DopplerSDK()
sdk.set_access_token(DOPPLERSDK_ACCESS_TOKEN)
results = sdk.service_account_tokens.delete(
	service_account = 'service_account',
	api_token = 'api_token'
)

pprint(vars(results))

```
