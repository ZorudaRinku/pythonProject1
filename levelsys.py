import discord
from discord import Embed
from discord.ext import commands
from pymongo import MongoClient
from discord.utils import get

general = 845056242644025376
talk_channels = [874828581514145874]
level = ["test", "kind of cool", "really cool", "too cool"]
levelnum = [2, 5, 10]

cluster = MongoClient("mongodb+srv://example:UZOqqs80djqxoB75@dis.l9p6n.mongodb.net/dis?retryWrites=true&w=majority")

levelling = cluster["discord"]["leveling"]

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id  not in talk_channels:
            stats = levelling.find_one({"id" :  message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" :  message.author.id, "xp" : 100}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id" :  message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl -= 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"well done {message.author.mention}! you levelled up to **level: {lvl}**")
                        for i in range(len(level)):
                            if lvl == levelnum[1]:
                                await message.author.add_role(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} you have gotten role **{level[1]}**")
                                embed.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == general:
            stats = levelling.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="you havent sent any mesages rank none")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * (lvl - 1))):
                        break
                    lvl -= 1
                xp -= ((50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort("xp",-1)
                for x in rankings:
                    rank += 1
                    if stats ["id"] == x["id"]:
                        break
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
                embed.add_field(name="Name", value=ctx.author.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="Name", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="progress bar [lvl]", value=boxes * ":blue_square:" + (20-boxes) *":large_white_squares:", inline=True)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)


    @commands.command()
    async def leaderbord(self, ctx):
        if (ctx.channel.id == general):
            rankings = levelling.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(title="Rankings")
            for x in rankings:
              try:
                  temp = ctx.guild.member(x["id"])
                  tempxp = x["xp"]
                  embed.add_field(name=f"{i}: {temp.name}",value=f"Total XP: {tempxp}", inline=False)
                  i+= 1
              except:
                  pass
              if 1 == 11:
                  break
            await ctx.channel.send(embed=embed)
def setup(client):
    client.add_cog(levelsys(client))