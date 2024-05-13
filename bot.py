from argparse import ArgumentParser
import discord
import logging
import json
import ollama

parser = ArgumentParser()
parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
args = parser.parse_args()


class Logger:
    def __init__(self, config:dict):

        print ("logger name ",__name__)
        self.__level___ = config["log_level"] 

        formatter = logging.Formatter(config["log_format"])

        handler = logging.StreamHandler()
        handler.setLevel(self.__level___)
        handler.setFormatter(formatter)

        f_handler = logging.FileHandler(config["log_file"])
        f_handler.setLevel(self.__level___)
        f_handler.setFormatter(formatter)

        self.log = logging.getLogger(__name__)
        self.log.setLevel(self.__level___)
        self.log.addHandler(handler)
        self.log.addHandler(f_handler)

    def infolog(self, msg: str):
        self.log.info(msg)

    def errorlog(self, msg: str):
        self.log.error(msg)

    def debuglog(self, msg: str):
        self.log.debug(msg)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        logger.infolog(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        #print(f'Message from {message.author} in {message.channel}: {message.content}')
        logger.infolog(f'Message from {message.author} in {message.channel}: {message.content}')    

        if message.content == config["prefix"] + 'help':
            await message.channel.send('Hello! I am a bot. I can respond to the following commands:\n\n' + 
                config["prefix"] + 'ping - I will respond with "Pong!"\n' +
                config["prefix"] + 'prompt <message> - I will respond with a message generated using Llama2'
            )

        if message.content == config["prefix"] + 'ping':
            await message.channel.send('Pong!')

        if message.content.startswith(config["prefix"] + 'prompt'):
            response = ollama.chat(model=config["model"], messages=[
                {
                    'role': 'user',
                    'content': message.content.split(' ', 1)[1],
                },
            ])
            await message.channel.send(response['message']['content'])

intents = discord.Intents.default()
intents.message_content = True

config = json.load(open(args.config))
logger = Logger(config["log_config"])

# Run the client
client = MyClient(intents=intents)
client.run(config["token"])