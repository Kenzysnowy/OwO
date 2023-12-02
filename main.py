#!/usr/bin/python
from colorama import init
init()
import time
import random
import atexit
from os import  system, startfile
from time import sleep
from tabulate import tabulate
import discum
from discord_webhook import DiscordWebhook
from data import data
client = data()

if client.grind:
	client.grind_status = '✅'
if client.coinflip or client.slot:
	client.benefit_status = '✅'

system('cls')
print("{}█▀█ █ █ ▄▀█ █▄ █ █▀▄ ▄▀█ ▀█▀".format(client.color.blue, client.color.reset))
print("{}█▀▀ █▀█ █▀█ █ ▀█ █▄▀ █▀█  █".format(client.color.blue, client.color.reset))

#logged
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
	if resp.event.ready_supplemental:
		user = bot.gateway.session.user
		print("{}Logged in as{} {}".format(client.color.red, client.color.reset, user['username']))

#time
def at():
	return f'\033[104m{time.strftime("%H:%M:%S", time.localtime())}\033[0m'

#webhook
def webhookPing(message: str) -> None:
	if client.webhook:
		webhook = DiscordWebhook(url = client.webhook, content=message)
		webhook = webhook.execute()

#captcha bypass
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

#coinflip check
@bot.gateway.command
def cfcheck(resp):
	if not client.stopped and client.coinflip:
		if resp.event.message_updated:
			m = resp.parsed.auto()
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

#slot check
@bot.gateway.command
def scheck(resp):
	if not client.stopped and client.slot:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channel:
				if m['author']['id'] == client.OwOID:
						if 'won nothing' in m['content']:
							print("{} {}[INFO] Slot Lost {} Cowoncy{}".format(at(), client.color.red, client.current_sbet, client.color.reset))
							client.benefit_amount -= client.current_sbet
							client.current_sbet *= client.srate
						if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
							print("{} {}[INFO] Slot Draw{}".format(at(), client.color.bold, client.color.reset))
						if '<:heart:417475705899712522> <:heart:417475705899712522> <:heart:417475705899712522>' in m['content']:
							print("{} {}[INFO] Slot Won {} Cowoncy{}".format(at(), client.color.green, client.current_sbet, client.color.reset))
							client.benefit_amount += client.current_sbet
							client.current_sbet = client.sbet
						if '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
							print("{} {}[INFO] Slot Won {} Cowoncy{}".format(at(), client.color.green, client.current_sbet * 2, client.color.reset))
							client.benefit_amount += client.current_sbet * 2
							client.current_sbet = client.sbet
						if '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:
							print("{} {}[INFO] Slot Won {} Cowoncy{}".format(at(), client.color.green, client.current_sbet * 3, client.color.reset))
							client.benefit_amount += client.current_sbet * 3
							client.current_sbet = client.sbet
						if '<:o_:417475705899843604> <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:
							print("{} {}[INFO] Slot Won {} Cowoncy{}".format(at(), client.color.green, client.current_sbet * 9, client.color.reset))
							client.benefit_amount += client.current_sbet * 9
							client.current_sbet = client.sbet

#grind
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
		
#coinflip
def cf():
	if client.current_cfbet  > 250000:
		client.current_cfbet = client.cfbet
	if not client.stopped and client.coinflip:
		choice = random.choice(client.side)
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owo cf {} {}".format(client.current_cfbet, choice))
		print("{} {}[SENT] owo cf {} {}{}".format(at(), client.color.yellow, client.current_cfbet, choice, client.color.reset))
		sleep(random.randint(1, 2))

#slot
def s():
	if client.current_sbet  > 250000:
		client.current_sbet = client.sbet
	if not client.stopped and client.slot:
		bot.typingAction(client.channel)
		bot.sendMessage(str(client.channel), "owo s {}".format(client.current_sbet))
		print("{} {}[SENT] owo s {}{}".format(at(), client.color.yellow,client.current_sbet,client.color.reset))
		sleep(random.randint(1, 2))

#run
@bot.gateway.command
def loop(resp):
	if resp.event.ready:
		while True:
			if client.stopped:
				bot.gateway.close()
			if not client.stopped:
				grind()
				sleep(random.randint(3, 5))
				cf()
				s()
				sleep(random.randint(10, 15))
bot.gateway.run()

#exit
@atexit.register
def exit():
	startfile('music.mp3')
	client.stopped = True
	stat = [['🐮', 'AMOUNT','STATUS'],
	['🎯', (client.grind_amount), (client.grind_status)],
	['💵', (client.benefit_amount), (client.benefit_status)],]
	webhookPing(f"**<a:Bar:1065047410809770014> chà có sự cố ở <#{client.channel}> <@{client.ping}> kìa <a:PepeHack:1065047722199089222>**")
	print("{}█▀▀ ▄▀█ █▀█ ▀█▀ █▀▀ █ █ ▄▀█{}".format(client.color.red, client.color.reset))
	print("{}█▄▄ █▀█ █▀▀  █  █▄▄ █▀█ █▀█{}".format(client.color.red, client.color.reset))
	print()
	print(tabulate(stat, headers="firstrow", tablefmt="simple"))
	print('{}{}'.format(at(), client.color.reset))
	input("{}Enter 3 Times to Restart{}".format(client.color.blue, client.color.reset))
	input("{}Enter 2 Times to Restart{}".format(client.color.blue, client.color.reset))
	input("{}Enter 1 Times to Restart{}".format(client.color.blue, client.color.reset))
	system('python "main.py"')