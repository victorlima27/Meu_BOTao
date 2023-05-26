# from xmlrpc.client import DateTime
import discord
import os
# import asyncio
import time
import schedule
import random
from discord import file
from discord.ext import commands, tasks
import speedtest
import datetime
from dotenv import load_dotenv

load_dotenv()

reacoes = ['🆙','🤩','😎','😍','😃','💞','👊','😎','🤗','💯','🙏','💪']


@tasks.loop(hours=24)
async def bomdia():
    print('entrei')
    now = datetime.datetime.now()
    print(now.hour)
    if now.weekday() == 3 and now.hour == 10:  # 4 representa a sexta-feira (segunda-feira é 0)
        # channels = [689903332877140008,860333711635775518 ]
        channels = [1032282639433998410]
        person = [239781637812912128]

        # channel_id = 860333711635775518  # Substitua pelo ID do canal onde você deseja enviar a mensagem
        for i in channels :
            for p in person:
                channel = client.get_channel(i)
                user = await client.fetch_user(p)
                await channel.send(f'Bom dia! {user.mention}')

@tasks.loop(hours=24)
async def sexta():
    print('sexta')
    now = datetime.datetime.now()
    if now.weekday() == 4:  # 4 representa a sexta-feira (segunda-feira é 0)
        # channels = [1032282639433998410]
        channels = [876487244834308097]
        for i in channels :
            channel = client.get_channel(i)
            await channel.send('Hoje é sexta feira, dia de bucetinha!!')
            await channel.send('@everyone')
            await channel.send(":speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil::speak_no_evil::speak_no_evil::speak_no_evil:")
            await channel.send(file=discord.File('sexta.mp4'))

@tasks.loop(minutes=1)
async def TESTE():
    print('entrei')
    now = datetime.datetime.now()
    # print(now.hour)
    # now.weekday() == 3 
    if now.hour == 11 and now.minute == 14:  # 4 representa a sexta-feira (segunda-feira é 0)
        # channels = [689903332877140008,860333711635775518 ]
        channels = [860333711635775518]
        users = [251875810959556609]
        # channel_id = 860333711635775518  # Substitua pelo ID do canal onde você deseja enviar a mensagem
        for i in channels:
            for p in users:
                channel = client.get_channel(i)
                user = await client.fetch_user(p)
                await channel.send(f"Bom dia! {user.mention}")
    else:
        print('mas não é o horário correto')
    
