from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() #she opens Firefox
        self.browser.implicitly_wait(3) #if anything goes wrong stop after 3 sec

    def tearDown(self):
        self.browser.quit() #window closes

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage.
        self.browser.get('http://localhost:8000') #go to the homepage

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        #find h1 tag on the page
        hearder_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', hearder_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feather" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add another item
        # She enters 'Use peacock feathers to make fly'
        # (Edith is very methodological)

        # The homepage updates again, and now shows both its items on her lists

        # Edith wonders whether the site will remember her lists.  Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits the URL - her to-do lists is still there.

        # Satisfied, she goes back to sleep.
        self.fail('Finish the app!')

# like main method
if __name__ == '__main__':
        unittest.main() #run main test and ignore all warnings
