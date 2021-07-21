import aiohttp
import discord
import json
from bs4 import BeautifulSoup
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
discord_key = 'ODY3MjkwMTYwOTk0MzIwNDE1.YPe85w.lOeFPlzrvMcAiWI3ThntoUD6GuM'
kakao_key = '4809b7c511ced1fc9e115f0079b2a018' #rest_api key
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

@bot.command(name="검색")
# 다음 검색 작업 - 카카오 API 사용
async def search(ctx, *args):
    URL = 'https://dapi.kakao.com/v2/search/web'
    parameter = {
        'query': ' '.join(args),
        'sort' : 'accuracy',
        'size' : 3
    }

    header = {
        'Authorization': f'KakaoAK {kakao_key}'
    } 

    response = await requests.get(URL, params=parameter, headers=header)

    if response.status_code != 200:
        print(response.text)
        await ctx.send('검색 중 문제가 발생했어요!!!')
        return

    tmp = json.loads(response.text)

    for dt in tmp['documents']:
        await ctx.send(dt['title'] + ' ' + dt['contents'])




@bot.command()
async def hello(ctx):
    await ctx.send('안녕!')
    
@bot.command(name="게시판_조회")
async def board_search(ctx, *args):
    request_URL = server_URL + '/board'
    response = await requests.get(request_URL)

    if response.status_code != 200:
        print(response.text)
        await ctx.send('검색 중 문제가 발생했어요!!!')
        return

    await ctx.send(json.loads(response.text))


@bot.command(name="게시판_작성")
async def board_write(ctx, arg, *args): # 비밀번호, 게시글
    if not args:
        await ctx.send("입력이 잘못되었습니다!!")
        return

    if len(arg) > 20:
        await ctx.send("비밀번호의 길이는 20글자를 넘을 수 없습니다.")
        return

    data = {
        'password' : arg,
        'content' : ' '.join(args)
    }

    request_URL = server_URL + '/board'

    response = await requests.post(request_URL, json=data)
    # HTML로 보냅니다.
    # JSON으로 안 감
    # 서버 처리 방법이 달라짐!!

    if response.status_code != 200:
        print(response.text)
        await ctx.send('삽입 중 문제가 발생했어요!!!')
        return

    await ctx.send(json.loads(response.text))


@bot.event
async def on_ready():
    print(f'{bot.user} 봇이 가동되었습니다!!')

bot.run(discord_key)