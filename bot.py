import discord
from discord.ext import commands
from fonksiyonlar import *
import os,random
from yeni import *



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

# img_list = os.listdir("images")
# img = random.choice(img_list)
# print(img)

@bot.command()
async def yazı(ctx):
    await ctx.send("Dünyamız, yaşamımızı sürdürdüğümüz tek evimizdir. Ancak, giderek artan kirlilik sorunu, bu değerli kaynağın sağlığını ve güzelliğini tehdit etmektedir. Kirliliğin yaygın etkileri arasında hava, su ve toprak kirliliği bulunur; bu da ekosistemlerin dengesini bozabilir, insan sağlığını tehlikeye atabilir ve biyolojik çeşitliliği azaltabilir.")


    

        

@bot.command()
async def rakam(ctx):
    a=random.randint(1,100)
    await ctx.send(a)

@bot.command()
async def islem(ctx):
    sayi1=random.randint(1,10)
    sayi2=random.randint(10,20)
    taplam=sayi1+sayi2
    await ctx.send(f"{sayi1} + {sayi2} = {taplam}")


@bot.command()
async def random_m(ctx):
    img_list = os.listdir('images')
    img = random.choice(img_list)
    with open(f'images/{img}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


bot.run("")
