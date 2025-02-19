import tkinter as tk
import random
import time
import threading

class Selectionsort:
    def __init__(self, root):
        self.root = root
        
        self.start_timer = None
        self.timer_running = False

        self.canvas = tk.Canvas(root, width=700, height=400, bg='white')
        self.canvas.create_text(350, 200, text="SELECTIONSORT", font=("Helvetica", 24), fill="blue")
        self.canvas.pack(pady=20)

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(pady=20)

        self.scale_for_bars = tk.Scale(self.controls_frame, from_=10, to=100, orient=tk.HORIZONTAL, label="Anzahl der Balken")
        self.scale_for_bars.grid(row=0, column=0, padx=10)

        self.scale_update = tk.Scale(self.controls_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="Geschwindigkeit")
        self.scale_update.grid(row=0, column=1, padx=10)

        self.button_mix_bars = tk.Button(self.controls_frame, text='Mischen', command=self.mix)
        self.button_mix_bars.grid(row=1, column=0, padx=10, pady=10)

        self.button_worst_case = tk.Button(self.controls_frame, text='Worst Case', command=self.worst_case)
        self.button_worst_case.grid(row=0, column=2, padx=10, pady=10)

        self.button_sort_bars = tk.Button(self.controls_frame, text='Sortieren', command=self.start_sort)
        self.button_sort_bars.grid(row=1, column=1, padx=10, pady=10)

        self.button_stop_sort = tk.Button(self.controls_frame, text='Abbrechen', command=self.stop_sort, state=tk.DISABLED)
        self.button_stop_sort.grid(row=1, column=2, padx=10, pady=10)

        self.label_timer = tk.Label(root, text='Zeit: 0.00s')
        self.label_timer.pack(pady=20)

        self.bars = []
        self.rectangles = []

    def make_bars(self, a):
        self.canvas.delete('all')
        self.rectangles = []
        self.c_width = 700
        self.c_height = 400
        self.bars_width = self.c_width // len(a)
        self.max_value = max(a)

        for i, height in enumerate(a):
            x0 = i * self.bars_width
            y0 = self.c_height - (self.c_height * height) / self.max_value
            x1 = (i + 1) * self.bars_width
            y1 = self.c_height

            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
            self.rectangles.append(rect)

    def mix(self):
        x = self.scale_for_bars.get()
        self.bars = [random.randint(1, x) for _ in range(x)]
        self.make_bars(self.bars)

    def worst_case(self):
        x = self.scale_for_bars.get()
        self.bars = [x - _ for _ in range(x)]
        self.make_bars(self.bars)

    def update_timer(self):
        while self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.label_timer.config(text=f"Zeit: {elapsed_time:.4f}s")
            time.sleep(0.01)

    def start_sort(self):
        self.start_time = time.time()
        self.timer_running = True
        self.disable_buttons()
        timer_thread = threading.Thread(target=self.update_timer)
        timer_thread.start()
        self.selectionsort()
        self.timer_running = False
        self.enable_buttons()

    def stop_sort(self):
        self.timer_running = False
        self.label_timer.config(text="Sortierung abgebrochen")
        self.enable_buttons()

    def disable_buttons(self):
        self.scale_for_bars.config(state=tk.DISABLED)
        self.scale_update.config(state=tk.DISABLED)
        self.button_worst_case.config(state=tk.DISABLED)
        self.button_mix_bars.config(state=tk.DISABLED)
        self.button_sort_bars.config(state=tk.DISABLED)
        self.button_stop_sort.config(state=tk.NORMAL)

    def enable_buttons(self):
        self.scale_for_bars.config(state=tk.NORMAL)
        self.scale_update.config(state=tk.NORMAL)
        self.button_worst_case.config(state=tk.NORMAL)
        self.button_mix_bars.config(state=tk.NORMAL)
        self.button_sort_bars.config(state=tk.NORMAL)
        self.button_stop_sort.config(state=tk.DISABLED)

    def selectionsort(self):
        t = self.scale_update.get()
        n = len(self.bars)
        for i in range(n):
            big_idx = 0
            for j in range(n - i):
                if self.bars[j] > self.bars[big_idx]:
                    big_idx = j
                self.highlight_bars(j, big_idx)
                self.canvas.update()
                self.canvas.after(t)

            self.bars[big_idx], self.bars[n - i - 1] = self.bars[n - i - 1], self.bars[big_idx]
            self.update_canvas()
            self.canvas.update()
            self.canvas.after(t)

    def update_canvas(self):
        self.canvas.delete('all')
        self.rectangles = []
        for i, height in enumerate(self.bars):
            x0 = i * self.bars_width
            y0 = self.c_height - (self.c_height * height) / self.max_value
            x1 = (i + 1) * self.bars_width
            y1 = self.c_height

            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
            self.rectangles.append(rect)

    def highlight_bars(self, idx1, idx2):
        for i, rect in enumerate(self.rectangles):
            if i == idx1:
                self.canvas.itemconfig(rect, fill='red')
            elif i == idx2:
                self.canvas.itemconfig(rect, fill='green')
            else:
                self.canvas.itemconfig(rect, fill='blue')
        self.canvas.update_idletasks()
