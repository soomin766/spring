import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_member_join(member):
    await member.send("Welcome to international friend! i hope you have a great time on the international friend channel! , if you wanna find some command look at these words(!tutorial,hello,Hello,help,!korean,pepsi,bye,penguin)")

@bot.command(aliases=['korean'])
async def shortwords(ctx):
    responses = [
       "안녕 = hello / Pronunciation : annyeong", #1
       "반가워 = nice to meet you / Pronunciation : bangawo", #2
       "어떻게 지내요 = How are you doing? / Pronunciation : eotteohge jinaeyo", #3
       "다음에 봐 = see you next time / Pronunciation : da-eum-e bwa", #4
       "잘가 = Good-bye / Pronunciation : jalga", #5
       "오랜만이에요 = long time no see / Pronunciation : olaenman-ieyo", #6
       "네 = Yes / Pronunciation : ne", #7
       "아니요 = no / Pronunciation : aniyo", #8
       "이건 뭐야? = what's this? / Pronunciation : igeon mwoya?", #9
       "무슨 일 있어? = What's going on?? / Pronunciation : museun il iss-eo?", #10
       "잘했어요! = Good job! / Pronunciation : jal haeso-eo!", #11
       "뭐하고 있어? = What are you doing / Pronunciation : mwohago iss-eo?", #12
       "괜찮아 = it's ok / Pronunciation : gwaenchanh-a", #13
       "고마워 = thank you / Pronunciation : gamsahabnida", #14
       "미안해 = sorry / Pronunciation : mianhae", #15
       "주문할게요 = I'd like to order. / Pronunciation : jumunhalgeyo", #16
       "이상해 = It's weird / Pronunciation : isanghae", #17
       "달라 = to be different / Pronunciation : dalla", #18
       "조심해 = be careful / Pronunciation : josimhae", #19
       "지금 몇시야? = what time is it? / Pronunciation : jigeum myeoch siji?", #20
       "잘 지내고 있어 = I'm doing well / Pronunciation : naneun jal jinaego iss-eo / for instance : How are you doing(eotteohge jinaeyo) answer:I'm doing well(naneun jal jinaego iss-eo)", #21
       "진짜? = Really? / Pronunciation : jinjja?", #22
       "궁금해 = I wonder? / Pronunciation : gung-geumhae", #23
       "맛있어? = Is it good?(food) / Pronunciation : joh-eungayo?", #24
       "어디야? = where are you? / Pronunciation : eodiya?", #25
       "~~에서 태어났어 = I was born in ~~ / Pronunciation : ~~eseo taeeonass-eo", #26
       "어려워 = Difficult / Pronunciation : eolyeowo", #27
       "내가 해냈어! = I made it! / Pronunciation : naega haenaess-eo!", #28
       "이겼어! = I won! / Pronunciation : igyeoss-eo!", #29
       "대박이네 = That's great! / Pronunciation : daebag-ine", #30
       "영어 = English / Pronunciation : yeong-eo", #31
       "한국어 = Korean / Pronunciation : hangug-eo", #32
       "가능해 = It's possible / Pronunciation : ganeunghae", #33
       "~~~를 배운다 = I learn ~~ / Pronunciation : ~~~leul baeunda", #34
       "멋지다! = Cool! / Pronunciation : meosjida!", #35
       "인기있어 = Popular / Pronunciation : ingi iss-eo", #36
       "신난다! = awesome! / Pronunciation : sinnanda", #37
       "번역가 =  translator / Pronunciation : beon-yeogga", #38
       "피곤해 = I'm tired / Pronunciation : pigonhae", #39
       "한국에서 유명한 음식은 무엇인가요? = What is a popular food in Korea? / Pronunciation : hangug-eseo yumyeonghan eumsig-eun mueos-ingayo?", #40
       "먹어도 돼? = can I eat? / Pronunciation : meog-eodo dwae?",
       "놀랐어 = Surprise / Pronunciation : nollass-eo",
       "이건 진짜야 = It's real / Pronunciation : igeon jinjjaya",
       "~로 간다 = I'm going~ / Pronunciation : ~ro ganda",
       "~를 추천해 = I recommend~ / Pronunciation : ~leul chucheonhae",
       "일본어 = Japanese / Pronunciation : ilbon-eo",
       "아침 = morning / Pronunciation : achim",
       "점심 = lunch / Pronunciation : jeomsim",
       "저녁 = dinner / Pronunciation : jeonyeog",
       "끝 = End / Pronunciation : kkeut",
    ]

    await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def tutorial(ctx):
    embed = discord.Embed(title=f"International friend" , description=f"welcome to international friend! I hope you have a great time on the international friend channel!", color=0x00ff56)
    embed.add_field(name=f"Discord Channel" , value=f"what is this channel?: I made new channel for conversation!",inline=False)
    embed.add_field(name=f"Error", value=f"if Jessi,Spring Bot don't have moving?: Soomin logged out of the computer.",inline=False)
    embed.add_field(name=f"Command", value=f"Jessi[hello/Hello/help]----Spring[!korean/!tutorial] ",inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/nifzVtD.gif")
    await ctx.send(embed=embed)

access_token = os.environ['BOT TOKEN']
bot.run("NzU2MDI0NzQ0OTQzNDE5NDAy.X2L06Q.giyht_3KWKnP4tvYflyIXLEuCxY")
