const redis = require('redis')
const client = redis.createClient()

client
  .MULTI()
  .HSET('HolbertonSchools', 'Portland', 50, redis.print)
  .HSET('HolbertonSchools', 'Seattle', 80, redis.print)
  .HSET('HolbertonSchools', 'New York', 20, redis.print)
  .HSET('HolbertonSchools', 'Bogota', 20, redis.print)
  .HSET('HolbertonSchools', 'Cali', 40, redis.print)
  .HSET('HolbertonSchools', 'Paris', 2, redis.print)
  .EXEC();

client.HGETALL('HolbertonSchools', (err, data)=>{
  console.log(data)
})
