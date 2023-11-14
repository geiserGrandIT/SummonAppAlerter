from splinter import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchWindowException
import asyncio, pyautogui
import datetime
import subprocess
async def start():
    chrome_options = Options()

    # Does not start if using headless mode
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    with Browser('chrome', options=chrome_options) as browser:
        url = "https://summon.tech"
        username = "1889office@gmail.com"
        password = "front-gGh-1889"
        sound_file = "synthesize.mp3"
        warning_file = "doNotCloseSummonWindow.mp3"
        browser.visit(url)
        WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

        #alert Sound file
        sound = sound_file
        warning = warning_file
        email_input = browser.find_by_name("email")[1]
        password_input = browser.find_by_name("password")[1]

        email_input.fill(username)
        password_input.fill(password)

        submit_button = browser.driver.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-user-login/ion-footer/ion-toolbar/ion-button")

        if submit_button:
            submit_button.click()
        await asyncio.sleep(5)
        print('This is the Summon alert bot, do not close this window')
        print("listening...")
        min = 2
        attempt_warn = True

        try: 
            while True:
                try:
                    _t = len(browser.find_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-location/ion-tab-bar/ion-tab-button[3]").first.find_by_xpath('*'))
                except NoSuchWindowException as err:
                    log(f'Window was closed\n{err}')
                    asyncio.get_event_loop().create_task(play(warning))
                    raise Exception
                except Exception as  err:
                    _t = 3
                    print("\nalert was still open\n", err, type(err))
                    log('Alert was still open')
                
                if _t > 2:
                    print('_t', _t)
                    # Warn commands, sets up a sound, sets when to warn next, and sets a system alert        
                    asyncio.get_event_loop().create_task(play(sound))
                    executeScript(browser)
                    
                    log("vehicle requested")
                    await asyncio.sleep(60)
                    
                
                await asyncio.sleep(1)
        except Exception as e:
            log(e)

    # If for some reason the system goes down, attempt restart
    attempt_restart()
def executeScript(browser):
    js_code = """
    alert("Guest has requested a vehicle");
    """
    browser.execute_script(js_code)

def log(e, location="//192.168.1.3/level1/IT/summonAlerter"):
    lines = []
    lines.append(f"{datetime.datetime.now()}: {e}")
    print("log called:",lines)

    try:

        with open(f"{location}/Logs/log", "r", encoding="utf-8") as f:
            ls = f.readlines()
            for l in ls:
                lines+=l
            with open(f"{location}/Logs/log", "w", encoding="utf-8") as f:
                    f.writelines(lines)
    except:
        if location != ".":
            log("unable to connect to synology", location=".")
            log(e,location=".")
    
async def warn_again():
    await asyncio.sleep(60)
    return True

def attempt_restart():
   print('Window Closed, Attempting to restart')
   asyncio.get_event_loop().create_task(start())

async def play(file):
    try:
        ffmpeg_cmd = ['ffplay', '-i', file, '-autoexit', '-nodisp']
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:

        print(f"play sound failed {e}")

def main():
    asyncio.get_event_loop().run_until_complete(start())
    
if __name__ == "__main__":
    main()
