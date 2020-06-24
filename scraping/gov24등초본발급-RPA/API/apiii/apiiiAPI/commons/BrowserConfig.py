from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

## Chrome
def chromeConfig():
    ## Driver Path   
    chromedriverPath = "C:\web_project\WholethingAPI\wholeThingAPI\wholething\wholethingAPI\Driver/chromedriver.exe"       

    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument( "--headless" )     # 크롬창이 열리지 않음
    chrome_options.add_argument( "--no-sandbox" )   # GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
    chrome_options.add_argument( "--disable-gpu" )  # GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
    chrome_options.add_argument(f"--window-size={ WINDOW_SIZE }")
    chrome_options.add_argument('Content-Type=application/json; charset=utf-8')

    driver = webdriver.Chrome( executable_path=chromedriverPath, chrome_options=chrome_options )

    return driver

## IE
def IEConfig():    
    ## Driver Path 
    IEdriverPath     = "C:\web_project\WholethingAPI\wholeThingAPI\wholething\wholethingAPI\Driver/IEDriverServer.exe"        
    driver = ''
    return driver
