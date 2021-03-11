import subprocess,sys,json,os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def install(package):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if package in installed_packages:
        pass
    else:
        import pip
        os.system("pip install --user "+ package)

def login(user, password):
    driver = webdriver.Chrome()
    driver.get('https://www.messenger.com/')
    clickme = driver.find_element_by_xpath('//*[contains(@id,"u_0_g")]')
    clickme.click()
    time.sleep(2)
    clickme = driver.find_element_by_xpath('//*[contains(@id,"email")]')
    clickme.click()
    clickme.send_keys(user)
    clickme = driver.find_element_by_xpath('//*[contains(@id,"pass")]')
    clickme.send_keys(password)
    clickme = driver.find_element_by_xpath('//*[contains(@id,"loginbutton")]')
    clickme.click()
    driver.get("https://www.messenger.com/t/3346267432111017/")
    time.sleep(3)
    return driver