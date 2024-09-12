palavra = str(input("Digite uma frase: ")) # Ele irá pegar a frase do usuário
palavra_lista = list(palavra) # transformando em lista ["l", "e", "t", "r", "a"]
palavra_list = list(palavra) # transformando em lista mas em outra variavel ["l", "e", "t", "r", "a"]
palavra_list.reverse() # Invertendo as posições.

if palavra_lista == palavra_list: # Conferindo pra ver se mesmo invertido o resultado é o mesmo
    print("A frase é um palíndromo")
else: # Caso não for ele mostra que é diferente.
    print("A frase não é um palíndromo")