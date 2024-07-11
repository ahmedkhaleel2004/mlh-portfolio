#!/bin/bash

# Variables
API_URL="http://localhost:5000/api/timeline_post"
NAME="Test User"
EMAIL="testuser@example.com"
CONTENT="This is a test post with random content $(date +%s)" # use date to identify

# Function to create a new timeline post
create_post() {
    echo "Creating a new timeline post..."
    RESPONSE=$(curl -s -X POST $API_URL \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "name=$NAME" \
        -d "email=$EMAIL" \
        -d "content=$CONTENT")
    POST_ID=$(echo $RESPONSE | jq -r '.id')
    echo "Post creation response: $RESPONSE"
}

# Function to get timeline posts
get_posts() {
    echo "Fetching timeline posts..."
    RESPONSE=$(curl -s -X GET $API_URL)
    echo "Timeline posts: $RESPONSE"
}

# Function to delete a timeline post
delete_post() {
    echo "Deleting the timeline post with ID $POST_ID..."
    DELETE_RESPONSE=$(curl -s -X DELETE "$API_URL/$POST_ID")
    echo "Delete response: $DELETE_RESPONSE"
}

# Create a new timeline post
create_post

# Verify the post was added (search for the content)
get_posts | grep "$CONTENT" &> /dev/null

if [ $? -eq 0 ]; then
    echo "Post was successfully added."
else
    echo "Failed to add the post."
fi

delete_post