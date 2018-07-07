import unittest
from blog import Blog

class TestBlog(unittest.TestCase):

    def test_create_post(self):
        b = Blog('Test', "Test Author")
        b.create_post('Test Post', 'Test Content')

        self.assertEqual((len(b.posts)), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')