import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog
import subprocess  # per aprire il file su Windows

# 📁 Specifica il percorso della cartella contenente i PDF
cartella_pdf = os.getcwd() 

# 🔎 Mostra i file trovati nella cartella
print("\n File trovati nella cartella:")
try:
    for f in os.listdir(cartella_pdf):
        print("-", f)
except FileNotFoundError:
    print(f" Cartella non trovata: {cartella_pdf}")
    exit()

# 📝 Ordine preciso dei file da unire
ordine_preciso = [
    "nome_file1.pdf",
    "nome_file2.pdf",
]

# 🔄 Crea il merger
merger = PdfMerger()

# ➕ Aggiungi ogni file secondo l’ordine definito
pdf_aggiunti = 0
for file in ordine_preciso:
    percorso_file = os.path.join(cartella_pdf, file)
    if os.path.exists(percorso_file):
        merger.append(percorso_file)
        print(f"Aggiunto: {file}")
        pdf_aggiunti += 1
    else:
        print(f"[ATTENZIONE] File non trovato: {file}")

if pdf_aggiunti == 0:
    print("[❌] Nessun file PDF trovato da unire. Uscita.")
    exit()

# --- Finestra di dialogo per scegliere dove salvare ---
root = tk.Tk()
root.withdraw()  # nasconde la finestra principale

output_path = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")],
    title="Scegli dove salvare il PDF unito",
    initialfile="SistemiOperativi.pdf"
)

if not output_path:
    print("[INFO] Operazione annullata dall'utente. Nessun file salvato.")
    exit()

# 💾 Scrive il file finale
merger.write(output_path)
merger.close()

print(f"\n[✔] PDF unito creato: {output_path}")

# --- Apri automaticamente il PDF (solo su Windows) ---
try:
    if os.name == "nt":
        os.startfile(output_path)
    else:
        # per macOS e Linux puoi aggiungere altre chiamate come 'open' o 'xdg-open'
        print("[INFO] Apri manualmente il file PDF creato.")
except Exception as e:
    print(f"[ERRORE] Impossibile aprire il file PDF: {e}")
