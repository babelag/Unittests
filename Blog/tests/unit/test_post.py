from unittest import TestCase
from post import Post

class PostTest(TestCase):

    def test_create_post(self):
        p = Post('title', 'content')

        self.assertEqual('title', p.title)
        self.assertEqual('content', p.content)

    def test_json(self):
        p = Post('title', 'content')

        expected = {'title' : 'title', 'content' : 'content'}
        self.assertDictEqual(expected, p.json())

