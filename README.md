# aswaifu (unofficial)
<img src='https://waifu.pics/favicon.ico'>
A asynchronous lib of https://waifu.pics.

# Docs
  https://waifu.pics/docs

# lib Usage
```py
import aiowaifu
import aiohttp

async with aiohttp.ClientSession() as session:
  client = aiowaifu.HttpClient(session)
  await client.get(endpoint=aiowaifu.endpoint('type', 'category'))
  # will return -> https://i.waifu.pics/<FileName>
```
