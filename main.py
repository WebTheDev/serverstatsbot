import discord
import asyncio
import sys
from discord.ext import commands
from discord.ext.tasks import loop
from discord.ext.commands import Bot
from discord.utils import get
from config import token, CommandPrefix, activitytype, botstatusmessage, embedcolor, developerid, statscooldownamount, guildID, IDofChannelForServerMembers, NameofStatsChannel1, Role1CountCheckEnabled, IDofChannelForRole1Check, NameofRole1Channel, ServerMembersCheckEnabled, IDofRole1, BotCountCheckEnabled, IDofChannelForBotCheck, NameofBotChannel, BansCountCheckEnabled, IDofChannelForBansCheck, NameofBansChannel, Role2CountCheckEnabled, IDofChannelForRole2Check, IDofRole2, NameofRole2Channel

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=CommandPrefix, intents=intents)
bot.remove_command('help')

def filterOnlyBots(member):
    return member.bot

@loop(seconds=statscooldownamount)
async def checkallmembers():
    try:
        guild = bot.get_guild(guildID)
        MembersInServerCount = len(guild.members)
        tchannel1 = get(guild.channels, id=IDofChannelForServerMembers)
        amount1 = (MembersInServerCount)
        prevtname = str(f'{NameofStatsChannel1}{amount1}')
        tname = tchannel1.name
        if prevtname == tname:
            pass
        elif prevtname != tname:
            await tchannel1.edit(name=f'{NameofStatsChannel1}{amount1}')
    except Exception as e:
        developer = get(guild.members, id=developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='checkallmembers function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("checkallmembers loop fail\n" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")

@loop(seconds=statscooldownamount)
async def checkrole1():
    try:
        guild = bot.get_guild(guildID)
        tchannel2 = get(guild.channels, id=IDofChannelForRole1Check)
        Role = get(guild.roles, id=IDofRole1)  
        Rolecount = len(Role.members)
        tname2 = tchannel2.name
        prevtname2 = str(f'{NameofRole1Channel}{Rolecount}')
        if prevtname2 == tname2:
            pass
        elif prevtname2 != tname2:
            await tchannel2.edit(name=f'{NameofRole1Channel}{Rolecount}')
    except Exception as e:
        developer = get(guild.members, id=developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='checkrole1 function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("checkrole1 loop fail\n" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")

@loop(seconds=statscooldownamount)
async def checkrole2():
    try:
        guild = bot.get_guild(guildID)
        tchannel6 = get(guild.channels, id=IDofChannelForRole2Check)
        Role = get(guild.roles, id=IDofRole2)  
        Rolecount = len(Role.members)
        tname6 = tchannel6.name
        prevtname6 = str(f'{NameofRole2Channel}{Rolecount}')
        if prevtname6 == tname6:
            pass
        elif prevtname6 != tname6:
            await tchannel6.edit(name=f'{NameofRole2Channel}{Rolecount}')
    except Exception as e:
        developer = get(guild.members, id=developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='checkrole2 function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("checkrole2 loop fail\n" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")

@loop(seconds=statscooldownamount)
async def checkbots():
    try:
        guild = bot.get_guild(guildID)
        tchannel4 = bot.get_channel(IDofChannelForBotCheck)
        MembersInServer = guild.members
        Bots = list(filter(filterOnlyBots, MembersInServer))
        botcount = len(Bots)
        prevtname4 = str(f'{NameofBotChannel}{botcount}')
        tname4 = tchannel4.name
        if prevtname4 == tname4:
            pass
        elif prevtname4 != tname4:
            await tchannel4.edit(name=f'{NameofBotChannel}{botcount}')
    except Exception as e:
        developer = get(guild.members, id=developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='checkbots function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("checkbots loop fail\n" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")

@loop(seconds=statscooldownamount)
async def checkbans():
    try:
        guild = bot.get_guild(guildID)
        tchannel5 = get(guild.channels, id=IDofChannelForBansCheck)
        bans = await guild.bans()
        bans2 = (len(bans))
        prevtname5 = str(f'{NameofBansChannel}{bans2}')
        tname5 = tchannel5.name
        if prevtname5 == tname5:
            pass
        elif prevtname5 != tname5:
            await tchannel5.edit(name=f'{NameofBansChannel}{bans2}')
    except Exception as e:
        developer = get(guild.members, id=developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='checkbans function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("checkbans loop fail\n" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    activity2 = discord.Activity(type=discord.ActivityType.playing, name="booting...")
    await bot.change_presence(status=discord.Status.idle, activity=activity2)
    print("\n/////////////////////////////////")
    print("//                             //")
    print("//        ServerStatsBot       //")
    print("//                             //")
    print("/////////////////////////////////\n")
    print("Bot Infomation:")
    print ("------------------------------------")
    print (f"Bot Name: {bot.user.name}#{bot.user.discriminator}")
    print (f"Bot ID: {bot.user.id}")
    creator = bot.get_user(387002430602346499)
    print(f'Creator: {creator}')
    print ("Discord Version: " + discord.__version__)
    guild = bot.get_guild(guildID)
    print(f'Operating Guild Name: {guild}')
    print ("-----------------------------------------")
    print("[MESSAGE]: Bot has logged into discord sucessfully.")
    print("----------------------------------------------------")
    await asyncio.sleep(2)
    print("Loops Enabled/Diabled Self Check:")
    if ServerMembersCheckEnabled == True:
        print(f'Checkallmembers: Enabled')
    else:
        print(f'Checkallmembers: Disabled')
    if Role1CountCheckEnabled == True:
        print(f'Checkrole1: Enabled')
    else:
        print(f'Checkrole1: Disabled')
    if Role2CountCheckEnabled == True:
        print(f'Checkrole2: Enabled')
    else:
        print(f'Checkrole2: Disabled')
    if BotCountCheckEnabled == True:
        print(f'Checkbots: Enabled')
    else:
        print(f'Checkbots: Disabled')
    if BansCountCheckEnabled == True:
        print(f'Checkbans: Enabled')
    else:
        print(f'Checkbans: Disabled')
    print("----------------------------------------------------")
    print(f'[MESSAGE]: Starting enabled loops')
    print("----------------------------------------------------")
    await asyncio.sleep(1)
    try:
        if ServerMembersCheckEnabled == True:
            checkallmembers.start()
            await asyncio.sleep(1)
        else:
            pass
        if Role1CountCheckEnabled == True:
            checkrole1.start()
            await asyncio.sleep(1)
        else:
            pass
        if Role2CountCheckEnabled == True:
            checkrole2.start()
            await asyncio.sleep(1)
        else:
            pass
        if BotCountCheckEnabled == True:
            checkbots.start()
            await asyncio.sleep(1)
        else:
            pass
        if BansCountCheckEnabled == True:
            checkbans.start()
            await asyncio.sleep(1)
        else:
            pass
        print("[MESSAGE:] All enabled loops started sucessfully")
        print("----------------------------------------------------")
    except Exception as r:
        developer = get(guild.members, id=developerid)
        embed = discord.Embed(title='`On_Ready Function Fail (Enabled Loops Start Fail)`', description=f'{str(r)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("On_Ready Function Fail (Enabled Loops Start Fail)\n" + str(r))
        print("[ERROR]: Enabled loops were attempted to start running but an error occurred, the loops are most likely already running, more details have been sent to the developer specified in the config")
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("------------------------------------")
    if f'{activitytype}' == 'Playing':
        activity1 = discord.Activity(type=discord.ActivityType.playing, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Streaming':
        activity1 = discord.Activity(type=discord.ActivityType.streaming, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Watching':
        activity1 = discord.Activity(type=discord.ActivityType.watching, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Listening':
        activity1 = discord.Activity(type=discord.ActivityType.listening, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    else:
        activity1 = discord.Activity(type=discord.ActivityType.playing, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
        print('''[WARN]: You have incorrectly specified the bot's activity type, the default has been selected. ''')
        print("----------------------------------------------------")
    print("[MESSAGE]: Bot is ready!")
    print("------------------------------------")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        message1 = ctx.message
        await message1.delete()
        author = ctx.message.author
        message2 = await ctx.send(f'{author.mention}')
        await message2.delete()
        embed = discord.Embed(description=f'''{author.mention}, Huh? I don't know that command!''', color=embedcolor)
        embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
        embed.add_field(name='**__Debug Error:__**', value=f'```discord.ext.commands.errors.CommandNotFound: {error}```')
        embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=bot.user.avatar_url)
        try:
            message3 = await ctx.send(embed=embed)
        except discord.HTTPException:
            message3 = await ctx.send(f'''{author.mention}, I don't know that command!''')
        await asyncio.sleep(15)
        await message3.delete()


@bot.event
async def on_message(message):
    try:
        await bot.process_commands(message)
        if message.content.startswith(f"<@!{bot.user.id}>") or message.content.startswith(f"<@{bot.user.id}>"):
            latency = bot.latency * 1000
            embed = discord.Embed(description=f'Hi there! I see that you have mentioned me! My latency is **{latency:.2f}ms**.', color=embedcolor)
            embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=bot.user.avatar_url)
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=True)
                except discord.HTTPException:
                    await message.reply(f'Hi there! I see that you have mentioned me! My latency is **{latency:.2f}ms**``.', mention_author=True)
            except Exception:
                pass
        else:
            pass
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='on_message event fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("on_message event fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")


@bot.command()
async def logout(ctx):
    try:
        message1 = ctx.message
        author = ctx.message.author
        if author.id == developerid:
            await message1.add_reaction('✅')
            await bot.logout()
        else:
            await message1.delete()
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(description=f'''{author.mention}, you can't use that command! ❌''', color=embedcolor)
            embed5.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=bot.user.avatar_url) 
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(f'''{author.mention}, **you can't use that command! ❌**''')
            await asyncio.sleep(20)
            await message6.delete()
    except Exception as e:
        message2 = await ctx.send(f'{author.mention} a unknown error has occurred, a copy of the error has been sent to the developer ❌')
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.logout function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.logout function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 
        await asyncio.sleep(10)
        await message2.delete()

try:
    bot.run(f'{token}')
except Exception as e:
    print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
