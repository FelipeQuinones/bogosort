import sys
import random
from os import path, system, getcwd
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
from PyQt5.QtCore import QTimer, pyqtSignal

def open_sequence(seq_path):
    sequence_path = path.join(getcwd(), seq_path)
    with open(sequence_path, "r") as lines:
        for line in lines:
            sequence = line.split(",")
    return sequence

def sort(sequence):
    tries = 0
    is_sorted = all(int(a) <= int(b) for a, b in zip(sequence, sequence[1:]))
    while not is_sorted:
        tries += 1
        system("clear")
        random.shuffle(sequence)
        is_sorted = all(int(a) <= int(b) for a, b in zip(sequence, sequence[1:]))
        terminal_gui(sequence)
        print(f"Try: {tries}")
    return tries

def terminal_gui(sequence):
    for number in sequence:
        print("□" * int(number))
   
class Bogosort(QWidget):
    update_gui_signal = pyqtSignal()

    def __init__(self, sequence, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sequence = sequence
        self.labels = []
        self.init_gui()
        self.update_timer = QTimer()
        self.update_timer.setInterval(10)
        self.update_timer.timeout.connect(self.update_gui)
        self.update_timer.start()
        

    def init_gui(self):
        self.setWindowTitle("Bogosort")
        self.setGeometry(10, 10, 1000, 500)
        for number in self.sequence:
            label = QLabel(self)
            label.setFixedSize(int(1000 / len(sequence)), 40 * int(number))
            label.setStyleSheet("background-color: purple;")
            self.labels.append([int(number), label])

        self.positions = [(0, y) for y in range(len(self.labels))]

        self.matrix = QGridLayout()
        self.sort_gui()
        self.matrix.setSpacing(0)
        self.setLayout(self.matrix)

        self.show()
        
    def update_gui(self):
        system("clear")
        random.shuffle(self.labels)
        is_sorted = all(int(a[0]) <= int(b[0]) for a, b in zip(self.labels, self.labels[1:]))
        self.sort_gui()
        if is_sorted == True:
            self.update_timer.stop()

    def sort_gui(self):
        for label, position in zip(self.labels, self.positions):
            self.matrix.addWidget(label[1], *position)    
    
if __name__ == "__main__":
    tries = 0

    seq_path = "sequence.txt"
    sequence = open_sequence(seq_path)
    """tries = sort(sequence)
        
    print(f"It took {tries} tries to find the solution")"""

    app = QApplication([])
    form = Bogosort(sequence)
    form.show()
    sys.exit(app.exec())
