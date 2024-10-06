from produkts import Produkts, Dators
import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Veikala noliktava")
root.geometry("500x500")

visi_produkti = []

# Ekrāns
frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

# Nosaukums label
nosaukums_label = ttk.Label(frame, text='Nosaukums')
nosaukums_label.grid(column=0, row=0, sticky='E', **options)

# Veids label
veids_label = ttk.Label(frame, text='Veids')
veids_label.grid(column=0, row=1, sticky='E', **options)

# skaits label
skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=2, sticky='E', **options)

# Nosaukums entry
nosaukums = tk.StringVar()
nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

# Veids entry
veids = tk.StringVar()
veids_entry = ttk.Entry(frame, textvariable=veids)
veids_entry.grid(column=1, row=1, **options)
veids_entry.focus()

# skaits entry
skaits = tk.IntVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=2, **options)
skaits_entry.focus()

# saraksta atjaunosana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for produkts in visi_produkti:
        listbox.insert("end","{},{},{}".format(produkts.nosaukums, produkts.veids, produkts.skaits))

# ražošana button
def razot_button_clicked():
    produkta_nosaukums = nosaukums.get()
    produkta_veids = veids.get()
    produkta_skaits = skaits.get()
    visi_produkti.append(Produkts(produkta_nosaukums, produkta_veids, produkta_skaits))
    result_label.config(text=visi_produkti[-1].info())
    nomainit_sarakstu()
    # listbox.insert("end","{},{},{}".format(produkta_nosaukums, produkta_veids, produkta_skaits))

razot_button = ttk.Button(frame, text='Ražot')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=razot_button_clicked)

# palielinat skaitu poga
def palielinat_skaitu():
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        visi_produkti[izveletais].paaugstinas_skaits()
        jaunais_teksts += visi_produkti[izveletais].info() + "\n"
    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()


skaits_button = ttk.Button(frame, text='Palielinat skaitu')
skaits_button.grid(column=1, row=5, sticky='W', **options)
skaits_button.configure(command=palielinat_skaitu)


# samazinat skaitu poga
def samazinat_skaitu():
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        visi_produkti[izveletais].samazinas_skaits()
        jaunais_teksts += visi_produkti[izveletais].info() + "\n"
    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()


skaits_button = ttk.Button(frame, text='Samazināt skaitu')
skaits_button.grid(column=1, row=6, sticky='W', **options)
skaits_button.configure(command=samazinat_skaitu)

# listbox

saturs = tk.Variable(value=tuple(visi_produkti))

listbox = tk.Listbox(
    root,
    listvariable=saturs,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.grid(row=4, columnspan=3, **options)


# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()