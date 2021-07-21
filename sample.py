import aiohttp
import discord
import json
from bs4 import BeautifulSoup
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
discord_key = '473dc1523daa0942e148276a69404510c642ee367e1ea7f89e1a8a912cd722da'
kakao_key = '여기에 카카오 키 입력'
server_URL = 'http://localhost:1234'

'''
이 부분은 절대 건드리시면 안 됩니다!
코루틴과 aiohttp에 대한 지식이 없는 상황에서 봇 제작을 해야 하므로,
여러분들이 사용할 수 있는 request와 최대한 흡사하게 수정하는 코드입니다...
'''
class requests_result():
    def __init__(self, st_code, contents):
        self.status_code = st_code
        self.text = contents
    
    def ok(self):
        return self.status_code == 200

class requests():
    @staticmethod
    async def get(url, headers=None, params=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                content = await response.read()
                return requests_result(response.status, content)

    @staticmethod
    async def post(url, data=None, headers=None, json=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data, json=json) as response:
                content = await response.read()
                return requests_result(response.status, content)

    @staticmethod
    async def delete(url, data=None, headers=None, json=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=headers, data=data, json=json) as response:
                content = await response.read()
                return requests_result(response.status, content)

    @staticmethod
    async def put(url, data=None, headers=None, json=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, data=data, json=json) as response:
                content = await response.read()
                return requests_result(response.status, content)
'''
이 부분은 절대 건드리시면 안 됩니다!
코루틴과 aiohttp에 대한 지식이 없는 상황에서 봇 제작을 해야 하므로,
여러분들이 사용할 수 있는 request와 최대한 흡사하게 수정하는 코드입니다...
'''

@bot.command()
async def hello(ctx):
    await ctx.send('안녕!')
    
@bot.event
async def on_ready():
    print(f'{bot.user} 봇이 가동되었습니다!!')

bot.run(discord_key)