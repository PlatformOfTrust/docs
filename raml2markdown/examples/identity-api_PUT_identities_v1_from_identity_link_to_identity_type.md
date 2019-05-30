```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829/link/86201e7d-6784-454b-9839-f7a6286f1791/Link \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"context": "https://standards.oftrust.net/contexts/link-owner.jsonld",
	"type": "Owner",
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
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/link-owner.jsonld",
  "@type": "Owner",
  "@id": "6ca1e7fb-48a7-4e2c-bb4f-98e2b934aa80",
  "from": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "to": "86201e7d-6784-454b-9839-f7a6286f1791",
  "createdBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "updatedBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "createdAt": "2019-04-10T08:27:00+00:00",
  "updatedAt": "2019-05-10T08:27:00+00:00"
}

```
