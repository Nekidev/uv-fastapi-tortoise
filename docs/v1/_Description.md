To run the project with live reload including the documentation, run uvicorn with the following
parameters:

```sh
uv run uvicorn project:app --reload --reload-include "docs/**/*.md"
```
