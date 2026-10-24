import base64
import os
from pathlib import Path
import requests

account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"].strip()
token = os.environ["CLOUDFLARE_API_TOKEN"].strip()
model = "@cf/black-forest-labs/flux-1-schnell"
url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
prompt = (
    "Photorealistic absurd internet meme photograph, vertical 9:16 composition. "
    "A school science fair award ceremony in a crowded middle-school gym. "
    "Four serious students stand behind impressive elaborate science projects "
    "while the fifth-place student is celebrating with ridiculous enthusiasm "
    "wearing a plain white t-shirt with a tiny fictional Dearwink brand mark. "
    "Authentic candid smartphone photo, natural overhead fluorescent lighting, "
    "realistic faces and hands, plausible cardboard science displays, documentary "
    "photography, funny visual contrast, detailed environment, no captions, "
    "no overlaid arrows, no watermarks, no graphic-design layout."
)
response = requests.post(
    url,
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json={"prompt": prompt, "num_steps": 4},
    timeout=180,
)
if not response.ok:
    print("Cloudflare image request failed:", response.status_code, response.text[:700])
response.raise_for_status()
payload = response.json()
if not payload.get("success", True):
    raise RuntimeError(f"Cloudflare API returned an error: {payload.get('errors')}")
result = payload.get("result", {})
image_b64 = result.get("image") if isinstance(result, dict) else None
if not image_b64:
    raise RuntimeError("Cloudflare response did not include a base64 image")
output = Path("output/dearwink_ai_test.png")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_bytes(base64.b64decode(image_b64))
print(f"Generated image: {output} ({output.stat().st_size} bytes)")
