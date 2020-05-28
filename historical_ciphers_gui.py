from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from historical_ciphers import *

"""
This function is called after the start button was pressed
"""
def calculate(output,comboBox,secret,text,mode):
    #print(caesar(text=str(text.get()), mode="e", s=3))
    result = ""
    output.delete('1.0', END)
    """
    Caesar Part
    """
    if comboBox.get() == "Caesar":
        if mode.get() == "encrypt":
            try:
                result = caesar(text=text.get(),mode="e",s=int(secret.get()))
                output.insert("end", str(result))
            except:
                messagebox.showinfo("ERROR", "Shift operator is no integer")
        elif mode.get() == "decrypt":
            try:
                result = caesar(text=text.get(), mode="d", s=int(secret.get()))
                output.insert("end", str(result))
            except:
                messagebox.showinfo("ERROR", "Shift operator is no integer")
    """
    Vigenere Part
    """
    if comboBox.get() == "Vigenere":
        # check if an integer is included
        if any(map(str.isdigit, secret.get())):
            messagebox.showinfo("ERROR", "Secret is not a full string")
        else:
            if mode.get() == "encrypt":
                result = vigenere(text=text.get(), mode="e", key=secret.get())
                output.insert("end", str(result))
            elif mode.get() == "decrypt":
                result = vigenere(text=text.get(), mode="d", key=secret.get())
                output.insert("end", str(result))


def windowTextUpdate(label,comboboxCipher):
    if comboboxCipher.get() == "Caesar":
        label.config(text="Enter Shiftoperator")
    elif comboboxCipher.get() == "Vigenere":
        label.config(text="Enter Secret")

class App:
    cipher = ["Caesar","Vigenere"]
    def __init__(self, master):
        """
        cipher type/mode
        """
        self.comboBox = ttk.Combobox(master,state='readonly',values=self.cipher)
        self.comboBox.current(0)
        self.comboBox.grid(column=0,row=0)
        self.comboBoxMode = ttk.Combobox(master,state='readonly',values=["encrypt","decrypt"])
        self.comboBoxMode.current(0)
        self.comboBoxMode.grid(column=1, row=0)
        self.entryTextLabel = Label(master,text="Enter Cipher-/Plaintext:")
        self.entryTextLabel.grid(column=0,row=1)
        self.entryText = Entry(master,width=26)
        self.entryText.grid(column=1,row=1)
        """
        Secret / Shiftoperator
        """
        self.entrySecretLabel = Label(master, text="Enter Shiftoperator")
        self.entrySecretLabel.grid(column=0, row=2)
        self.entrySecret = Entry(master, width=26)
        self.entrySecret.grid(column=1, row=2)
        """
        Output
        """
        self.outputLabel = Label(master,text="Output:")
        self.outputLabel.grid(column=0,row=3)
        self.output = Text(master,height=1, width=20)
        self.output.grid(column=1,row=3)

        """
        Action specific stuff
        """
        self.button = Button(master, text="Start", command=lambda:calculate(mode=self.comboBoxMode,secret=self.entrySecret,output=self.output, comboBox=self.comboBox,text=self.entryText))
        self.button.grid(column=3, row=0)
        self.comboBox.bind("<<ComboboxSelected>>", lambda event:windowTextUpdate(label=self.entrySecretLabel,comboboxCipher=self.comboBox))

if __name__ == "__main__":
    mainWindow = Tk()
    mainWindow.title("Caesar/Vigenere Cipher")
    mainWindowHeight=mainWindow.winfo_reqheight()
    mainWindowWidth=mainWindow.winfo_reqwidth()
    positionRight = int(mainWindow.winfo_screenwidth()/2 - mainWindowWidth)
    positionDown = int(mainWindow.winfo_screenheight()/3 - mainWindowHeight)
    mainWindow.geometry("500x500"+"+{}+{}".format(positionRight,positionDown))
    app = App(mainWindow)
    mainWindow.mainloop()