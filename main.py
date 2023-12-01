from os import system
import platform
import asyncio
import discord
from colorama import Fore, init, Style
from serverclone import Clone

init(autoreset=True)

mytitle = "Клонер - Developed by VirusTeam"
system("title " + mytitle)

os_system = platform.system()

if os_system == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(
    f"""{Fore.MAGENTA}                                       
                      ______    _           _____     ______     _______    ______  
                     / _____)  | |         / ___ \   |  ___ \   (_______)  (_____ \ 
                    | /        | |        | |   | |  | |   | |   _____      _____) )
                    | |        | |        | |   | |  | |   | |  |  ___)    (_____ ( 
                    | \_____   | |_____   | |___| |  | |   | |  | |_____         | |
                     \______)  |_______)   \_____/   |_|   |_|  |_______)        |_|
                                                                
    {Style.RESET_ALL}
    Создатель: VirusTeam.{Style.RESET_ALL}
    """
)

token = input(f'{Fore.CYAN}1. Введите токен аккаунта:\n >> {Style.RESET_ALL}')
guild_s = input(f'{Fore.CYAN}2. Id сервера, который нужно скопировать:\n >> {Style.RESET_ALL}')
guild = input(f'{Fore.CYAN}3. Id сервера, куда нужно вставить:\n >> {Style.RESET_ALL}')

input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token

print("  ")
print("  ")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{Fore.GREEN}Вход с аккаунта: {client.user}")
    print("Клонирование началось")

    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))

    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)

    print(
        f"""{Fore.BLUE}
                      ______    _           _____     ______     _______    _____   
                     / _____)  | |         / ___ \   |  ___ \   (_______)  (____ \  
                    | /        | |        | |   | |  | |   | |   _____      _   \ \ 
                    | |        | |        | |   | |  | |   | |  |  ___)    | |   | |
                    | \_____   | |_____   | |___| |  | |   | |  | |_____   | |__/ / 
                     \______)  |_______)   \_____/   |_|   |_|  |_______)  |_____/  
                                                                
        {Style.RESET_ALL}
        """
    )
    await asyncio.sleep(5)
    await client.close()

client.run(token, bot=False)
