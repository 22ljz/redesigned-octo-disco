from datetime import datetime
import discord
import json
import os
import asyncio

config = json.loads(os.environ['CONFIG'])

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Activity(
        type=discord.ActivityType.playing,
        application_id=config['application_id'],
        name=config['name'],
        assets=config['assets'],
        start=datetime.now(),
    )
    await client.change_presence(activity=game, status=discord.Status.online)
    await asyncio.sleep(4 * 60 * 60)
    client.close()

if __name__ == "__main__":
    client.run(config['token'], log_handler=None)
