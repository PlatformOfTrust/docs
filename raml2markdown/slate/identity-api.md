--- 

title: Identity 

language_tabs: 
   - shell 

toc_footers: 
   - <a href='#'>Sign Up for a Developer Key</a> 
   - <a href='https://github.com/lavkumarv'>Documentation Powered by lav</a> 

includes: 
   - errors 

search: true 

--- 

# Introduction 

The Identity API provides means to create, update and delete digital twins
(identities) and manage links between them.
The links provides the direction and type (sometimes called role) of the link.
 

**Version:** v1 

# /IDENTITIES/V1
## ***POST*** 

**Description:** Create a new identity

### HTTP Request 
`***POST*** /identities/v1` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## ***GET*** 

**Description:** List all identities created by currently logged in user

### HTTP Request 
`***GET*** /identities/v1` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /identities/{version}?type=App`, will list only the identities of `@type: "App"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

# /IDENTITIES/V1/{ID}
## ***GET*** 

**Description:** Read one identity by id

### HTTP Request 
`***GET*** /identities/v1/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## ***PUT*** 

**Description:** Update an identity by id

### HTTP Request 
`***PUT*** /identities/v1/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

## ***DELETE*** 

**Description:** Delete an identity by id

### HTTP Request 
`***DELETE*** /identities/v1/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

# /IDENTITIES/V1/{FROM_IDENTITY}/LINK/{TO_IDENTITY}
## ***POST*** 

**Description:** Creates a new link between two identities

### HTTP Request 
`***POST*** /identities/v1/{from_identity}/link/{to_identity}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 404 |  |
| 422 |  |

# /IDENTITIES/V1/{FROM_IDENTITY}/LINK/{TO_IDENTITY}/{TYPE}
## ***GET*** 

**Description:** Read a link by type

### HTTP Request 
`***GET*** /identities/v1/{from_identity}/link/{to_identity}/{type}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## ***PUT*** 

**Description:** Update a link

### HTTP Request 
`***PUT*** /identities/v1/{from_identity}/link/{to_identity}/{type}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 404 |  |
| 422 |  |

## ***DELETE*** 

**Description:** Delete a link by type

### HTTP Request 
`***DELETE*** /identities/v1/{from_identity}/link/{to_identity}/{type}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |
| 422 |  |

# /IDENTITIES/V1/{ID}/LINKS
## ***GET*** 

**Description:** List all links for a given identity

### HTTP Request 
`***GET*** /identities/v1/{id}/links` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /identities/{version}/{id}/links?type=Owner`, will list only the links of `@type: "Owner"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
