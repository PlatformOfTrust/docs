--- 

title: LifeEngine 

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

**Version:** v1 

# /MESSAGE
## ***POST*** 

**Description:** Create a new message

### HTTP Request 
`***POST*** /message` 

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

# /MESSAGE/{ID}
## ***GET*** 

**Description:** Read one message by id

### HTTP Request 
`***GET*** /message/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## ***PUT*** 

**Description:** Update a message by id

### HTTP Request 
`***PUT*** /message/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

## ***DELETE*** 

**Description:** Delete a message by id

### HTTP Request 
`***DELETE*** /message/{id}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

# /MESSAGE/{ID}/READ
## ***POST*** 

**Description:** Marks a message read by the currently logged in user.

### HTTP Request 
`***POST*** /message/{id}/read` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 403 |  |

# /MESSAGES/{TOIDENTITY}/LIST
## ***GET*** 

**Description:** List all messages belonging to the "to" identity.

### HTTP Request 
`***GET*** /messages/{toIdentity}/list` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the message belongs to. | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
