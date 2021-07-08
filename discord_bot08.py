import discord
import os
import asyncio
import random
from discord.ext import commands
import speedtest
import datetime

client = commands.Bot(command_prefix = "!", case_insensitive = True )

reacoes = ['🆙','🤩','😎','😍','😃','💞','👊','😎','🤗','💯','🙏','💪']

# Primeira comunicação com o Bot - como a comunicação é assíncrona 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Oi Papai Bença! Estou Online! Meu nome é', self.user)
        print(datetime.datetime.now())

    async def on_message(self, message):
# Para o bot não responder a nós mesmos
        if message.author == self.user:
            return

        if message.content.lower().startswith('!ajuda'):
            embed = discord.Embed(
                title = "Titulo aqui",
                description = "descrição",
                color = 11598249
            )
            
            embed.set_author(name='Autor', icon_url='https://photos.app.goo.gl/kN9gS8dajHyhJMz59')

            embed.set_thumbnail(url='https://photos.app.goo.gl/kN9gS8dajHyhJMz59')

            embed.set_image(url='https://photos.app.goo.gl/kN9gS8dajHyhJMz59')
            
            embed.set_footer(text='Sei la footer')

            embed.add_field(name='nome do field', value='valor dessa poha', inline=False)
            embed.add_field(name='nome do field', value='valor dessa poha', inline=True)
            embed.add_field(name='nome do field', value='valor dessa poha', inline=True)
            
            await message.channel.send(embed = embed)

        if message.content.lower().startswith('!help'):
            await message.channel.send('''
😀😀😀Obrigado por ter me convidado!😀😀😀

🤓 Aqui vai um pouco das dicas para usar o Meu_Botão 🤓

#############           COMANDOS            #############   
👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌

👏!oi - Comprimentar
👏!memepf - Imagens/gif, de memes variados
👏!net - Cálculo da velocidade de internet (obs.:Por enquanto só do hospedeiro)
👏fernando - Salve para o professor!
👏motiva - Frases Motivacionais

Aproveite!
''')

        if message.content.lower().startswith('!oi'):
            if message.author.id == 251875810959556609:
                await message.channel.send('Oi Papai Victão, tô Online!!!!')
            else:
                await message.channel.send('Olá, tô online amigo!!!!')

# O bot envia uma imagem png caso alguém digite !memepf.
        if message.content.lower().startswith('!memepf'):
            escolha_me = random.randint(1,8)
            print(f'valor random do meme foi {escolha_me}')

            if escolha_me == 1:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme.png'))
            if escolha_me == 2:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme2.png'))
            if escolha_me == 3:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme3.png'))
            if escolha_me == 4:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme4.jpg'))
            if escolha_me == 5:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme5.png'))
            if escolha_me == 6:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme6.png'))
            if escolha_me == 7:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('meme7.png'))
            if escolha_me == 8:
                await message.channel.send('É pra já meu chapa!')
                await message.channel.send(file=discord.File('bomdia.gif'))

# Caso alguém insira a palavra exatamente como está escrita Fernando, ele responde a mensagem que pré-definimos.
        if message.content.lower().startswith('fernando'):
            await message.channel.send('Hey Big Boss! Notinha 10 para o grupo no Ava!.')

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


client = MyClient()
#comando para rodar o bot de acordo com seu TOKEN
client.run('ODU5MTQ4NDQxNjYyMTI4MTU4.YNoeVg.hQtlx3VALkYe7ynbR7CHjWi1DGw')

