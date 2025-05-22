## Docker commands for environment testing

### Test

```bash
podman build . -t localhost/polycloud2025-custom-webapp-color
podman run -p 8080:8080 -e APP_COLOR=green -e ENV_JGALAIS=test localhost/polycloud2025-custom-webapp-color
```

### Build and Push

```bash
podman login docker.io
podman build . -t genesysao/polycloud2025-custom-webapp-color:1.0
podman push genesysao/polycloud2025-custom-webapp-color:1.0
```
