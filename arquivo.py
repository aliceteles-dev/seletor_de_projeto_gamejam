import csv
import statistics

#aqui eu crio um arquivo pra mostrar a lista
with open("gamedev.csv", "w", newline='') as game_ideas:
    w = csv.writer(game_ideas, delimiter = ",")
    #classificações
    w.writerow(["Id do Jogo", "Desenvolvimento da ideia", "Pixel Art", "Programação", "O quanto eu curto a ideia", "Média"])
    #dados
    dados = [
        ["Exemplo", 0, 0, 0, 0],
    ]

    #isso é pra fazer o programa tirar a média de cada item da lista e escrevê-la na última coluna da tabela
    for linha in dados:
        nome = linha[0]
        numeros = linha[1:]
        media = statistics.mean(numeros)
        w.writerow([nome] + numeros + [media])