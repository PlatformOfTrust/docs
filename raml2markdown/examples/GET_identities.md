```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identity/v1/identities \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
      "@type": "Person",
      "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
      "name": "John Doe",
      "data": {
        "firstName": "John",
        "lastName": "Doe",
        "gender": "Male"
      },
      "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "updatedBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "createdAt": "2019-03-14T10:50:51+00:00",
      "updatedAt": "2019-03-14T11:17:35+00:00",
      "status": 0,
      "inLinks": [],
      "outLinks": []
    },
    ...
  ]
}}

```
