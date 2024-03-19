import { Hono } from 'hono'
import * as crypto from 'crypto';

const app = new Hono()

app.get('/', (c) => {
  const buf = crypto.randomBytes(100)
  const hash = crypto.createHash('sha256').update(buf).digest('hex')
  c.status(200)
  return c.text(hash)
})

const port = process.env.PORT || 8080
console.log("Running on", port)

Bun.serve({
  port: port,
  fetch: app.fetch
})
