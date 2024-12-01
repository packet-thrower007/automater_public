from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from getpass import getpass


username = "test"
password = getpass()




try:
#    print("test")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(r'https://google.com.com/login')
    driver.implicitly_wait(15)

#    print("login step")
#    Right click on the login box or potion of a website you need python to control, click on inspect element choose copy full xpath
    loginBox = driver.find_element(By.XPATH,'//*[@id="react-container"]/div[2]/main/div/div/div/div/form/div[1]/div/div/input')
    loginBox.send_keys(username)

#    print(loginbox)
#    Right click on the login box or potion of a website you need python to control, click on inspect element choose copy full xpath
    nextButton = driver.find_elements(By.XPATH,'//*[@id="react-container"]/div[2]/main/div/div/div/div/form/div[3]/button')
    nextButton[0].click()

    passWordBox = driver.find_element(
        By.XPATH,'//*[@id="react-container"]/div[2]/main/div/div/div/div/form/div[2]/div[1]/div/div/input')
    passWordBox.send_keys(password)

    nextButton = driver.find_elements(By.XPATH,'//*[@id="react-container"]/div[2]/main/div/div/div/div/form/div[3]/button[2]/span')
    nextButton[0].click()

    print('Login Successful...!!')
except:
    print('Login Failed')
