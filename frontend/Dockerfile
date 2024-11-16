FROM oven/bun:latest

WORKDIR /app

COPY package.json bun.lockb ./

RUN bun install

COPY . .

EXPOSE 80 

CMD ["bun", "run", "dev"]