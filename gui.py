import tkinter as tk
from tkinter import messagebox
from decisore_di_abbonamenti import decisore

def calcola():
    viaggi = "".join("1" if var.get() else "." for var in giorni_vars)
    costo, abbonamenti = decisore(viaggi)
    risultato = f"Spesa minima: {round(costo,2)} €\n\nAbbonamenti da comprare:\n"
    for start, end, tipo in abbonamenti:
        risultato += f" - {tipo} (giorni {start}-{end})\n"
    messagebox.showinfo("Risultato", risultato)

def gui():
    root = tk.Tk()
    root.title("Pianificatore viaggi")

    tk.Label(root, text="seleziona tutti i giorni in cui viaggerai", font=("Helvetica", 16)).pack()

    giorni_frame = tk.Frame(root)
    giorni_frame.pack()

    giorni_vars = []
    for i in range(90):
        row = i // 7 
        column = i % 7
        padx = 5
        pady = 5
            
        var = tk.BooleanVar()
        chk = tk.Checkbutton(giorni_frame, text=str(i % 7 + 1), variable=var)
        chk.grid(row=row, column=column, padx=padx, pady=pady)
        giorni_vars.append(var)

    tk.Button(root, text="Calcola spesa minima", command=calcola, font=("Helvetica", 16)).pack(pady=10)

    root.mainloop()