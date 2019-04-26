```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
	"title": "Autumn feast 3",
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
  "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
  "@type": "Event",
  "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "title": "Autumn feast 2",
  "startDate": "2019-08-10T15:00:00+00:00",
  "endDate": "2019-08-10T18:00:00+00:00",
  "repeats": null,
  "content": "Autumn feast",
  "location": "Courtyard",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T14:02:29+00:00",
  "updatedAt": "2019-03-14T14:02:29+00:00"
}

```
