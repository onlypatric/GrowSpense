import os,sys
from tkinter import *;
from threading import Thread;
import ctypes as ct
from PyQt5.QtWidgets import QApplication;
QApplication(sys.argv)

class App:
    def __init__(self) -> None:
        self.main_background="#201f28"
        self.main2_background="#030508"
        self.activebackground="#242438"
        self.activeforeground="#fff"
        self.isStarted=False
        self.totalActivities=0
        self.currentAccount=None
        self.font="Helvetica 10 bold"
        self.thread=Thread(target=self.app);
    def dark_title_bar(self,window):
        """
        MORE INFO:
        https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        """
        try:
            window.update()
            if os.name=="nt":
                ct.windll.dwmapi.DwmSetWindowAttribute(
                    ct.windll.user32.GetParent(
                        window.winfo_id()
                    ), 
                    20, 
                    ct.byref(
                        ct.c_int(2)
                    ),
                    ct.sizeof(
                        ct.c_int(2)
                    )
                )
        except:pass
    def start(self):
        self.thread.start()
    def closeMain(self,*args,**kwargs):
        self.root.destroy()
        os.kill(os.getpid(),9)
    def close(self,*args,**kwargs):
        self.root.destroy()
        os.kill(os.getpid(),9)

    # Change focus on the respective button (see App.setup_menu)
    def changefocus(self,button:Button):
        self.homeButton.config(font="Helvetica 10 bold")
        self.configButton.config(font="Helvetica 10 bold")
        self.helpButton.config(font="Helvetica 10 bold")
        self.settingsButton.config(font="Helvetica 10 bold")
        self.moreButton.config(font="Helvetica 10 bold")
        button.config(font="Helvetica 10 bold underline")
        if button.cget("text")=="Home":
            self.home()
        elif button.cget("text")=="Settings":
            self.settings()
        elif button.cget("text")=="Config":
            self.configset()
        elif button.cget("text")=="Help":
            self.help()
        elif button.cget("text")=="More":
            self.more()
    def setup_menu(self):
        #Menu container
        self.mainMenu=Frame(self.root,bg=self.main_background,bd=1)
        self.mainMenu.pack(side=TOP,fill=X)

        #Home (first one to launch)
        self.homeButton=Button(self.mainMenu,text="Home",relief=SOLID,bg=self.main_background,fg="#fff",bd=0,activebackground="#242438",activeforeground="#fff",font="Helvetica 10 bold underline")
        self.homeButton.config(width=self.homeButton.winfo_width()+10,command=lambda:self.changefocus(self.homeButton))
        self.homeButton.pack(side=LEFT)

        #config (for setting up what activities to do)
        self.configButton=Button(self.mainMenu,text="Config",relief=SOLID,bg=self.main_background,fg="#fff",bd=0,activebackground="#242438",activeforeground="#fff",font="Helvetica 10 bold")
        self.configButton.config(width=self.configButton.winfo_width()+10,command=lambda:self.changefocus(self.configButton))
        self.configButton.pack(side=LEFT)

        #Help section (for knowing what to do)
        self.helpButton=Button(self.mainMenu,text="Help",relief=SOLID,bg=self.main_background,fg="#fff",bd=0,activebackground="#242438",activeforeground="#fff",font="Helvetica 10 bold")
        self.helpButton.config(width=self.helpButton.winfo_width()+10,command=lambda:self.changefocus(self.helpButton))
        self.helpButton.pack(side=LEFT)

        #Settings section (setup device and others)
        self.settingsButton=Button(self.mainMenu,text="Settings",relief=SOLID,bg=self.main_background,fg="#fff",bd=0,activebackground="#242438",activeforeground="#fff",font="Helvetica 10 bold")
        self.settingsButton.config(width=self.settingsButton.winfo_width()+10,command=lambda:self.changefocus(self.settingsButton))
        self.settingsButton.pack(side=LEFT)

        #other things like contact developer
        self.moreButton=Button(self.mainMenu,text="More",relief=SOLID,bg=self.main_background,fg="#fff",bd=0,activebackground="#242438",activeforeground="#fff",font="Helvetica 10 bold")
        self.moreButton.config(width=self.moreButton.winfo_width()+10,command=lambda:self.changefocus(self.moreButton))
        self.moreButton.pack(side=LEFT)

    def config(self):
        #config root
        self.root.config(background=self.main_background,bd=0,relief=SOLID,highlightthickness=0)
        self.root.geometry("1080x720");
        self.root.protocol("WM_DELETE_WINDOW",self.closeMain)
        self.root.bind("<Control-w>",self.closeMain)
        # Create transparent window
        try:self.root.attributes('-alpha',0.96)
        except:pass
        self.root.title("WinStall - Windows Package Manager")

        #setup menu
        self.setup_menu()

        #try title bar (win11 only)
        self.dark_title_bar(self.root)

        #mainFrame for containing all the things
        self.mainFrame = Frame(self.root,bg=self.main_background)
        self.mainFrame.pack(side=TOP,fill=BOTH,expand=True)

        #start from home
        self.home();
    def clear(self):
        for child in self.mainFrame.winfo_children():child.destroy();
    def settings(self):
        self.clear()
        self.cFrame=Frame(self.mainFrame,background=self.main_background)
        self.cFrame.pack(side=RIGHT,fill=BOTH,expand=1)

        Label(self.cFrame,text="Settings page").pack()
    def help(self):
        self.clear()
        self.cFrame=Frame(self.mainFrame,background=self.main_background)
        self.cFrame.pack(side=RIGHT,fill=BOTH,expand=1)

        Label(self.cFrame,text="help page").pack()
    def configset(self):
        self.clear()
        self.cFrame=Frame(self.mainFrame,background=self.main_background)
        self.cFrame.pack(side=RIGHT,fill=BOTH,expand=1)

        Label(self.cFrame,text="config page").pack()
    def more(self):
        self.clear()
        self.cFrame=Frame(self.mainFrame,background=self.main_background)
        self.cFrame.pack(side=RIGHT,fill=BOTH,expand=1)

        Label(self.cFrame,text="more page").pack()
    
    def home(self):
        self.clear()
        self.leftMenu=Frame(self.mainFrame,background=self.main_background,width=200)
        self.leftMenu.pack(side=LEFT,fill=Y)

        self.cFrame=Frame(self.mainFrame,background=self.main2_background)
        self.cFrame.pack(side=RIGHT,fill=BOTH,expand=1)

        self.dataFrame=Frame(self.cFrame,bg=self.main2_background)
        self.dataFrame.pack(side=TOP,fill=X)

        self.Searchlabel=Label(self.dataFrame,text=f"SEARCH",bg=self.main2_background,fg="#fff",font="Helvetica 12 bold",justify="left")
        self.Searchlabel.pack(side=LEFT,expand=True,anchor="e")
        self.SearchEntry=Entry(self.dataFrame,bg="#383838",font=self.font,width=30)
        self.SearchEntry.pack(side=LEFT,expand=True,anchor="w")
    def app(self):
        self.root=Tk();

        Thread(target=self.config).start();
        self.root.mainloop();

if __name__=="__main__":
    a = App()
    a.start()
