from pyrogram import Client
import os 


app = Client('my_account')
app.start()

print(app.get_me())

app.send_message('me', 'hi there, im using pyrogram!')

app.stop()
