from json import load, dump
from data import data
from os import  system
client = data()

#[1] Token
#[2] Channel
#[3] Grind
#[4] Coinflip
#[5] Coinflip Bet
#[6] Coinflip Rate
#[7] Slot
#[8] Slot bet
#[9] Slot Rate
#[10] Webhook
#[11] Ping

#Settings
def main():
	with open("config.json", "r") as f:
		data = load(f)
		system('cls')
	print("""{}█▀▄ ▄▀█ ▀█▀ ▄▀█
█▄▀ █▀█  █  █▀█{}
{}[1] Token
[2] Channel
[3] Grind
[4] Coinflip
[5] Coinflip Bet
[6] Coinflip Rate
[7] Slot
[8] Slot bet
[9] Slot Rate
[10] Webhook
[11] Ping{}""".format(client.color.blue, client.color.reset, client.color.purple, client.color.reset))
	choice = input("{}Enter Your Choice: {}".format(client.color.yellow, client.color.reset))
	if choice == "0":
		pass
	elif choice == "1":
		token(data, False)
	elif choice == "2":
		channel(data, False)
	elif choice == "3":
		grind(data, False)
	elif choice == "4":
		coinflip(data, False)
	elif choice == "5":
		cfbet(data, False)
	elif choice == "6":
		cfrate(data, False)
	elif choice == "7":
		slot(data, False)
	elif choice == "8":
		sbet(data, False)
	elif choice == "9":
		srate(data, False)
	elif choice == "10":
		webhook(data, False)
	elif choice == "11":
		ping(data, False)
	else:
		print("{}[INFO] Invalid!{}".format(client.color.red, client.color.reset))

#Token
def token(data, all):
	data['token'] = input("{}Enter Account Token: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Channel
def channel(data, all):
	data['channel'] = input("{}Enter Channel ID: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Grind
def grind(data, all):
	data['grind'] = input("{}Toggle Grinding (YES/NO): {}".format(client.color.blue, client.color.reset))
	data['grind'] = data['grind'].lower() == "yes"
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Coinflip
def coinflip(data, all):
	data['coinflip'] = input("{}Toggle Coinflip (YES/NO): {}".format(client.color.blue, client.color.reset))
	data['coinflip'] = data['coinflip'].lower() == "yes"
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Coinflip Bet
def cfbet(data, all):
	data['cfbet'] = input("{}Enter Coinflip Bet: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Coinflip Rate
def cfrate(data, all):
	data['cfrate'] = input("{}Enter Coinflip Rate: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Slot
def slot(data, all):
	data['slot'] = input("{}Toggle Slot (YES/NO): {}".format(client.color.blue, client.color.reset))
	data['slot'] = data['slot'].lower() == "yes"
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Slot Bet
def sbet(data, all):
	data['sbet'] = input("{}Enter Slot Bet: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Slot Rate
def srate(data, all):
	data['srate'] = input("{}Enter Slot Rate: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Webhook
def webhook(data, all):
	data['webhook'] = input("{}Enter Webhook Link: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

#Ping
def ping(data, all):
	data['ping'] = input("{}Enter Ping ID: {}".format(client.color.blue, client.color.reset))
	file = open("config.json", "w")
	dump(data, file, indent = 4)
	file.close()
	print("{}[INFO] Saved!{}".format(client.color.green, client.color.reset))
	if not all:
		main()

if __name__ == "__main__":
	main()
