from selenium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.common.keys import Keys
import pyperclip

try:
    driver = webdriver.Chrome('C:/Users/New user/Downloads/chromedriver.exe')
    
    lst = []
    number_for_account = ''

    count = 0

    number_list = list(map(lambda x : chr(x),list(range(48,58))))
    for _ in range(5):
        number_for_account += choice(number_list)

    print(number_for_account)
    
    number_of_accounts = int(input('Enter the Number of Account to Create: '))

    xxxnumber = list(map(lambda x : chr(x),list(range(48,58))))
    ynumber = ''
    for value in range(5):
        ynumber += choice(xxxnumber)
    
    for _ in range(number_of_accounts):
        with open('Boys_names.txt','r') as f:
            with open('Girl_names.txt','r') as f1:# here i have mixed both girls and boys name to generate the random names
                while f.readline().__len__()>0:
                    lst.append(f.readline().strip('\n'))
            while f.readline().__len__()>0:
                lst.append(f.readline().strip('\n'))
        first_name = choice(lst).strip(' ')
        last_name = choice(lst).strip(' ')
        print(first_name,last_name)
        alpha_list = list(range(65,125))
        alpha_list = list(map(lambda x:chr(x),alpha_list)) # use this to generate random password

        print(alpha_list)
        password = ''
        
        for value in range(choice(list(range(10,15)))):
            password += choice(alpha_list)
        print(password)
        print(len(password))

        

        driver.get('https://login.yahoo.com/account/create?specId=usernameReg&src=noSrc&intl=in&context=reg&done=https%3A%2F%2Fwww.yahoo.com')
        sleep(10)

        driver.execute_script('window.open('');')
        sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        print('Switched to TempMail')
        sleep(10)
        driver.get('https://temp-mail.org/en/')
        sleep(5)
        driver.find_element_by_xpath('//button[@id="click-to-delete"]').click()# refreshing the page so that new email is generated everytime
        sleep(10)
        driver.switch_to_window(driver.window_handles[0])
        print('Switched to Yahoo')
        sleep(3)
        
        if count==0:
            driver.find_element_by_xpath('//input[@name="firstName"]').send_keys(first_name)
            driver.find_element_by_xpath('//input[@name="lastName"]').send_keys(last_name)
            print('Name\'s Entered')
            sleep(5)
            driver.switch_to_window(driver.window_handles[1])
            driver.find_element_by_xpath('//input[@id="mail"]').send_keys(Keys.CONTROL,'a')
            driver.find_element_by_xpath('//input[@id="mail"]').send_keys(Keys.CONTROL,'c')


            
            driver.switch_to_window(driver.window_handles[0])
            # 0 --> yahoo mail
            # 1 --> tempmail

            
            
            driver.find_element_by_xpath('//input[@name="email"]').send_keys(Keys.CONTROL,'v')
            print(Keys.CONTROL,'v')
            sleep(5)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
            sleep(2)
            driver.find_element_by_xpath('//select[@name="mm"]').click()
            sleep(2)
            months = ["1","2","3","4","5","6","7","8","9","10","11","12"]
            driver.find_element_by_xpath('//option[@value='+choice(months)+']').click()
            print('Month Entered')
            sleep(2)
            days = list(range(1,28))
            driver.find_element_by_xpath('//input[@name="dd"]').send_keys(choice(days))
            print('Days Entered')
            del days,months
            sleep(2)
            years = list(range(1930,2001,+1))
            driver.find_element_by_xpath('//input[@name="yyyy"]').send_keys(choice(years))
            print('Year Entered')
            sleep(2)
            del years
            driver.find_element_by_xpath('//button[@type="submit"]').click()
            print('Continue Button Clicked')
            sleep(10)
            driver.switch_to_window(driver.window_handles[1])
            print('Switched to TempMail')
            sleep(15)

            driver.execute_script("window.scrollTo(0, 500)")
            sleep(20)
            #driver.refresh()
            driver.find_element_by_xpath('//a[@class="viewLink link"]/following::a/following::a/following::a/following::a').click()
            print('Clicked on the Mail')
            sleep(6)
            print('Mail is Opened')
            driver.execute_script("window.scrollTo(0, 900)")
            sleep(10)
            otp = driver.find_element_by_xpath('//b/following::b').text
            

            driver.switch_to_window(driver.window_handles[0])
            print('Switched to Yahoo')
            sleep(5)
            driver.find_element_by_xpath('//input[@id="verification-code-field"]').send_keys(otp)
            
            driver.find_element_by_xpath('//button[@name="verifyCode"]').click()
            print('Continue Clicked')
            sleep(10)
            driver.find_element_by_xpath('//button[contains(text(),"Done")]').click()
            sleep(3)
            driver.switch_to_window(driver.window_handles[1])
            print('Switched to TempMail')
            driver.close()
            print('TempMail Tab Closed')
            sleep(2)
            driver.switch_to_window(driver.window_handles[0])
            print('Yahoo Account Sucessfully Created')


            with open('user_name_and_password.txt','a') as f:
                # email_id, password, full_name
                f.write(pyperclip.paste()+','+password+','+first_name+' '+last_name+','+first_name+'_'+last_name+ynumber+'\n')

            with open('yahoo_account_created.txt','a') as f:
                f.write(pyperclip.paste()+','+password+','+first_name+' '+last_name+','+first_name+'_'+last_name+ynumber+'\n')

            
            sleep(20)
            
except Exception as e:
    print(e)
finally:    
    driver.quit()
    print('Browser Closed')
