import tkinter as tk
from Selectionsort import Selectionsort
from Insertionsort import Insertionsort
from Bubblesort import Bubblesort

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1080x720')

        self.title_label = tk.Label(self.root, text='Sortierverfahren', font=('Helvetica', 40))
        self.title_label.pack(padx=30, pady=30)

        button_frame1 = tk.Frame(self.root)
        button_frame1.pack(pady=40)

        self.selection_button = tk.Button(button_frame1, text='Selectionsort', font=('Helvetica', 24), command = self.open_selectionsort)
        self.selection_button.pack(side=tk.LEFT, padx=10)

        self.insertion_button = tk.Button(button_frame1, text='Insertionsort', font=('Helvetica', 24),  command = self.open_insertionsort)
        self.insertion_button.pack(side=tk.LEFT, padx=10)

        self.quick_button = tk.Button(button_frame1, text='Quicksort', font=('Helvetica', 24))
        self.quick_button.pack(side=tk.LEFT, padx=10)

        button_frame2 = tk.Frame(self.root)
        button_frame2.pack(pady=40)

        self.merge_button = tk.Button(button_frame2, text='Mergesort', font=('Helvetica', 24))
        self.merge_button.pack(side=tk.LEFT, padx=10)

        self.bubble_button = tk.Button(button_frame2, text='Bubblesort', font=('Helvetica', 24), command = self.open_bubblesort)
        self.bubble_button.pack(side=tk.LEFT, padx=10)

        self.other_button = tk.Button(button_frame2, text=' Maybe Anderer Sort', font=('Helvetica', 24))
        self.other_button.pack(side=tk.LEFT, padx=10)
    
    def open_selectionsort(self):
        open = tk.Toplevel(self.root)
        Selectionsort(open)

    def open_insertionsort(self):
        open = tk.Toplevel(self.root)
        Insertionsort(open)
    
    def open_bubblesort(self):
        open = tk.Toplevel(self.root)
        Bubblesort(open)
        print('BUBFENSTER')