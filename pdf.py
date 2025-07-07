import os
from PyPDF2 import PdfMerger

# 📁 Specifica il percorso della cartella contenente i PDF
cartella_pdf = "d:/Percorso"  # 🔁 Cambialo con il percorso reale della tua cartella

# 📝 Ordine preciso dei file da unire (scrivi esattamente i nomi, con estensione .pdf)
ordine_preciso = [
    "file1.pdf",
    "file2.pdf",    
    "file3.pdf",
    # ....
]

# 🔄 Crea il merger
merger = PdfMerger()

# ➕ Aggiungi ogni file secondo l’ordine definito
for file in ordine_preciso:
    percorso_file = os.path.join(cartella_pdf, file)
    if os.path.exists(percorso_file):
        merger.append(percorso_file)
        print(f"Aggiunto: {file}")
    else:
        print(f"[OK] PDF unito creato: {output_path}")


# 💾 Scrive il file finale
output_path = os.path.join(cartella_pdf, "nome_file.pdf")
merger.write(output_path)
merger.close()

print(f"\n[✔] PDF unito creato: {output_path}")
