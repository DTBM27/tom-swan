import random
import time
import json
from classes.sim import Sim
from classes.predio import Predio
from classes.andar import Andar
from classes.elevador import Elevador
from classes.bloco_informatica import BlocoInformacao

class Simulacao:
    def __init__(self):
        self.sims = []
        self.predios = [
            Predio("Centro de Vivência"),
            Predio("Refeitório"),
            BlocoInformacao("Bloco de Informática")
        ]
        self.elevador = Elevador(capacidade=5, andares=len(self.predios))

    def criar_sim(self, id):
        tipo = random.choice(["Aluno", "Servidor"])
        sim = Sim(id, tipo)
        self.sims.append(sim)
        return sim

    def iniciar(self):
        while True:
            sim_id = len(self.sims) + 1
            novo_sim = self.criar_sim(sim_id)
            predio_destino = random.choice(self.predios)
            predio_destino.adicionar_sim(novo_sim)

            # Lógica para interação com o elevador
            if len(self.elevador.sims_no_elevador) < self.elevador.capacidade:
                novo_sim.esperar()
                self.elevador.entrar(novo_sim)
                andar_destino = random.randint(0, self.elevador.andares - 1)
                self.elevador.mover_para(andar_destino)
                self.elevador.sair(novo_sim)

            time.sleep(1)  # Pausa para simular o tempo entre as ações

if __name__ == "__main__":
    simulacao = Simulacao()
    simulacao.iniciar()
