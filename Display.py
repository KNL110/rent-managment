from tkinter import *
from CRUD_OPS import *
from tkinter import messagebox, ttk
from datetime import datetime

Width = 270
Height = 370


class RentManagementGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Rent Management")
        self.root.minsize(600, 400)
        self.list_rent_tab()
        self.menu_bar()
        self.refresh_list()

    def add_rent_tab(self):
        self.add = Tk()
        self.add.title("Add Rent")
        self.add.geometry("270x370")
        self.add.maxsize(Width, Height)
        self.add.minsize(Width, Height)
        add_rent = ('Rent Id', 'Email_Id', 'USERNAME', 'PASSWORD', 'tenant_name', 'room_No', 'Rent amount', 'due_date')
        self.entries = []
        # add rent tab
        i = 0
        while i < len(add_rent):
            Label(self.add, text=f'{add_rent[i]}:').grid(row=i, column=0, padx=10, pady=10)
            entry = Entry(self.add)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries.append(entry)
            i = i + 1
        # add rent button
        Button(self.add, text="Add Rent", command=self.add_rent_button).grid(row=i, column=0, columnspan=2, pady=10)
        self.add.mainloop()

    def update_rent_tab(self):
        update_frame = self.update_frame = Tk()
        update_frame.title("Update Rent Data")
        update_frame.geometry("270x370")
        update_frame.maxsize(270, 370)
        update_frame.minsize(270, 370)
        # Update rent tab
        updated_rent = ('Rent Id', 'Email_Id', 'USERNAME', 'PASSWORD', 'tenant_name', 'room_No', 'Rent amount',
                        'due_date')
        self.updated_entry = []
        Label(update_frame, text='Rent Id to update:').grid(row=0, column=0, padx=10, pady=10)
        self.update_rent_entry = Entry(update_frame)
        self.update_rent_entry.grid(row=0, column=1, padx=10, pady=10)
        i = 1
        while i < len(updated_rent):
            Label(update_frame, text=f'New {updated_rent[i]}:').grid(row=i, column=0, padx=10, pady=10)
            entry = Entry(update_frame)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.updated_entry.append(entry)
            i = i + 1
        # update rent button
        Button(update_frame, text="Update Rent", command=self.update_rent_button).grid(row=8, column=0, columnspan=2,
                                                                                       pady=10)
        update_frame.mainloop()

    def delete_rent_tab(self):
        delete_rent_frame = self.delete_rent_frame = Tk()
        delete_rent_frame.title("Delete Rent Data")
        # Delete Rent Form
        Label(delete_rent_frame, text="Rent ID to Delete:").grid(row=0, column=0, padx=10, pady=10)
        self.delete_rent_id_entry = Entry(delete_rent_frame)
        self.delete_rent_id_entry.grid(row=0, column=1, padx=10, pady=10)
        # Delete Rent Button
        Button(delete_rent_frame, text="Delete Rent",
               command=self.delete_rent_button).grid(row=1, column=0, columnspan=2, pady=10)
        delete_rent_frame.mainloop()

    def list_rent_tab(self):
        # List Rents Table
        self.tree = ttk.Treeview(self.root, )
        self.tree["columns"] = (
            "Rent ID", "Email_Id", "USERNAME", "PASSWORD", "Tenant Name", "Room Number", "Amount", "Due Date")
        # Define columns
        self.tree.column("#0", width=0, stretch=NO)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=CENTER, width=190)
            self.tree.heading(col, text=col, anchor=CENTER)
        self.tree.pack(expand=True, fill=BOTH)
        # Refresh Button
        refresh_button = Button(self.root, text="Refresh", command=self.refresh_list)
        refresh_button.pack(fill='x', side='bottom')
        self.refresh_list()

    def add_rent_button(self):
        self.add_values = [entry.get() for entry in self.entries]
        try:
            Id = int(self.add_values[0])
            amount = float(self.add_values[6])
            datetime.strptime(self.add_values[7], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid Rent Id/Amount/Due Date format.")
            return

        create_rent(Id, self.add_values[1], self.add_values[2], self.add_values[3], self.add_values[4],
                    self.add_values[5], amount, self.add_values[7])
        messagebox.showinfo("Success", "Rent added successfully.")
        self.add.destroy()
        self.refresh_list()

    def update_rent_button(self):
        self.update_values = [entry.get() for entry in self.updated_entry]
        try:
            amount = float(self.update_values[5])
            datetime.strptime(self.update_values[6], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount or Due Date format.")
            return

        rent_id = int(self.update_rent_entry.get())
        new_data = {
            'Email_Id': self.update_values[0],
            'USERNAME': self.update_values[1],
            'PASSWORD': self.update_values[2],
            'tenant_name': self.update_values[3],
            'room_No': self.update_values[4],
            'amount': amount,
            'due_date': self.update_values[6]
        }
        update_rent(rent_id, new_data)
        messagebox.showinfo("Success", "Rent updated successfully.")
        self.update_frame.destroy()
        self.refresh_list()

    def delete_rent_button(self):
        rent_id = int(self.delete_rent_id_entry.get())
        delete_rent(rent_id)
        messagebox.showinfo("Success", "Rent deleted successfully.")
        self.delete_rent_frame.destroy()
        self.refresh_list()

    def refresh_list(self):
        all_rents = []
        for item in self.tree.get_children():
            self.tree.delete(item)

        cursor.execute("SELECT * FROM Rent")
        rents = cursor.fetchall()
        for rent in rents:
            passkey = list(rent)
            passkey[3] = "*****"
            all_rents.append(tuple(passkey))
        for rent in all_rents:
            self.tree.insert("", "end", values=rent)

    def menu_bar(self):
        main_menu = Menu(self.root)
        m1 = Menu(main_menu, tearoff=0)
        m1.add_command(label="Add rent", command=self.add_rent_tab)
        m1.add_command(label="Update Rent", command=self.update_rent_tab)
        m1.add_command(label="Delete Rent", command=self.delete_rent_tab)
        self.root.config(menu=main_menu)
        main_menu.add_cascade(label='Edit', menu=m1)
