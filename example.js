

retext()
  .use(keywords)
  .process(vfile.readSync('example.txt'), done)

function done(err, file) {
  if (err) throw err

  console.log('Keywords:')
  file.data.keywords.forEach(function(keyword) {
    console.log(toString(keyword.matches[0].node))
  })

  console.log()
  console.log('Key-phrases:')
  file.data.keyphrases.forEach(function(phrase) {
    console.log(phrase.matches[0].nodes.map(stringify).join(''))
    function stringify(value) {
      return toString(value)
    }
  })
}