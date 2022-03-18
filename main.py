import tkinter as tk
import atexit
class Blocksite(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title('Website Blocker')
        self.hosts_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts"
        self.hosts_temp = "hosts"
        self.redirect = "127.0.0.1"
        self.blocksiteFile = open('blocksiteFile.txt', 'r+')
        self.web_sites_list = [line.replace('\n', '') for line in self.blocksiteFile]
        self.is_on = False #Toggle is on/off
        self.imgDelete = tk.PhotoImage(file = "img/delete.png")
    def Label(self):
        self.header = tk.Label (self, text="Website Blocker", font="Arial 30")
        self.header.pack(pady=(70, 40))
    def Entry(self):
        self.url = tk.Entry(self, font=('Arial 20'), width=35)
        self.url.insert(0, "Enter URL here...")
        self.url.bind("<FocusIn>", self.some_callback)
        self.url.pack(pady=20)
    def some_callback(self, event):
        self.url.delete(0, "end")
        return None
    def Button(self):
        self.blocked = tk.PhotoImage(file = "img/blocked.png")
        self.blockButton = tk.Button(self, image = self.blocked, command = self.openNewWindow)
        self.blockButton.pack()
        self.on = tk.PhotoImage(file = "img/on.png")
        self.off = tk.PhotoImage(file = "img/off.png")
        self.button = tk.Button(self, text='Block!', font='Arial 15', width=30, command=self.onAddBlock)
        self.button.pack(pady=5)
        self.toggle = tk.Button(self, image = self.off, bd = 0, command = self.switch)
        self.toggle.pack(pady = 50)
    def onAddBlock(self): #Block button is clicked
        newSite = self.url.get()
        blocksiteFile_add = open('blocksiteFile.txt', 'a')
        blocksiteFile_add.write(newSite + '\n')
        blocksiteFile_add.close()

        self.blocksiteFile = open('blocksiteFile.txt', 'r+')
        self.web_sites_list = [line.replace('\n', '') for line in self.blocksiteFile]
        if self.is_on:
            with open(self.hosts_path, 'r+') as file:
                content = file.read()
                for website in self.web_sites_list:
                    if website in content:
                        pass
                    else:
                        file.write(self.redirect + ' ' + website + '\n')
            print(self.web_sites_list)
    def switch(self): #Toggle is switched
        if self.is_on:
            self.toggle.config(image = self.off)
            self.is_on = False
            self.onOffToggle()
        else:
            self.toggle.config(image = self.on)
            self.is_on = True
            self.onOnToggle()
    def onOffToggle(self):
        with open(self.hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in self.web_sites_list):
                    file.write(line)
            file.truncate()
        print("Blocksite App is off")
    def onOnToggle(self):
        print("Blocksite App is on")
        with open(self.hosts_path, 'r+') as file:
                content = file.read()
                for website in self.web_sites_list:
                    if website in content:
                        pass
                    else:
                        file.write(self.redirect + ' ' + website + '\n')
        print(self.web_sites_list)

    def onDelete(self, window, name):
        print(f'You deleted {name} from your blocked list')
        self.web_sites_list.remove(name)
        with open("blocksiteFile.txt", "r+") as f:
            readLines = f.readlines()
            f.seek(0)
            for website in readLines:
                if website != name + '\n':
                    f.write(website)
            f.truncate()
        window.destroy()
        self.openNewWindow()

    def openNewWindow(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Blocked websites")
        newWindow.geometry("500x400")
        siteIndex = 0
        for wt in self.web_sites_list:
            web = tk.Label(newWindow, text = wt, font = ("Arial 20", 10))
            web.grid(row = siteIndex, column = 0, sticky = tk.W, pady = 3, padx = 20)
            remove = tk.Button(newWindow, image = self.imgDelete, command=lambda wName = wt: self.onDelete(newWindow, wName))
            remove.grid(row = siteIndex, column = 1, sticky = tk.E)
            siteIndex += 1

if __name__ == "__main__":
    Main = Blocksite()
    Main.Label()
    Main.Entry()
    Main.Button()
    Main.onOffToggle()
    Main.mainloop()
    atexit.register(Main.onOffToggle)

    