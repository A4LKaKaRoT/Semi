#Tyrone Reimers, Finlay Plöger; 09.01.2025

import tkinter as tk
import Main_Menu as m


def main():
    root = tk.Tk()
    root.title("Sortierverfahren")
    menu = m.MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()

