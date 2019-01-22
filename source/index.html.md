--- 

title: Platform Of Trust APIs 

language_tabs: 
   - shell 
   - java
   - python
   - javascript

toc_footers: 
   - <a href='#'>Sign Up for a Developer Key</a> 
   - <a href='https://github.com/lavkumarv'>Documentation Powered by lav</a> 

includes: 
   - errors 
   - feedback

search: true 

--- 

# Platform of Trust APIs

This could be rather static introduction to Platform of Trust APIs and written in separate file. Then just preprocess the files and merge all, or do it 
manually. Nope! Includes go all to bottom. 

# Authentication

Again this could be external file which is just injected to final markup file....not, see above

# Examples use sandbox environment

<aside class="notice">
All the documentation code examples use our sandbox environment. When you are done with testing, you should switch to production environment. Easiest way is to store API root url in variable and when needed, change it there. Thus the code examples contain API-root variable as an exmaple. 
</aside>

# Translator API 

**Version:** v1 

API Description should come from the code as well...

## /HEALTH

Jotain kuvausta.

```java
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.delete(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://sandbox.oftrust.net/api/translator/health"
  -X GET
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.delete(2);
```

### ***GET*** 


> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

**Description:** Health check endpoint

### HTTP Request 
`***GET*** /health` 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /FETCH
### ***POST*** 

```java
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.delete(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://example.com/api/kittens/2"
  -X DELETE
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.delete(2);
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

**Description:** Get the data for the translator

### HTTP Request 
`***POST*** /fetch` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| X-PoT-Signature | header | A HMAC-SHA256 generated signature of the payload. E.g. HMAC-SHA256(sharedSecret, body)  | Yes | string |
| X-PoT-Token | header | The user's OAuth token | No | string |
| X-PoT-App | header | App name (App ID) | No | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 422 |  |



# Login API 

# Context API 

# Data Broker API 

# Product API 

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
