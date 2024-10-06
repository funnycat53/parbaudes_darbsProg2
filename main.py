from produkts import Produkts
import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Veikala noliktava")
root.geometry("350x600")

visi_produkti = []
total_sold_price = 0.0  # Variable to hold the total sold price

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

# skaits label
skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=2, sticky='E', **options)

# cena label
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

# skaits entry
skaits = tk.IntVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=2, **options)

# cena entry
cena = tk.DoubleVar()
cena_entry = ttk.Entry(frame, textvariable=cena)
cena_entry.grid(column=1, row=3, **options)

# saraksta atjaunosana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for produkts in visi_produkti:
        listbox.insert("end", "{}, {}, {}, {}€".format(produkts.nosaukums, produkts.veids, produkts.skaits, produkts.cena))

# ražošana button
def razot_button_clicked():
    produkta_nosaukums = nosaukums.get()
    produkta_veids = veids.get()
    produkta_skaits = skaits.get()
    produkta_cena = cena.get()

    # Create a new product instance and append it to the list
    visi_produkti.append(Produkts(produkta_nosaukums, produkta_veids, produkta_skaits, produkta_cena))
    result_label.config(text=visi_produkti[-1].info())
    nomainit_sarakstu()

    # Clear entries after adding
    nosaukums_entry.delete(0, END)
    veids_entry.delete(0, END)
    skaits_entry.delete(0, END)
    cena_entry.delete(0, END)

razot_button = ttk.Button(frame, text='Pievienot produktu')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=razot_button_clicked)

# Listbox Title
listbox_title = ttk.Label(frame, text='Produktu Saraksts')
listbox_title.grid(row=4, columnspan=3, **options)

# Listbox for the main product list
listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=5, columnspan=3, **options)

listbox = tk.Listbox(listbox_frame, height=6, width=50, selectmode=tk.EXTENDED)
listbox.grid(row=0, column=0, sticky='nsew')

# Scrollbar for the product list
listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
listbox_scrollbar.grid(row=0, column=1, sticky='ns')

listbox.configure(yscrollcommand=listbox_scrollbar.set)

# Title for the sold products and their prices
sold_products_title = ttk.Label(frame, text='Pārdoto produktu cenas')
sold_products_title.grid(row=6, columnspan=3, **options)

# New Listbox for sold product prices
sold_listbox_frame = ttk.Frame(frame)
sold_listbox_frame.grid(row=7, columnspan=3, **options)

sold_listbox = tk.Listbox(sold_listbox_frame, height=6, width=30, selectmode=tk.SINGLE)
sold_listbox.grid(row=0, column=0, sticky='nsew')

# Scrollbar for the sold product list
sold_listbox_scrollbar = ttk.Scrollbar(sold_listbox_frame, orient=tk.VERTICAL, command=sold_listbox.yview)
sold_listbox_scrollbar.grid(row=0, column=1, sticky='ns')

sold_listbox.configure(yscrollcommand=sold_listbox_scrollbar.set)

# Title for the total sold price
total_price_title = ttk.Label(frame, text='Kopējā pārdoto produktu vērtība')
total_price_title.grid(row=8, columnspan=3, **options)

# New Listbox for total sold price
total_price_listbox = tk.Listbox(frame, height=1, width=30, selectmode=tk.SINGLE)
total_price_listbox.grid(row=9, columnspan=3, **options)

# Updated mainit_saturu function
def mainit_saturu():
    # Get the currently selected item index in the Listbox
    selected_indices = listbox.curselection()

    if selected_indices:
        selected_index = selected_indices[0]
        selected_product = visi_produkti[selected_index]

        # Get new values from entry fields
        jauns_nosaukums = nosaukums.get() if nosaukums.get() else selected_product.nosaukums
        jauns_veids = veids.get() if veids.get() else selected_product.veids

        # Handle skaits (count) field
        jauns_skaits = selected_product.skaits  # Default to current value
        if skaits_entry.get():
            try:
                jauns_skaits = int(skaits_entry.get())
            except ValueError:
                showinfo("Input Error", "Please enter a valid integer for the count.")
                return

        # Handle cena (price) field
        jauna_cena = selected_product.cena  # Default to current value
        if cena_entry.get():
            try:
                jauna_cena = float(cena_entry.get())
            except ValueError:
                showinfo("Input Error", "Please enter a valid float for the price.")
                return

        # Update the selected product
        selected_product.nosaukums = jauns_nosaukums
        selected_product.veids = jauns_veids
        selected_product.skaits = jauns_skaits
        selected_product.cena = jauna_cena

        # Update the specific entry in the Listbox
        listbox.delete(selected_index)
        listbox.insert(selected_index, f"{jauns_nosaukums}, {jauns_veids}, {jauns_skaits}, {jauna_cena}€")

        # Clear entries after updating
        nosaukums_entry.delete(0, END)
        veids_entry.delete(0, END)
        skaits_entry.delete(0, END)
        cena_entry.delete(0, END)

# Edit Button
mainit_button = ttk.Button(frame, text='Rediģēt datus')
mainit_button.grid(column=2, row=1, sticky='W', **options)
mainit_button.configure(command=mainit_saturu)

# Updated pardots_produkts function
def pardots_produkts():
    global total_sold_price  # Reference the global total price variable
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        product = visi_produkti[izveletais]

        # Check if the product count is greater than zero before selling
        if product.skaits <= 0:
            showinfo("Stock Error", f"{product.nosaukums} ir izpārdots!")  # Show an error message if stock is zero
            continue  # Skip to the next selected item

        # Add the price of the sold product to the total
        total_sold_price += product.cena

        # Insert sold product info to the sold Listbox
        sold_listbox.insert(END, f"{product.nosaukums}, {product.cena}€")

        # Update the total sold price Listbox
        total_price_listbox.delete(0, END)  # Clear previous total
        total_price_listbox.insert(END, f"Total Sold Price: {total_sold_price}€")

        product.pardotais_produkts()  # Call the method to mark the product as sold
        jaunais_teksts += product.info() + "\n"

    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()

# Sold Product Button
pardots_button = ttk.Button(frame, text='Produkts Pārdots')
pardots_button.grid(column=2, row=2, sticky='W', **options)
pardots_button.configure(command=pardots_produkts)

# Result Label
result_label = ttk.Label(frame, text='')
result_label.grid(columnspan=3, **options)

root.mainloop()
