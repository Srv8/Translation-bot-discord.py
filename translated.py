from translate.languages import languages
from googletrans import Translator
import discord


async def trans(reaction):
  if reaction.emoji:
    reactedemoji = reaction.emoji
    if not(languages.get(reactedemoji)):
      await reaction.message.channel.send("Language not added...Try another flag")
    else:
      selectedlanguage = str(languages.get(reactedemoji))
      # print(reactedemoji)
      sentmessage = str(reaction.message.content)
      translater = Translator()
      sendmessage = translater.translate(sentmessage, dest=selectedlanguage)
      embed=discord.Embed(title='Translated',
                    description=sendmessage.text,
                    color=0x91FDE5)
      await reaction.message.channel.send(embed=embed)
