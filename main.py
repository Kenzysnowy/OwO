#!/usr/bin/python
from colorama import init
init()
import time
from time import sleep, strftime, localtime, time
import random
import atexit
from os import  system, startfile
from tabulate import tabulate
import discum
from discord_webhook import DiscordWebhook
from data import data
client = data()

#Status
if client.grind:
	client.grind_status = '✅'
if client.coinflip or client.slot:
	client.benefit_status = '✅'

#Time
def at() -> str:
	return f'\033[104m{strftime("%H:%M:%S", localtime())}\033[0m'

#Intro
system('cls')
print("{}█▀█ █ █ ▄▀█ █▄ █ █▀▄ ▄▀█ ▀█▀".format(client.color.blue, client.color.reset))
print("{}█▀▀ █▀█ █▀█ █ ▀█ █▄▀ █▀█  █".format(client.color.blue, client.color.reset))

#Log In
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
	if resp.event.ready_supplemental:
		user = bot.gateway.session.user
		print("{}Logged in as{} {}".format(client.color.red, client.color.reset, user['username']))

#Webhook
def webhook(message: str) -> None:
	webhook = DiscordWebhook(url = client.link, content=message)
	webhook = webhook.execute()

#Captcha Bypass
@bot.gateway.command
def check(resp):
	if resp.event.message:
		m = resp.parsed.auto()
		if m['channel_id'] == client.channel:
			if m['author']['id'] == client.OwOID:
				if '⚠' in m['content']:
					client.stopped = True
				if '(1/5)' in m['content']:
					client.stopped = True
				if '(2/5)' in m['content']:
					client.stopped = True
				if '(3/5)' in m['content']:
					client.stopped = True
				if '(4/5)' in m['content']:
					client.stopped = True
				if '(5/5)' in m['content']:
					client.stopped = True
				if 'https://owobot.com/captcha' in m['content']:
					client.stopped = True	
				if 'don\'t have enough cowoncy!' in m['content']:
					client.stopped = True

#Coinflip Check
@bot.gateway.command
def cfcheck(resp):
	if not client.stopped and client.coinflip:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channel:
					if m['author']['id'] == client.OwOID:
							if 'you lost' in m['content']:
								print("{} {}[INFO] Coinflip Lost {} Cowoncy{}".format(at(), client.color.red, client.current_cfbet, client.color.reset))
								client.benefit_amount -= client.current_cfbet
								client.current_cfbet *= client.cfrate
							if 'you won' in m['content']:
								print("{} {}[INFO] Coinflip Won {} Cowoncy{}".format(at(), client.color.green, client.current_cfbet, client.color.reset))
								client.benefit_amount += client.current_cfbet
								client.current_cfbet = client.cfbet
			except KeyError:
				pass

#Slot Check
@bot.gateway.command
def scheck(resp):
	if not client.stopped and client.slot:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channel:
					if m['author']['id'] == client.OwOID:
							if 'won nothing' in m['content']:
								print("{} {}[INFO] Slot Lost {} Cowoncy{}".format(at(), client.color.red, client.current_sbet, client.color.reset))
								client.benefit_amount -= client.current_sbet
								client.current_sbet *= client.srate
							if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
								print("{} {}[INFO] Slot Draw{}".format(at(), client.color.bold, client.color.reset))
							if '<:heart:417475705899712522> <:heart:417475705899712522> <:heart:417475705899712522>' in m['content']:
								print("{} {}[INFO] Slot Won {} Cowoncy (x2){}".format(at(), client.color.green, client.current_sbet, client.color.reset))
								client.benefit_amount += client.current_sbet
								client.current_sbet = client.sbet
							if '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
								print("{} {}[INFO] Slot Won {} Cowoncy (x3){}".format(at(), client.color.green, client.current_sbet * 2, client.color.reset))
								client.benefit_amount += client.current_sbet * 2
								client.current_sbet = client.sbet
							if '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:
								print("{} {}[INFO] Slot Won {} Cowoncy (x4){}".format(at(), client.color.green, client.current_sbet * 3, client.color.reset))
								client.benefit_amount += client.current_sbet * 3
								client.current_sbet = client.sbet
							if '<:o_:417475705899843604> <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:
								print("{} {}[INFO] Slot Won {} Cowoncy (x10){}".format(at(), client.color.green, client.current_sbet * 9, client.color.reset))
								client.benefit_amount += client.current_sbet * 9
								client.current_sbet = client.sbet
			except KeyError:
				pass

#Grind
def grind():
	if not client.stopped and client.grind:
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owo")
		print("{} {}[SENT] owo{}".format(at(), client.color.yellow, client.color.reset))
		sleep(random.randint(1, 2))
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owoh")
		print("{} {}[SENT] owoh{}".format(at(), client.color.yellow, client.color.reset))
		sleep(random.randint(1, 2))
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owob")
		print("{} {}[SENT] owob{}".format(at(), client.color.yellow, client.color.reset))
		client.grind_amount += 1
		
#Coinflip
def coinflip():
	if client.current_cfbet  > 250000:
		client.current_cfbet = client.cfbet
	if not client.stopped and client.coinflip:
		choice = random.choice(client.side)
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owo cf {} {}".format(client.current_cfbet, choice))
		print("{} {}[SENT] owo cf {} {}{}".format(at(), client.color.yellow, client.current_cfbet, choice, client.color.reset))
		sleep(random.randint(1, 2))

#Slot
def slot():
	if client.current_sbet  > 250000:
		client.current_sbet = client.sbet
	if not client.stopped and client.slot:
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owo s {}".format(client.current_sbet))
		print("{} {}[SENT] owo s {}{}".format(at(), client.color.yellow,client.current_sbet, client.color.reset))
		sleep(random.randint(1, 2))

#Run
@bot.gateway.command
def run(resp):
	if resp.event.ready:
		while not client.stopped and resp.event.ready:
				grind()
				sleep(random.randint(3, 5))
				coinflip()
				slot()
				sleep(random.randint(10, 15))
	if client.stopped:
		bot.gateway.close()
bot.gateway.run(auto_reconnect=True)

#Exit
@atexit.register
def exit():
	startfile('music.mp3')
	client.stopped = True
	stat = [['🐮', 'AMOUNT','STATUS'],
	['🎯', (client.grind_amount), (client.grind_status)],
	['💵', (client.benefit_amount), (client.benefit_status)],]
	print("{}█▀▀ ▄▀█ █▀█ ▀█▀ █▀▀ █ █ ▄▀█{}".format(client.color.red, client.color.reset))
	print("{}█▄▄ █▀█ █▀▀  █  █▄▄ █▀█ █▀█{}".format(client.color.red, client.color.reset))
	print()
	print(tabulate(stat, headers="firstrow", tablefmt="simple"))
	print()
	if client.webhook == True:
		webhook(f"**<a:Bar:1065047410809770014> chà có sự cố ở <#{client.channel}> <@{client.ping}> kìa <a:PepeHack:1065047722199089222>**")
		webhook(f"**<a:Bar:1065047410809770014> chà có sự cố ở <#{client.channel}> <@{client.ping}> kìa <a:PepeHack:1065047722199089222>**")
		webhook(f"**<a:Bar:1065047410809770014> chà có sự cố ở <#{client.channel}> <@{client.ping}> kìa <a:PepeHack:1065047722199089222>**")
	input("{}Enter 3 Times to Restart{}".format(client.color.blue, client.color.reset))
	input("{}Enter 2 Times to Restart{}".format(client.color.blue, client.color.reset))
	input("{}Enter 1 Times to Restart{}".format(client.color.blue, client.color.reset))
	system('python "main.py"')
