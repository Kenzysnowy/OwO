<h1 align="center">🐮 OwO Farm by Phandat 🐮</h1>
<p align="center">

<a href="https://github.com/phandat1405/OwO"><img src="https://hits.sh/github.com/phandat1405/OwO.svg?view=today-total&label=Repo%20Today/Total%20Views&color=770ca1&labelColor=007ec6"/></a>
<a href="https://github.com/phandat1405/OwO"><img src="https://img.shields.io/github/last-commit/phandat1405/OwO" /></a><br>
</p>

[⭐・Star History](#star-history)<br>
[🔮・Features](#features)<br>
[⚙・Config.json](#configjson)<br>
[📡・Usage](#usage)<br>
[🎯・Demo](#demo)<br>

## ⭐・Star History
<h2 align="center">Goal: <a href="https://github.com/phandat1405/OwO/stargazers"><img src="https://img.shields.io/github/stars/phandat1405/OwO" /></a> / 1000</h2>

[![Star History Chart](https://api.star-history.com/svg?repos=phandat1405/OwO&type=Date)](https://star-history.com/#phandat1405/OwO&Date)

## 🔮・Features

-   Auto Grind
    -   Auto Hunt
    -   Auto Battle
    -   Auto Say OwO
-   Auto Gamble
    -   Auto Coinflip
    -   Auto Slot
    -   Custom Bet
    -   Multiply When Lose
-   Captcha Protection
    -   Stop When Captcha Appears
    -   Play Music When Captcha Appears
    -   Notify Via Webhook When Captcha Appears

## ⚙・config.json
```
{
  "token": "", your token
  "channel": "", channel id
  "grind": "", true or false
  "coinflip": "", true or false
  "cfbet": "", the coinflip bet you want to start
  "cfrate": "", the coinflip rate you want to multiply
  "slot": "", true or false
  "sbet": "", the slot bet you want to start
  "srate": "", the slot rate you want to multiply
  "webhook": "", the webhook you want to be notified captcha
  "ping": "", the id user you want to be notified captcha
}
```

## 📡・Usage
### Pc or Laptop 💻
Download and install [Python](https://www.python.org/downloads)

Go to cmd file and type:
```
pip install -r requirements.txt
```
Edit `config.json` or type:
```
python setting.py
```
Start `run.cmd` or type:
```
python main.py
```

### Termux
Download and install [Termux](https://f-droid.org/packages/com.termux)
Open termux app and type:

```
pkg update
pkg upgrade
pkg install git
pkg install python
```
```
git clone https://github.com/phandat1405/OwO.git
cd OwO
pip install -r requirements.txt
```
```
python setting.py
```
```
python main.py
```

## 🎯・Demo
![Preview](https://media.discordapp.net/attachments/1155833237025869876/1180791532165546065/image.png?ex=657eb4cf&is=656c3fcf&hm=b13f263c6947161d214bdf69658604321ade752415641c462346c66e0c0f1013&=&format=webp&quality=lossless)
