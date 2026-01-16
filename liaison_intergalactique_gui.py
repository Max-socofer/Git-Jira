"""
Interface graphique de test de liaison
VS Code <-> GitHub <-> Jira

Outil critique pour vérifier que tout fonctionne,
même si absolument rien ne fait rien.
"""

import tkinter as tk
from tkinter import ttk
import time
import random
import platform
from datetime import datetime
from dataclasses import dataclass
import threading


# --------------------------------------------------
# DATACLASS ULTRA IMPORTANTE
# --------------------------------------------------
@dataclass
class Systeme:
    nom: str
    version: str
    statut: str = "INCONNU"

    def verifier(self):
        time.sleep(random.uniform(0.5, 1.2))
        self.statut = random.choice(
            ["OK", "OK", "OK", "OK MAIS À SURVEILLER"]
        )
        return self.statut


# --------------------------------------------------
# APPLICATION GUI
# --------------------------------------------------
class LiaisonApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Protocole de Liaison Intergalactique")
        self.geometry("700x500")
        self.resizable(False, False)

        self.creer_widgets()

    # ---------------- UI ----------------
    def creer_widgets(self):
        titre = ttk.Label(
            self,
            text="🚀 Test de Liaison VS Code / GitHub / Jira",
            font=("Segoe UI", 16, "bold")
        )
        titre.pack(pady=10)

        self.zone_log = tk.Text(
            self,
            height=20,
            width=85,
            state="disabled",
            bg="#111",
            fg="#33ff33",
            font=("Consolas", 10)
        )
        self.zone_log.pack(padx=10, pady=10)

        frame_boutons = ttk.Frame(self)
        frame_boutons.pack(pady=10)

        self.btn_lancer = ttk.Button(
            frame_boutons,
            text="▶ Lancer le test",
            command=self.lancer_test
        )
        self.btn_lancer.grid(row=0, column=0, padx=5)

        self.btn_clear = ttk.Button(
            frame_boutons,
            text="🧹 Effacer les logs",
            command=self.clear_logs
        )
        self.btn_clear.grid(row=0, column=1, padx=5)

        self.btn_quitter = ttk.Button(
            frame_boutons,
            text="❌ Quitter",
            command=self.destroy
        )
        self.btn_quitter.grid(row=0, column=2, padx=5)

    # ---------------- LOGS ----------------
    def log(self, message):
        self.zone_log.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.zone_log.insert("end", f"[{timestamp}] {message}\n")
        self.zone_log.see("end")
        self.zone_log.configure(state="disabled")

    def clear_logs(self):
        self.zone_log.configure(state="normal")
        self.zone_log.delete("1.0", "end")
        self.zone_log.configure(state="disabled")

    # ---------------- LOGIQUE ----------------
    def lancer_test(self):
        self.btn_lancer.config(state="disabled")
        thread = threading.Thread(target=self.sequence_complete)
        thread.start()

    def sequence_complete(self):
        self.log("Initialisation du protocole de liaison...")
        time.sleep(1)

        self.log("Récupération des informations système...")
        self.afficher_infos_machine()

        self.log("Démarrage des vérifications...")
        systemes = [
            Systeme("VS Code", "1.x"),
            Systeme("GitHub", "cloud-infini"),
            Systeme("Jira", "enterprise-edition")
        ]

        resultats_ok = True

        for systeme in systemes:
            self.log(f"Vérification de {systeme.nom}...")
            statut = systeme.verifier()
            self.log(f"→ {systeme.nom} : {statut}")
            if not statut.startswith("OK"):
                resultats_ok = False

        self.log("Simulation d'une opération critique...")
        time.sleep(1)

        if resultats_ok:
            self.log("🎉 SUCCÈS : La liaison intergalactique est opérationnelle.")
        else:
            self.log("⚠️ ATTENTION : Tout n'est pas parfait, mais on valide quand même.")

        self.log("Fin du test.")
        self.btn_lancer.config(state="normal")

    def afficher_infos_machine(self):
        infos = {
            "OS": platform.system(),
            "Version OS": platform.version(),
            "Python": platform.python_version(),
            "Machine": platform.machine(),
        }

        for cle, valeur in infos.items():
            self.log(f"{cle} : {valeur}")
        time.sleep(0.5)


# --------------------------------------------------
# LANCEMENT
# --------------------------------------------------
if __name__ == "__main__":
    app = LiaisonApp()
    app.mainloop()
