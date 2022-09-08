import discord 
import tweepy
import random
import praw
import datetime
import wikipedia
from discord.ext import commands

client = commands.Bot(command_prefix = "taki ", case_insensitive=True)
client.remove_command("help")

reddit = praw.Reddit(client_id="", # Keys must be kept safe
                     client_secret="", # Keys must be kept safe
                     password="", # Keys must be kept safe
                     user_agent="bot taki",
                     username="taki-bot")
print(reddit.user.me())

try:
    authenticator = open("authenticator.taki","r+") 
    client.keys = [line.rstrip() for line in authenticator] #0 = api, 1 = apisecret, 2 = accesstoken, 3 = accesstokensecret
    authenticator.close()
except:
    client.keys = []
    pass

def verify(apikey, apikey_secret, accesstoken, accesstoken_secret):
    client.keys = [apikey, apikey_secret, accesstoken, accesstoken_secret] #0 = api, 1 = apisecret, 2 = accesstoken, 3 = accesstokensecret

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("taki help ~"))
    print("client is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments!")
    else:
        await ctx.send(f"An error occurred.\nError: `{error}`")


@client.command()
async def ping(ctx):
    print("Pinging")
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def help(ctx):
    print("Helping a cutie")
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Cute help menu:", colour=value)
    embed.add_field(name="Image Commands:", value="taki monkey\ntaki jojo\ntaki wholesome\ntaki meme\ntaki dank", inline=True)
    embed.add_field(name="Cool Commands:", value="taki tweet <Your Tweet>\ntaki 8ball <Your Question?>\ntaki kill <Victim>\ntaki fact <Topic>\ntaki fact random", inline=True)
    embed.add_field(name="System Commands:", value="taki ping\ntaki authenticate\ntaki authhelp\ntaki authshow", inline=True)
    await ctx.send("",embed=embed)

@client.command()
async def authhelp(ctx):
    print("Helping a technical cutie")
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Cute advanced help menu OwO:", colour=value)
    embed.add_field(name="Follow this guide to Authenticate you twitter!", value="Step 1: Create a new twitter for your bot!\nStep 2: Sign up to Twitter Developer and create a new application!\nStep 3: Go into your app settings and change it to read and write!\nStep 4: Get your tokens and regenerate them all!\nStep 5: Use 'taki authenticate' and give taki the keys he asks for!", inline=True)
    await ctx.send("",embed=embed)

@client.command()
async def christmas(ctx):
    print("CHRISTMAS")
    today = datetime.date.today()
    x = datetime.datetime.now()
    christmas = datetime.date(int(x.strftime("%Y")), 12, 25)
    diff = christmas - today
    msg = ["GET YOUR STOCKING READY", "Time to put up the tree yet?", "Clear out the fireplace!", "Snow is falling, All around us-", "ALL I WANT FOR CHRISTMAS IS-", "Crhistmasasfa TIMEAdiadmi", "Sitting by the fire...", ":D", ":3", "YES"]
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title=f"{diff.days} DAYS UNTIL CHRISTMAS", description=f"{random.choice(msg)}", colour=value)
    await ctx.send("",embed=embed)

@client.command()
async def fact(ctx, *, fact):
    print("Cute fact for a cute person")
    if fact != "random":
        result = wikipedia.search(fact)
        try:
            page = wikipedia.page(result[0])
        except wikipedia.exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[0])
    else:
        result = wikipedia.random(pages=10)
        try:
            page = wikipedia.page(result[0])
        except wikipedia.exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[0])
        
    desc = wikipedia.summary(page, sentences=5)
    if len(desc) > 2000:
        desc = desc[:2000] + "..."

    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title=f"{page.title}", description=f"{desc}", colour=value)
    embed.set_image(url=f"{page.images[0]}")
    embed.set_footer(text=f"{page.url}")
    await ctx.send("",embed=embed)

