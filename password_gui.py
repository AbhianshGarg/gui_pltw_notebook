from cgitb import text
import tkinter as tk
 
 
def login_button():
  frame_auth.tkraise()
  password = ent_password.get()
  print(password)
  show_password = tk.Label(frame_auth, text=password)
  show_password.pack()
 
# main window
root = tk.Tk()
root.wm_geometry("300x300")
frame_login = tk.Frame(root)
root.title('Authorization')
frame_login.grid(row=0, column=0, sticky='news')
 
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack()
 
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
username = ent_username.get()
 
lbl_password = tk.Label(frame_login, text= 'Password:', font='Courier')
lbl_password.pack()
 
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
 
 
login = tk.Button(frame_login, text='Login', font= 'Courier',command=login_button)
login.pack()
 
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')
 
 
 
frame_login.tkraise()
 
 
 
root.mainloop()
