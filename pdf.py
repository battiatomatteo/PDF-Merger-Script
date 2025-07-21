import os
from PyPDF2 import PdfMerger

# Legge l’ordine dei file dal file di testo generato da 'seleziona_file.py'
try:
    with open("ordine_pdf.txt", "r", encoding="utf-8") as f:
        ordine_preciso = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("[ERRORE] File con ordine PDF non trovato. Esegui prima 'seleziona_file.py'")
    exit()

# Crea il merger per unire i PDF
merger = PdfMerger()

# Aggiunge i file uno a uno seguendo l’ordine scelto
for file_path in ordine_preciso:
    if os.path.exists(file_path):
        merger.append(file_path)
        print(f"Aggiunto: {os.path.basename(file_path)}")
    else:
        print(f"[ATTENZIONE] File non trovato: {file_path}")

# Apre una finestra per chiedere dove salvare il PDF unito
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Nasconde la finestra principale

# Finestra per scegliere il percorso di salvataggio
output_path = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF", "*.pdf")],
    title="Scegli dove salvare il PDF unito",
    initialfile="nomeFile.pdf"
)

# Salva il file se è stato selezionato un percorso valido
if output_path:
    merger.write(output_path)
    merger.close()
    print(f"\n[✔] PDF unito creato: {output_path}")
else:
    print("[INFO] Operazione annullata.")
