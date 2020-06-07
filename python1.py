from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile 
from tkinter.ttk import Progressbar
from tkinter import messagebox
from array import *
import random
from   PIL    import Image, ImageTk, ImageDraw


window = Tk()

#Opcije prozora
window.title("Kriptografija")
window.geometry("550x770")
window.iconbitmap('C:\\Users\\ferat.000\\Desktop\\Kriptografija\\pROBA\\logo.ico')

#Kreiranje tabova

s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L','11','bold'))
s.configure('TFrame', background='#ddede6')


tab_control = ttk.Notebook(window)


tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Zadatak 1')

tab_control.add(tab2, text='Zadatak 2')

################################################################################################################
#
# Prvi zadatak
#
################################################################################################################

#Labela Title u tab1
titleLable = Label(tab1, text="DOBRODOŠLI!",  fg = "Black", font = "Verdana 15 bold",bg = '#ddede6')
titleLable.pack()

#Naslov u tab1
kriptoLable = Label(tab1, text="ENKRIPCIJA/DEKRIPCIJA",  fg = "Black", font = "Verdana 15 bold",bg = '#ddede6')
kriptoLable.pack()

#Labela za jezik tab1
langText = Label(tab1, text="Izaberite jezik : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
langText.pack(padx=5, pady=10)

#Combobox za jezike tab1
comboLang = ttk.Combobox(tab1, 
                            values=[
                                    "Engleski", 
                                    "Crnogorski",
                                    "Njemački"
                                    ], width = 25, height = 1)

comboLang.current(1)
comboLang.pack()
  
#Dugme koje mijenja jezik  
btnComboLagn = Button(tab1, text ='Promijeni', command = lambda:updateLang(), width= 15,borderwidth = '1',fg = 'black',bg = 'skyblue') 
btnComboLagn.pack(padx=5, pady=10)
  

#Labela za radioButton tab1
modeText = Label(tab1, text="Izaberite jednu od opcija : ",  fg = "Black",   font = "Verdana 10", width = 25, height = 1,bg = '#ddede6')
modeText.pack(pady=5)

#radioButton tab1
selected = IntVar()

rad1 = Radiobutton(tab1,text='Enkripcija', value=1, variable=selected,bg = '#ddede6')
rad2 = Radiobutton(tab1,text='Dekripcija', value=2, variable=selected,bg = '#ddede6')

rad1.pack()
rad2.pack()

#Labela za algoritam tab1
enkripDekripText = Label(tab1, text="Izaberite algoritam : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
enkripDekripText.pack(pady=5)

#Combobox za algoritam tab1
comboEnrkipDekrip = ttk.Combobox(tab1, 
                            values=[
                                    "Supstitucioni algoritam", 
                                    "Viženerov algoritam"
                                    ], width = 30)


comboEnrkipDekrip.current(1)
comboEnrkipDekrip.pack()

#TextLable key
textKey = Label(tab1, text="Ključ : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
textKey.pack(pady=8)

#Key
key = Entry(tab1,width=36)
key.pack()


#btnGeneriši ključ
genKljuc =  Button(tab1, text ='Generiši ključ',command = lambda:genereteKey(comboLang.get(),key), width= 15,borderwidth = '1',fg = 'white',bg = 'gray') 
genKljuc.pack(pady=12)
 


#TextArea title
textAreaText = Label(tab1, text="Unesite poruku : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
textAreaText.pack()

#TextArea tab1
txt = scrolledtext.ScrolledText(tab1,width=40,height=7)
txt.insert(INSERT,'Poruka...')
txt.pack(pady=5)

#File input title
fileText = Label(tab1, text="Unesite fajl : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
fileText.pack()

#File Input button
def open_file(): 

    
      file = askopenfile(mode ='r', filetypes =[('Text', '*.txt')]) 

      if file is not None: 
        content = file.read() 
        print(content) 
        #Ime fajla
        firstLetter = str(file)
        lastLetter = str(file)
        fLetter = firstLetter.rfind("name=")+6
        lLetter = lastLetter.rfind(".")+4
        fileCopy = str(file)
        
        txt.configure(state=DISABLED, bg='gray')
        btnFile.configure(text=fileCopy[fLetter:lLetter], width = 50,bg = 'black')



btnFile = Button(tab1, text ='Otvori', command = lambda:open_file(), width= 15,borderwidth = '1',fg = 'white',bg = 'orange') 
btnFile.pack( pady = 10)

#ProgresBar tab1
style = ttk.Style()

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(tab1, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 3

bar.pack()

#Button submit
btnSubmit = Button(tab1, text ='Počni', width= 15,  command = lambda:submitForm(),borderwidth = '1',fg = 'white',bg = 'gray') 
btnSubmit.pack(pady = 10)

names = Label(tab1, text= 'Elmaz Feratović 30/17 /\/\/\/\ Vladan Babić 24/17',fg = "Black",   font = "Verdana 10",bg = '#f2f2f2')
names.pack()
#Update jezik

def updateLang():
     if comboLang.get() == 'Engleski' or comboLang.get() == 'English' or comboLang.get() == 'Englisch':

         titleLable.configure(text='WELCOME!')
         kriptoLable.configure(text='ENCRYPTION/DECRYPTION')
         langText.configure(text = 'Choose language : ')
         comboLang.configure(values=["English","Montenegrin","German"])
         comboLang.current(0)
         btnComboLagn.configure(text='Change')
         modeText.configure(text='Choose one of the options : ')
         rad1.configure(text='Encryption')
         rad2.configure(text='Decryption')
         enkripDekripText.configure(text='Choose  cipher : ')
         comboEnrkipDekrip.configure(values=['Substitution cipher',"Vigenère's cipher"])
         comboEnrkipDekrip.current(0)
         textKey.configure(text= 'Key : ')
         genKljuc.configure(text='Generate key')
         textAreaText.configure(text = 'Enter a messsage : ')
         txt.delete(1.0,END)
         txt.insert(INSERT,'Message...')
         fileText.configure(text='Enter a file : ')
         btnFile.configure(text = 'Open')
         btnSubmit.configure(text = 'Start')

     elif comboLang.get() == 'Njemački' or comboLang.get() == 'German' or comboLang.get() == 'Deutsch':

         titleLable.configure(text='WILLKOMMEN!')
         kriptoLable.configure(text='VERSCHLÜSSELUNG/ENTSCHLÜSSELUNG')
         langText.configure(text = 'Wählen Sie eine Sprache : ')
         comboLang.configure(values=['Englisch','Montenegrinisch','Deutsch'])
         comboLang.current(2)
         btnComboLagn.configure(text='Verändern')
         modeText.configure(text='Wählen Sie eine Option : ')
         rad1.configure(text='Verschlüsselung')
         rad2.configure(text='Entschlüsselung')
         enkripDekripText.configure(text='Wählen Sie einen algorithmus : ')
         comboEnrkipDekrip.configure(values=["Ersatz-Algorithmen","Der Viser-Algorithmus"])
         comboEnrkipDekrip.current(0)
         textKey.configure(text= 'Schlüssel : ')
         genKljuc.configure(text='Generieren Sie den Schlüssel',width=22)
         textAreaText.configure(text = 'Eingeben : ')
         txt.delete(1.0,END)
         txt.insert(INSERT,'Nachricht...')
         fileText.configure(text='Dateneingabe : ')
         btnFile.configure(text = 'Offnen')
         btnSubmit.configure(text = 'Starten')

     else:

         titleLable.configure(text='DOBRODOŠLI!', width='13')
         kriptoLable.configure(text='ENKRIPCIJA/DEKRIPCIJA')
         langText.configure(text = 'Izaberite jezik :')
         comboLang.configure(values=["Engleski","Crnogorski","Njemački"])
         comboLang.current(1)
         btnComboLagn.configure(text='Promijeni')
         modeText.configure(text='Izaberite jednu od opcija :')
         rad1.configure(text='Enkripcija')
         rad2.configure(text='Dekripcija')
         enkripDekripText.configure(text='Izaberite algoritam : ')
         comboEnrkipDekrip.configure(values=["Supstitucioni  algoritam","Viženerov algoritam"])
         comboEnrkipDekrip.current(1)
         textKey.configure(text= 'Ključ : ')
         genKljuc.configure(text='Generiši ključ')
         textAreaText.configure(text = 'Unesite poruku : ')
         txt.delete(1.0,END)
         txt.insert(INSERT,'Poruka...')
         fileText.configure(text='Unesite fajl : ')
         btnFile.configure(text = 'Otvori')
         btnSubmit.configure(text = 'Počni')

############################################################################################################################################################
def submitForm():
    bar['value'] = 100
    if selected.get() == 1:
        print('Izabrana je Enkripcija podataka')
        
        if txt['state'] == 'disabled':
                print('Unijeli ste fajl')

                if comboEnrkipDekrip.get() == 'Supstitucioni  algoritam' or comboEnrkipDekrip.get() == 'Substitution cipher' or comboEnrkipDekrip.get() == 'Ersatz-Algorithmen':
                    
                    supsAlgEncriptFile(key,btnFile['text'],comboLang.get())
                    

                else:

                    vizenerAlgEncriptFile(key,btnFile['text'],comboLang.get())
          
        else:
                print('Nijeste unijeli fajl.Tekst se uzima iz TextArea')

                if comboEnrkipDekrip.get() == 'Supstitucioni  algoritam' or comboEnrkipDekrip.get() == 'Substitution cipher' or comboEnrkipDekrip.get() == 'Ersatz-Algorithmen':
                    
                    supsAlgEncriptText(key,txt,comboLang.get())

                else:
                    print('Vas izbor je Vizenerov algoritam')
                    vizenerAlgEncriptText(key,txt,comboLang.get())

                
    elif selected.get() == 2:
        print('Izabrana je Dekripcija podataka')

        if txt['state'] == 'disabled':
                print('Unijeli ste fajl')

                if comboEnrkipDekrip.get() == 'Supstitucioni  algoritam' or comboEnrkipDekrip.get() == 'Substitution cipher' or comboEnrkipDekrip.get() == 'Ersatz-Algorithmen':
                   
                    supsAlgDecriptFile(key,btnFile['text'],comboLang.get())

                else:
                    print('Vas izbor je Vizenerov algoritam')
                    
                    vizenerAlgDecriptFile(key,btnFile['text'],comboLang.get())
                    
        else:
                print('Nijeste unijeli fajl.Tekst se uzima iz TextArea')

                if comboEnrkipDekrip.get() == 'Supstitucioni  algoritam' or comboEnrkipDekrip.get() == 'Substitution cipher' or comboEnrkipDekrip.get() == 'Ersatz-Algorithmen':
                    
                    supsAlgDecriptText(key,txt,comboLang.get())

                else:
                    print('Vas izbor je Vizenerov algoritam')

                    vizenerAlgDecriptText(key,txt,comboLang.get())

    else:
        

        if comboLang.get() == 'Crnogorski' or comboLang.get() == 'Montenegrian' or comboLang.get() == 'Montenegrinisch':
            outPutError = messagebox.askretrycancel('Greška','Molimo Vas popunite sva polja')

        elif comboLang.get() == 'Engleski' or comboLang.get() == 'English' or comboLang.get() == 'Englisch':
            outPutError  = messagebox.askretrycancel('Error','Please fill out all forms')

        else:
            outPutError  = messagebox.askretrycancel('Fehler','Bitte füllen Sie alle Felder aus')

    refresh(btnFile,txt,comboLang.get())

#################################################################################################################################################################   
    
def genereteKey(lang,key):
        

        EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
        GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']
        
        if key.get() != ' ':
           key.delete(first=0,last=30)

        strTemp = ' '

        if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            tempAzbuka = random.sample(MneAzbuka, k=len(MneAzbuka))
            strTemp = ''.join(tempAzbuka)
            key.insert(INSERT,strTemp)

        elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            tempAzbuka = random.sample(EnglAzbuka, k=len(EnglAzbuka))
            strTemp = ''.join(tempAzbuka)
            key.insert(INSERT,strTemp)

        else:
            tempAzbuka = random.sample(GerAzbuka, k=len(GerAzbuka))
            strTemp = ''.join(tempAzbuka)
            key.insert(INSERT,strTemp)

################################################################################################################################################################

def supsAlgEncriptText(key,txt,lang):
    
    key = key.get().upper()
    poruka = txt.get("1.0",END).upper()
    temp = list(key)
    poruka = list(poruka)
    
    stringEcripted = ''

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    for slovo in poruka:
        
        if slovo == ' ' or slovo == '.' or slovo == ',' or slovo == '-' or slovo == '\n' or slovo == '_':
           continue

        index = lang.index(slovo)
        stringEcripted = stringEcripted + temp[index]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEcripted + '\n' + 'Key : ' + key)
    outPutFile(stringEcripted,key)
#############################################################################################################################################################

def supsAlgDecriptText(key,txt,lang):
    
    key = key.get().upper()
    poruka = txt.get("1.0",END).upper()
    temp = list(key)
    poruka = list(poruka)
    
    stringEcripted = ''

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    for slovo in poruka:
        
        if slovo == ' ' or slovo == '.' or slovo == ',' or slovo == '-' or slovo == '\n' or slovo == '_':
           continue

        index = temp.index(slovo)
        stringEcripted = stringEcripted + lang[index]

    outPut  = messagebox.showinfo('Output','Decript : ' + stringEcripted + '\n' + 'Key : ' + key)
    outPutFile(stringEcripted,key)

##############################################################################################################################################################

def supsAlgEncriptFile(key,txt,lang):
    
    file = open(txt,'r')
    poruka = file.read().upper() 
    key = key.get().upper()
    temp = list(key)
    poruka = list(poruka)
    
    stringEcripted = ''

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    for slovo in poruka:
        
        if slovo == ' ' or slovo == '.' or slovo == ',' or slovo == '-' or slovo == '\n' or slovo == '_':
           continue

        index = lang.index(slovo)
        stringEcripted = stringEcripted + temp[index]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEcripted + '\n' + 'Key : ' + key)
   
    outPutFile(stringEcripted,key)

##############################################################################################################################
def supsAlgDecriptFile(key,txt,lang):
    
    file = open(txt,'r')
    poruka = file.read().upper() 
    key = key.get().upper()
    temp = list(key)
    poruka = list(poruka)

    stringEcripted = ''

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    for slovo in poruka:
        
        if slovo == ' ' or slovo == '.' or slovo == ',' or slovo == '-' or slovo == '\n' or slovo == '_':
           continue

        index = temp.index(slovo)
        stringEcripted = stringEcripted + lang[index]

    outPut  = messagebox.showinfo('Output','Decript : ' + stringEcripted + '\n' + 'Key : ' + key)
    
    outPutFile(stringEcripted,key)
 
#########################################################################################################################################
def refresh(btnFile,txt,lang):
    
    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
        
        btnFile.configure(text = 'Otvori')
        txt.configure(state = NORMAL, bg = 'white')


    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
        
        btnFile.configure(text = 'Open')
        txt.configure(state = NORMAL, bg = 'white')


    else:
        
        btnFile.configure(text = 'Offnen')
        txt.configure(state = NORMAL, bg = 'white')

################################################################################################################################
def swamp(Engl,br):
    br = int(br)
    Azbuka = Engl[0:br]
    EnglCopy = Engl[br:len(Engl)] + Azbuka
    return EnglCopy


###################################################################################################################################################
def vizenerAlgEncriptText(key,txt,lang):
    
    key = key.get().upper()
    poruka = txt.get("1.0",END).upper()
    poruka = list(poruka)

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    T = [lang]
    broj = 1


    while broj < len(lang):
          est = swamp(lang,broj)
          T.insert(broj, est)
          broj = broj + 1
   
    brojac = 0
    stringEncipt = ''

    for slovo in poruka:

        if slovo == ' ' or slovo == '\n' or slovo == '.' or slovo == ',' or slovo == '_' or slovo == '-':
           continue

        if brojac == len(key):
           brojac = 0
        
        x = lang.index(slovo)
        y = lang.index(key[brojac])
        
        brojac = brojac + 1
        stringEncipt = stringEncipt + T[x][y]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEncipt + '\n' + 'Key : ' + key)
    outPutFile(stringEncipt,key)
#############################################################################################################################
def vizenerAlgEncriptFile(key,txt,lang):
    
    file = open(txt,'r')
    poruka = file.read().upper() 
    key = key.get().upper()
    poruka = list(poruka)

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    T = [lang]
    broj = 1


    while broj < len(lang):
          est = swamp(lang,broj)
          T.insert(broj, est)
          broj = broj + 1
   
    brojac = 0
    stringEncipt = ''

    for slovo in poruka:

        if slovo == ' ' or slovo == '\n' or slovo == '.' or slovo == ',' or slovo == '_' or slovo == '-':
           continue

        if brojac == len(key):
           brojac = 0
        
        x = lang.index(slovo)
        y = lang.index(key[brojac])
        
        brojac = brojac + 1
        stringEncipt = stringEncipt + T[x][y]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEncipt + '\n' + 'Key : ' + key)
    outPutFile(stringEncipt,key)
#########################################################################################################################
def vizenerAlgDecriptText(key,txt,lang):
    
    key = key.get().upper()
    poruka = txt.get("1.0",END).upper()
    poruka = list(poruka)

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    T = [lang]
    broj = 1


    while broj < len(lang):
          est = swamp(lang,broj)
          T.insert(broj, est)
          broj = broj + 1
   
    brojac = 0
    stringEncipt = ''

    for slovo in poruka:

        if slovo == ' ' or slovo == '\n' or slovo == '.' or slovo == ',' or slovo == '_' or slovo == '-':
           continue

        if brojac == len(key):
           brojac = 0
        
        
        y = lang.index(key[brojac])
        x = T[y].index(slovo)
        
        brojac = brojac + 1
        stringEncipt = stringEncipt + lang[x]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEncipt + '\n' + 'Key : ' + key)
    outPutFile(stringEncipt,key)
################################################################################################################################################
 
def vizenerAlgDecriptFile(key,txt,lang):
    
    file = open(txt,'r')
    poruka = file.read().upper() 
    key = key.get().upper()
    poruka = list(poruka)

    EnglAzbuka = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MneAzbuka  = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'Ś', 'T', 'U', 'V', 'Z', 'Ź', 'Ž']
    GerAzbuka  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü','ß']

    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
            lang = MneAzbuka

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
            lang = EnglAzbuka

    else:
            lang = GerAzbuka
    
    T = [lang]
    broj = 1


    while broj < len(lang):
          est = swamp(lang,broj)
          T.insert(broj, est)
          broj = broj + 1
   
    brojac = 0
    stringEncipt = ''

    for slovo in poruka:

        if slovo == ' ' or slovo == '\n' or slovo == '.' or slovo == ',' or slovo == '_' or slovo == '-':
           continue

        if brojac == len(key):
           brojac = 0
        
        
        y = lang.index(key[brojac])
        x = T[y].index(slovo)
        
        brojac = brojac + 1
        stringEncipt = stringEncipt + lang[x]

    outPut  = messagebox.showinfo('Output','Encript : ' + stringEncipt + '\n' + 'Key : ' + key)
    outPutFile(stringEncipt,key)
