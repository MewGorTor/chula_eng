import tkinter as tk
import random

# Thai consonants and their names
consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("\u0E02", "Kho Khai (ขอ ไข่)"),
    ("\u0E04", "Kho Khuat (คอ ควาด)"),
    ("\u0E07", "Ngo Ngu (งอ งู)")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="raised", borderwidth=2)
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()
        
        self.current_card = None
        self.is_flipped = False
        self.next_card()
    
    def flip_card(self):
        if not self.is_flipped:
            self.label.config(text=self.current_card[1], font=("Arial", 20))
            self.is_flipped = True
        else:
            self.label.config(text=self.current_card[0], font=("Arial", 50))
            self.is_flipped = False
    
    def next_card(self):
        self.current_card = random.choice(consonants)
        self.label.config(text=self.current_card[0], font=("Arial", 50))
        self.is_flipped = False

root = tk.Tk()
app = FlashcardGame(root)
root.mainloop()
