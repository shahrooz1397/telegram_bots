from pyrogram import Client, Filters
import requests
import re
#import os 


app = Client('7643683h86:AAGCdoJj4C1I8H9c')

def get_url():
    content=requests.get('https://random.dog/woof.json').json()
    url = content['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url



@app.on_message(Filters.command('bop'))
def bop(client, message):
    url = get_image_url()
    print(url)
    message.reply_photo(url)

@app.on_message(~Filters.command(['start', 'help', 'bop']))
def unknown(client, message):
    message.reply('i don`t understand this command ')
    
 
app.run()