@client.command()
async def kill(ctx, member: discord.Member):
    print(f"{ctx.author.display_name} is killing {member.display_name}")

    if ctx.author.display_name != member.display_name:
        deaths = ["kills", "stabs", "slaughters", "assassinates", "murders", "erases", "exterminates"]
        murders = ["https://media1.tenor.com/images/a80b2bf31635899ac0900ea6281a41f6/tenor.gif",
                    "https://media1.tenor.com/images/eb7fc71c616347e556ab2b4c813700d1/tenor.gif",
                    "https://media1.tenor.com/images/2c945adbbc31699861f411f86ce8058f/tenor.gif",
                    "https://media1.tenor.com/images/af100ce94589c2f10c7aaadb3a5b27cb/tenor.gif",
                    "https://media1.tenor.com/images/c8e45541220b07e444e77b814feee38c/tenor.gif",
                    "https://media1.tenor.com/images/862272da6f71b28b53ec262bcca6763a/tenor.gif",
                    "https://media1.tenor.com/images/79cc6480652032a20f1cb5c446b113ae/tenor.gif",
                    "https://media1.tenor.com/images/3daa078c7128766260beea97172e5c46/tenor.gif",
                    "https://media1.tenor.com/images/48db9d669598ddc1257c612faad38c5e/tenor.gif",
                    "https://media1.tenor.com/images/b55aace72003e3fa100c208c8fefe250/tenor.gif"]
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(title=f"{ctx.author.display_name} {random.choice(deaths)} {member.display_name}", colour=value)
        embed.set_image(url=f"{random.choice(murders)}")
        await ctx.send("",embed=embed)
    else:
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(title=f"F for {ctx.author.display_name}", colour=value)
        embed.set_image(url="https://media1.tenor.com/images/bd67f01a9865f798a70a0ec0ac9c3d3c/tenor.gif?itemid=13980130")
        await ctx.send("",embed=embed)

@client.command(aliases=["monkey", "monke", "monki", "monkie"])
async def _monkey(ctx):
    print("Mmmmm Monke")
    monkeys = ["https://media1.tenor.com/images/41cc7fff9a89471443ba89c1578e2a52/tenor.gif",
                "https://media1.tenor.com/images/090a55f65d9be8da56372f8db6d1a551/tenor.gif",
                "https://media1.tenor.com/images/4622084b9398de186f3219b6b07b1ddb/tenor.gif",
                "https://media1.tenor.com/images/783975700609747c3a6a992becc369a3/tenor.gif",
                "https://media1.tenor.com/images/c9dc51406b3f5c810ee17ee90fc6d6c3/tenor.gif",
                "https://media1.tenor.com/images/96209b4b17b56c855217eda1b8c27498/tenor.gif",
                "https://media1.tenor.com/images/77b68c1e9feb33920aee2ae4088da8f3/tenor.gif",
                "https://media1.tenor.com/images/41c13b91b659560c14b2e4c1506bc09e/tenor.gif",
                "https://media1.tenor.com/images/aabd9011da88425a21bdc8601588842d/tenor.gif",
                "https://media1.tenor.com/images/b54c6fca05181a2aa49f55b35e52dd7f/tenor.gif",
                "https://media1.tenor.com/images/ae96ee628ef967b0e7dcdc4b3dbff0e8/tenor.gif",
                "https://media1.tenor.com/images/211b4be1f3ac71d07f57e838a373558e/tenor.gif"]
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Mmmm Monke", colour=value)
    embed.set_image(url=f"{random.choice(monkeys)}")
    await ctx.send("Monkey",embed=embed)

@client.command(aliases=["kinky", "bdsm"])
@commands.is_nsfw()
async def kink(ctx):
    print("Someone is sinning")
    top25 = []
    subreddit = reddit.subreddit("BDSMGW")
    posts = subreddit.hot(limit=25)
    for post in posts:
        top25.append(post)
    pick = random.choice(top25)
    if pick.title == "Mild Megathread - Share your mild images here!":
        pick = random.choice(top25)
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title=f"{pick.title}", colour=value)
    embed.set_image(url=f"{pick.url}")
    embed.set_footer(text=f"Sauce: {pick.url}")
    await ctx.send("",embed=embed)

@client.command(aliases=["crusade", "jo"])
async def jojo(ctx):
    print("Grabbing jojo ass...")
    top25 = []
    subreddit = reddit.subreddit("ShitPostCrusaders")
    posts = subreddit.hot(limit=25)
    for post in posts:
        top25.append(post.url)
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="So you're approaching me?", colour=value)
    embed.set_image(url=f"{random.choice(top25)}")
    await ctx.send("",embed=embed)

@client.command(aliases=["cute"])
async def wholesome(ctx):
    print("Cute meme for a cute person")
    top25 = []
    subreddit = reddit.subreddit("wholesomememes")
    posts = subreddit.hot(limit=25)
    for post in posts:
        top25.append(post.url)
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Cute meme for a cute person :3", colour=value)
    embed.set_image(url=f"{random.choice(top25)}")
    await ctx.send("",embed=embed)

@client.command()
async def meme(ctx):
    print("Big funny meme")
    top25 = []
    subreddit = reddit.subreddit("memes")
    posts = subreddit.hot(limit=25)
    for post in posts:
        top25.append(post.url)
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Big funny below", colour=value)
    embed.set_image(url=f"{random.choice(top25)}")
    await ctx.send("",embed=embed)

