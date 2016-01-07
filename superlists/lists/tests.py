from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.models import Item
from lists.models import Item, List
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')

        self.assertEqual(response.content.decode(), expected_html)



class NewListTest(TestCase):
    def test_save_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data = {'item_text': 'A new list item'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data = {'item_text': 'A new lists item'}
        )
        new_list = List.objects.first() #get id just created
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')


class ItemAndListModelsTest(TestCase):
    def test_saving_and_retrieving_items_in_list(self):
        new_list = List()
        new_list.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = new_list
        first_item.save() #instance method to save data to data base

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = new_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(new_list, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.list, new_list)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        new_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (new_list.id, ))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_list(self):
        new_list = List.objects.create()
        Item.objects.create(text = 'itemey 1', list = new_list)
        Item.objects.create(text = 'itemey 2', list = new_list)

        other_list = List.objects.create()
        Item.objects.create(text = 'other item 1', list = other_list)
        Item.objects.create(text = 'other item 2', list = other_list)

        response = self.client.get('/lists/%d/' % (new_list.id, ))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')
