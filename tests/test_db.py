# test_db.py

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# Use an in-memory SQLite database for tests.
test_db = SqliteDatabase(':memory:')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Drop tables and close the connection to the database.
        test_db.drop_tables(MODELS)
        test_db.close()

class TestTimelinePost(BaseTestCase):
    def test_create_and_retrieve_timeline_posts(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content='Hello world, I\'m John!'
        )
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world, I\'m Jane!'
        )
        self.assertEqual(second_post.id, 2)

        # Retrieve and assert the timeline posts.
        timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
        self.assertEqual(len(timeline_posts), 2)

        first_fetched_post = timeline_posts[1]
        second_fetched_post = timeline_posts[0]

        self.assertEqual(first_fetched_post.name, 'John Doe')
        self.assertEqual(first_fetched_post.email, 'john@example.com')
        self.assertEqual(first_fetched_post.content, 'Hello world, I\'m John!')

        self.assertEqual(second_fetched_post.name, 'Jane Doe')
        self.assertEqual(second_fetched_post.email, 'jane@example.com')
        self.assertEqual(second_fetched_post.content, 'Hello world, I\'m Jane!')

if __name__ == '__main__':
    unittest.main()
