from Display import *
import atexit
from CRUD_OPS import export_to_text
from tkinter import filedialog

Width = 270  # Increase the width
Height = 150  # Decrease the height


class SignIn:
    def __init__(self):
        self.main()

    def main(self):
        self.root = Tk()
        self.root.title("Home page")
        self.root.geometry(f"{Width}x{Height}")
        self.root.maxsize(Width, Height)
        self.root.minsize(Width, Height)
        b1 = Button(self.root, text="Admin Log In", command=self.admin_page, width=20, height=2)
        b1.grid(row=2, column=1, padx=60, pady=15)
        b2 = Button(self.root, text="Tenant Log In", command=self.tenant_page, width=20, height=2)
        b2.grid(row=3, column=1, padx=60, pady=10)
        self.root.mainloop()

    def admin_page(self):
        self.root.destroy()
        self.admin = Tk()
        self.admin.title("Admin Login")
        self.admin.geometry(f"{Width}x{Height}")
        self.admin.maxsize(Width, Height)
        self.admin.minsize(Width, Height)
        Label(self.admin, text="Username").grid(row=0, column=0, padx=10, pady=10)
        Label(self.admin, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.auser_entry = Entry(self.admin)
        self.apass_entry = Entry(self.admin, show="*")
        self.auser_entry.grid(row=0, column=1, padx=10, pady=10)
        self.apass_entry.grid(row=1, column=1, padx=10, pady=10)
        Button(self.admin, text="Log In", command=self.admin_signin).grid(row=2, column=1, padx=10, pady=10)
        self.admin.mainloop()

    def tenant_page(self):
        self.root.destroy()
        self.tenant = Tk()
        self.tenant.title("Tenant Login")
        self.tenant.geometry(f"{Width}x{Height}")
        self.tenant.maxsize(Width, Height)
        self.tenant.minsize(Width, Height)
        Label(self.tenant, text="Username").grid(row=0, column=0, padx=10, pady=10)
        Label(self.tenant, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.user_entry = Entry(self.tenant)
        self.pass_entry = Entry(self.tenant, show="*")
        self.user_entry.grid(row=0, column=1, padx=10, pady=10)
        self.pass_entry.grid(row=1, column=1, padx=10, pady=10)
        Button(self.tenant, text="Log In", command=self.tenant_signin).grid(row=2, column=1, padx=10, pady=10)
        self.tenant.mainloop()

    def admin_signin(self):
        if self.auser_entry.get() == "root" and self.apass_entry.get() == "qsc24nfyv6":
            messagebox.showinfo("Success", "Login In successfully.")
            self.admin.destroy()
            root1 = Tk()
            RentManagementGui(root1)
            atexit.register(close_connection)
            root1.mainloop()
        else:
            messagebox.showinfo("Error!", "Invalid credentials.Please try again!")

    def tenant_signin(self):
        self.labels = (
            'Rent Id', 'Email_Id', 'USERNAME', 'PASSWORD', 'tenant_name', 'room_No', 'Rent amount', 'due_date')
        self.tenant_detail = []
        cursor.execute("SELECT * FROM Rent")
        rents = cursor.fetchall()
        i = 0
        while i < len(rents):
            if self.user_entry.get() in rents[i] and self.pass_entry.get() in rents[i]:
                self.tenant_detail = rents[i]
                break
            else:
                i = i + 1
        try:
            if self.user_entry.get() == self.tenant_detail[2] and self.pass_entry.get() == self.tenant_detail[3]:
                messagebox.showinfo("Success", "Login In successfully.")
                self.tenant.destroy()
                detail = Tk()
                self.detail = detail
                detail.title(f"{self.tenant_detail[4]}'s Rent Detail")
                Width = 270
                Height = 370
                detail.geometry(f"{Width}x{Height}")
                detail.maxsize(Width, Height)
                detail.minsize(Width, Height)
                i = 0
                while i < len(self.labels):
                    Label(detail, text=f"{self.labels[i]}:").grid(row=i, column=0, padx=10, pady=10)
                    Label(detail, text=f"{self.tenant_detail[i]}").grid(row=i, column=1, padx=10, pady=10)
                    i = i + 1
                Button(detail, text="Export to Text", command=self.export_button).grid(row=i, column=1, padx=10,
                                                                                       pady=10)
                Button(detail, text="Back", command=self.back).grid(row=i, column=0, padx=10, pady=10)
                detail.mainloop()
            else:
                messagebox.showinfo("Error!", "Invalid credentials.Please try again!")
        except:
            messagebox.showinfo("Error!", "Invalid credentials.Please try again!")

    def export_button(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filepath:
            export_to_text(self.labels, self.tenant_detail, filepath)


enter = SignIn()
