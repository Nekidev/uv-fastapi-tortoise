import scripts


def main():
    scripts.run(
        "tortoise migrate",
    )
    scripts.run(
        "uvicorn naoka:app --host ${PROJECT_BIND_HOST:-0.0.0.0} --port ${PROJECT_BIND_PORT:-8000} --workers ${PROJECT_WORKERS:-$(getconf _NPROCESSORS_ONLN)}"
    )
