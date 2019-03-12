--- 

title: New Platform Of Trust Documentation 

language_tabs: 
   - shell 
   - java
   - python
   - javascript

toc_footers: 
   - <a href='#'>Sign Up for a Developer Key</a> 
   - <a href='https://github.com/lavkumarv'>Documentation Powered by lav</a> 

includes: 
   - authentication
   - ontologies
   - errors 
   - feedback
   

search: true 

--- 

# Platform of Trust Documentation

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

# BROKER-API

**Version:** v0.1 

## /HEALTH
### ***GET*** 

**Description:** Health check endpoint

#### HTTP Request 
`***GET*** /health` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /FETCH-DATA-PRODUCT
### ***POST*** 

**Description:** Fetch data product

#### HTTP Request 
`***POST*** /fetch-data-product` 

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
# CALENDAR-API

**Version:** v1 

## /CALENDAR
### ***POST*** 

**Description:** Create a new calendar entry

#### HTTP Request 
`***POST*** /calendar` 

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

## /CALENDAR/{ID}
### ***GET*** 

**Description:** Read one calendar by id

#### HTTP Request 
`***GET*** /calendar/{id}` 

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

### ***PUT*** 

**Description:** Update a calendar by id

#### HTTP Request 
`***PUT*** /calendar/{id}` 

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

### ***DELETE*** 

**Description:** Delete a calendar by id

#### HTTP Request 
`***DELETE*** /calendar/{id}` 

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

## /CALENDAR/{TOIDENTITY}/LIST
### ***GET*** 

**Description:** List all calendars belonging to the "to" identity.

#### HTTP Request 
`***GET*** /calendar/{toIdentity}/list` 

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
# PRODUCT-API

**Version:** v1 

## /PRODUCTS
### ***POST*** 

**Description:** Create a new product

#### HTTP Request 
`***POST*** /products` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

### ***GET*** 

**Description:** Lists all available products.

#### HTTP Request 
`***GET*** /products` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /PRODUCTS/{PRODUCT_CODE}
### ***GET*** 

**Description:** Reads a single product by product code

#### HTTP Request 
`***GET*** /products/{product_code}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### ***PUT*** 

**Description:** Update a product by product code

#### HTTP Request 
`***PUT*** /products/{product_code}` 

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

### ***DELETE*** 

**Description:** Delete a product by product code

#### HTTP Request 
`***DELETE*** /products/{product_code}` 

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
