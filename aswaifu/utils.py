from __future__ import annotations

import aiohttp

class AioHttp:
    def __init__(self, verb: str, route: str):
        self.verb = verb
        self.route = route
 
    async def request(self, session: aiohttp.ClientSession):
        async with session.request(self.verb, self.route) as response:
            if response.status != 200:
                return await response.text()
            return await response.json()
