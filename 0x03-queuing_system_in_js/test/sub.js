const redis = require('redis')
const client = redis.createClient()

client.on('connect', ()=>{
  console.log('Redis client connected to the server')
})

client.on('error', (e)=>{
  console.log(`Redis client not connected to the server: ${e}`)
})

client.SUBSCRIBE('channel1')

client.on('message', (c, message)=>{
  if (message === 'KILL_SERVER'){
    client.UNSUBSCRIBE();
    client.QUIT()
  }
  console.log(message)
})
