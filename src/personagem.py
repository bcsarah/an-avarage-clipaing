import auxiliary

class Personagem:
    def __init__(self, nome, vida, mana, str, con, dex, int, fth, lck, exp, nivel, reis):
        self.nome = nome
        self.vida = vida
        self.vidaTotal = vida
        self.mana = mana
        self.manaTotal = 6
        self.str = str
        self.con = con
        self.dex = dex
        self.int = int
        self.fth = fth
        self.lck = lck
        self.exp = exp
        self.nivel = nivel
        self.reis = reis

    def mostrar_informacoes(self):
        desc = \
            f"Vida: {self.vida}/{self.vidaTotal}\n" \
            f"Mana: {self.mana}/{self.manaTotal}\n\n" \
            f"Str: {self.str}\n" \
            f"Con: {self.con}\n" \
            f"Dex: {self.dex}\n" \
            f"Int: {self.int}\n" \
            f"Fth: {self.fth}\n" \
            f"Lck: {self.lck}\n\n" \
            f"Nível: {self.nivel} ({self.exp} exp)\n" \
            f"Nível: {self.nivel}\n\n" \
            f"Reis: {self.reis}" \

        entrada = auxiliary.entitular(self.nome, desc, ["Voltar"])
        if entrada == 1:
            return