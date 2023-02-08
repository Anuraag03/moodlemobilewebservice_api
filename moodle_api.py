import secrets

from fastapi import Depends, FastAPI, HTTPException, status,Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium .webdriver.support.wait import WebDriverWait

app = FastAPI()

security = HTTPBasic()

userName=input('Username/Gmail: ') #enter your username/gmail
passWord = input('Password: ') #enter your password

driver= webdriver.Chrome() #opens webdriver
driver.get("https://cms.bits-hyderabad.ac.in/login/index.php") #directs to CMS page
waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,value='Google')) #click on google login link
gLink =driver.find_element(By.LINK_TEXT,value='Google') 
gLink.click()

usr = driver.find_element(By.ID,'identifierId').send_keys(userName,Keys.ENTER) #enters username
driver.implicitly_wait(1)
waiter = WebDriverWait(driver, timeout=5,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,"password")) #enters password
pwd = driver.find_element(By.NAME,"password").send_keys(passWord,Keys.ENTER)
waiter = WebDriverWait(driver, timeout=5,poll_frequency=0.5).until(lambda d: d.find_element(By.ID,"user-menu-toggle"))
driver.implicitly_wait(1)
profile = driver.find_element(By.ID,"user-menu-toggle") #clicks on user menu
profile.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[3]/nav/div[2]/div[5]/div/div/div/div/div/div/a[7]"))
pref = driver.find_element(By.XPATH,"/html/body/div[3]/nav/div[2]/div[5]/div/div/div/div/div/div/a[7]") # clicks on preferences
pref.click()
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,"Security keys"))
seckey = driver.find_element(By.LINK_TEXT,"Security keys")
seckey.click() #clicks o security keys
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div/div/table/tbody/tr[1]/td[6]/a"))
docum = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div/div/table/tbody/tr[1]/td[6]/a")
docum.click() # click on the documentation
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[2]/div/div[1]/a/img"))





docAllArray=[]
def docCatalog(): #for loop to store all the api endpoints/documentation titles in an array 
    print("please wait while the data is being scraped")
    for i in range(2,395):
        docText= driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{i}]").text
        docAllArray.append(docText)
    print("Scraped all document titles! ")
docCatalog()

def aquire_current_username(credentials: HTTPBasicCredentials = Depends(security)): # HTTPBasic for username/password authentication
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



@app.get("/users/me") # authenticates username/password
def read_current_user(username: str = Depends(aquire_current_username)):
    return {"username": username}
@app.get("/index")
def getallDocs(username: str = Depends(aquire_current_username)):
    return docAllArray
@app.get("/index/{docSe}") # takes the required documentation name as input and gives out the documentation
def getDoc(docSe : str):
    def binary_search(arr,first,last,target): #binary search to speedup the searching of the xpath of element so result is displayd instantly
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
    def docShow(): # function that implements the binary search and displays the documentation as a JSON data
        index = binary_search(docAllArray,0,len(docAllArray)-1,docSe)
        docClicker = driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[1]/a")
        docClicker.click()
        docText= driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[1]/a/strong").text
        full_div = driver.find_element(By.XPATH,f"/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[{index}]/div/div[2]").text
        docDict.update({docText:full_div})
    docShow()
    return Response(content=docDict[docSe], media_type="application/json")
@app.get("/") # landing page i 
def mainPage():
    return {"message":"Moodle Mobile web service API"}