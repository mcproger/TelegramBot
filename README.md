# Telegram Bot #

## In this project I created Telegram Bot, which gives the user latest news about Python programming language from publics and communities from vk.com  ##
This Bot takes information from vk.com used API VK. You can familiarize with it [here](https://vk.com/dev). Before start the work, you should create your Application [here](https://vk.com/editapp?act=create), get your application's ID. This data will allow you be autorized and work with API VK Methods. Also it uses module VK to facilitate work with API requests 

# Groups about Python  #

In this part we will log in in VK using #####getpass.getpass()##### to enter our data. You should run this file from console, enter you application ID, VK login and password. This script will create file in your project's directory. Using API methods this script will check VK publics by keyword "Python" and find news which contain this keyword. ID of suitable groups will dump in json-file

### Example of token ###
1ebe2aa78b39fafdbbf3f9e6833a99e7

# 2. your_DataBase #

This programm allow you to download information about 1000 films and create DataBase. You should to enter your api key v3 and path to place, where you want to save your DataBase.

# 3. movie_by_key_word #

This program can find in your DataBase film by key word. You should point place which contains your DataBase, enter key word and program will show your all films which title contains this word. 

 **Example:**  
 **Enter path to your movie list:**  
 movie_list.txt  
 **Enter key word:**   
 Saw   
 **Saw**  
 **Saw III**  
 **Saw II**  
 **Saw IV**  
    
# 4. search_for_recommendation #

This programm can recommend which film can interest you, after you enter title some film. Also you should point place which contains your DataBase.
 **Example:**  
 **Enter path to your movie list:**  
 movie_list.txt  
 **Enter  word:**  
  Saw II  
 **Recomend films:**    
 **Four Rooms**  
 **Absolute Power**  
 **Las Hurdes**  
 **The Lord of the Rings**  
 **48 Hrs.**  
 **Lost in Translation**  
 **The Interpreter**  
 **Star Trek: Generations**  
 **......................**  
