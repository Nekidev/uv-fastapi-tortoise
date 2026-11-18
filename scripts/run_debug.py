import scripts


def main():
    scripts.run(
        'uvicorn project:app --reload --reload-include "docs/**/*.md" --reload-include .env',
    )
