# bot.py
import openai
import discord
from discord.ext import commands
openai.api_key = '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'
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='#', intents=intents)




@bot.command()
async def gpt(ctx, query):
  print(query)
  response = openai.Completion.create(
  		model="text-davinci-003",
  		prompt=query,
  		temperature=0.3,
  		max_tokens=4000,
  		top_p=1,
  		frequency_penalty=1,
  		presence_penalty=1,
  		stop=[" Human:", " AI:"]
		)
  text = response['choices'][0]['text']
  print (text)
  await ctx.reply(" " + text)


bot.run('MTA2NjU4NzMxMDk5MDMxNTYzMA.G86h_H.RE566GotH0EzWUC_dLrpDKRKpx07a5hFVjyOjo')
