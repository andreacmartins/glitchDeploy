const express = require('express')
const path = require('path')
const app = express()
const port = 3000

// Serve static files in the root dir. THIS IS A MIDDLEWARE!
// html files
app.use('/html', express.static(path.join(__dirname, '../public/html')));
// image files. Any HTTP request with a path starting with /images will be redirected to ../public/images relative to index.js.
app.use('/images', express.static(path.join(__dirname, '../public/images')));


// OBS: this would be a global middleware (I THINK)
// app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
  // Send the index
  res.sendFile(path.join(__dirname, '../public/html', 'index.html'))
});

app.listen(port, () => {
  console.log(`Example app listening on port 127.0.0.1:${port}`)
})