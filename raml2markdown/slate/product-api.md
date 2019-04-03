--- 

title: Platform Of Trust Product API 

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

The Product API provides means to manage products provided by PoT core.
The product defines the URL to the translator, as well as a product code to
use when requesting data from the translator.
 

**Version:** v1 

# /
## ***POST*** 

**Description:** Create a new product

### HTTP Request 
`***POST*** /` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header |  | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## ***GET*** 

**Description:** Lists all available products. *NOTE*: This is a CORS enabled endpoint.


### HTTP Request 
`***GET*** /` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

# /{PRODUCT_CODE}
## ***GET*** 

**Description:** Reads a single product by product code. *NOTE*: This is a CORS enabled endpoint.


### HTTP Request 
`***GET*** /{product_code}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## ***PUT*** 

**Description:** Update a product by product code

### HTTP Request 
`***PUT*** /{product_code}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| Authorization | header |  | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

## ***DELETE*** 

**Description:** Delete a product by product code

### HTTP Request 
`***DELETE*** /{product_code}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| Authorization | header |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
