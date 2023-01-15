# aiowaifu (unofficial)
<p align="center">
 <h2 align="center">
 </h2>
 <p align="center">
    <img src='https://waifu.pics/favicon.ico'>
 </p>

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