##################################################################################################################################################

def outPutFile(str1,key):
    f = open('Desktop\\CIPHERCode.txt','w+')

    f.write('Text: ' + str1 + '\r\nKey : ' + key)

    f.close()

#########################################################################################################################################################

#########################################################################################################################################################
#
#############   Drugi zadatak  ##########################################################################################################################
#
#########################################################################################################################################################

#Labela Title u tab1
titleLable2 = Label(tab2, text="DOBRODOŠLI!",  fg = "Black", font = "Verdana 15 bold",bg = '#ddede6')
titleLable2.pack()

#Naslov u tab1
kriptoLable2 = Label(tab2, text="KINESKA TEOREMA O OSTACIMA",  fg = "Black", font = "Verdana 15 bold",bg = '#ddede6')
kriptoLable2.pack()


#Labela za jezik tab1
langText2 = Label(tab2, text="Izaberite jezik : ",  fg = "Black",   font = "Verdana 10",bg = '#ddede6')
langText2.pack(padx=5, pady=10)

#Combobox za jezike tab1
comboLang2 = ttk.Combobox(tab2, 
                            values=[
                                    "Engleski", 
                                    "Crnogorski",
                                    "Njemački"
                                    ], width = 25, height = 1)

comboLang2.current(1)
comboLang2.pack()
  



