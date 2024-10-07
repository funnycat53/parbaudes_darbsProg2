from produkts import Produkts
import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Veikala noliktava")
root.geometry("350x600")

visi_produkti = []
pardota_vertiba = 0.0  # Mainīgais, ka satur visu produktu pārdoto vērtību

# Ekrāns
frame = ttk.Frame(root)
frame.grid(padx=10, pady=10)

options = {'padx': 5, 'pady': 5}

# Nosaukums label
nosaukums_label = ttk.Label(frame, text='Nosaukums')
nosaukums_label.grid(column=0, row=0, sticky='E', **options)

# Veids label
veids_label = ttk.Label(frame, text='Veids')
veids_label.grid(column=0, row=1, sticky='E', **options)

# Skaits label
skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=2, sticky='E', **options)

# Cena label
cena_label = ttk.Label(frame, text='Cena')
cena_label.grid(column=0, row=3, sticky='E', **options)

# Nosaukums entry
nosaukums = tk.StringVar()
nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)

# Veids entry
veids = tk.StringVar()
veids_entry = ttk.Entry(frame, textvariable=veids)
veids_entry.grid(column=1, row=1, **options)

# Skaits entry
skaits = tk.IntVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=2, **options)

# Cena entry
cena = tk.DoubleVar()
cena_entry = ttk.Entry(frame, textvariable=cena)
cena_entry.grid(column=1, row=3, **options)

# Saraksta atjaunošana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for numurs, produkts in enumerate(visi_produkti, start=1):
        listbox.insert("end", "{}. {}, {}, {}, {}€".format(numurs, produkts.nosaukums, produkts.veids, produkts.skaits, produkts.cena))

# Produkta pievienošanas button
def pievienot_produktu_button_clicked():
    produkta_nosaukums = nosaukums.get()
    produkta_veids = veids.get()
    produkta_skaits = skaits.get()
    produkta_cena = cena.get()

    visi_produkti.append(Produkts(produkta_nosaukums, produkta_veids, produkta_skaits, produkta_cena))
    result_label.config(text=visi_produkti[-1].info())
    nomainit_sarakstu()

    # Attīra teksta ievades lauciņus
    nosaukums_entry.delete(0, END)
    veids_entry.delete(0, END)
    skaits_entry.delete(0, END)
    cena_entry.delete(0, END)

# Pievienot produktu button
pievienot_button = ttk.Button(frame, text='Pievienot produktu')
pievienot_button.grid(column=2, row=0, sticky='W', **options)
pievienot_button.configure(command=pievienot_produktu_button_clicked)

# Listbox nosaukums
listbox_title = ttk.Label(frame, text='Produktu Saraksts')
listbox_title.grid(row=4, columnspan=3, **options)

# Listbox produktiem
listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=5, columnspan=3, **options)

listbox = tk.Listbox(listbox_frame, height=6, width=50, selectmode=tk.EXTENDED)
listbox.grid(row=0, column=0, sticky='nsew')

# Scrollbar priekš produktu saraksta listbox
listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
listbox_scrollbar.grid(row=0, column=1, sticky='ns')

listbox.configure(yscrollcommand=listbox_scrollbar.set)

# Nosaukums pārdoto produktu listbox
pardotie_produkti_title = ttk.Label(frame, text='Pārdoto produktu cenas')
pardotie_produkti_title.grid(row=6, columnspan=3, **options)

# Pārdoto produktu listbox
pardotie_listbox_frame = ttk.Frame(frame)
pardotie_listbox_frame.grid(row=7, columnspan=3, **options)

pardotie_listbox = tk.Listbox(pardotie_listbox_frame, height=6, width=30, selectmode=tk.SINGLE)
pardotie_listbox.grid(row=0, column=0, sticky='nsew')

# Scrollbar priekš pārdoto produktu listbox
pardotie_listbox_scrollbar = ttk.Scrollbar(pardotie_listbox_frame, orient=tk.VERTICAL, command=pardotie_listbox.yview)
pardotie_listbox_scrollbar.grid(row=0, column=1, sticky='ns')

pardotie_listbox.configure(yscrollcommand=pardotie_listbox_scrollbar.set)

