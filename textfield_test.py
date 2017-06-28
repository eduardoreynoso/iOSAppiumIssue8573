from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import os
import time


def wait_for_element_by_name(driver, element_name):
    # Poll for 5 secs until element is found
    timeout = 5000
    poll_frequency = 0.2
    end_time = time.time() + timeout
    while True:
        try:
            return driver.find_element_by_name(element_name)
        except NoSuchElementException:
            pass
        except WebDriverException:
            pass
        time.sleep(poll_frequency)
        if time.time() > end_time:
            break
    raise TimeoutException('Element named: {} could not be found'.format(element_name))

if __name__ == "__main__":
    capabilities = {
            'automationName': 'XCUITest',
            'platformName': 'iOS',
            'platformVersion': '10.3',
            'deviceName': 'iPhone 7',
            'noReset': False,
            'newCommandTimeout': 180,
            'sendKeyStrategy': 'setValue',
            'app': os.path.abspath('SpotHero.app')
        }
    textfield_selector = 'Address or landmark'
    search_address = '215 West Washington st'

    for i in range(0, 100):
        print('Run {}'.format(i))
        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', capabilities)
        # Dismiss the onboarding screen
        wait_for_element_by_name(driver, 'Close').click()
        # Dismiss the instructions overlay
        wait_for_element_by_name(driver, 'Tap anywhere to dismiss').click()

        wait_for_element_by_name(driver, textfield_selector).click()
        wait_for_element_by_name(driver, textfield_selector).send_keys(search_address)
        element_text = wait_for_element_by_name(driver, textfield_selector).text
        if element_text != search_address:
            # Means that we could not set the text to the input
            import pdb
            pdb.set_trace()
        else:
            driver.quit()



