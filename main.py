from datetime import datetime, timedelta
import discord
import json
import os
import asyncio
import sys
import time

config = json.loads(os.environ["CONFIG"])

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Activity(
        type=discord.ActivityType.playing,
        application_id=config["application_id"],
        name=config["name"],
        assets=config["assets"],
        start=datetime.now(),
    )
    await client.change_presence(activity=game, status=discord.Status.online)

    start = time.time()

    for guild in client.guilds:
        async for message in guild.search(
            authors=[client.user],
            before=datetime.now() - timedelta(days=7),
            limit=sys.maxsize,
        ):
            await message.delete()

    for friend in client.friends:
        async for message in friend.user.search(
            authors=[client.user],
            before=datetime.now() - timedelta(days=7),
            limit=sys.maxsize,
        ):
            await message.delete()

    await asyncio.sleep(4 * 60 * 60 - (time.time() - start))
    await client.close()


if __name__ == "__main__":
    client.run(os.environ["TOKEN"], log_handler=None)
