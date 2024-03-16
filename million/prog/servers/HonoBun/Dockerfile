FROM oven/bun:1.0.5-alpine

COPY . /app
WORKDIR /app
RUN bun install --frozen-lockfile --production

EXPOSE 8080
ENTRYPOINT [ "bun", "run", "src/index.ts" ]
