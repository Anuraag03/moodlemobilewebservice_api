# moodlemobilewebservice_api
## About Project
The purpose was to build a python script that can scrape documentation of the Moodle Mobile web service from the Course Management System (<a href="https://moodle.org/">Moodle CMS<a>)
## Languages and modules used
- python
- Selenium module (find documentation <a href="https://selenium-python.readthedocs.io/">here</a>)
- FastAPI (find documentation <a href = "https://fastapi.tiangolo.com/">here</a>)
- uvicorn module( find documentation <a href="https://www.uvicorn.org/">here</a>) 
  ## How to Run
  - Download the script and chromedriver.exe in the same directory
  - Install the Selenium module (<a href="https://pypi.org/project/selenium/">Installation Guide </a>), FastAPI (Check <a href="https://fastapi.tiangolo.com/tutorial/">documentation</a>) and uvicorn using pip (Check <a href="https://www.uvicorn.org/#quickstart">quickstart</a> guide)
  - Next open your terminal in an IDE
  - And run the following code 
  ```
  uvicorn moodle_api:app 
  ```
  or

  ```
  python -m uvicorn moodle_api:app 
  ```
  - The Chrome browser opens automatically and starts scraping the documentation 
  - Go back to the IDE and wait for confirmation that data has been scraped
  
  ![server runnning](https://user-images.githubusercontent.com/95640377/217568743-c38e835b-253a-4aed-94a3-2e08136caabd.jpg)
  -  Now go to the link displayed in your terminal
  
  ![server runnning url](https://user-images.githubusercontent.com/95640377/217569390-8741ebe5-4535-4e9c-9407-a2fd3454ff65.jpg)
  
  or
  
  - go to http://localhost:8000
  
  ![localhost main page](https://user-images.githubusercontent.com/95640377/217570136-32ae6ba1-dddc-4713-99bb-0a506c71f668.jpg)
  - You can preview all the API endpoints / documentation titles by going to    http://localhost:8000/index
  - However before you can actually view all the documentation titles you will be promted to provide username and password authentication ; this username and password is the same as your gmail and gmail password(BITS account)
  
  ![authentication](https://user-images.githubusercontent.com/95640377/217602709-6361acdf-5c78-4cc9-9bfb-41c2318ca9d8.jpg)
  
  
![localhostindex](https://user-images.githubusercontent.com/95640377/217571198-e844589d-083f-418b-9b6c-cdc61cedb800.jpg)
- Now you can search and paginate through all the different api end points
  - Example: if you want to view the documentation o f "block_recentlyaccesseditems_get_recent_items"
  You can do so by going to http://localhost:8000/index/block_recentlyaccesseditems_get_recent_items
  
  - Tip: If you see a blank white screen instead of the required documentation try refreshing the page.
  
  ![documentation](https://user-images.githubusercontent.com/95640377/217572403-a2c6a4f3-6c48-4cee-91c5-756f162eb6bb.jpg)
  
 

