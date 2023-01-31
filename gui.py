import tkinter
from tkinter import *
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

########################creating window####################
root = tkinter.Tk()
root.wm_title("Embedding in Tk")
#rootWindow.configure(bg="blue")

######################### heading###########################
Label(root, text = 'GUI FOR BIOMEDICAL CLASSIFICATION',bg='pink',fg='red', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 3)
photo = PhotoImage(file='uet_logo.PNG')
Button(root, text = 'UNIVERSITY OF ENGINEERING AND TECHNOLOGY ,TAXILA',font=('Verdana',15), image = photo, 
                    compound = LEFT).pack(side = TOP,pady=5)

#######################loading data#########################
global df
def load():

    name = askopenfilename(filetypes=[('CSV', '.csv',), ('Excel', ('.xls', '*.xlsx'))])

    if name:
        if name.endswith('.csv'):
            df = pd.read_csv(name)
        else:
            df = pd.read_excel(name)

            filename = name
Button(root, text = 'LOAD YOUR DATA TO DISPLAY',font=('Verdana',15), 
                    compound = LEFT,command=load).pack(side = TOP,pady=5)

#print(df)
##########################plotting graph################################

fig = Figure(figsize=(4, 4), dpi=100)
t = np.arange(0, 3, .01)
#    t=df.iloc[:,0]
y=2 * np.sin(100 * np.pi * t);
#    y=df.iloc[0,:]

fig.add_subplot(221).plot(t, y)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)
#
#
canvas.mpl_connect("key_press_event", on_key_press)




status=98;

####################training###############################################
def train(self):
        if self.df is None:
            self.load()
                  # display if loaded
                 
        if self.df is not None:
            model=svm.SVC(cache_size=5000,  decision_function_shape='ovo', degree=3, gamma='auto', kernel='linear');
            model.fit(trgFeat,trgLabel);
            svm_results=model.predict(testFeat);
            print("svm_result")
w = Label(root, text="TRAIN YOUR DATA", bg="white", fg="black").place(x=430,y=630)
button = tkinter.Button(master=root, text="TRAIN",command=train).place(x=550,y=630)
#####################results##################################################
w = Label(root, text="ACCURACY IS:", bg="white", fg="black").place(x=430,y=660)
button = tkinter.Button(master=root, text=status).place(x=550,y=660)
###########################quitting#########################################
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

w = Label(root, text="CLICK TO EXIT", bg="white", fg="black").place(x=430,y=690)
button = tkinter.Button(master=root, text="Quit", command=_quit).place(x=550,y=700)


tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager