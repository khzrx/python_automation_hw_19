import pytest
from appium import webdriver
from selene import browser
import utils
from dotenv import load_dotenv
import config

def pytest_addoption(parser):

    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    utils.allure.attach_screenshot()
    utils.allure.attach_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        utils.allure.attach_bstack_video(session_id)

