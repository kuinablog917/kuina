import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# 許可するロール名（例: 'admin'）
ALLOWED_ROLE_NAME = 'クイナロール'

# 制限するワードのリストを指定します
RESTRICTED_WORDS = [
    'ワード1',
    'ワード2',
    'ワード3',
    # 必要なワードを追加してください
]

@bot.event
async def on_ready():
    print(f' {bot.user}ログインしました')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "占い" in message.content.lower():
        ohayo = ["今日の運勢は・・『大吉』だよー❣️❣️❣️🌈🌈🌈でーじなってるさー♪✨🏖️","今日の運勢は・・『吉』だよー❣️🌈チャンプルーの日かもしれないねー♪🤤✨","今日の運勢は・・『中吉』だね❣️☺️✨コツコツちばりよー🤩💪💪💪","今日の運勢は・・『凶』みたい。よんなーよんなー☺️✨","今日の運勢は・・『大凶』みたい。なんくるないさー😆✨","今日の運勢は...むむ、ボクにはわからないよぉ。城間さんが知ってるかも😍❣️❣️❣️"]
        choice = random.choice(ohayo)
        await message.channel.send(choice)

    if "うらない" in message.content.lower():
        ohay = ["今日の運勢は・・『大吉』だよー❣️❣️❣️🌈🌈🌈でーじなってるさー♪✨🏖️","今日の運勢は・・『吉』だよー❣️🌈チャンプルーの日かもしれないねー♪🤤✨","今日の運勢は・・『中吉』だね❣️☺️✨コツコツちばりよー🤩💪💪💪","今日の運勢は・・『凶』みたい。よんなーよんなー☺️✨","今日の運勢は・・『大凶』みたい。なんくるないさー😆✨","今日の運勢は...むむ、ボクにはわからないよぉ。城間さんが知ってるかも😍❣️❣️❣️"]
        choice = random.choice(ohay)
        await message.channel.send(choice)
        
    # URLを含む場合かつ、ロールまたは管理者の場合のみメッセージを削除しない
    if ('http://' in message.content or 'https://' in message.content) and \
            (has_allowed_role(message.author) or message.author.guild_permissions.administrator):
        return
    else:
        # メッセージに制限されたワードが含まれるかを確認します
        if contains_restricted_word(message.content):
            await message.delete()
            await message.channel.send(f'{message.author.mention} さん\nURLまたは制限されたワードが含まれていたので削除しましたワン😢🐶')

    await bot.process_commands(message)

def has_allowed_role(member):
    # ロールが存在するか確認
    role = discord.utils.get(member.guild.roles, name=ALLOWED_ROLE_NAME)
    if role is not None:
        return role in member.roles
    return False

def contains_restricted_word(text):
    for word in RESTRICTED_WORDS:
        if word in text:
            return True
    return False

bot.run('MTEzNDcwOTU0NzQ0NjA0Njc1MA.GZvlyu.koIyPiIXG80_JRYofATgj3Wb1JiNWxkV2U-gog')
