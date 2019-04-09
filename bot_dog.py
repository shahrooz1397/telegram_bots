from telegram.ext import Updater, CommandHandler
import requests
import re 
#from boto.s3.connection import S3Connection
#import os


#token = S3Connection(os.environ['API_TOKEN'])

def help_(update, context):
    h = '''
        hello {} 
        commands list:
        /bop to generate new image
        /help to show this text
    '''.format(update.message.from_user['first_name'])
    context.bot.send_message(chat_id=update.message.chat_id, text=h)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json() 
    url = contents['url']
    return url 

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id 
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
   updater = Updater('764368386:AAHfzXHnhFRKeWTWfo6-WR31N6ivY9ZkwpI', use_context=True)
   db = updater.dispatcher
   db.add_handler(CommandHandler('bop', bop))
   db.add_handler(CommandHandler('help', help_))
   updater.start_polling()
   updater.idle()


if __name__=='__main__':
    main()
    
