import json
class data:
	def __init__(self):
		with open('config.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			self.channel = data["channel"]
			self.grind = data["grind"]
			self.coinflip = data["coinflip"]
			self.cfbet = int(data["cfbet"])
			self.cfrate = int(data["cfrate"])
			self.slot = data["slot"]
			self.sbet = int(data["sbet"])
			self.srate = int(data["srate"])
			self.webhook = data["webhook"]
			self.link = data["link"]
			self.ping = data["ping"]
			self.side = ["h","t"]
			self.stopped = False
			self.grind_amount = 0
			self.grind_status = '❌'
			self.benefit_amount = 0
			self.benefit_status = '❌'
			self.current_cfbet = self.cfbet
			self.current_sbet = self.sbet
			self.OwOID = '408785106942164992'
	class color:
		mark = "\033[104m"
		bold = "\033[1m"
		blue = "\033[94m"
		green = "\033[92m"
		yellow = "\033[93m"
		red = "\033[91m"
		purple = "\033[35m"
		reset = "\033[0m"
