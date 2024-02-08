const kue = require('kue')
const queue = kue.createQueue()

let jobData = {
  phoneNumber: '111111111',
  message: 'Hello, how are you doing',
}

const job = queue.create('push_notification_code', jobData).save((err)=>{
  if (!err){
    console.log(`Notification job created ${job.id}`)
  }
})

job.on('complete', (result)=>{
  console.log('Notification job completed')
})

job.on('failed', (err)=>{
  console.log('Notification job failed')
})
