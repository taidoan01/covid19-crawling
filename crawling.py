from selenium import webdriver
import pandas as pd


browser = webdriver.Chrome(executable_path=r".\chromedriver.exe")
browser.get("https://covid19.gov.vn/")
# chuyen toi frame can lay data
browser.switch_to.frame(1)

target = browser.find_elements_by_xpath("/html/body/div[2]/div[1]/div")
# lay tung co trong target
for t in target:
    cities = t.find_elements_by_class_name("city")
    totals = t.find_elements_by_class_name("total")
    dies = t.find_elements_by_class_name("die")
    

list_cities = [city.text for city in cities]
list_totals = [total.text for total in totals]
list_dies = [die.text for die in dies]

browser.close()
 
df = pd.DataFrame(list(zip(list_cities,list_totals,list_dies)))
df_new = pd.DataFrame(df.values[1:],columns = df.iloc[0])
df_new.to_csv("Covid-19_VN_Dataset.csv")
    