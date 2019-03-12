--- 

title: Platform Of Trust Documentation 

language_tabs: 
   - shell 
   - java
   - python
   - javascript

toc_footers: 
   - <a href='https://developers.oftrust.net'>Developer Portal</a> 

includes: 
   - authentication
   - ontologies
   - errors 
   - feedback
   

search: true 

--- 

# Platform of Trust API Documentation

This could be rather static introduction to Platform of Trust APIs and written in separate file. Then just preprocess the files and merge all, or do it 
manually. Nope! Includes go all to bottom. 

# Getting started

## Auth practices
We use OAuth xxx flow. Every API call is required to have ..... Read more from [Authentication section](#authentication)

## Standards used

* For time and dates we use a subset of ISO-8601 - [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt). Example <code>2008-09-15T15:53:00+05:00</code>

## Code Examples 

<aside class="warning">
All the documentation code examples use our sandbox environment. When you are done with testing, you should switch to production environment. Easiest way is to store API root url in variable and when needed, change it there. Thus the code examples contain API-root variable as an exmaple. 
</aside>


# OAuth

To make API requests, you need to authenticate to Upwork API. Currently, we support OAuth 2.0 authentication. All API requests MUST be signed following the RFC 5849 specification.


## Client credentials

For each application you develop, you need to obtain new client credentials. These include a client identifier and a client shared-secret. You can find these credentials at https://developers.oftrust.net/profile while logged into your Upwork account. You will receive a public and a private key for each client identifier and client shared-secret you request.


## OAuth 2.0 workflow

## Get request token

**Endpoint**

POST /api/auth/v1/oauth/token/request

HTTPS is required. All the names of variables follow OAuth specification (see RFC 5849).

```python

import upwork
client = upwork.Client(public_key, secret_key, **credentials)
client.auth.get_request_token()

```

# Broker API

**Version:** v0.1 

## /health
### **get** 

**Description:** Health check endpoint

#### http request 
**GET** /health 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /fetch-data-product
### **post** 

**Description:** Fetch data product

#### http request 
**POST** /fetch-data-product 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 422 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Calendar API

**Version:** v1 

## /calendar
### **post** 

**Description:** Create a new calendar entry

#### http request 
**POST** /calendar 

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

## /calendar/{id}
### **get** 

**Description:** Read one calendar by id

#### http request 
**GET** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a calendar by id

#### http request 
**PUT** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a calendar by id

#### http request 
**DELETE** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /calendar/{toidentity}/list
### **get** 

**Description:** List all calendars belonging to the "to" identity.

#### http request 
**GET** /calendar/{toIdentity}/list 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the calendar belongs to. | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Identity API

**Version:** v1 

## /identity
### **post** 

**Description:** Create a new identity

#### http request 
**POST** /identity 

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

## /identity/{id}
### **get** 

**Description:** Read one identity by id

#### http request 
**GET** /identity/{id} 

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

### **put** 

**Description:** Update an identity by id

#### http request 
**PUT** /identity/{id} 

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

### **delete** 

**Description:** Delete an identity by id

#### http request 
**DELETE** /identity/{id} 

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

## /identities
### **get** 

**Description:** List all identities created by currently logged in user

#### http request 
**GET** /identities 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /identities/{from_identity}/link/{to_identity}
### **post** 

**Description:** Creates a new link between two identities

#### http request 
**POST** /identities/{from_identity}/link/{to_identity} 

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

## /identities/{from_identity}/link/{to_identity}/{type}
### **put** 

**Description:** Update a link

#### http request 
**PUT** /identities/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
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

### **delete** 

**Description:** Delete a link by type

#### http request 
**DELETE** /identities/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |
| 422 |  |

## /identities/{id}/links
### **get** 

**Description:** List all links for a given identity

#### http request 
**GET** /identities/{id}/links 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## /identities/{id}/links/{type}
### **get** 

**Description:** List all links of type {type} for given identity

#### http request 
**GET** /identities/{id}/links/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Message API

**Version:** v1 

## /message
### **post** 

**Description:** Create a new message

#### http request 
**POST** /message 

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

## /message/{id}
### **get** 

**Description:** Read one message by id

#### http request 
**GET** /message/{id} 

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

### **put** 

**Description:** Update a message by id

#### http request 
**PUT** /message/{id} 

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

### **delete** 

**Description:** Delete a message by id

#### http request 
**DELETE** /message/{id} 

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

## /message/{id}/read
### **post** 

**Description:** Marks a message read by the currently logged in user.

#### http request 
**POST** /message/{id}/read 

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

## /messages/{toidentity}/list
### **get** 

**Description:** List all messages belonging to the "to" identity.

#### http request 
**GET** /messages/{toIdentity}/list 

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
# Product API

**Version:** v1 

## /products
### **post** 

**Description:** Create a new product

#### http request 
**POST** /products 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

### **get** 

**Description:** Lists all available products.

#### http request 
**GET** /products 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /products/{product_code}
### **get** 

**Description:** Reads a single product by product code

#### http request 
**GET** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a product by product code

#### http request 
**PUT** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a product by product code

#### http request 
**DELETE** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
