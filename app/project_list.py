import tkinter
import tkinter.ttk


class ProjectWindow:
    def __init__(self, strings):
        self.strings = strings
        self.ACTIONS_COLOR = "#111111"
        self.ACTIONS_COLOR_FG = "#fefefe"

        self.window = tkinter.Tk()
        self.project_list = tkinter.Frame(self.window, bg="#050505")
        self.actions = tkinter.Frame(self.window, bg=self.ACTIONS_COLOR)

        self.calc_window_geometry()
        self.add_frames()
        self.make_action_frame()


    def calc_window_geometry(self):
        sc_h = self.window.winfo_screenheight()
        sc_w = self.window.winfo_screenwidth()

        self.h = round(sc_h/2.5)
        self.w = round(sc_w/2.5)
        
        self.x = round(sc_w/2 - self.w/2)
        self.y = round(sc_h/2 - self.h/2)

        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.minsize(self.w,self.h)
        self.window.maxsize(self.w,self.h)

    def add_frames(self):
        self.project_list.place(width=round(self.w/2), height=round(self.h),
                                x=0, y=0)
        self.actions.place(width=round(self.w/2), height=round(self.h),
                                x=round(self.w/2), y=0)
    
    def make_action_frame(self):
        tkinter.ttk.Label(self.actions, text=self.strings.APP_NAME, background=self.ACTIONS_COLOR, foreground=self.ACTIONS_COLOR_FG).pack()

    def start(self):
        self.window.mainloop()
    