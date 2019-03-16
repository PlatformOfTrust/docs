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

# /PRODUCTS
## ***POST*** 

**Description:** Create a new product

### HTTP Request 
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

## ***GET*** 

**Description:** Lists all available products.

### HTTP Request 
`***GET*** /products` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

# /PRODUCTS/{PRODUCT_CODE}
## ***GET*** 

**Description:** Reads a single product by product code

### HTTP Request 
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

## ***PUT*** 

**Description:** Update a product by product code

### HTTP Request 
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

## ***DELETE*** 

**Description:** Delete a product by product code

### HTTP Request 
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
