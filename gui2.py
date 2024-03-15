import tkinter as tk
from tkinter import messagebox

def calculate_distance():
    word1 = entry1.get()
    word2 = entry2.get()
    
    if not word1 or not word2:
        messagebox.showerror("Error", "Please enter both words.")
        return
    
    distance = LevenshteinDistance(word1, word2)
    messagebox.showinfo("Distance", f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}.")

def LevenshteinDistance(word1, word2):
    """Dynamic programming solution"""
    m = len(word1)
    n = len(word2)
    
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = min(
                    table[i - 1][j] + 1,
                    table[i][j - 1] + 1,
                    table[i - 1][j - 1]
                )
            else:
                table[i][j] = min(
                    table[i - 1][j] + 1,
                    table[i][j - 1] + 1,
                    table[i - 1][j - 1] + 1
                )
    return table[-1][-1]

# Create the main window
root = tk.Tk()
root.title("Levenshtein Distance Calculator")
root.configure(bg='#333333')  # Dark background for the window

# Create labels and entry widgets with styling
label1 = tk.Label(root, text="Word 1:", bg='#333333', fg='white', padx=10, pady=10)
label1.grid(row=0, column=0, sticky="W")
entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Word 2:", bg='#333333', fg='white', padx=10, pady=10)
label2.grid(row=1, column=0, sticky="W")
entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create calculate button with styling
calculate_button = tk.Button(root, text="Calculate Distance", command=calculate_distance, bg='#007ACC', fg='white', padx=5, pady=5)
calculate_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

# Run the application
root.mainloop()
