FROM git.moan.dev/docker/python/with-uv:3.14-alpine

# Only copy uv-related files, necessary for syncing and caching.
WORKDIR /app
COPY pyproject.toml uv.lock /app/

# Run with --no-dev on not to install dev dependencies.
RUN python3 -m uv sync --no-dev

# Copy the rest of your app.
COPY . /app/

ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "cd /app && uv run run:release" ]
