# vx-link-converter

A local script that watches your Discord messages and automatically rewrites Twitter/X and Instagram links before you send them.

## What it does

- Converts `twitter.com` links → `vxtwitter.com`
- Converts `x.com` links → `vxtwitter.com`
- Converts `instagram.com` links → `kkinstagram.com`

## Why

Discord embeds for Twitter/X are frequently broken — videos won't play, previews don't load, and links often require the recipient to be logged in. `vxtwitter.com` fixes this by serving proper embeds directly in Discord. Same idea for Instagram — `kkinstagram.com` lets anyone see the content without needing an account.

## Requirements

- Python 3.x - dotenv and discord libraries
- Discord Token
- Run locally on your laptop —  no browser extension, no admin rights needed

## How to run

```bash
python3 main.py
```

Keep the terminal open while you use Discord. The script runs in the background and does its thing automatically.

## How it works

The script monitors user messages. When it detects a Twitter, X, or Instagram link, it automatically rewrites the URL, deletes the user's message and replaces it with the converted link along with user name for clarity on whose link it was.

```
twitter.com/user/status/123  →  vxtwitter.com/user/status/123
x.com/user/status/123        →  vxtwitter.com/user/status/123
instagram.com/p/abc123       →  kkinstagram.com/p/abc123
```

## Files

```
tweet_to_vx/
├── main.py              # Main script
├── responses.py         # URL conversion logic
└── README.md            # This file
```

## Notes

- Only runs when you have the terminal open — close the terminal to stop it
- Does not connect to the internet, collect data, or store anything
- Discord desktop app only — does not affect the browser version of Discord

## License

MIT
