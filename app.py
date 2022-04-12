from flask import Flask, render_template, redirect
from restaurante import Restaurante
from avaliacao import Avaliacao

app = Flask(__name__)

restaurantes = {'ReliquiaRestaurante': Restaurante(0, 'Reliquia Restaurante',
                                                   'R. Barão de Capivari - Centro, Vassouras - RJ, 27700-000',
                                                   '(24) 2471-4065',
                                                   'Carnes, Pizzas, Petiscos, Bebidas', '09:00', '01:00',
                                                   'https://media-cdn.tripadvisor.com/media/photo-m/1280/1c/43/af/81/img-20201101-131018948.jpg'),
                'RestauranteVarandas': Restaurante(1, 'Restaurante Varandas',
                                                   'Av. Expedicionário Osvaldo de Almeida Ramos, 110 - Centro, Vassouras - RJ, 27700-000',
                                                   '(24) 2471-4100',
                                                   'Carnes, Pizzas, Petiscos, Bebidas', '11:00', '00:00',
                                                   'https://media-cdn.tripadvisor.com/media/photo-s/06/df/cf/3f/retaurante-varandas.jpg'),
                'DeliciasLanches': Restaurante(2, 'Delicias Lanches',
                                               'Proximo a antiga estação - Praça Martinho Nóbrega, 10 - loja 1 - Centro, Vassouras - RJ, 27700-000',
                                               '(24) 99237-8845', 'Batatas, Hamburguers, Bebidas', '18:00', '01:00',
                                               'https://img.restaurantguru.com/r98e-Delicias-Lanches-interior-2020-08.jpg'),
                }
avaliacoes = [Avaliacao(0, 'João', 4, 'Bom Demais!', 'Reliquia Restaurante'),
              Avaliacao(1, 'Maria', 1, 'Muito ruim', 'Reliquia Restaurante'),
              Avaliacao(2, 'Pedro', 5, 'Ótimo!', 'Restaurante Varandas'),
              Avaliacao(3, 'Joana', 0, 'Péssimo!', 'Restaurante Varandas'),
              Avaliacao(4, 'José', 5, 'Ótimo!', 'Restaurante Varandas'),
              Avaliacao(5, 'Joana', 4, 'Bom Demais!', 'Reliquia Restaurante'),
              Avaliacao(6, 'Ster', 3, 'Não Gostei de nada', 'Restaurante Varandas'),
              Avaliacao(7, 'Stephany', 4, 'Bom Demais!', 'Reliquia Restaurante'),
              Avaliacao(8, 'Tiago', 5, 'Ótimo!', 'Delicias Lanches'),
              Avaliacao(9, 'Lucas', 4, 'Bom Demais!', 'Delicias Lanches'),
              Avaliacao(10, 'Carlos', 2, 'Demorou muito!', 'Delicias Lanches'),
              Avaliacao(11, 'Tássio', 4, 'Melhor Lanche!', 'Delicias Lanches'),]

for avaliacao in avaliacoes:
    restaurantes[avaliacao.getRestaurante().replace(" ", "")].setAvaliacao(avaliacao)


@app.route('/')
def index():
    return render_template('index.html', restaurantes=restaurantes)


@app.route('/restaurante/<string:nome>')
def restaurante(nome):
    if nome in restaurantes:
        return render_template('restaurante.html', restaurante=restaurantes[nome])
