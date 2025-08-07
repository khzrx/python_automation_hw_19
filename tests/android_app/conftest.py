import allure
import allure_commons
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser, support
import os
import utils
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': os.getenv('bstack_platformVersion'),
        'deviceName': os.getenv('bstack_deviceName'),

        'app': os.getenv('bstack_app'),

        'bstack:options': {
            'projectName': 'QA.GURU homework 19',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            'userName': os.getenv('bstack_userName'),
            'accessKey': os.getenv('bstack_accessKey')
        }
    })

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.allure.attach_screenshot()
    utils.allure.attach_xml()

    session_id = browser.driver.session_id

    with allure.step('Teardown app session'):
        browser.quit()

    utils.allure.attach_bstack_video(session_id)

