import asyncio
import discord
import os
import re

client = discord.Client()
name = "Dad"
pattern = re.compile("^\$name=(\w+)")
pattern2 = re.compile("^\$spam=(\w+)")
articles = ["a ", "the ", "an "]
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    global name
    global articles
    if message.author != client.user:
        match = pattern.match(message.content)
        match2 = pattern2.match(message.content)
        comtoken = ["comrade", "Russia", "proletariat", "bourgeois", "communist", "communism"]
        for str in comtoken:
            if str in message.content.lower():
                await client.send_message(message.channel, "Greetings, Comrade. Workers/Calc Students of the world unite!")
        if match:
            name = match.group(1)
            output = "Name changed to " + name + "."
            await client.send_message(message.channel, output)
        elif match2:
            map = {
                "fgpt": "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.",
                "freedom": "When in the Course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.",
                }
            output = map.get(match2.group(1))
            if output:
                await client.send_message(message.channel, output)
        else:
            text = "padding " + message.content
            splits = [" I am ", " i am ", " i'm ", " iam ", " Im ", " im "]
            for str in splits:
                text = text.replace(str, "  I'm  ")
            print(text);
            iem = text.split(" I'm ")
            if len(iem) > 1:
                victim = iem[len(iem) - 1]
                for str in articles:
                    if victim.startswith(str) and len(victim) > len(str):
                        victim = victim[len(str):len(victim)]
                victim = victim.strip();
                output = "Hi " + victim + ", I'm " + name + ". Nice to meet you."
                await client.send_message(message.channel, output)
            
            splits = [" You are ", " you are ", " ur ", " u are ", " u r ", " you're ", " You're ", " Ur ", " U r "]
            for str in splits:
                text = text.replace(str, "  ur  ")
            print(text);
            iem = text.split(" ur ")
            if len(iem) > 1:
                victim = iem[len(iem) - 1]
                for str in articles:
                    if victim.startswith(str) and len(victim) > len(str):
                        victim = victim[len(str):len(victim)]
                victim = victim.strip();
                output = "You are " + victim + ", but what am I?"
                await client.send_message(message.channel, output)
token = "NTEzNDE2NjY0MTYzODExMzM4.DtH0cg.SfLkFI4pONtM6eTjOKyIk-bF0Z8"
client.run(token)
