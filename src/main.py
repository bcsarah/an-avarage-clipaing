import auxiliary
import personagem

# Main
def main():
    protagonista = personagem.Personagem("Sarah", 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
    protagonista = personagem.Personagem("Gabriel", 100, 1, 10, 10, 10, 10, 10, 10, 0, 1, 0)
    protagonista.mostrar_informacoes()

main()