# Pārdoto produktu kopējās vērtības listbox nosaukums
kopeja_vertiba_title = ttk.Label(frame, text='Kopējā pārdoto produktu vērtība')
kopeja_vertiba_title.grid(row=8, columnspan=3, **options)

# Listbox priekš pārdoto produktu kopējās vērtības
kopeja_vertiba_listbox = tk.Listbox(frame, height=1, width=30, selectmode=tk.SINGLE)
kopeja_vertiba_listbox.grid(row=9, columnspan=3, **options)

def mainit_saturu():
    # Dabū sarakstā izvēlēto objektu
    izveletie = listbox.curselection()

    if izveletie:
        izveletais = izveletie[0]
        izveletais_produkts = visi_produkti[izveletais]

        # Dabū jaunos datus, kurus ievadīja teksta laukā
        jauns_nosaukums = nosaukums.get() if nosaukums.get() else izveletais_produkts.nosaukums
        jauns_veids = veids.get() if veids.get() else izveletais_produkts.veids

        # Dabū jaunos datus, kurus ievadīja skaits laukā
        jauns_skaits = izveletais_produkts.skaits  # Ja nekas nav ievadīts, paliek skaitlis, kas iepriekš bija
        if skaits_entry.get():
            try:
                jauns_skaits = int(skaits_entry.get())
            except ValueError:
                showinfo("Kļūda", "Lūdzu ievadiet skaitli.")
                return

        # Dabū jaunos datus, kurus ievadija cena laukā
        jauna_cena = izveletais_produkts.cena  # Ja nekas nav ievadīts, paliek skaitlis, kas iepriekš bija
        if cena_entry.get():
            try:
                jauna_cena = float(cena_entry.get())
            except ValueError:
                showinfo("Kļūda", "Lūdzu ievadiet skaitli.")
                return

        # Atjaunina izvēlēto produktu
        izveletais_produkts.nosaukums = jauns_nosaukums
        izveletais_produkts.veids = jauns_veids
        izveletais_produkts.skaits = jauns_skaits
        izveletais_produkts.cena = jauna_cena

        # Atjaunina attiecīgo ievades lauku
        listbox.delete(izveletais)
        listbox.insert(izveletais, f"{jauns_nosaukums}, {jauns_veids}, {jauns_skaits}, {jauna_cena}€")

        # Attīra teksta ievades lauciņus
        nosaukums_entry.delete(0, END)
        veids_entry.delete(0, END)
        skaits_entry.delete(0, END)
        cena_entry.delete(0, END)

# Rediģēt Button
rediget_button = ttk.Button(frame, text='Rediģēt datus')
rediget_button.grid(column=2, row=1, sticky='W', **options)
rediget_button.configure(command=mainit_saturu)

def pardots_produkts():
    global pardota_vertiba 
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        produkts = visi_produkti[izveletais]

        # Pārbauda vai produkta skaits ir virs 0
        if produkts.skaits <= 0:
            showinfo("Kļūda", f"{produkts.nosaukums} ir izpārdots!")  # Parāda error, ja skaits ir 0 un vēl cenšas izmantot pārdot button
            continue  

        # Summē kopā visu produktu cenas
        pardota_vertiba += produkts.cena

        # Ievieto pārdotos produktus pārdoto produktu listbox
        pardotie_listbox.insert(END, f"{produkts.nosaukums}, {produkts.cena}€")

        # Atjaunina kopēja pārdoto produktu vērtība listbox
        kopeja_vertiba_listbox.delete(0, END)  # izdzēš iepriekšējo vērtību
        kopeja_vertiba_listbox.insert(END, f"{pardota_vertiba}€")

        produkts.pardotais_produkts()
        jaunais_teksts += produkts.info() + "\n"

    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()

# Pārdoto produktu Button
pardots_button = ttk.Button(frame, text='Produkts Pārdots')
pardots_button.grid(column=2, row=2, sticky='W', **options)
pardots_button.configure(command=pardots_produkts)

# Rezultātu Label
result_label = ttk.Label(frame, text='')
result_label.grid(columnspan=3, **options)

root.mainloop()
