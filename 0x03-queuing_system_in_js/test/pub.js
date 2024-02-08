const redis = require('redis')
const client = redis.createClient()
const prompt = require("prompt-sync")({ sigint: true });
function main(){
	client.on('connect', ()=>{
	  console.log('Redis client connected to the server')
	})

	client.on('error', (e)=>{
	  console.log(`Redis client not connected to the server: ${e}`)
	})
}




function inter(){
	while (true){
		res = prompt('Info: ')
		client.PUBLISH('channel1', res);
	}
}
main()
