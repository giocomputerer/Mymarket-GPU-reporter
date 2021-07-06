from selenium import webdriver
from selenium.webdriver.common.by import By
import io
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def remove_non_ascii_1(text):

    return ''.join(i for i in text if ord(i)<128)


url = "https://beta.mymarket.ge/ka/search/121/videobaraTi/?CatID=121&Page=1"
driver = webdriver.Chrome()
driver.get(url)



card_names = driver.find_elements_by_class_name('card-title')
card_prices =driver.find_elements_by_class_name('mr-3px')

for i in range(len(card_names)):
    print (card_names[i].text+"-"+card_prices[i].text + "gel")
    
    
now= datetime.now()
CurrentMinute=now.strftime("%M")
CurrentHour=now.strftime("%H")
CurrentDay=now.strftime("%d")
CurrentMonth=now.strftime("%m")

if CurrentMonth=="01":
    CurrentMonth="Jan"
elif CurrentMonth=="02":
    CurrentMonth="Feb" 
elif CurrentMonth=="03":
    CurrentMonth="Mar" 
elif CurrentMonth=="04":
    CurrentMonth="Apr"
elif CurrentMonth=="05":
    CurrentMonth="May" 
elif CurrentMonth=="06":
    CurrentMonth="Jun"
elif CurrentMonth=="07":
    CurrentMonth="Jul" 
elif CurrentMonth=="08":
    CurrentMonth="Aug"
elif CurrentMonth=="09":
    CurrentMonth="Sep" 
elif CurrentMonth=="10":
    CurrentMonth="Oct"
elif CurrentMonth=="11":
    CurrentMonth="Nov" 
elif CurrentMonth=="12":
    CurrentMonth="Dec"
    
CurrentYear=now.strftime("%Y")

nm=str("Report_"+CurrentHour+'hr'+CurrentMinute+"_"+CurrentDay+"_"+CurrentMonth+"_"+CurrentYear+".txt")


f= open (nm,"a+")


for i in range(len(card_names)):
    f.write(str(remove_non_ascii_1(card_names[i].text+"--------------------------------"+card_prices[i].text + "gel"))+"\n")



f.close()

driver.close()