import tkinter as tk

def roma_to_arabic(roma_numarasi):
    roma_numarasi_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    toplam = 0

    for i in range(len(roma_numarasi)):
        if i > 0 and roma_numarasi_dict[roma_numarasi[i]] > roma_numarasi_dict[roma_numarasi[i - 1]]:
            toplam += roma_numarasi_dict[roma_numarasi[i]] - 2 * roma_numarasi_dict[roma_numarasi[i - 1]]
        else:
            toplam += roma_numarasi_dict[roma_numarasi[i]]

    return toplam

def convert_roman_to_arabic():
    girilen_roma = roman_number_entry.get().upper()

    try:
        normal_rakam = roma_to_arabic(girilen_roma)
        answer.config(text=f"{girilen_roma} = {normal_rakam}")
    except KeyError:
        answer.config(text="Invalid Number.")

# GUI
window = tk.Tk()
window.title("Number Converter")
window.minsize(height=400, width=500)

# Roman number entry and title
roman_number_title = tk.Label(text="Enter Roman Number", font=("Arial", 20, "bold"))
roman_number_title.pack(pady=5)

roman_number_entry = tk.Entry()
roman_number_entry.config(width=50, border=10)
roman_number_entry.focus()
roman_number_entry.pack(pady=10)

# Convert Button
button = tk.Button(text="Convert", command=convert_roman_to_arabic)
button.config(width=20, height=2)
button.pack(pady=5)

# Answer Label
answer = tk.Label(text="", font=("Arial", 15, "bold"))
answer.pack(pady=15)

window.mainloop()
