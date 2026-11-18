import asyncio

import subprocess

from project.db import lifespan


def run(cmd: str):
    subprocess.run(["/bin/sh", "-c", cmd], check=False)


def main(func):
    def inner():
        loop = asyncio.new_event_loop()

        loop.run_until_complete(lifespan.on_startup())
        try:
            loop.run_until_complete(func())
        finally:
            loop.run_until_complete(lifespan.on_shutdown())

    return inner
