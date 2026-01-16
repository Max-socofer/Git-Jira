"""
Module : liaison_intergalactique.py

Objectif totalement officiel :
Tester la liaison VS Code <-> GitHub <-> Jira
tout en simulant un service critique de niveau intergalactique.

⚠️ Ne sert absolument à rien.
"""

import time
import random
import logging
import platform
from dataclasses import dataclass
from datetime import datetime


# --------------------------------------------------
# CONFIGURATION DU LOGGING (parce que c'est sérieux)
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("LIAISON-TEST")


# --------------------------------------------------
# DATACLASS TOTALEMENT INDISPENSABLE
# --------------------------------------------------
@dataclass
class Systeme:
    nom: str
    version: str
    statut: str = "INCONNU"

    def verifier(self):
        logger.info(f"Vérification du système : {self.nom}")
        time.sleep(random.uniform(0.2, 0.6))
        self.statut = random.choice(["OK", "OK", "OK", "PAS OK MAIS ON DIT OK"])
        return self.statut


# --------------------------------------------------
# FONCTIONS ULTRA IMPORTANTES
# --------------------------------------------------
def recuperer_infos_machine():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python": platform.python_version(),
        "machine": platform.machine(),
        "timestamp": datetime.now().isoformat()
    }


def afficher_infos(infos: dict):
    logger.info("Informations système détectées :")
    for cle, valeur in infos.items():
        logger.info(f" - {cle} : {valeur}")


def sequence_de_demarrage():
    logger.info("Démarrage du protocole de liaison...")
    for i in range(3):
        logger.info(f"Initialisation du sous-système {i + 1}/3")
        time.sleep(0.5)
    logger.info("Tous les sous-systèmes sont vaguement opérationnels.")


# --------------------------------------------------
# SCENARIO PRINCIPAL
# --------------------------------------------------
def main():
    logger.info("=== DÉBUT DU TEST DE LIAISON ===")

    sequence_de_demarrage()

    infos = recuperer_infos_machine()
    afficher_infos(infos)

    systemes = [
        Systeme("VS Code", "1.x"),
        Systeme("GitHub", "cloud-infini"),
        Systeme("Jira", "enterprise-ultimate-plus")
    ]

    logger.info("Vérification des intégrations...")
    for systeme in systemes:
        statut = systeme.verifier()
        logger.info(f"Résultat {systeme.nom} : {statut}")

    logger.info("Simulation d'une opération critique...")
    time.sleep(1)

    if all(s.statut.startswith("OK") for s in systemes):
        logger.info("🎉 SUCCÈS : La liaison fonctionne (selon nos critères très laxistes).")
    else:
        logger.warning("🤔 ÉTRANGE : Un problème détecté, mais on commit quand même.")

    logger.info("=== FIN DU TEST ===")


# --------------------------------------------------
# POINT D'ENTRÉE
# --------------------------------------------------
if __name__ == "__main__":
    main()
