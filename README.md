<h1 align="center">OwO Farm Bot</h1>

<p align="center">
  
<a href="https://github.com/phandat1405/OwO"><img src="https://hits.sh/github.com/phandat1405/OwO.svg?view=today-total&label=Repo%20Today/Total%20Views&color=770ca1&labelColor=007ec6"/></a>
<a href="https://github.com/phandat1405/OwO"><img src="https://img.shields.io/github/last-commit/phandat1405/OwO" /></a><br>
⭐ Give this repository a star for new feature ⭐
</p>

## ⭐・Star History
<h2 align="center">Goal: <a href="https://github.com/phandat1405/OwO/stargazers"><img src="https://img.shields.io/github/stars/phandat1405/OwO" /></a> / 1000</h2>

[![Star History Chart](https://api.star-history.com/svg?repos=phandat1405/OwO&type=Date)](https://star-history.com/#phandat1405/OwO&Date)

## 👑・Features

-   Auto Farm
    -   Auto Hunt
    -   Auto Battle
    -   Auto Say OwO
-   Auto Pray
-   Auto Gamble
    -   Auto Coinflip
    -   Auto Slot
    -   Custom Bet
    -   Multiply When Lose
-   Captcha(Ban) Protection v0.1.8 (beta)
    -   Stop When Captcha Appears
    -   Play Music When Captcha Appears
    -   Notify Via Webhook When Captcha Appears

## ⚙・config.json example

```
{
    "settings": {
        "huntandbattle": "", true or false
        "banbypass": "", true or false
        "discordrpc": "", true or false
        "pray": "", true or false
        "extratoken": "", true or false
        "autoquest": "", true or false
        "inventory": {
            "inventorycheck": "", true or false
            "gemcheck": "", true or false
            "lootboxcheck": "", true or false
            "fabledlootboxcheck": "", true or false
            "cratecheck": "", true or false
            "eventcheck": "" true or false
        },
        "animals": {
            "enable": "", true or false
            "type": "" sell or sacrifice
            "ifsacrifice": {
                "common": "", true or false
                "uncommon": "", true or false
                "rare": "", true or false
                "epic": "", true or false
                "mythical": "", true or false
                "patreon": "", true or false
                "cpatreon": "", true or false
                "legendary": "", true or false
                "gem": "", true or false
                "bot": "", true or false
                "distorted": "", true or false
                "fabled": "", true or false
                "special": "", true or false
                "hidden": "" true or false
            }
        },
        "upgradeautohunt": {
            "enable": "", true or false
            "type": "" efficiency, duration, cost, gain, exp or radar
        },
        "gamble": {
            "coinflip": {
                "default_amount"= , Enter the amount you want to start from
                "max_amount": 250000, Enter the amount where the bot will not bet more than that
                "multipler": , Enter a number by which the lost amount will be multipled by
                "enable": "", true or false
                "amount": "1"
            },
            "slots": {
                "enable": "", true or false
                "amount": "1"
            }
        }
    },
    "main":{
        "token":"", main token (if you use replit please edit .env file)
        "userid":"", token user id
        "channelid":"", channel id for main token
        "owodmchannelid":"", owo bot dm channel id
        "gamblechannelid":"", channel if for gambling
        "autoquestchannelid":"" auto quest channel id
    },
    "extra":{
        "token":"", extra token (if you use replit please edit .env file)
        "userid":"", extra token user id
        "channelid":"", channel id for extra token
        "gamblechannelid":"", channel if for gambling
        "owodmchannelid":"" extra token owo bot dm channel id
    }
}


```


# Demo
![Preview](https://media.discordapp.net/attachments/1155833237025869876/1180791532165546065/image.png?ex=657eb4cf&is=656c3fcf&hm=b13f263c6947161d214bdf69658604321ade752415641c462346c66e0c0f1013&=&format=webp&quality=lossless)

## Requirement
Laptop or PC: [Python](https://www.python.org/downloads/)

Android

IOS: 

### Termux
pkg update
pkg upgrade
pkg install git
pkg install python
git clone https://github.com/phandat1405/OwO.git
cd OwO
pip install -r requirements.txt
python setting.py
python main.py
