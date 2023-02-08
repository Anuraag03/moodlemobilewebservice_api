import secrets

from fastapi import Depends, FastAPI, HTTPException, status,Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium .webdriver.support.wait import WebDriverWait
from getpass import getpass
app = FastAPI()

security = HTTPBasic()

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

def aquire_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = bytes(userName,'utf-8')
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = bytes(passWord,'utf-8')
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or Password!!!!",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username



@app.get("/users/me")
def read_current_user(username: str = Depends(aquire_current_username)):
    return {"username": username}
@app.get("/index")
def getallDocs(username: str = Depends(aquire_current_username)):
    return docAllArray
@app.get("/index/{docSe}")
def getDoc(docSe : str):
    def binary_search(arr,first,last,target):
        if last >=first:
            mid = (last +first) // 2
            if arr[mid] == target:
                return mid+2

            elif arr[mid] > target:
                return binary_search(arr,first, mid - 1, target)
 
            else:
                return binary_search(arr, mid + 1,last, target)
 
        else:
            print("Element not in documentation")
            return -1
    
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