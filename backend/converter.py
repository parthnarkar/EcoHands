import os
import requests

# HANDSPEAK.COM URL for a given word
def handspeak_url(word):
    word = word.lower
    if len(word) < 3:
        return None
    return f"https://www.handspeak.com/word/{word[0]}/{word[:3]}/{word}.mp4"

# Checking status of this handspeak url(if video is present or not)
def video_exists(url):
    