import tkinter as tk
from tkinter import messagebox
import base64
import hashlib
import random
from cryptography.fernet import Fernet

MASTER_PASSWORD = "10032005"

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_data(data, key):
    return Fernet(key).encrypt(data.encode())

def decrypt_data(token, key):
    return Fernet(key).decrypt(token).decode()

def generate_2fa():
    return str(random.randint(100000, 999999))

class MobileSecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📱 Mobile Security")
        self.root.geometry("400x430")
        self.root.resizable(False, False)
        
        self.key = generate_key(MASTER_PASSWORD)
        self.encrypted_data = None
        self.generated_2fa = None

        tk.Label(root, text="📱 Mobile Security Demo", font=("Arial", 16, "bold")).pack(pady=10)

        self.permission_text = tk.Text(root, height=4, width=45)
        self.permission_text.pack()
        self.display_permissions()

        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Secret (e.g., token):").pack()
        self.secret_entry = tk.Entry(root)
        self.secret_entry.pack()

        tk.Button(root, text="🔐 Encrypt & Send 2FA", command=self.encrypt_and_send_2fa).pack(pady=10)

        tk.Label(root, text="Enter 2FA Code:").pack()
        self.otp_entry = tk.Entry(root)
        self.otp_entry.pack()

        tk.Button(root, text="🔓 Decrypt Secret", command=self.decrypt_secret).pack(pady=10)

    def display_permissions(self):
        permissions = {"Camera": False, "Location": False, "Contacts": True}
        for perm, granted in permissions.items():
            status = "✅" if granted else "❌"
            self.permission_text.insert(tk.END, f"Permission for {perm}: {status}\n")
        self.permission_text.config(state='disabled')

    def encrypt_and_send_2fa(self):
        secret = self.secret_entry.get()
        if not secret:
            messagebox.showwarning("Input Error", "Please enter your secret.")
            return

        self.encrypted_data = encrypt_data(secret, self.key)
        self.generated_2fa = generate_2fa()
        messagebox.showinfo("2FA Sent", f"2FA Code: {self.generated_2fa} (simulated)")

    def decrypt_secret(self):
        if self.otp_entry.get() != self.generated_2fa:
            messagebox.showerror("2FA Failed", "❌ 2FA failed! Access denied.")
            return

        try:
            decrypted = decrypt_data(self.encrypted_data, self.key)
            messagebox.showinfo("Access Granted", f"✅ Your secret is: {decrypted}")
        except:
            messagebox.showerror("Access Denied", "❌ Decryption failed!")

root = tk.Tk()
app = MobileSecurityApp(root)
root.mainloop()
