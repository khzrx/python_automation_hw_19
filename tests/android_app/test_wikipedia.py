import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():
    with allure.step('Skip onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_and_click():
    with allure.step('Skip onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with allure.step('Click on content'):
        results.first.click()


def test_onboarding_texts():
    with allure.step('Verify text on 1st page of onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('The Free Encyclopedia\n…in over 300 languages'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text('We’ve found the following on your device:'))

    with allure.step('Click "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify text on 2nd page of onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'Dive down the Wikipedia rabbit hole with a constantly updating Explore feed. \n'
            'Customize the feed to your interests – whether it’s learning about historical events '
            'On this day, or rolling the dice with Random.'))

    with allure.step('Click "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify text on 3rd page of onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'You can make reading lists from articles you want to read later, even when you’re offline. \n'
            'Login to your Wikipedia account to sync your reading lists. Join Wikipedia'))

    with allure.step('Click "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify text on 3rd page of onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Data & Privacy'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'We believe that you should not have to provide personal information to participate in the free knowledge '
            'movement. Usage data collected for this app is anonymous. '
            'Learn more about our privacy policy and terms of use.'))

    with allure.step('Verify button has text "Get Started"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')
                        ).should(have.text('Get started'))

    with allure.step('Click "Get started" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with allure.step('Verify search field is visible'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).should(be.visible)