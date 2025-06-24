from datetime import datetime, time
import discord
import json
import os

config = json.loads(os.environ['CONFIG'])

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Activity(
        type=discord.ActivityType.playing,
        application_id=config['application_id'],
        name=config['name'],
        assets=config['assets'],
        start=datetime.combine(datetime.now().date(), time(3, 0, 0)),
    )
    await client.change_presence(activity=game, status=discord.Status.idle)

if __name__ == "__main__":
    client.run(config['token'], log_handler=None)
