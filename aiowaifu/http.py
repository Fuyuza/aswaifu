import aiohttp

from .utils import AioHttp

class HttpClient:
    def __init__(self, session: aiohttp.ClientSession):
        self.route = 'https://api.waifu.pics/'
        self.session = session

    async def get(self, *, endpoint):
        res = await AioHttp('GET', self.route + endpoint).request(self.session)
        return res['url']
