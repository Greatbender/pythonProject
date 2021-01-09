from tkinter import *

class UI:

    def TinkerUI():

        master = Tk()
        Label(master, text="Where do you want to go skiing?  \nLatitude").grid(row=0)
        Label(master, text="Longitude").grid(row=1)

        e1 = Entry(master)
        e2 = Entry(master)

        e1.insert(10,"47.11547")
        e2.insert(10,"13.13467")

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        Button(master, text='Continue', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)

        mainloop( )


        lat = e1.get()
        lon = e2.get()

        return(lat, lon)
