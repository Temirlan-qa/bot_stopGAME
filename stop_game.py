import requests
from bs4 import BeautifulSoup
import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,'+str(message.from_user.first_name)+".У нас есть /start и /top30")
@bot.message_handler(commands=['top30'])
def parse(message):
	URL="https://stopgame.ru/topgames"
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	}
	response = requests.get(URL,headers=headers)
	soup=BeautifulSoup(response.content,'html.parser')
	items=soup.findAll('div',class_='item game-summary game-summary-horiz')
	comps=[]
	z=0
	for item in items:
		comps.append({
			"title": item.find('div',class_="caption caption-bold").get_text(strip=True),
			"totall": item.find('div',class_="score").get_text(strip=True)
		})
	global comp
	for comp in comps:
		z+=1
		bot.send_message(message.chat.id,str(z)+')'+comp["title"]+' '+comp["totall"])
#битти
bot.polling()