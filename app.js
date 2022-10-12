const express = require('express')
const app = express()
const spawn = require("child_process").spawn;
//const pythonEmailExtractProcess = spawn('python',["C:\\Users\\user\\Desktop\\CDRFinal\\EmailReciver.py", arg1, arg2]);

const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
  
  const pythonEmailExtractProcess = spawn('python',["C:\\Users\\user\\Desktop\\CDRFinal\\EmailReciver.py"]);
  pythonEmailExtractProcess.stdout.on('data', (data) => {

    console.log()
  });

})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})


 