from .base import TodoFunctionalTest
from selenium import webdriver

class ToggleDoneTest(TodoFunctionalTest):
    def toggle_todo_done(self, todo_text):
        row = self.find_table_row(todo_text)
        row.find_element_by_tag_name('input').click()
        self.browser.find_element_by_id('toggle_done')

    def check_marked_off(self, todo_text):
        pass

    def test_can_toggle_finished_items(self):
        #Edith makes a quick shopping List noticing a checkbox to toggle done items
        self.browser.get(self.live_server_url) #open url
        self.enter_a_new_item('Buy peacock feathers') #enter items
        self.enter_a_new_item('Buy fishing line')

        checkbox_selector = 'input[type = "checkbox"]'
        checkboxes = self.browser.find_elements_by_css_selector(checkbox_selector)
        self.assertEqual(len(checkboxes), 2)

        #At the store, Edith puts the feathers in her cart and marks them done on the todo List
        self.toggle_todo_done('Buy peacock feathers')
        self.toggle_todo_done('Buy fishing line')

        #Edith returns home, re-opens her to-do list, and sees that her shopping list is still marked and crossed off
        current_list_url = self.browser.current_url
        self.browser.quit()

        self.browser = webdriver.Firefox()
        self.browser.get(current_list_url)
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        #She adds a todo item to tie her flys and marks them as done after a night of tying
        self.enter_a_new_item('Tie some flys')
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        self.toggle_todo_done('Tie some flys')
        self.check_marked_off('Tie some flys')
