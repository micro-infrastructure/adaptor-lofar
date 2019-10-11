# LOFAR

### `lta2hpc`
The `src` object can specify either `paths` (SURLs) or `id` (observation ID).

```json
{
    "cmd": {
        "src": {
            "paths": ["<surl>", "..."],
	    "id": <id>
        }, 
        "dest": {
            "host": "<host>",
            "path": "<path>",
        },
        "credentials": {
            "lofarUsername": "<user>",
            "lofarPassword": "<password",
            "srmCertificate": "<certificate>",
            "hpcUsername": "<user>",
            "hpcPassword": "<password>"
        }
    }, 
    "webhook": {
        "method": "POST",
        "url": "<url>",
        "headers": {}
    },
    "options": {}
}
```
