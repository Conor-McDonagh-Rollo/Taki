import discord 
import tweepy
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "taki ")

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
    print("client is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments!")


@client.command()
async def ping(ctx):
    print("Pinging")
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["monke", "monki", "monkie"])
async def monkey(ctx):
    print("Mmmmm Monke")
    monkeys = ["https://media1.tenor.com/images/41cc7fff9a89471443ba89c1578e2a52/tenor.gif",
                "https://media1.tenor.com/images/090a55f65d9be8da56372f8db6d1a551/tenor.gif",
                "https://media1.tenor.com/images/4622084b9398de186f3219b6b07b1ddb/tenor.gif",
                "https://media1.tenor.com/images/783975700609747c3a6a992becc369a3/tenor.gif",
                "https://media1.tenor.com/images/c9dc51406b3f5c810ee17ee90fc6d6c3/tenor.gif",
                "https://media1.tenor.com/images/96209b4b17b56c855217eda1b8c27498/tenor.gif"]
    monke=discord.Embed(title="Mmmm Monke")
    monke.set_image(url=f"{random.choice(monkeys)}")
    await ctx.send("Monkey",embed=monke)

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
    if message.content.startswith("taki authenticate"):
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
            L = [apikey,"\n", apikey_secret,"\n", accesstoken,"\n", accesstoken_secret] #write tokens
            authenticator.writelines(L) 
            authenticator.close() #close file stream
            verify(apikey, apikey_secret, accesstoken, accesstoken_secret)

    await client.process_commands(message)



client.run("NzgzMDczMTE0NTAxMjgzODkw.X8Vbqw.jAtubQ7-9BTw4FlUH2ovVBIc-1s")