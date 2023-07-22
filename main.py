import discord
import lyricsgenius as genius
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from functions import *
api = genius.Genius('75U-mps8ZlaFzoejXvdpSO2p-JiJAmNZ3zJ1ak1Ch_HCyyyTeecYbvgWe_li3tl2')
import os
from dotenv import load_dotenv
load_dotenv()

game = Game

gryffindor_p = 0,
ravenclaw_p = 0,
hufflepuff_p = 0,
slytherin_p = 0

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
intents = discord.Intents.default()
intents.message_content = True

Bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Relatively simple bot example for my portfolio',
    intents=intents,
)
@Bot.event
async def on_message(message):
    if message.author.bot:
        return
###don't mind this
    if message.content == "emo":
        channel = message.channel
        await channel.send("I WAS SITTING IN MY ROOM BLASTING✨MY CHEMICAL ROMANCE✨🖤\nAND MY MOM YELLS TURN THAT GARBAGE DOWN😒\nMY ✨ BLACK EYELINER✨ STREAMS DOWN MY FACE 😦😦\nNO ONE UNDERSTANDS ME 😠😠😠😠 \nBEING TWELVE IS HARDER THAN ANYTHING ELSE💔🥶😣 \nBUT ATLEAST, I HAVE GERARD WAY 🥵🥵🥵🥵🥵")

    if message.content == ('botservers'):
        await message.channel.send("I'm" + str(len(Bot.guilds)) + "that many server!")

###a little turkish joke
    if message.content == ('nerdesin'):
        await message.channel.send("BURDAYIM BE BURDAYIM! SİZ DE BURDASINIZ! BUR DA YIM!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.ctx.send(
        f"{member} Welcome to our server!  https://tenor.com/view/the-office-bow-michael-scott-steve-carell-office-gif-3931556")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(
        f"{member} buh-bye! https://tenor.com/view/friends-lisa-kudrow-phoebe-buffay-good-bye-bye-bye-gif-4621371")
    print(f"{member} buh-bye!  https://tenor.com/view/friends-lisa-kudrow-phoebe-buffay-good-bye-bye-bye-gif-4621371")

game = Game()


@Bot.command()
async def roll(ctx, *args):
    if "dice" in args:
        await ctx.send("{}".format(game.roll_dice()))
    else:
        await ctx.send("what should i do with roll?")

