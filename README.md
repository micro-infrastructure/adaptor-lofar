# LOFAR

### `lta2hpc`
```json
{
    "cmd": {
        "src": {
            "paths": [
                "<surl>"
            ]
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