# Primeira comunicação com o Bot - como a comunicação é assíncrona
class MyClient(discord.Client):

    async def on_ready(self):
        print('Oi Papai Bença! Estou Online! Meu nome é', self.user)
        print('Version 3.v04')
        print('Dia 26/05/2023 08:20')
        y = datetime.datetime.now()
        # locale.setlocale(locale.LC_ALL, '')
        z = y.strftime("%H")
        # bomdia.start()
        # TESTE.start()
        sexta.start()


    async def on_message(self, message):
        #Para o bot não responder a nós mesmos

        x = datetime.datetime.now()
        Ex = message.content.lower().startswith
        Env_Msg = message.channel.send

        if Ex('teste'):
            await message.channel.send('Ok testa ai')

        if message.author == self.user:
            return

        if message.content.lower().startswith('!ajuda'):
            embed = discord.Embed(
                title = "Prazer eu sou o Meu_BoTão! Filho do Victão!",
                description = '''Estou aprendendo aos poucos mas já sei fazer isso aqui ó:''',
                color = discord.Color.random()
            )

            embed.set_author(name= f'Fala {message.author.name}, tudo beleza?!', icon_url= message.author.avatar)

            embed.set_thumbnail(url='https://w7.pngwing.com/pngs/996/981/png-transparent-osu-hearts-of-iron-iv-scp-foundation-reddit-video-game-mouth-smile-miscellaneous-game-people.png')

            # embed.set_image(url='https://lh3.googleusercontent.com/TmjSvqmxPLt0rsP-sSDKuScKDI6_jwo3r1-WEhmlbdYxOrtOYQ0GUZ98wmdx2Y8QBEbQU2e24AweU_ddSiyIhsdRKcqCw0VwvKEC__KGT2A9VJDenLzKKcfrOzccZSgC7JY8xD5CYGqqAC2Zfj8wjyi1_yw2kXbgjy-li_uBagtH8Du-9GkDhZqdGDUM8K3IeiLQH4lrd9-ElKWMUwAysmZAKVtBrXFN5FRvcxOdEv3YlC1HT-r4coUUjKjOQkN2JNz0CKm-YHO9CqguPsGy2KILwNZimff-f_pLYV1vFA9F5_o8UeMCAFNtHHFBBOegJvXOaihUKvx_uP6GPFkqgT_DLanVNNMhDCiknxFqo-ga3lJs7qtD20L5xYTMpoN--ao9mk9nYgCRQRleR03CAXtcZ5uF__McjtZ4XpxB_0iylTQZLWXqHavMCwe05dc6zU0IbZl6KiT9N9kDDOWL7kQFzUm8Cz03y_jYLDjcPqzwXIpl1vsggzrLTRG6aOFGIlDDcO2eLMcICGnBmz9rPm-B-pHEp3473JA75VH0QwmnGo_h3kl1IyQE8uQOVNi9RA_cfqsltIUzyRqDkowIU1i7CR4TVnjSqQYuUULcMxbqdz8CV6KclvLtogdtVUWm6KHrfXsKMtCicsqivc9iHJdUZ6SnkbIVqIO5P5-SiHvHov4pMzkiwXbCgnZuxtMFY6HaAa6jBnPhq3_N7o_ohkL5=w288-h429-no?authuser=0')

            # embed.set_footer(text='Foto do meu Papai Lindão')

            embed.add_field(name= 'Gosto de Comprimentar', value='- Diga oi no chat',  inline=False)
            embed.add_field(name= 'Compartilho memes rs', value='- Diga !meme no chat',  inline=False)
            #embed.add_field(name= 'Salve Professor Fernando', value='- Diga Fernando no chat',  inline=False)
            embed.add_field(name= 'Sou Coach nas vagas horas', value='- Diga motiva no chat',  inline=False)
            embed.add_field(name= 'Salve Professor Fernando', value='- Diga Fernando no chat',  inline=False)
            embed.add_field(name= 'Descubro o que é o meu pai!', value='- Diga victao no chat',  inline=False)
            embed.add_field(name= 'Sexta-feira dia de B........', value='- Surpresa no chat do geral gunto',  inline=False)




            await message.channel.send(embed = embed)

        if message.content.lower().startswith('oi'):
            if message.author.id == 251875810959556609:
                await message.channel.send('Oi Papai Victão, tô Online!!!!')
            elif message.author.id == 282859044593598464:
                await message.channel.send('---')
            else:
                await message.channel.send('Oi, Lindona')
        if message.content.lower().startswith('olha quem voltou'):
            await message.channel.send('Eu sento rebolando chamando o seu nome')

        # O bot envia uma imagem png caso alguém digite !memepf.
        if message.content.lower().startswith('!meme'):
            escolha_me = random.randint(1,8)
            print(f'valor random do meme foi {escolha_me}')

            if escolha_me == 1:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme.png'))
            if escolha_me == 2:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme2.png'))
            if escolha_me == 3:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme3.png'))
            if escolha_me == 4:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme4.jpg'))
            if escolha_me == 5:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme5.png'))
            if escolha_me == 6:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme6.png'))
            if escolha_me == 7:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('meme7.png'))
            if escolha_me == 8:
                await message.channel.send(f'É pra já {message.author.name}!')
                await message.channel.send(file=discord.File('bomdia.gif'))

        # só falar bem da tia catarina
        if message.author.id == 402168333153337347:
            frase_cat = random.randint(1,3)

            if frase_cat == 1:
                    await message.channel.send('digam oi pra Tia Catarina ai caraiooo')

            if frase_cat == 2:
                    await message.channel.send('Ajoelhem perante a nossa ADM')

            if frase_cat == 3:
                    await message.channel.send('quem vai de ban hoje ?')

        # só falar merda do nandinho
        if message.author.id == 282859044593598464:
            frase_nan = random.randint(1,3)

            if frase_nan == 1:
                await message.channel.send('Caralho nandinho tu é muito chato')

            if frase_nan == 2:
                await message.channel.send('Cala boca filho da puta')

            if frase_nan == 3:
                await message.channel.send('Mano para de encher a poha do saco muleque')


        # Caso alguém insira a palavra exatamente como está escrita Fernando, ele responde a mensagem que pré-definimos.
        if message.content.lower().startswith('fernando'):
            await message.channel.send('Hey Big Boss! Notinha 10 para o grupo no Ava!.')

        if message.content.lower().startswith('obrigado'):
            await message.channel.send('Não tem de quê, amo vc amigo 💞')

        # Utilizamos a biblioteca Random para o bot assim que ele receber uma mensagem que contenha o "motiva" independente
        # de ser maiusculo ou minusculo, ele nos responde com uma mensagem motivacional como pré-definimos e adiciona uma reação ao comentário.
        if message.content.lower().startswith('motiva'):

            escolha_m = random.randint(1,9)
            print(f'valor random da escolha foi {escolha_m}')
            reacao = random.randint(0,11)
            print(f'valor random da reação foi {reacao}')

            if escolha_m == 1:
                await message.channel.send('A persistência é o caminho do êxito.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 2:
                await message.channel.send('O que não provoca minha morte faz com que eu fique mais forte.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 3:
                await message.channel.send('Pedras no caminho? Eu guardo todas. Um dia vou construir um castelo.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 4:
                await message.channel.send('O que me preocupa não é o grito dos maus. É o silêncio dos bons.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 5:
                await message.channel.send('O insucesso é apenas uma oportunidade para recomeçar com mais inteligência.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 6:
                await message.channel.send('No meio da dificuldade encontra-se a oportunidade.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 7:
                await message.channel.send('O sucesso é ir de fracasso em fracasso sem perder o entusiasmo.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 8:
                await message.channel.send('É parte da cura o desejo de ser curado.')
                await message.add_reaction(f'{reacoes[reacao]}')
            if escolha_m == 9:
                await message.channel.send('Não importa o que você decidiu. O que importa é que isso te faz feliz.')
                await message.add_reaction(f'{reacoes[reacao]}')

        # O bot faz o calculo aproximado da velocidade de internet, mas conseguimos implantar apenas para o calculo da velocidade do Host do bot.
        if message.content.lower().startswith('!net'):
            await message.channel.send('Por favor Aguarde! Estamos calculando sua velocidade!😮‍💨')
            test_vel = speedtest.Speedtest()
            downl = round(test_vel.download()/1000000,2)
            upl = round(test_vel.upload()/1000000,2)
            await message.channel.send(f'Sua velocidade de Download é de {downl}Mbps e o Upload é de {upl}Mbps')

        if message.content.lower().startswith('ronaldo'):
            await message.channel.send('Primeiro que eu odeio esse cara, segundo q ele é um merda')

        if message.content.lower().startswith('eae'):
            await message.channel.send('e ae meu brodi')

        if Ex('meu botão') or Ex('meu botao'):
            await message.channel.send('Oi amiguinhoooo')

        if Ex('botao') or Ex('botão'):
            await message.channel.send('que te come atrás do portão')

        if Ex('catrina') or Ex('ctrina'):
            await message.channel.send('Obrigado por me permetir aqui amiga AnaCatarina')

        if Ex('o pai'):
            await Env_Msg('O Pai ta Forte!!!')
            await Env_Msg(file=discord.File('hotmart.mp4'))

        if message.content.lower().startswith('quem'):
            await message.channel.send('te pega?')

        if message.content.lower().startswith('nao') or Ex('no'):
            await message.channel.send('Eu também não')

        if message.content.lower().startswith('eu'):
            await message.channel.send('Eu não')

        if message.content.lower().startswith('kkk') or Ex('haha'):
            await message.channel.send('hahahahahahhahahahahhaahaha de fuder')

        if Ex('victao') or Ex('victão') or Ex('victor'):
            await message.channel.send('Nada mais nada menos que o meu pai. O mais brabo de vitória e adjacências, o cara pika')

        if message.content.lower().startswith('bolão'):
            await message.channel.send('Você já viu o bolão do meu papai ? Pergunte a ele e desvende essa Magia')

        if Ex('sexta') or Ex("sextou"):
            if x.strftime("%A") == ("Friday"):
                await message.channel.send('Hoje é sexta feira, dia de bucetinha!!')
                await message.channel.send('@everyone')
                await Env_Msg(":speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil: :speak_no_evil::speak_no_evil::speak_no_evil::speak_no_evil:")
                # await Env_Msg(file=discord.File('mbuc.webp'))
                await Env_Msg(file=discord.File('sexta.mp4'))
                # await Env_Msg(file=discord.File('mbuc.webp'))
            else:
                await Env_Msg("Sexta não chegou ainda não mongoloide")

        if message.content.lower().startswith('shrek'):
            embed = discord.Embed(
                title = ":arrows_counterclockwise:",
                color = discord.Color.red()
            )
            await message.channel.send(embed = embed)

            embed = discord.Embed(
                title = "...",
                color = discord.Color.gold()
            )
            await message.channel.send(embed = embed)

            embed = discord.Embed(
                title = "Processando!... :arrows_counterclockwise: ",
                color = discord.Color.blue()
            )
            await message.channel.send(embed = embed)

            embed = discord.Embed(
                title = "...",
                color = discord.Color.gold()
            )
            await message.channel.send(embed = embed)

            embed = discord.Embed(
                title = ":arrows_counterclockwise:",
                color = discord.Color.red()
            )
            await message.channel.send(embed = embed)

            embed = discord.Embed(
                title = "Parabéns Você acabou de Ganhar o Filme do Shrek 1,2,3,4 em apenas 1 Minuto! Free Grátiss!!!!!! Não é Vírus, pode confiar!!!",
                color = discord.Color.green()
            )
            await message.channel.send(embed = embed)

            file = discord.File("shrek.gif")
            embed = discord.Embed(
                title = ":arrow_forward: ",
                color = discord.Color.green()
            )
            embed.set_image(url="attachment://shrek.gif")
            await message.channel.send(embed = embed, file=file)
            await message.channel.send(file=discord.File('shrek.gif'))

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "!", case_insensitive = True, intents=intents)


client = MyClient(intents=intents)
#comando para rodar o bot de acordo com seu TOKEN
client.run(str(os.getenv('client.run')))
