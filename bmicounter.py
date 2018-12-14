# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("BMI calculator")
        self.__teksti1 = Label(self.__mainwindow, text="Insert weight(in kg):")
        self.__teksti2 = Label(self.__mainwindow, text="Insert height(in cm):")
        self.__teksti1.grid(column=0, row=0)
        self.__teksti2.grid(column=0, row=2)

        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        self.__inputw = Entry(self.__mainwindow, width=10)
        self.__inputh = Entry(self.__mainwindow, width=10)
        self.__inputw.grid(column=0, row=1)
        self.__inputh.grid(column=0, row=3)

        self.__weight_value = self.__inputw
        self.__height_value = self.__inputh



        self.__calculate_button = Button(self.__mainwindow,
                                         text= "Calculate BMI",
                                         bg="blue", fg="yellow",
                                         command=self.calculate_BMI)

        self.__result_text = Label(text="")
        self.__result_text.grid(column=1, row=1)


        self.__explanation_text = Label(text="")
        self.__explanation_text.grid(column=1, row=0)


        self.__stop_button = Button(self.__mainwindow, text="STOP", bg="red",
                                    fg="white", command=self.stop)
        self.__stop_button.grid(column=0, row=5)


        self.__calculate_button.grid(column=0, row=4)


    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text.

            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text.
        """
        try:


            w = float(self.__weight_value.get())
            h_m = float(self.__height_value.get())
            h = h_m*0.01
            if h <= 0:
                self.__explanation_text.configure(text="Error: height and "
                                                       "weight must be "
                                                       "positive.")
                self.reset_fields()
            elif w < 0:
                self.__explanation_text.configure(text="Error: height and "
                                                       "weight must be "
                                                       "positive.")
                self.reset_fields()
            else:
                b = (w/(h**2))
                self.__result_text.configure(
                    text="{0:.2f}".format(b))
                if b < 18.5:
                    self.__explanation_text.configure(text="You are "
                                                           "underweight.")
                elif b > 25:
                    self.__explanation_text.configure(text="You are "
                                                           "overweight.")
                else:
                    self.__explanation_text.configure(text="Your weight is "
                                                           "normal.")

        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight "
                                                   "must be numbers.")
            self.reset_fields()






    # TODO: Implement this method.
    def reset_fields(self):
        self.__inputh.delete(0, END)
        self.__inputw.delete(0, END)

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
