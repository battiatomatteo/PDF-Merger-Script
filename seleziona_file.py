import tkinter as tk
from tkinter import filedialog, messagebox

# Classe che gestisce la GUI per selezionare e ordinare i file PDF
class FileSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleziona e ordina i PDF")
        self.selected_files = []  # Lista dei file selezionati

        # Bottone per selezionare i file PDF
        tk.Button(root, text="Scegli PDF", command=self.choose_files).pack(pady=5)

        # Lista visuale dei file scelti
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80)
        self.listbox.pack(padx=10, pady=10)

        # Frame che contiene i pulsanti per riordinare i file
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        # Pulsanti per spostare su/giù e confermare
        tk.Button(btn_frame, text="↑ Su", command=self.move_up).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="↓ Giù", command=self.move_down).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="✔ Conferma", command=self.confirm).grid(row=0, column=2, padx=5)

    # Apertura finestra per selezionare i file
    def choose_files(self):
        files = filedialog.askopenfilenames(
            title="Seleziona i file PDF",
            filetypes=[("PDF files", "*.pdf")]
        )
        if files:
            self.selected_files = list(files)
            self.update_listbox()

    # Aggiorna la lista visuale con i file selezionati
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.listbox.insert(tk.END, file)

    # Sposta il file selezionato in alto nella lista
    def move_up(self):
        i = self.listbox.curselection()
        if not i or i[0] == 0:
            return
        i = i[0]
        self.selected_files[i], self.selected_files[i - 1] = self.selected_files[i - 1], self.selected_files[i]
        self.update_listbox()
        self.listbox.select_set(i - 1)

    # Sposta il file selezionato in basso nella lista
    def move_down(self):
        i = self.listbox.curselection()
        if not i or i[0] == len(self.selected_files) - 1:
            return
        i = i[0]
        self.selected_files[i], self.selected_files[i + 1] = self.selected_files[i + 1], self.selected_files[i]
        self.update_listbox()
        self.listbox.select_set(i + 1)

    # Conferma l’ordine selezionato e lo salva in un file di testo
    def confirm(self):
        if not self.selected_files:
            messagebox.showerror("Errore", "Nessun file selezionato.")
            return
        with open("ordine_pdf.txt", "w", encoding="utf-8") as f:
            for path in self.selected_files:
                f.write(path + "\n")
        self.root.destroy()

# Avvia l’interfaccia
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelector(root)
    root.mainloop()
