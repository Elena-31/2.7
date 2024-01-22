from selenium.webdriver import Chrome, Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_binary

def run_script():
   #chrome_options = ChromeOptions()
   #options.add_argument("--headless")
   #driver = Chrome(options=options)
   #driver.get("https://skillbox.ru")
   #driver.quit()

   #driver = Remote(desired_capabilities={
     #  "browserName": "chrome",
       # "browserVersion": "latest"
   #}, command_executor="http://127.0.0.1:4444/wd/hub")
   options = ChromeOptions()
   driver = Remote(command_executor='server', options=options)
   driver.get("https://skillbox.ru")
   driver.quit()




if __name__ == "__main__":
    run_script()