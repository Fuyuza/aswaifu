# aswaifu (unofficial)
<img src='https://waifu.pics/favicon.ico'>
A asynchronous lib of https://waifu.pics.

# Docs
  https://waifu.pics/docs

# lib Usage
```py
import aswaifu
import aiohttp

async with aiohttp.ClientSession() as session:
  client = aswaifu.HttpClient(session)
  await client.get(endpoint=aswaifu.endpoint('type', 'category'))
  # will return -> https://i.waifu.pics/<FileName>
```
