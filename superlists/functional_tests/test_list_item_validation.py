from unittest import skip
from .base import TodoFunctionalTest


class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this")
    def test_cannot_add_empty_list_item(self):
        #Edith goes to the home page and accidentally tries to submit an empty
        #list item

        #She hits "enter" on the empty item box

        #The home page refreshes and there is an error messages
        #saying that list items cannot be blank

        # She tries again with some etext for the item
        # which now works

        # Edith perversely tries to enter a second blank item
        # She receives a similar warning on the list page

        # and she can correct it by filling some text in.
        self.fail('Finish the test!')
