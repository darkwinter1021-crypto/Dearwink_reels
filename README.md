# Dearwink Reels
GitHub Actions + Cloudinary upload pipeline.

Run **Actions > Upload Dearwink Reel > Run workflow** and specify the path to an MP4/MOV that exists in the repository.

Cloudinary cloud: `qjh0dnin`; unsigned upload preset: `dearwink_reels`.

The workflow outputs `PUBLIC_VIDEO_URL` in the job logs. Windsor.ai can publish a Reel using that URL, but publishing is **not** wired into this workflow.

**Current limitation:** ChatGPT-generated files do not automatically enter this GitHub repository. Do not commit API keys, tokens, or private files. This public repository makes committed files visible to everyone.
