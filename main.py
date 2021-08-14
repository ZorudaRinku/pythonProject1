# # import os
import discord
from discord.ext import commands
# from keep_alive import keep_alive
from discord.utils import get
import levelsys

# from keep_alive import keep_alive
botFunctions = ['!help', '!']
client = commands.Bot(command_prefix='?pip')
client.remove_command('help')

cogs = [levelsys]

for i in range(len(cogs)):
    cogs[i].setup(client)



@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(872563973084573706)
    await member.add_roles(muted_role)
    await ctx.send(member.mention + " has been muted")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('why ae you looking at me'))
    print('bot is online')


@client.event
async def on_member_join(member):
    print(f'{member} has joined da server')


@client.event
async def on_member_remove(member):
    print(f"{member} has left the server voluntarily")


@client.event
async def on_ready():
    print('logged in')


@client.command()
async def mute(ctx, member: discord.Member = None):
    if not member:
        return await ctx.send('Define the member.')
    try:
        role = get(ctx.guild.roles, name="stinky")
    except discord.errors.NotFound:
        print("Role not found")
    else:
        await member.add_roles(member, role)


@client.command()
async def hey(ctx):
    await ctx.send('Hello')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None, ):
    await member.kick(reason=reason)
    await ctx.send(f"lmao kicked{member.name}# {member.mention}")


@client.command()
# @commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None, ):
    await member.ban(reason=reason)
    await ctx.send(f"lmao banned {member.name}# {member.mention}")


@client.command()
# @commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'lmao unbanned {user.mention}')
            return


@client.command()
async def Goodbye(ctx):
    await ctx.send('Hello')


def glimmer_i(ctx):
    return ctx.author.id == 730479178440507484


@client.command()
@commands.check(glimmer_i)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def nts(ctx):
    await ctx.send('ew')


@client.command()
async def bruh(ctx):
    await ctx.send(f"bruh {ctx.author} https://tenor.com/view/bruh-bye-ciao-gif-5156041")

    #  def is_it_me(ctx):
    return ctx.author.id == 237478564272799744


@client.command()
# @commands.check(is_it_me)
async def yo(ctx):
    await ctx.send(f"hi im {ctx.author}")


@client.command()
async def sleep(ctx):
    await ctx.send("sleep bad")


@client.command()
async def welcome(ctx):
    await ctx.send("unwelcomes")


@client.command()
async def Welcome(ctx):
    await ctx.send("unwelcomes")


@client.command()
async def pokemon(ctx):
    await ctx.send("yum")


@client.command()
async def Pokemon(ctx):
    await ctx.send("yum")


@client.command()
async def Grinkle(ctx):
    await ctx.send("grinkle")


@client.command()
async def grinkle(ctx):
    await ctx.send("grinkle")


@client.command()
async def Bingus(ctx):
    await ctx.send("bingus")


@client.command()
async def bingus(ctx):
    await ctx.send("bingus")


@client.command()
async def help(ctx):
    await ctx.send(
        "Hello! I'm a bot!\nHere is a list of functions you can try:")

    str = ''
    for item in botFunctions:
        str += (item + '\n')
    await ctx.send(str)


@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    if message.author.bot:  # checks if author is a bot
        return

    await client.process_commands(message)


# my_secret: str = os.environ['TOKEN']

# TOKEN = "ODU1MTk0NzYxNDE3NTg4NzY2.YMu8Lw.8Ezi1GotLRWAixHmH8CivqDpPH4"


# keep_alive()
# client.run(os.getenv("TOKEN"))
client.run("ODU1MTk0NzYxNDE3NTg4NzY2.YMu8Lw.8Ezi1GotLRWAixHmH8CivqDpPH4")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
