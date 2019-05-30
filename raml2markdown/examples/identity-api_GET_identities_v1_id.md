```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
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
  "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
  "@type": "Person",
  "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "name": "John Doe",
  "data": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "createdBy": "4c276e02-719c-4415-abba-a7afc4edc0c0",
  "updatedBy": null,
  "createdAt": "2019-03-14T10:50:51+00:00",
  "updatedAt": "2019-03-14T10:50:51+00:00",
  "status": 0,
  "inLinks": [],
  "outLinks": []
}

```
