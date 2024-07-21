import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
import math

def main():
    #create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Enter radius:")

    # Create an float entry box where the user will enter the radius.
    ent_radius = FloatEntry(frm_main, width=4, lower_bound=12, upper_bound=90)

    # Create a label that displays "years"
    #lbl_age_units = Label(frm_main, text="years")

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_slow = Label(frm_main, width=3)
    #lbl_fast = Label(frm_main, width=3)
    lbl_area_units = Label(frm_main, text="m2/cm2")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_radius.grid(      row=0, column=1, padx=3, pady=3)
    #lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_slow.grid(      row=1, column=1, padx=3, pady=3)
    #lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
    lbl_area_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the radius.
            radius = ent_radius.get()

            #compute the area of the circle with the given radius.
            area = math.pi * radius **2

            #display the area.
            lbl_slow.config(text=f"{area:.0f}")

            # Compute the user's maximum heart rate.
            #max_rate = 220 - age

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            #slow = max_rate * 0.65
            #fast = max_rate * 0.85

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            #lbl_slow.config(text=f"{slow:.0f}")
            #lbl_fast.config(text=f"{fast:.0f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_slow.config(text="")
            #lbl_fast.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_slow.config(text="")
        #lbl_fast.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()