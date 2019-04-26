```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendars/v1/34fe0b13-e031-4ef2-822e-17eabad63259/list \
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
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
      "@type": "Event",
      "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
      "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "title": "Autumn feast",
      "startDate": "2019-08-10T14:00:00+00:00",
      "endDate": "2019-08-10T18:00:00+00:00",
      "repeats": null,
      "content": "Autumn feast stuff to do",
      "location": "Courtyard",
      "cc": [
        "34fe0b13-e031-4ef2-822e-17eabad63259"
      ],
      "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "updatedBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "createdAt": "2019-03-14T14:02:29+00:00",
      "updatedAt": "2019-03-14T14:02:29+00:00"
    }
  ]
}


```
