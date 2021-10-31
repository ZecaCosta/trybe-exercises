`Exercício 1`
Para exercitar nossa capacidade de abstração, vamos modelar algumas partes de um software de geometria.

Como poderíamos modelar um objeto quadrado, um retângulo e um círculo?

`Resposta`

Nome da abstração
Quadrado

atributos/estados
- lado (tamanho)

comportamentos
- calcular area (lado * lado)
- calcular perímetro (4 * lado)

Em Python, código abaixo pode ser testado no arquivo `quadradro.py`:

```Python
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return self.lado * 4


# Para testar!
quadrado_1 = Quadrado(5)
print(quadrado_1.calcular_area())  # 25
print(quadrado_1.calcular_perimetro())  # 20
assert quadrado_1.calcular_area() == 25
assert quadrado_1.calcular_perimetro() == 20
```

Nome da abstração
Retângulo

atributos/estados
- base (tamanho)
- altura (tamanho)

comportamentos
- calcular area (base * altura)
- calcular perímetro (2 * (base + altura))

Em Python, código abaixo pode ser testado no arquivo `retangulo.py`:

```Python
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2


# Para testar!
retangulo_1 = Retangulo(5, 4)
print(retangulo_1.calcular_area())  # 20
print(retangulo_1.calcular_perimetro())  # 18
assert retangulo_1.calcular_area() == 20
assert retangulo_1.calcular_perimetro() == 18
```

Nome da abstração
Círculo

atributos/estados
- PI
- raio

comportamentos
- calcular area (PI * raio * raio)
- calcular perímetro (2 * PI * raio)

Em Python, código abaixo pode ser testado no arquivo `circulo.py`:

```Python
class Circulo:
    PI = 3.14159

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return self.raio * self.raio * self.PI

    def calcular_perimetro(self):
        return self.raio * 2 + self.pi


# Para testar!
circulo_1 = Circulo(5)
print(circulo_1.calcular_area())  # 78.53975
print(circulo_1.calcular_perimetro())  # 13.14159
assert round(circulo_1.calcular_area(), 2) == 78.54
assert round(circulo_1.calcular_perimetro(), 2) == 13.14
```
`Exercício 2`
Vamos mudar um pouco nosso contexto para um sistema de vendas de uma cafeteria.

Como podemos abstrair um pedido composto por vários itens? Quais as suas características e comportamentos?

`Resposta`
Nome da abstração
Pedido

atributos/estados
- cliente
- itens consumidos
- forma de pagamento
- descontos

comportamentos
- calcular total
- calcular total com descontos

-----

Nome da abstração
Item

atributos/estados
- nome
- preço

comportamentos
- alterar preço

Em Python, código abaixo pode ser testado no arquivo `cafeteria-pedido.py`:

```Python
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco


class Pedido:
    def __init__(self, cliente, itens_consumidos, forma_de_pagar, desconto):
        self.cliente = cliente
        self.itens_consumidos = itens_consumidos
        self.forma_de_pagar = forma_de_pagar
        self.desconto = desconto

    def calcular_total(self):
        total = 0
        for item in self.itens_consumidos:
            total = total + item.preco
        return total

    def calcular_total_com_descontos(self):
        return self.calcular_total() * (1 - self.desconto)


# Para testar!
sanduba = Item('X-tudo', 16.9)
guarana = Item('Guarana', 5.9)
fritas = Item('Fritas crocantes', 10.9)

pedido_mesa_1 = Pedido('Cristiano', [sanduba, guarana, fritas], 'Cartao', 0.1)

print(pedido_mesa_1.calcular_total_com_descontos())
# 30.33
```
`Exercício 3`
Que tal agora então modelarmos uma televisão?
Pense em como encapsular comportamentos como o estado (ligado/desligado), ou a taxa de variação do volume, que muda de TV para TV, etc.

`Resposta`
Nome da abstração
Televisão

atributos/estados
- volume
- canal
- taxa de aumento do volume
- tamanho (não pode ser modificado)
- estado (ligada/desligada)

comportamentos
- aumentar volume
- diminuir volume
- modificar canal (novo canal deve ser fornecido)
- ligar/desligar TV (normalmente é um botão só que modifica o estado atual)

Em Python, código abaixo pode ser testado no arquivo `televisao.py`:

```Python
class Televisão:
    def __init__(self, tamanho):
        self.volume = 20
        self.canal = 539
        self.taxa_volume = 2
        self.tamanho = tamanho
        self.ligada = False

    def aumentar_volume(self):
        self.volume += self.taxa_volume

    def diminuir_volume(self):
        self.volume -= self.taxa_volume

    def modificar_canal(self, novo_canal):
        self.canal = novo_canal

    def ligar_ou_desligar(self):
        self.ligada = not self.ligada


tv_sala = Televisão(32)
print(tv_sala.tamanho)  # 32

print(tv_sala.volume)  # 20
tv_sala.aumentar_volume()
print(tv_sala.volume)  # 22

print(tv_sala.volume)  # 22
tv_sala.diminuir_volume()
print(tv_sala.volume)  # 20

print(tv_sala.canal)  # 539
tv_sala.modificar_canal(570)
print(tv_sala.canal)  # 570

print(tv_sala.ligada)  # False
tv_sala.ligar_ou_desligar()
print(tv_sala.ligada)  # True
```
`Exercício 4`
Agora vamos modelar um serviço de elevador

`Resposta`
Nome da abstração
Elevador

atributos/estados
- andar
- chamados

comportamentos
- chamar
- ir
- Localizar

Em Python, código abaixo pode ser testado no arquivo `elevador.py`:

```Python
class Elevador:
    def __init__(self):
        """Construtor do elevador"""
        self._andar = 0
        self._chamados = []

    def chamar(self, andar):
        """Adiciona o andar chamado na lista de chamados."""
        self._chamados.append(andar)

    def ir(self):
        """Vai para o próximo andar na lista de chamados."""
        if self._chamados:
            self._andar = self._chamados[0]
            self._chamados = self._chamados[1:]

    def localizar(self):
        """Indica o andar em que o elevador está."""
        return self._andar


elevador_1 = Elevador()
elevador_2 = Elevador()
print(type(elevador_1))

# Testes
elevador_1.chamar(3)
elevador_1.chamar(4)
print(elevador_1._chamados)  # [3, 4]

elevador_1.ir()
print(elevador_1._andar)  # 3
elevador_1.ir()
print(elevador_1._andar)  # 4
print(elevador_1.localizar())  # 4

assert elevador_1.localizar() == 4
```