#Dugme koje mijenja jezik  
btnComboLagn2 = Button(tab2, text ='Promijeni', command = lambda:updateLang2(), width= 15,borderwidth = '1',fg = 'black',bg = 'skyblue') 
btnComboLagn2.pack(padx=5, pady=10)

numbers = Label(tab2,text="Unesite brojeve : ",  fg = "Black",   font = "Verdana 15",bg = '#ddede6')
numbers.pack(pady= 10)

m1 = PanedWindow(tab2)
m1.pack()

num1 = Entry(m1, width = 3)
sign = Label(m1, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2 = Entry(m1, width = 3)
mod  = Label(m1, text="mod", font = "Verdana 15",bg = '#ddede6')
num3 = Entry(m1, width = 3)
m1.add(num1)
m1.add(sign)
m1.add(num2)
m1.add(mod)
m1.add(num3)

m2 = PanedWindow(tab2)
m2.pack()

num1_2 = Entry(m2, width = 3)
sign = Label(m2, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_2 = Entry(m2, width = 3)
mod  = Label(m2, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_2= Entry(m2, width = 3)
m2.add(num1_2)
m2.add(sign)
m2.add(num2_2)
m2.add(mod)
m2.add(num3_2)

m3 = PanedWindow(tab2)
m3.pack()

num1_3 = Entry(m3, width = 3)
sign = Label(m3, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_3 = Entry(m3, width = 3)
mod  = Label(m3, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_3 = Entry(m3, width = 3)
m3.add(num1_3)
m3.add(sign)
m3.add(num2_3)
m3.add(mod)
m3.add(num3_3)

m4 = PanedWindow(tab2)
m4.pack()

num1_4 = Entry(m4, width = 3)
sign = Label(m4, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_4 = Entry(m4, width = 3)
mod  = Label(m4, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_4 = Entry(m4, width = 3)
m4.add(num1_4)
m4.add(sign)
m4.add(num2_4)
m4.add(mod)
m4.add(num3_4)

m5 = PanedWindow(tab2)
m5.pack()

num1_5 = Entry(m5, width = 3)
sign = Label(m5, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_5 = Entry(m5, width = 3)
mod  = Label(m5, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_5 = Entry(m5, width = 3)
m5.add(num1_5)
m5.add(sign)
m5.add(num2_5)
m5.add(mod)
m5.add(num3_5)

m6 = PanedWindow(tab2)
m6.pack()

num1_6 = Entry(m6, width = 3)
sign = Label(m6, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_6 = Entry(m6, width = 3)
mod  = Label(m6, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_6 = Entry(m6, width = 3)
m6.add(num1_6)
m6.add(sign)
m6.add(num2_6)
m6.add(mod)
m6.add(num3_6)

m7 = PanedWindow(tab2)
m7.pack()

num1_7 = Entry(m7, width = 3)
sign = Label(m7, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_7 = Entry(m7, width = 3)
mod  = Label(m7, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_7 = Entry(m7, width = 3)
m7.add(num1_7)
m7.add(sign)
m7.add(num2_7)
m7.add(mod)
m7.add(num3_7)

m8 = PanedWindow(tab2)
m8.pack()

num1_8 = Entry(m8, width = 3)
sign = Label(m8, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_8 = Entry(m8, width = 3)
mod  = Label(m8, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_8 = Entry(m8, width = 3)
m8.add(num1_8)
m8.add(sign)
m8.add(num2_8)
m8.add(mod)
m8.add(num3_8)

m9 = PanedWindow(tab2)
m9.pack()

num1_9 = Entry(m9, width = 3)
sign = Label(m9, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_9 = Entry(m9, width = 3)
mod  = Label(m9, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_9 = Entry(m9, width = 3)
m9.add(num1_9)
m9.add(sign)
m9.add(num2_9)
m9.add(mod)
m9.add(num3_9)

m10 = PanedWindow(tab2)
m10.pack()

num1_10 = Entry(m10, width = 3)
sign = Label(m10, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_10 = Entry(m10, width = 3)
mod  = Label(m10, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_10 = Entry(m10, width = 3)
m10.add(num1_10)
m10.add(sign)
m10.add(num2_10)
m10.add(mod)
m10.add(num3_10)

m11 = PanedWindow(tab2)
m11.pack()

num1_11 = Entry(m11, width = 3)
sign = Label(m11, text="x  ≡ ", font = "Verdana 15",bg = '#ddede6')
num2_11 = Entry(m11, width = 3)
mod  = Label(m11, text="mod", font = "Verdana 15",bg = '#ddede6')
num3_11 = Entry(m11, width = 3)
m11.add(num1_11)
m11.add(sign)
m11.add(num2_11)
m11.add(mod)
m11.add(num3_11)


str1 = 'Rešenje je : '
res = Label(tab2, text = str1, font = "Verdana 15",bg = '#ddede6')
res.pack(pady = 25)

btnSubmit2 = Button(tab2, text ='Počni', width= 15, font = "Verdana 10", command = lambda:submitForm2(),borderwidth = '1',fg = 'white',bg = 'gray') 
btnSubmit2.pack(pady = 10)

names = Label(tab2, text= 'Elmaz Feratović 30/17 /\/\/\/\ Vladan Babić 24/17',fg = "Black",   font = "Verdana 10",bg = '#f2f2f2')
names.pack()

def updateLang2():

    lang = comboLang2.get()

    
    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':   

            titleLable2.configure(text = 'DOBRODOŠLI!')
            kriptoLable2.configure(text = 'KINESKA TEOREMA O OSTACIMA')
            comboLang2.configure(values=[
                                    "Engleski", 
                                    "Crnogorski",
                                    "Njemački"
                                    ])
            btnComboLagn2.configure(text = 'Promijeni')
            numbers.configure(text="Unesite brojeve : " )
            btnSubmit2.configure(text = 'Počni')
            res.configure(text = 'Rešenje je : ')

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':

            titleLable2.configure(text = 'WELCOME!')
            kriptoLable2.configure(text = 'CHINESE REMAINDER THEOREM')
            comboLang2.configure(values=[
                                    "English", 
                                    "Montengrian",
                                    "German"
                                    ])
            btnComboLagn2.configure(text = 'Change')
            numbers.configure(text="Enter numbers : " )
            btnSubmit2.configure(text = 'Start')
            res.configure(text = 'Solution is : ')

    else:
            titleLable2.configure(text = 'WILLKOMMEN!')
            kriptoLable2.configure(text = 'DER CHINESISCHER RESTSATZ')
            comboLang2.configure(values=[
                                    "Englisch", 
                                    "Montenegrinisch",
                                    "Deutsch"
                                    ])
            btnComboLagn2.configure(text = 'Verändern')
            numbers.configure(text="Geben Sie die Zahlen ein : ")
            btnSubmit2.configure(text = 'Starten')
            res.configure(text = 'Der Lösung ist :')

############################################################################################################################

def submitForm2():
    
    one(num1)
    one(num1_2)
    one(num1_3)
    one(num1_4)
    one(num1_5)
    one(num1_6)
    one(num1_7)
    one(num1_8)
    one(num1_9)
    one(num1_10)
    one(num1_11)


    
    numKoefArray =[]
    numArray = []
    modArray = [] 

    chekcInput(numArray,modArray,numKoefArray,num1.get(),num2.get(),num3.get())
    chekcInput(numArray,modArray,numKoefArray,num1_2.get(),num2_2.get(),num3_2.get())
    chekcInput(numArray,modArray,numKoefArray,num1_3.get(),num2_3.get(),num3_3.get())
    chekcInput(numArray,modArray,numKoefArray,num1_4.get(),num2_4.get(),num3_4.get())
    chekcInput(numArray,modArray,numKoefArray,num1_5.get(),num2_5.get(),num3_5.get())
    chekcInput(numArray,modArray,numKoefArray,num1_6.get(),num2_6.get(),num3_6.get())
    chekcInput(numArray,modArray,numKoefArray,num1_7.get(),num2_7.get(),num3_7.get())
    chekcInput(numArray,modArray,numKoefArray,num1_8.get(),num2_8.get(),num3_8.get())
    chekcInput(numArray,modArray,numKoefArray,num1_9.get(),num2_9.get(),num3_9.get())
    chekcInput(numArray,modArray,numKoefArray,num1_10.get(),num2_10.get(),num3_10.get())
    chekcInput(numArray,modArray,numKoefArray,num1_11.get(),num2_11.get(),num3_11.get())
    

    
    print(modArray)

    koeficijentX = 0

    while koeficijentX < len(modArray):

        if nzd(numKoefArray[koeficijentX],modArray[koeficijentX]) == 1:
            numArray[koeficijentX] = int(numArray[koeficijentX]) + int(modArray[koeficijentX])

        if nzd(numKoefArray[koeficijentX],modArray[koeficijentX]) % int(numArray[koeficijentX]) == 0:
            numArray[koeficijentX] = int(numArray[koeficijentX]) / int(numKoefArray[koeficijentX])
            numKoefArray[koeficijentX] = 1

        koeficijentX = koeficijentX + 1


    M = []
    elem = 0

    while elem < len(modArray):
        
        suma = 1
        j = 0 
        while j < len(modArray):
             
            if j != elem:
               suma = suma * int(modArray[j])

            j = j + 1

        M.append(str(suma))
        elem = elem + 1


    Y = []
    elem1 = 0

    while elem1 < len(modArray):
        Y.append(str(findY(int(M[elem1]),int(modArray[elem1]))))

        elem1 = elem1 + 1 

    i = 0
    modUlt = 1
    while i < len(modArray):
          modUlt = int(modArray[i]) * modUlt
          i = i + 1

   
    i = 0
    fin = 1
    finSuma = 0
    while i < len(modArray):
        fin = int(numArray[i]) * int(M[i]) * int(Y[i])
        finSuma = fin + finSuma
        i = i + 1
     
    print(M)
    print(Y)
    print(numArray)
    final = finSuma % modUlt
    
    print(finSuma)
    print(modUlt)
    lang = comboLang2.get()
    
    if lang == 'Crnogorski' or lang == 'Montenegrian' or  lang == 'Montenegrinisch':               
        res.configure(text = 'Rešenje je : ' + str(final))

    elif lang == 'Engleski' or lang == 'English' or lang == 'Englisch':
        res.configure(text = 'Solution is : ' + str(final))

    else:
       
        res.configure(text = 'Der Lösung ist : ' + str(final))

    iDup = 0
    
    while iDup < len(modArray) - 1:
        j = iDup + 1
       
        while j < len(modArray):
           
            if nzd(modArray[iDup],modArray[j]) != 1:
               
                if comboLang2.get() == 'Crnogorski' or comboLang2.get() == 'Montenegrian' or  comboLang2.get() == 'Montenegrinisch':               
                   res.configure(text = 'Ne postoji jedinstveno rešenje')

                elif comboLang2.get() == 'Engleski' or comboLang2.get() == 'English' or comboLang2.get() == 'Englisch':
                   res.configure(text = 'There is no unique solution ')

                else:
                   res.configure(text = 'Es gibt keine lösung ')

                break
            

                
            

            j = j + 1
        iDup = iDup + 1
    
  
    


#######################################################################################################################

def findY(n,m):

    a = n
    b = m

    mod = 2
    brojac = 0
    inter = 1


    while mod > 1:
    
        a1 = a * inter
        mod = a1 % b

        brojac = brojac + 1
        inter = inter + 1
    
        if inter > 100:
           break

    
    return brojac

#########################################################################################################

def nzd(a,b): 
    a = int(a)
    b = int(b)
    if(b==0): 
        return a 
    else: 
        return nzd(b,a%b) 
  
#########################################################################################################

def one(a):
   
    if a.get() == '':
       a.insert(0, "1")

##################################################################################################################

def chekcInput(numArray,modArray,numKoefArray,numX,number,mod):
    
    if mod != '':
     numKoefArray.append(numX)
     modArray.append(mod)
     numArray.append(number)

    
########################################################################################################################



tab_control.pack(expand=1, fill='both')

window.mainloop()