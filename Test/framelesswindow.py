from tkinter import *

class TkWin(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "root", useTk: bool = True, sync: bool = True, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        def get_pos(event:Event):
            self.xwin = self.winfo_x()
            self.ywin = self.winfo_y()
            startx = event.x_root
            starty = event.y_root

            self.ywin = self.ywin - starty
            self.xwin = self.xwin - startx
            self.width=self.winfo_width()
            self.height=self.winfo_height()

            startx = event.x_root
            starty = event.y_root


        def move_window(event):
            self.geometry("{0}x{1}".format(self.width,self.height) + '+{0}+{1}'.format(event.x_root + self.xwin, event.y_root + self.ywin))
        title_bar = Frame(self, bg='white', relief='raised', bd=2)
        title_bar.bind('<B1-Motion>', move_window)

        title_bar.bind('<Button-1>', get_pos)
        self.overrideredirect(True) # turns off title bar, geometry
        self.geometry('400x100+200+200') # set new geometry

        # put a close button on the title bar
        close_button = Button(title_bar, text='X', command=self.destroy)

        # a canvas for the main area of the window
        window = Canvas(self, bg='black')

        # pack the widgets
        title_bar.pack(expand=1, fill=X)
        close_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)

if __name__=="__main__":
    root=TkWin()
    root.mainloop()