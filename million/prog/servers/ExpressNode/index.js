const express = require('express')
const crypto  = require('crypto')

const app = express()
const PORT = 8080

app.get("/", (req, res) => {
  const buf = crypto.randomBytes(100)

  const hash = crypto.createHash('sha256').update(buf).digest('hex')

  res.send(hash)
})

app.listen(PORT, () => {
  console.log("Listening on " + PORT.toString())
})
