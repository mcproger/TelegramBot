# Telegram Bot #

## In this project I created Telegram Bot, which gives the user latest news about Python programming language from publics and communities from vk.com  ##
This Bot takes information from vk.com used API VK. You can familiarize with it [here](https://vk.com/dev). Before start the work, you should create your Application [here](https://vk.com/editapp?act=create), get your application's ID. This data will allow you be autorized and work with API VK Methods. Also it uses module VK to facilitate work with API requests. To start working with [Telegram](http://web.telegram.org.ru/#/login) API find @BotFather, send him /start, /newbot, write the name of the bot and you will get your access token.

### Example of Telegram token ###

277777666:AAEaF2tUOpBKdQWXZhMV5lYYfvbETdAviMg

# Groups about Python  #

In this part we will log in in VK using **getpass.getpass()** to enter our data. You should run this file from console, enter you application ID, VK login and password. This script will create file in your project's directory. Using API methods this script will check VK publics by keyword "Python" and search news which contain this keyword. ID of suitable groups will dump in json-file

**Using methods**
[Group seacrh](https://vk.com/dev/groups.search)
[News check](https://vk.com/dev/wall.search)


# Python Posts #

Further, using file from first script, we will make some data base with news about Python from VK publics. We will also use, as before VK API Methods, and find tematic news about Python. ID of publics about Python will help us. At the end of this script we will have json-file with news. This script requires authorization in VK, just like in first script. 

**Using methods**
[Search news by ID of public](https://vk.com/dev/wall.search)

# NewsBot #

And finally directly bot. As it was said, you need Telegram token for work with Telegram API. This script using json-file from previous script and take title of news and link. To start working with this bot, you should find it in Telegram's search by the name NewsBot. Press start and command **/python_news** gives you latest news about Python. 
 
 
 
 
 
