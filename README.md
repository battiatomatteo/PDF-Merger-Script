# 📎 PDF Merger Script

Script semplice in Python per unire più file PDF in un unico documento, seguendo un ordine specificato manualmente.

## 🛠 Funzionalità

- ✅ Unisce file PDF in un ordine personalizzato
- 📂 Lavora su una cartella locale contenente i PDF
- 📄 Crea un unico file PDF unificato
- 📂 Fa scegliere all'utente dove salvare il file aprendo una finestra dell'esplora risorse

## 📋 Requisiti

- Python 3.6+
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Puoi installare PyPDF2 con:

```bash
pip install PyPDF2
```
### 1. `seleziona_file.py` – Interfaccia grafica per selezionare e ordinare i PDF
Avvia una semplice interfaccia con Tkinter che permette di:
- Aprire una finestra dell’esplora risorse per **scegliere i file PDF** da unire.
- Visualizzare i file selezionati in una lista.
- Cambiare l’**ordine dei file** con i pulsanti "Su" e "Giù".
- Salvare l’ordine scelto in un file `ordine_pdf.txt`.

> ⚠️ Questo file deve essere eseguito **prima** di `pdf.py`.

### 2. `pdf.py` – Unisce i PDF nell’ordine scelto
Legge il file `ordine_pdf.txt` e unisce i PDF corrispondenti, quindi:
- Mostra una **finestra per scegliere dove salvare** il PDF unito.
- Salva il risultato in un unico file PDF con i documenti nell’ordine specificato.

---

### ▶️ Come usarlo

1. Esegui: `python seleziona_file.py`
   - Seleziona i PDF desiderati.
   - Riordinali a piacere.
   - Clicca su "✔ Conferma" per salvare.
2. Esegui: `python pdf.py`
   - Ti verrà chiesto dove salvare il file finale.
