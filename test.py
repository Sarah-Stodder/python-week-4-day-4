from distutils.log import error
from unittest import TestCase, main

from userhelp import get_category_list, get_books

class Category(TestCase):
    def test_1(self):
        self.assertEqual(get_category_list(books), {'Cooking',
 'Entertainment',
 'Marriage',
 'Marriage Advice',
 'Programming',
 'Science',
 'Self Help'})
    def test_nonAlpha(self):
        self.assertEquals(get_category_list(cooking), error)

if __name__ == '__main__':
    main()