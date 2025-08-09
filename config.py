import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
import utils


def to_driver_options(context):
    options = UiAutomator2Options()

    options.set_capability('remote_url', os.getenv('REMOTE_URL'))
    options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
    options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))


    if context in ('local_emulator', 'local_real_device'):
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('app', os.getenv('APP'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        load_dotenv(dotenv_path=utils.file.abs_path_from_project(
            '.env.credentials'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('BSTACK_USERNAME'),
                'accessKey': os.getenv('BSTACK_ACCESSKEY'),
            },
        )

    return options