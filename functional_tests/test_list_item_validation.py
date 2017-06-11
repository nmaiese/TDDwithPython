from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank


        error = self.browser.find_element_by_class_name('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #self.browser.implicitly_wait(20)
        # She tries again with some text for the item, which now works
        #pdb.set_trace()
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item

        self.get_item_input_box().send_keys(Keys.ENTER)
        #pdb.set_trace()
        time.sleep(2)
        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_class_name('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

