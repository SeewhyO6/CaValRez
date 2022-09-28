#!/usr/bin/python3
"""
*** Resistor Calculator v1.0 *** @seewhy

Programme servant à calculer la valeur d'une résistance électronique par rapport
à la couleur et au nombre de ses anneaux.
"""
import sys
import tkinter as tk
from tkinter import ttk
from platform import system
import pyglet


class App(tk.Tk):
    def __init__(self):
        super().__init__(className="Calculateur de resistance")

        # Style
        self.app_style = ttk.Style()
        self.app_style.theme_create('appstyle', parent='alt',
                                    settings={'TCombobox': {'configure': {'selectbackground': "white",
                                                                          'fieldbackground': "white",
                                                                          'background': "white",
                                                                          'selectforeground': "black"}}
                                              })
        self.app_style.theme_use('appstyle')

        # Données utiles
        self.result = ""
        self.choices = ["Noir", "Marron", "Rouge", "Orange", "Jaune", "Vert", "Bleu", "Violet", "Gris", "Blanc"]
        self.mult = ["Noir", "Marron", "Rouge", "Orange", "Jaune", "Vert", "Bleu", "Violet", "Gris", "Blanc", "Or",
                     "Argent"]
        self.choices_dict = {"Noir": 0, "Marron": 1, "Rouge": 2, "Orange": 3, "Jaune": 4,
                             "Vert": 5, "Bleu": 6, "Violet": 7, "Gris": 8, "Blanc": 9}
        self.mult_dict = {"Noir": 10e-1, "Marron": 10e0, "Rouge": 10e1, "Orange": 10e2, "Jaune": 10e3, "Vert": 10e4,
                          "Bleu": 10e5, "Violet": 10e6, "Gris": 10e7, "Blanc": 10e8, "Or": 10e-2, "Argent": 10e-3}
        self.color_dict = {"Noir": "#000000", "Marron": "#470000", "Rouge": "#ff0000", "Orange": "#ffa500",
                           "Jaune": "#ffff00", "Vert": "#008000", "Bleu": "#0000ff", "Violet": "#800080",
                           "Gris": "#808080", "Blanc": "#ffffff", "Or": "#ffd700", "Argent": "#c0c0c0"}
        self.tolerance_list = ["Marron", "Rouge", "Vert", "Bleu", "Violet", "Gris", "Or", "Argent"]
        self.tolerance_dict = {"Marron": 1, "Rouge": 2, "Vert": 0.5, "Bleu": 0.25, "Violet": 0.1, "Gris": 0.05,
                               "Or": 5, "Argent": 10}

        # Couleur et police
        pyglet.font.add_file("./font/Lato-Regular.ttf")
        self.frame_color = "#50bab8"
        self.font = ("Lato", 14)
        self.option_add('*TCombobox*Listbox.font', self.font)
        self.option_add('*TCombobox*Listbox.justify', "center")
        self.option_add('*TCombobox*Scrollbar.width', 40)
        self.app_style.configure('TCombobox', arrowsize=20)

        # Options de root
        self.title("Resistor Calculator")
        self.resizable(False, False)
        self.config(bg=self.frame_color)
        self.wm_protocol("WM_DELETE_WINDOW", self.on_close)
        if system() == "Linux":
            self.img = tk.PhotoImage(file="./images/logo.png")
            self.iconphoto(True, self.img)

        # Layers et séparateur
        self.input_frame = tk.Frame(self, bg=self.frame_color)
        self.separator = ttk.Separator(self, orient='horizontal')
        self.output_frame = tk.Frame(self, bg=self.frame_color)

        self.input_frame.pack()
        self.separator.pack(fill="x")
        self.output_frame.pack()

        # Input frame ##########################################################
        # Boutons radios et labels boutons radios
        self.choice_an = tk.IntVar()

        self.an4 = tk.Radiobutton(self.input_frame, variable=self.choice_an, value=1, bg=self.frame_color)
        self.an5 = tk.Radiobutton(self.input_frame, variable=self.choice_an, value=2, bg=self.frame_color)
        self.label_radio = tk.Label(self.input_frame, text="Anneaux :", bg=self.frame_color, fg="black")

        self.an4.config(command=self.on_radio_change, borderwidth=3, relief="groove")
        self.an5.config(command=self.on_radio_change, borderwidth=3, relief="sunken")
        self.label_radio.config(font=self.font, justify="center", anchor="center")

        self.an4.grid(row=1, column=0, padx=10, pady=10)
        self.an5.grid(row=2, column=0, padx=10, pady=10)
        self.label_radio.grid(row=0, column=0, columnspan=2, padx=10)

        self.an5.select()

        self.an4_label = tk.Label(self.input_frame, text="4", font=self.font)
        self.an5_label = tk.Label(self.input_frame, text="5", font=self.font)

        self.an4_label.config(justify="center", bg=self.frame_color, fg="black")
        self.an5_label.config(justify="center", bg=self.frame_color, fg="black")

        self.an4_label.bind("<Button-1>", self.on_click1)
        self.an5_label.bind("<Button-1>", self.on_click2)

        self.an4_label.grid(row=1, column=1, padx=(0, 60), pady=10)
        self.an5_label.grid(row=2, column=1, padx=(0, 60), pady=10)

        # Labels hauts Combobox
        self.label_haut_1 = tk.Label(self.input_frame, font=self.font)
        self.label_haut_2 = tk.Label(self.input_frame, font=self.font)
        self.label_haut_3 = tk.Label(self.input_frame, font=self.font)
        self.label_haut_mult = tk.Label(self.input_frame, font=self.font)
        self.label_haut_tol = tk.Label(self.input_frame, font=self.font)

        self.label_haut_1.config(text="Couleur 1", justify="center", bg=self.frame_color, fg="black")
        self.label_haut_2.config(text="Couleur 2", justify="center", bg=self.frame_color, fg="black")
        self.label_haut_3.config(text="Couleur 3", justify="center", bg=self.frame_color, fg="black")
        self.label_haut_mult.config(text="Multiplicateur", justify="center", bg=self.frame_color, fg="black")
        self.label_haut_tol.config(text="Tolérance", justify="center", bg=self.frame_color, fg="black")

        self.label_haut_1.grid(row=0, column=2, padx=10, pady=(10, 0))
        self.label_haut_2.grid(row=0, column=3, padx=10, pady=(10, 0))
        self.label_haut_3.grid(row=0, column=4, padx=10, pady=(10, 0))
        self.label_haut_mult.grid(row=0, column=6, padx=10, pady=(10, 0))
        self.label_haut_tol.grid(row=0, column=7, padx=10, pady=(10, 0))

        # Combobox
        self.choice1 = ttk.Combobox(self.input_frame, values=self.choices)
        self.choice2 = ttk.Combobox(self.input_frame, values=self.choices)
        self.choice3 = ttk.Combobox(self.input_frame, values=self.choices)
        self.choice_mult = ttk.Combobox(self.input_frame, values=self.mult, height=15)
        self.choice_tol = ttk.Combobox(self.input_frame, values=self.tolerance_list, height=15)

        self.choice1.config(state="readonly", justify="center", width=8, font=self.font)
        self.choice2.config(state="readonly", justify="center", width=8, font=self.font)
        self.choice3.config(state="readonly", justify="center", width=8, font=self.font)
        self.choice_mult.config(state="readonly", justify="center", width=8, font=self.font)
        self.choice_tol.config(state="readonly", justify="center", width=8, font=self.font)

        self.choice1.bind("<<ComboboxSelected>>", self.on_choice1)
        self.choice2.bind("<<ComboboxSelected>>", self.on_choice2)
        self.choice3.bind("<<ComboboxSelected>>", self.on_choice3)
        self.choice_mult.bind("<<ComboboxSelected>>", self.on_choice_mult)
        self.choice_tol.bind("<<ComboboxSelected>>", self.on_choice_tol)

        self.choice1.set("Marron")
        self.choice2.set("Marron")
        self.choice3.set("Marron")
        self.choice_mult.set("Noir")
        self.choice_tol.set("Marron")

        self.choice1.grid(row=1, column=2, padx=10, pady=(10, 0))
        self.choice2.grid(row=1, column=3, padx=10, pady=(10, 0))
        self.choice3.grid(row=1, column=4, padx=10, pady=(10, 0))
        self.choice_mult.grid(row=1, column=6, padx=10, pady=(10, 0))
        self.choice_tol.grid(row=1, column=7, padx=10, pady=(10, 0))

        # Labels bas Combobox
        self.label_bas_1 = tk.Label(self.input_frame)
        self.label_bas_2 = tk.Label(self.input_frame)
        self.label_bas_3 = tk.Label(self.input_frame)
        self.label_bas_4 = tk.Label(self.input_frame)
        self.label_bas_mult = tk.Label(self.input_frame)
        self.label_bas_tol = tk.Label(self.input_frame)

        self.label_bas_1.config(text="1", justify="center", bg=self.frame_color, fg="black", font=self.font)
        self.label_bas_2.config(text="1", justify="center", bg=self.frame_color, fg="black", font=self.font)
        self.label_bas_3.config(text="1", justify="center", bg=self.frame_color, fg="black", font=self.font)
        self.label_bas_4.config(text="X", justify="center", bg=self.frame_color, fg="black", font=self.font)
        self.label_bas_mult.config(text="1", justify="center", bg=self.frame_color, fg="black", font=self.font)
        self.label_bas_tol.config(text="1", justify="center", bg=self.frame_color, fg="black", font=self.font)

        self.label_bas_1.grid(row=2, column=2, padx=10, pady=10)
        self.label_bas_2.grid(row=2, column=3, padx=10, pady=10)
        self.label_bas_3.grid(row=2, column=4, padx=10, pady=10)
        self.label_bas_4.grid(row=2, column=5, padx=10, pady=10)
        self.label_bas_mult.grid(row=2, column=6, padx=10, pady=10)
        self.label_bas_tol.grid(row=2, column=7, padx=10, pady=10)

        # Output frame ##########################################################
        self.label_resultat = tk.Label(self.output_frame)
        self.contener_couleur = tk.Frame(self.output_frame, bg="#c6aa83")
        self.label_couleur1 = tk.Label(self.contener_couleur, width=1, height=2, bg="#470000")
        self.label_couleur2 = tk.Label(self.contener_couleur, width=1, height=2, bg="#470000")
        self.label_couleur3 = tk.Label(self.contener_couleur, width=1, height=2, bg="#470000")
        self.label_couleur_mult = tk.Label(self.contener_couleur, width=1, height=2, bg="black")
        self.label_couleur_tol = tk.Label(self.contener_couleur, width=1, height=2, bg="#470000")

        self.label_resultat.config(bg=self.frame_color, text="111 Ω - 1 %", font=("Lato", 20), fg="black")

        self.label_couleur1.grid(row=0, column=0, padx=10)
        self.label_couleur2.grid(row=0, column=1, padx=10)
        self.label_couleur3.grid(row=0, column=2, padx=10)
        self.label_couleur_mult.grid(row=0, column=3, padx=10)
        self.label_couleur_tol.grid(row=0, column=4, padx=10)

        self.contener_couleur.grid(row=0, column=0)
        self.label_resultat.grid(row=0, column=1, padx=(100, 0), pady=20)

    def on_click1(self, *args):
        """
        Methodes callback du click sur le label
        du bouton radio 4
        """
        self.an4.select()
        self.on_radio_change()
        return args

    def on_click2(self, *args):
        """
        Methodes callback du click sur le label
        du bouton radio 5
        """
        self.an5.select()
        self.on_radio_change()
        return args

    def on_radio_change(self, *args):
        """
        Methode callback sur le changement des bouttons
        radios, suppression ou ajout de la dernière couleur
        """

        if self.choice_an.get() == 1:

            self.title("Resistor Calculator")

            self.an4.config(relief="sunken")
            self.an5.config(relief="groove")

            self.label_haut_3.grid_forget()
            self.label_bas_3.grid_forget()
            self.choice3.grid_forget()
            self.label_couleur3.grid_forget()

        elif self.choice_an.get() == 2:

            self.title("Resistor Calculator")

            self.an5.config(relief="sunken")
            self.an4.config(relief="groove")

            self.label_haut_3.grid(row=0, column=4, padx=10, pady=(10, 0))
            self.label_bas_3.grid(row=2, column=4, padx=10, pady=10)
            self.choice3.grid(row=1, column=4, padx=10, pady=(10, 0))
            self.label_couleur3.grid(row=0, column=2, padx=5)

        self.display_result()
        return args

    def on_choice1(self, *args):
        """
        Methode callback de la combobox 1 pour actualiser
        la couleur et le label
        """
        self.label_bas_1.config(text=str(self.choices_dict[self.choice1.get()]))
        self.label_couleur1.config(bg=self.color_dict[self.choice1.get()])
        self.display_result()
        return args

    def on_choice2(self, *args):
        """
        Methode callback de la combobox 2 pour actualiser
        la couleur et le label
        """
        self.label_bas_2.config(text=str(self.choices_dict[self.choice2.get()]))
        self.label_couleur2.config(bg=self.color_dict[self.choice2.get()])
        self.display_result()
        return args

    def on_choice3(self, *args):
        """
        Methode callback de la combobox 3 pour actualiser
        la couleur et le label
        """
        self.label_bas_3.config(text=str(self.choices_dict[self.choice3.get()]))
        self.label_couleur3.config(bg=self.color_dict[self.choice3.get()])
        self.display_result()
        return args

    def on_choice_mult(self, *args):
        """
        Methode callback de la combobox multiplicatuer pour actualiser
        la couleur et le label
        """
        if self.mult_dict[self.choice_mult.get()] < 1:
            self.label_bas_mult.config(text=str(self.mult_dict[self.choice_mult.get()]))
        else:
            self.label_bas_mult.config(text=str(int(self.mult_dict[self.choice_mult.get()])))
        self.display_result()
        self.label_couleur_mult.config(bg=self.color_dict[self.choice_mult.get()])
        return args

    def on_choice_tol(self, *args):
        """
        Methode callback de la combobox tolerance pour actualiser
        la couleur et le label
        """
        self.label_bas_tol.config(text=str(self.tolerance_dict[self.choice_tol.get()]))
        self.label_couleur_tol.config(bg=self.color_dict[self.choice_tol.get()])
        self.display_result()
        return args

    def display_result(self):
        """
        Méthode appelée pour afficher les résultats en
        fonction des options choisies
        """
        if self.choice_an.get() == 1:
            self.result = float(str(self.choices_dict[self.choice1.get()]) +
                                str(self.choices_dict[self.choice2.get()])) * self.mult_dict[self.choice_mult.get()]
        elif self.choice_an.get() == 2:
            self.result = float(str(self.choices_dict[self.choice1.get()]) + str(self.choices_dict[self.choice2.get()])
                                + str(self.choices_dict[self.choice3.get()])) * self.mult_dict[self.choice_mult.get()]

        if 0 < self.result <= 999:
            self.label_resultat.config(text=str(round(self.result, 3)) + " Ω - " +
                                       str(self.tolerance_dict[self.choice_tol.get()]) + " %")

        elif 10e2 <= self.result <= 10e5 - 1:
            self.result = self.result / 10e2
            self.label_resultat.config(text=str(round(self.result, 3)) + " kΩ - " +
                                       str(self.tolerance_dict[self.choice_tol.get()]) + " %")

        elif 10e5 <= self.result <= 10e8 - 1:
            self.result = self.result / 10e5
            self.label_resultat.config(text=str(round(self.result, 3)) + " MΩ - " +
                                       str(self.tolerance_dict[self.choice_tol.get()]) + " %")

        else:
            self.result = self.result / 10e8
            self.label_resultat.config(text=str(round(self.result, 3)) + " GΩ - " +
                                       str(self.tolerance_dict[self.choice_tol.get()]) + " %")

    def on_close(self):
        self.destroy()
        sys.exit(0)


if __name__ == "__main__":
    Calculator = App()
    Calculator.mainloop()
