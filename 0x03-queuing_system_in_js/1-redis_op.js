import { createClient, print } from 'redis';

const client = createClient()

client.on('connect', ()=>{
  console.log('Redis client connected to the server')
})

client.on('error', (e)=>{
  console.log(`Redis client not connected to the server: ${e}`)
})

function setNewSchool(schoolName, value){
  client.set(schoolName, value, print)
}

function displaySchoolValue(schoolName){
  //let res = client.get(schoolName)
  //console.log(res)
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