@client.command()
async def dank(ctx):
    print("Big funny dank meme")
    top25 = []
    subreddit = reddit.subreddit("dankmemes")
    posts = subreddit.hot(limit=25)
    for post in posts:
        top25.append(post.url)
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="Big dank funny below", colour=value)
    embed.set_image(url=f"{random.choice(top25)}")
    await ctx.send("",embed=embed)

@commands.cooldown(1, 300, commands.BucketType.user)
@client.command(aliases=["tw"])
async def tweet(ctx, *, msg):
    auth = tweepy.OAuthHandler(client.keys[0], client.keys[1])
    auth.set_access_token(client.keys[2], client.keys[3])
    api = tweepy.API(auth)
    print(f"Taki just tweeted {msg}")
    value = random.randint(0, 0xffffff)
    embed=discord.Embed(title="{0} just tweeted".format(ctx.author), colour=value)
    embed.add_field(name="{0}".format(msg), value="At {0}".format(datetime.datetime.now().date()), inline=True)
    await ctx.send("", embed=embed)
    api.update_status(msg)
    print("tweeted")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    print("Shaking 8ball")
    responses = ["It is certain",
                "Without a doubt",
                "You may rely on it",
                "Yes definitely",
                "It is decidedly so",
                "As I see it, yes",
                "Most likely",
                "Yes",
                "Outlook good",
                "Signs point to yes",
                "Reply hazy try again",
                "Better not tell you now",
                "Ask again later",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don’t count on it",
                "Outlook not so good",
                "My sources say no", 
                "Very doubtful",
                "My reply is no"]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
@client.event
@commands.has_permissions(administrator=True)
async def authshow(ctx):
    print("Showing API keys")
    await ctx.send("__**Your API keys are as follows:**__")
    await ctx.send(f"**API:**  {client.keys[0]}\n**API_SECRET:**  {client.keys[1]}\n**ACCESS_TOKEN:**  {client.keys[2]}\n**ACCESS_TOKEN_SECRET:**  {client.keys[3]}")

@client.event
async def on_message(message):
    if message.content.startswith("taki authenticate") and message.author.guild_permissions.administrator:
        print("attempting to authenticate")
        #API key auth

        channel = message.channel
        await channel.send("Please enter your **API key!**")

        def check1(author):
            def check_msg(message): 
                if message.author != author:
                    return False
                try: 
                    str(message.content) 
                    return True 
                except ValueError: 
                    return False
            return check_msg

        try:
            key = await client.wait_for('message', check=check1(message.author), timeout=60)
            apikey = key.content
            await key.delete()
        except:
            pass
        else:
            await channel.send("*Key has been stored successfully!*")

        #API Secret key auth
        
        await channel.send("Please enter your **API Secret key!**")

        def check2(author):
            def check_msg(message): 
                if message.author != author:
                    return False
                try: 
                    str(message.content) 
                    return True 
                except ValueError: 
                    return False
            return check_msg

        try:
            key = await client.wait_for('message', check=check2(message.author), timeout=60)
            apikey_secret = key.content
            await key.delete()
        except:
            pass
        else:
            await channel.send("*Key has been stored successfully!*")

        #accesstoken key auth
        
        await channel.send("Please enter your **Access Token!**")

        def check3(author):
            def check_msg(message): 
                if message.author != author:
                    return False
                try: 
                    str(message.content) 
                    return True 
                except ValueError: 
                    return False
            return check_msg

        try:
            key = await client.wait_for('message', check=check3(message.author), timeout=60)
            accesstoken = key.content
            await key.delete()
        except:
            pass
        else:
            await channel.send("*Key has been stored successfully!*")

        #accesstoken secret key auth
        
        await channel.send("Please enter your **Access Token Secret!**")

        def check4(author):
            def check_msg(message): 
                if message.author != author:
                    return False
                try: 
                    str(message.content) 
                    return True 
                except ValueError: 
                    return False
            return check_msg

        try:
            key = await client.wait_for('message', check=check4(message.author), timeout=60)
            accesstoken_secret = key.content
            await key.delete()
        except:
            pass
        else:
            await channel.send("*Key has been stored successfully!*")

            authenticator = open("authenticator.taki","a+") #open file in append mode
            authenticator.close()
            authenticator = open("authenticator.taki","r+")
            authenticator.truncate(0)
            L = [apikey,"\n", apikey_secret,"\n", accesstoken,"\n", accesstoken_secret] #write tokens
            authenticator.writelines(L) 
            authenticator.close() #close file stream
            verify(apikey, apikey_secret, accesstoken, accesstoken_secret)

    await client.process_commands(message)



client.run("") # Keys must be kept safe
