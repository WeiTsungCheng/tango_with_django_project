from django.test import TestCase
from rango.models import Category, Page
from django.urls import reverse
from django.utils import timezone

def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()

    return  category

def add_page(category, title, url, views=0, last_visit=timezone.now()):
    page = Page.objects.get_or_create(category=category, title=title, url=url)[0]

    return page

class CategoryTestCase(TestCase):

    def test_ensure_views_are_positive(self):
        category = add_category(name='Test', views=-1, likes=0)
        self.assertEqual((category.views >= 0), True)

    def test_slug_line_creation(self):
        category = add_category(name='Random Category String')
        self.assertEqual(category.slug, 'random-category-string')

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_category('Python', 1, 1)
        add_category('C++', 1, 1)
        add_category('Erlang', 1, 1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Python')
        self.assertContains(response, 'C++')
        self.assertContains(response, 'Erlang')

        num_categories = len(response.context['categories'])
        self.assertEqual(num_categories, 3)

    def test_page_is_created_or_viewed_in_past(self):
        category = add_category(name='Test3')
        page = add_page(category, title='Test', url='/test/')
        self.assertEqual(page.last_visit < timezone.now(), True)

    def test_after_viewed_page_last_visit_is_renewed(self):
        category = add_category(name='Test4')
        page = add_page(category, title='Test2', url='/test2/')
        before = page.last_visit
        response = self.client.get(reverse('rango:goto'), {'page_id': page.id})
        self.assertEqual(response.status_code, 302)

        page.refresh_from_db()
        after = page.last_visit
        self.assertLess(before, after)