@Bot.command()
async def rolldice(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Should be NdN format!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send('Youre dice: '
                   '{}'.format(result))

@Bot.command()
async def serverinvite(ctx):
    invite_link = await ctx.channel.create_invite(max_uses=1, unique=True)

    embed = discord.Embed(title='Server Invite', description='Invite link:', color=discord.Color.blue())
    embed.set_thumbnail(url="https://i.ibb.co/WnHw1LW/uwp2646598a.png")
    embed.add_field(name='Invite link', value=str(invite_link), inline=False)

    await ctx.send(embed=embed)

@Bot.command()
async def invite(ctx):
    invite_link = "https://discord.com/oauth2/authorize?client_id=959807866963898408&scope=bot&permissions=1099511627775"

    embed = discord.Embed(title='Invite to Server', description='Invite link:', color=discord.Color.blue())
    embed.set_thumbnail(url="https://i.ibb.co/WnHw1LW/uwp2646598a.png")
    embed.add_field(name='Invite link', value=str(invite_link), inline=False)

    await ctx.send(embed=embed)

@Bot.command()
async def sil(ctx, limit:int):

    await ctx.channel.purge(limit=limit)
    await ctx.send(f"{limit} messages deleted.")
    await ctx.send(f"{limit} messages deleted.")

@Bot.command()
async def ship(ctx, member1: discord.Member, member2: discord.Member):
    ship_percentage = random.randint(0, 100)

    if ship_percentage < 30:
        description = f'{member1.display_name} ❤️ {member2.display_name} = %{ship_percentage} please stay away from each oter... 😢'
    elif ship_percentage <= 50:
        description = f'{member1.display_name} ❤️ {member2.display_name} = %{ship_percentage} , a little more effort needed!! 🙂'
    elif ship_percentage < 80:
        description = f'{member1.display_name} ❤️ {member2.display_name} = %{ship_percentage}, you could be good couple 😊'
    elif ship_percentage < 90:
        description = f'{member1.display_name} ❤️ {member2.display_name} = %{ship_percentage}, dammnnn thats so sweet! ❤️'
    else:
        description = f'{member1.display_name} ❤️ {member2.display_name} = %{ship_percentage}, look like soul mates have found each other! 💖'

    embed = discord.Embed(title='Uyum Yüzdesi', color=discord.Color.dark_purple())
    embed.add_field(name='Kullanıcılar', value=f'{member1.display_name} ve {member2.display_name}', inline=False)
    embed.add_field(name='Uyum Yüzdesi', value=f'%{ship_percentage}', inline=False)
    embed.add_field(name='Sonuç', value=description, inline=False)

    await ctx.send(embed=embed)

###this is all turkish

@Bot.command()
async def sorting_hat(ctx):
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    question_1 = await ctx.send(
        "Kendini nasıl tanımlarsın? \na) cesur \nb) çalışkan \nc) sadık \nd) hırslı\n")
    await asyncio.sleep(1)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await Bot.wait_for('message', check=check, timeout=None)

    if msg.content == "a":
        gryffindor += gryffindor + 1
    elif msg.content == "b":
        ravenclaw += 1
    elif msg.content == "c":
        hufflepuff += 1
    elif msg.content == "d":
        slytherin += 1

    question_2 = await ctx.send(
        "Haftasonu ne yaparsın \na) Maceradan maceraya akarım \nb) Ödevlerimi yaparım \nc) Arkadaşlarımla ve ailemle zaman geçiririm \nd) Düşmanlarımdan intikam almak için plan yaparım\n")
    await asyncio.sleep(1)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await Bot.wait_for('message', check=check, timeout=None)

    if msg.content == "a":
        gryffindor += 1
    elif msg.content == "b":
        ravenclaw += 1
    elif msg.content == "c":
        hufflepuff += 1
    elif msg.content == "d":
        slytherin += 1

    q3_answer = await ctx.send(
        "Karanlık lord okulu işgal etse ne yaparsın? \na) Savaşırdım! \nb) Lanetlere karşı savunma kitabı arardım. \nc) Arkadaşlarımın yanında olurdum. Ne olursa olsun. \nd) Karanlık Lord'a okulun içinden yardım ederdim\n")
    await asyncio.sleep(1)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await Bot.wait_for('message', check=check, timeout=None)

    if msg.content == "a":
        gryffindor += 1
    elif msg.content == "b":
        ravenclaw += 1
    elif msg.content == "c":
        hufflepuff += 1
    elif msg.content == "d":
        slytherin += 1

    if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
        await ctx.send("GRYFFINDOR!!!!!!")
    elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
        await ctx.send("RAVENCLAW!!!!!!")
    elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
        await ctx.send("HUFFLEPUFF!!!!!!")
    elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
        await ctx.send("SLYTHERIN!!!!!!")
    else:
        await ctx.send("Hmmm... Karar vermekte zorlanıyorum bir daha denemelisin.")

###This all turkish too. If you want to translate it. It's from first book of Harry Potter that describe the house stereotypes with poems.

@Bot.command()
async def houses(ctx):
    q1_answer = await ctx.send(
        "Hangi bina hakkında bilgi almak istiyorsun?  \nGryffindor  \nSlytherin  \nHufflepuff  \nRavenclaw")
    await asyncio.sleep(1)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await Bot.wait_for('message', check=check, timeout=None)

    if msg.content == "Gryffindor":
        await ctx.send(
            "Seni Gryffindor’a yollarım belki \nZamanla olursun aslanın teki  \nYiğittir Gryffindor’da kalan çocuklar  \nHepsinin yüreği, nah, mangal kadar")
    if msg.content == "gryffindor":
        await ctx.send(
            "Seni Gryffindor’a yollarım belki \nZamanla olursun aslanın teki  \nYiğittir Gryffindor’da kalan çocuklar  \nHepsinin yüreği, nah, mangal kadar")
    if msg.content == "gry":
        await ctx.send(
            "Seni Gryffindor’a yollarım belki \nZamanla olursun aslanın teki  \nYiğittir Gryffindor’da kalan çocuklar  \nHepsinin yüreği, nah, mangal kadar")
    if msg.content == "Hufflepuff":
        await ctx.send(
            "Belki de düşersin Hufflepuff’a  \nHaksızlığı hemen kaldırıp rafa  \nAdalet uğruna savaş verirsin  \nHer yere mutluluk götürmek için")
    if msg.content == "hufflepuff":
        await ctx.send(
            "Belki de düşersin Hufflepuff’a  \nHaksızlığı hemen kaldırıp rafa  \nAdalet uğruna savaş verirsin  \nHer yere mutluluk götürmek için")
    if msg.content == "huff":
        await ctx.send(
            "Belki de düşersin Hufflepuff’a  \nHaksızlığı hemen kaldırıp rafa  \nAdalet uğruna savaş verirsin  \nHer yere mutluluk götürmek için")
    if msg.content == "Ravenclaw":
        await ctx.send(
            "Ravenclaw kısmetin belki  \nOradakilerin hiç çıkmaz sesi  \nMantıktır onlarca önemli olan  \nÖyle kurtulurlar tüm sorunlardan")
    if msg.content == "ravenclaw":
        await ctx.send(
            "Ravenclaw kısmetin belki  \nOradakilerin hiç çıkmaz sesi  \nMantıktır onlarca önemli olan  \nÖyle kurtulurlar tüm sorunlardan")
    if msg.content == "rav":
        await ctx.send(
            "Ravenclaw kısmetin belki  \nOradakilerin hiç çıkmaz sesi  \nMantıktır onlarca önemli olan  \nÖyle kurtulurlar tüm sorunlardan")
    if msg.content == "Slytherin":
        await ctx.send(
            "Düşersin belki de Slytherin’e sen  \nBir başkadır sanki oraya giden  \nAmaçları için neler yapmazlar  \nAçıklasam bitmez sabaha kadar")
    if msg.content == "slytherin":
        await ctx.send(
            "Düşersin belki de Slytherin’e sen  \nBir başkadır sanki oraya giden  \nAmaçları için neler yapmazlar  \nAçıklasam bitmez sabaha kadar")
    if msg.content == "sly":
        await ctx.send(
            "Düşersin belki de Slytherin’e sen  \nBir başkadır sanki oraya giden  \nAmaçları için neler yapmazlar  \nAçıklasam bitmez sabaha kadar")

### I leaved it turkish too because it's fully customizable.

@Bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title='Yardım', description='!yardım ... şeklinde kullabilirsiniz', color=discord.Color.light_grey())
    embed.add_field(name='Yardım kategorileri:', value='Moderasyon, Eğlence, Araçlar', inline=False)

    await ctx.send(embed=embed)



