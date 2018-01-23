import tkinter as tk
import dictionary as dict



def clearAll():
    inputText.set(' ')
    outputText.set(' ')

def translateText():
    textToTranslate = inputText.get()
    selectedRadio = v.get()
    if selectedRadio == 1:
        result = dict.translateFromMorse(textToTranslate)
        outputText.set(result)
    else:
        result = dict.translateToMorse(textToTranslate)
        outputText.set(result)


master = tk.Tk()
master.title('Morse Code Translator')
master.configure(background='black')

usageText = """Type in the text you want decrypted/encrypted in the top entry box, select the option you want, then click on "Translate!" 
            Press C to clear or Exit to exit the application.
             Note: when translating from Morse code, separate characters with a space and words with two spaces"""
lbUsage = tk.Label(master,
                   text=usageText,
                   justify=tk.CENTER).pack(side=tk.TOP,padx=10,pady=10)

inputText = tk.StringVar()
tk.Entry(master,
         width=100,
         textvariable=inputText).pack(side=tk.TOP,padx=10,pady=10)

outputText = tk.StringVar()
tk.Entry(master,
         width=100,
         state='readonly',
         textvariable=outputText).pack(side=tk.TOP,padx=10,pady=10)


v = tk.IntVar()
v.set(1)
tk.Radiobutton(master,
               text='Translate from Morse code',
               variable=v,
               value=1).pack(anchor=tk.S)
tk.Radiobutton(master,
               text='Translate to Morse code',
               variable=v,
               value=2).pack(anchor=tk.S)

tk.Button(master,text='C',command=clearAll).pack(side=tk.TOP)
tk.Button(master,text='Translate',command=translateText).pack(side=tk.TOP)
tk.Button(master,text='EXIT',command=master.destroy).pack(side=tk.TOP)

tk.mainloop()