from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=10, pady=10)


def click_button():
    try:
        boy = float(entry_boy.get())
        kg = float(entry_kg.get())
        sonuc = kg / (boy / 100) ** 2

        if sonuc <= 18.4:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - Zayıfsınız.")
        elif 18.5 < sonuc <= 24.9:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - normal kilodasınız.")
        elif 25 < sonuc <= 29.9:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - fazla kilolusunuz.")
        elif 30 < sonuc <= 34.9:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - 1. derece obezsiniz.")
        elif 35 < sonuc <= 39.9:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - 2. derece obezsiniz.")
        else:
            label_sonuc.config(text=f"Sonucunuz: {sonuc:.3f} - ileri derecede obezsiniz.")
    except ValueError:
        label_sonuc.config(text="Hatalı giriş!")


#kg lable
lable_kg = Label(text="kilonuzu giriniz (kg)")
lable_kg.pack()

#entry-1
entry_kg = Entry(width=20)
entry_kg.pack()

#boy lable
lable_boy = Label(text="boyunuzu giriniz (cm)")
lable_boy.pack()

#entry-2
entry_boy = Entry(width=20)
entry_boy.pack()

#button
my_button = Button(text="hesapla", command=click_button)
my_button.pack()

label_sonuc = Label(window, text="Sonuç: ")
label_sonuc.pack()

window.mainloop()