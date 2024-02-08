//import { createClient, print } from 'redis';
const redis = require('redis')
const util = require('util')

const client = redis.createClient()

client.on('connect', ()=>{
  console.log('Redis client connected to the server')
})

client.on('error', (e)=>{
  console.log(`Redis client not connected to the server: ${e}`)
})

function setNewSchool(schoolName, value){
  client.set(schoolName, value, redis.print)
}

async function displaySchoolValue(schoolName){
  const get = util.promisify(client.get).bind(client)
  const val = await get(schoolName)
  console.log(val)
}

async function jj(){
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
jj()