@help.command()
async def moderation(ctx):
    embed = discord.Embed(title='moderasyon', description='Moderasyonla ilgili komutları burada bulabilirsiniz', color=discord.Color.blue())
    embed.add_field(name='Daha bir şey eklemedik...', value='Bakacak bir şey yok... 🥹', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def tools(ctx):
    embed = discord.Embed(title='Araçlar', description='İşinize yarayabilecek, kolaylaştırabilecek çeşitli araçlar 😊', color=discord.Color.blue())
    embed.add_field(name='sil', value='!sil <miktar> şeklinde kullanılır. Belirtilen miktarda mesaj silinir', inline=False)
    embed.add_field(name='lyr', value='!lyr <şarkıadı> - <sanatçadı> şeklinde kullanılır.', inline=False)
    embed.add_field(name='sunucu', value='!sunucu şeklinde kullanılır. Sunucu hakkında bilgi verir. Kaç kişi var hangi bölgede vb.', inline=False)
    embed.add_field(name='davet', value='!davet şeklinde kullanılır.Botumuzun davet linkini bu şekilde bulabilirisiniz 😊', inline=False)

    await ctx.send(embed=embed)



@help.command()
async def fun(ctx):
    embed = discord.Embed(title='Eğlence', description='Eğlence ilgili komutları burada bulabilirsiniz',color=discord.Color.blue())
    embed.add_field(name='seçmen şapka', value='!seçmen_şapka şeklinde kullanılır. Hangi binada olduğunuzu öğrenebilirsiniz.', inline=False)
    embed.add_field(name='binalar', value='!binalar şeklinde kullanılır. Bütün Hogwarts binaları hakkında kitapta yazılan şiirlerden alıntı olarak bilgi edineiblirisniz.', inline=False)
    embed.add_field(name='zar', value='!zar at şeklinde kullanılır.Basitçe 6 üzerinden zar atar', inline=False)
    embed.add_field(name='zarat', value='!zarat 1d10 şeklinde kullanılır. İstediğiniz sayıda istediğiniz yüzlü zar atabilirisniz. d harfinin soluna yazacağınız sayı kaç zar atacağınızı, sağına yazacağınız sayı kaç yüzlü olacağını belirler.', inline=False)
    embed.add_field(name='xox', value='!xox @birincioyuncu @ikincioyuncu şeklinde kullanılır. Oyun başladıktan sonra !y <yer> olarak yerleştirebilirisniz.', inline=False)
    embed.add_field(name='ship', value='!ship @birincikullanıcı @ikincikullanıcı şeklinde kullanılır. İki kişi arasındaki uyumu gösterir 🫢', inline=False)

    await ctx.send(embed=embed)
@Bot.command()
async def lyr(ctx, *arg):
    string = ''  # empty string to store user input(arg)
    a = ''  # empty string to store artist name
    s = ''  # empty string to store song name
    string = arg

    if len(arg) == 0:  # if no input from the user
        embed = discord.Embed(
            title="Error",
            description="Search like this: Barış Manço - Bu son olsun ",
            colour=discord.Colour.from_rgb(255, 7, 58)
        )
        await ctx.channel.send(embed=embed)

    for str in string:
        if (str == '-'):
            break
        a = a + " " + str

    a

    lyrics_list = []  # list to store lyrics of the song
    s_ = string[string.index('-'): len(string)]  # Slicing method
    for _s in s_:
        if (_s == '-'):
            continue
        s = s + " " + _s

    s

    if len(arg) != 0:
        await ctx.channel.send("Searching for song {} - {} ...".format(s, a))
        song = api.search_song(s, a)
        if song:
            url = song.url
            await ctx.channel.send("There is a link:\n{}".format(url))
            lyrics = song.lyrics.split("\n")
            for line in lyrics:
                if line == '':
                    lyrics.remove(line)
                else:
                    lyrics_list.append(line)

            lyrics_list[:-2]

            embed = discord.Embed(
                title='Embedded lyrics',
                description='\n'.join(lyrics_list),
                colour=discord.Colour.from_rgb(57, 255, 20)
            )

            await ctx.channel.send(embed=embed)

@Bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Info",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@Bot.event
async def on_ready():
    print(f'Logged in as {Bot.user} (ID: {Bot.user.id})')
    print('------')
    botactivity = discord.Activity(type=discord.ActivityType.listening,
                                   name="!help",
                                   large_image_url='https://i.ibb.co/YdDWB1S/Ekran-g-r-nt-s-2023-02-25-050618.png')
    await Bot.change_presence(activity=botactivity, status=discord.Status.online)

if __name__ == "__main__" :
    Bot.run(os.getenv('DISCORD_TOKEN'))
