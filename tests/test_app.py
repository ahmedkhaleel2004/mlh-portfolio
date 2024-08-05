# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Ahmed Khaleel - MLH Fellow</title>" in html
        
        # More tests
        assert "About Myself" in html

    def test_timeline(self):
        # Test GET /api/timeline_post
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Test POST /api/timeline_post
        response = self.client.post("/api/timeline_post", data={
            'name': 'Jett',
            'email': 'jett@val.com',
            'content': 'WATCH THIS'
        })

        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == 'Jett'
        assert json["email"] == 'jett@val.com'
        assert json["content"] == 'WATCH THIS'

        # Verify that the post was added to the database
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == 'Jett'
        assert json["timeline_posts"][0]["email"] == 'jett@val.com'
        assert json["timeline_posts"][0]["content"] == 'WATCH THIS'

        # Test the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<p>Stay up to date in my career by reading some of my timeline posts!</p>" in html
        assert "<style>" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

