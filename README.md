# Overview

Use Django REST Framework to create an API, then “containerize” it with Docker

### Notes 
You’ll need to run a command to convert pyproject.toml dependencies to requirements.txt

```
poetry export -f requirements.txt -o requirements.txt
```