--- 

title: Platform Of Trust Documentation 

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

# Products API

**Version:** v1 

API Description should come from the code as well...

## /HEALTH

Jotain kuvausta.


```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://sandbox.oftrust.net/api/products"
  -X GET
  -H "Authorization: meowmeowmeow"
```


### ***GET*** 


> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

**Description:** Get all products 

### HTTP Request 
`***GET*** /products` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

### ***POST*** 


```shell
# Notice the sandbox URL, change to production when needed. 
curl "http://sandbox.oftrust.net/api/translator/products" \
  -X POST \
  -H "X-PoT-Signature: xxx" \
  -H "X-PoT-Token: meowmeowmeow" \
  -H "X-PoT-App: xxx" 
```


> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "product" : ":("
}
```


# Context API 



<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
