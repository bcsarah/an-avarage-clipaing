import personagem

# Teste
def teste():
    sarah = personagem.Personagem("Sarah", 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
    gabriel = personagem.Personagem("Gabriel", 100, 1, 10, 10, 10, 10, 10, 10, 0, 1, 0)
    sarah.mostrar_informacoes()
    gabriel.mostrar_informacoes()

teste()