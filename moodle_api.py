from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fastapi import FastAPI,Response
from selenium .webdriver.support.wait import WebDriverWait
from getpass import getpass
app = FastAPI()

userName=input('Username/Gmail: ') #enter your username/gmail
passWord = getpass('Password: ')

driver= webdriver.Chrome() 
driver.get("https://cms.bits-hyderabad.ac.in/login/index.php") 
waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,value='Google'))
gLink =driver.find_element(By.LINK_TEXT,value='Google') 
gLink.click()

usr = driver.find_element(By.ID,'identifierId').send_keys(userName,Keys.ENTER) 
driver.implicitly_wait(1)
waiter = WebDriverWait(driver, timeout=5,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,"password"))
pwd = driver.find_element(By.NAME,"password").send_keys(passWord,Keys.ENTER)
waiter = WebDriverWait(driver, timeout=5,poll_frequency=0.5).until(lambda d: d.find_element(By.ID,"user-menu-toggle"))
driver.implicitly_wait(1)
profile = driver.find_element(By.ID,"user-menu-toggle")
profile.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[3]/nav/div[2]/div[5]/div/div/div/div/div/div/a[7]"))
pref = driver.find_element(By.XPATH,"/html/body/div[3]/nav/div[2]/div[5]/div/div/div/div/div/div/a[7]")
pref.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,"Security keys"))
seckey = driver.find_element(By.LINK_TEXT,"Security keys")
seckey.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div/div/table/tbody/tr[1]/td[6]/a"))
docum = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div/div/table/tbody/tr[1]/td[6]/a")
docum.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/div/div[1]/a/img"))




docAllArray=[]
def docCatalog():
    print("please wait while the data is being scraped")
    for i in range(2,395):
        docText= driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{i}]").text
        docAllArray.append(docText)
    print("Scraped all document titles! ")
docCatalog()

@app.get("/index")
def getallDocs():
    return docAllArray
@app.get("/index/{docSe}")
def getDoc(docSe : str):
    def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid+2

            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
 
            else:
                return binary_search(arr, mid + 1, high, x)
 
        else:
            return print("element not in array")
    
    docDict={}
    def docShow():
        index = binary_search(docAllArray,0,len(docAllArray)-1,docSe)
        docClicker = driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[1]/a")
        docClicker.click()
        docText= driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[1]/a/strong").text
        full_div = driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[2]").text
        docDict.update({docText:full_div})
    docShow()
    return Response(content=docDict[docSe], media_type="application/json")
@app.get("/")
def mainPage():
    return {"message":"Moodle Mobile web service API"}


