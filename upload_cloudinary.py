import os
import sys
from pathlib import Path
import requests

path = Path(sys.argv[1])
if path.suffix.lower() not in ('.mp4', '.mov'):
    raise ValueError('Expected MP4 or MOV')
with path.open('rb') as video:
    response = requests.post(
        f"https://api.cloudinary.com/v1_1/{os.environ['CLOUDINARY_CLOUD_NAME']}/video/upload",
        data={'upload_preset': os.environ['CLOUDINARY_UPLOAD_PRESET'], 'folder': 'dearwink_reels'},
        files={'file': (path.name, video, 'video/mp4')}, timeout=180)
response.raise_for_status()
print('PUBLIC_VIDEO_URL=' + response.json()['secure_url'])
