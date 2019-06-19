```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/identities/v1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"context": "https://standards.oftrust.net/contexts/identity-building.jsonld",
	"type": "Building",
  "name": "Platform of Trust HQ",
  "data": {
        "description": "Platform of Trust headquarters in Tampere."
  }
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
    "@context": "https://standards.oftrust.net/contexts/identity-building.jsonld",
    "@id": "83518d92-5147-4204-8b6b-b728b4a31f53",
    "@type": "Building",
    "createdAt": "2019-06-19T04:19:09+00:00",
    "createdBy": "3b3eeffb-b660-4def-b5a8-ae4828f2526a",
    "data": {
        "description": "Platform of Trust headquarters in Tampere."
    },
    "inLinks": [],
    "name": "Platform of Trust HQ",
    "outLinks": [],
    "status": 0,
    "updatedAt": "2019-06-19T04:19:09+00:00",
    "updatedBy": null
}

```
