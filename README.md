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
  - Install the Selenium module (<a href="https://pypi.org/project/selenium/">Installation Guide </a>), FastAPI(Check <a href="https://fastapi.tiangolo.com/tutorial/">documentation</a>) and uvicorn using pip (Check <a href="https://www.uvicorn.org/#quickstart">quickstart</a> guide)
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
  
  
