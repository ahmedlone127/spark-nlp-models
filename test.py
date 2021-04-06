from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions	
import pandas as pd
import json
import datetime
import os
folder_name_ = 'covid'
def get_path(directory,extension):
    """Finds all specific type of files in given directory.
        
    Keyword arguments:
    direcotry  -- directory to search file for 
    extension -- what kind of file to search for
    """
    list_of_path = []
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                list_of_path.append(os.path.join(root,file))# join root and file to form a complete path 
    return list_of_path
def json_to_csv(file):
	with open(file, encoding="utf-8") as data_file:    
	    data = json.load(data_file)  
	_=(data["meta"]["userindex"])
	name = []
	for i in range(0,len(_)):
		try :
			name.append(f'{data["meta"]["users"][_[i]]["name"]}#{data["meta"]["users"][_[i]]["tag"]}')
		except:
			pass
	messages = []
	indexes = []
	time = []
	for  channel in data["data"].values():
		for message in channel.values():
			try :
				list_ = [name[message["u"]],message["m"],datetime.datetime.fromtimestamp(message["t"]/1000).strftime('%Y-%m-%d %H:%M:%S.%f')]
				indexes.append(name[message["u"]])
				messages.append(message["m"])
				time.append(datetime.datetime.fromtimestamp(message["t"]/1000).strftime('%Y-%m-%d %H:%M:%S.%f'))
				
			except :
				pass
	data = {"text": messages,
			"author": indexes,
			"sent_at":time}
	df = pd.DataFrame(data)
	df.to_csv(f"{file.replace('txt','csv')}")
def crawl_discord(channel,initial_total_messages, messages_per_loop,amount_of_time_to_wait_per_loop,folder_name,number_of_loops):
	"""Crawls a given discord channel 

	Keyword arguments : 
	Channel -- the channel to crawl(user should be part of the given channel).
	initial_total_messages -- number of messages to crawl from the channel before starting the loop .
	messages_per_loop -- number of messages to crawl in ever loop after crawling inital total messages . 
	amount_of_time_to_wait_per_loop -- amount of time(in seconds) between each loop  . 
	folder_name -- name of folder to save the files to .	
	number_of_loops -- number of times too loop .
	"""
	
	profile = webdriver.FirefoxProfile("vnsujllc.default-release") 
	options = FirefoxOptions()
	worked  = False
	profile.set_preference("browser.download.dir", f"/tmp/{folder_name}")
	profile.set_preference("browser.download.folderList",2)	
	options.add_argument("--headless")
	driver = webdriver.Firefox(firefox_profile=profile,options=options) 
	driver.get(channel)
	time.sleep(15)
	while worked ==False: 
		try : 
			driver.find_element_by_xpath('//*[@id="dht-userscript-trigger"]').click()
			worked= True
		except: 
			print('Error finding buttton , Trying again! ')
	
	time.sleep(3)
	
	driver.find_element_by_xpath('//*[@id="dht-ctrl-track"]').click()
	time.sleep(int(initial_total_messages)/50)	
	driver.find_element_by_xpath('//*[@id="dht-ctrl-track"]').click()



	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="dht-ctrl-download"]').click()
	time.sleep(3)
	for i in range(int(number_of_loops)):  
		time.sleep(int(amount_of_time_to_wait_per_loop))
		print("starting next loop")

		driver.get(channel)
		time.sleep(15)
		worked  = False	
		while worked ==False: 
			try : 
				driver.find_element_by_xpath('//*[@id="dht-userscript-trigger"]').click()
				worked= True
			except: 
				print('Error finding buttton , Trying again! ')
		time.sleep(2)

		driver.find_element_by_xpath('//*[@id="dht-ctrl-track"]').click()

		driver.save_screenshot(f"/tmp/second.png")

		time.sleep(int(messages_per_loop)/50)
		
		driver.find_element_by_xpath('//*[@id="dht-ctrl-track"]').click()
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="dht-ctrl-download"]').click()
crawl_discord("https://discord.com/channels/267624335836053506/729674110270963822",20000,100,100,folder_name_,1)
list_of_jsons =(get_path(f"/tmp/{folder_name_}",".txt"))
for text_file_ in list_of_jsons: 
	json_to_csv(text_file_)
list_of_csvs =(get_path(f"/tmp/{folder_name_}",".csv"))
df = pd.read_csv(f'/tmp/{folder_name_}/dht.csv')
for csv in list_of_csvs :
	df1= pd.read_csv(csv) 
	df = pd.concat([df,df1])
df =df[["text","author","sent_at"]]
#df.drop_duplicates(subset='sent_at',keep="first",inplace=True)
print(df)
df.to_csv(f"/tmp/{folder_name_}/{folder_name_}.csv")
