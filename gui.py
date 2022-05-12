from tkinter import *
from calculations import *


class GUI:
    """
    Class for the main GUI
    """
    def __init__(self, window):
        """
        Initializes graphics
        """
        self.window = window

        self.frame_choice = Frame(self.window)

        self.label_status = Label(self.frame_choice, text='Choice')
        self.radio_status = IntVar()
        self.radio_status.set(-1)
        self.radio_sum = Radiobutton(self.frame_choice, text='Calculate Sum of numbers from n to 1', variable=self.radio_status, value=0)
        self.radio_power = Radiobutton(self.frame_choice, text='Calculate Power', variable=self.radio_status, value=1)
        self.radio_both = Radiobutton(self.frame_choice, text='Display numbers from n to 1', variable=self.radio_status, value=2)
        self.radio_sum_of_sums = Radiobutton(self.frame_choice, text='Calculate Sum of Sums from n1 to n2', variable=self.radio_status, value=3)
        self.label_status.pack(side='left')
        self.radio_sum.pack()
        self.radio_power.pack()
        self.radio_both.pack()
        self.radio_sum_of_sums.pack()
        self.frame_choice.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)

        self.button_next = Button(self.frame_button, text='NEXT', command=self.next)
        self.button_next.pack(pady=10)
        self.frame_button.pack()

    def next(self):
        """
        Transitions to next screen based on option
        """
        status = self.radio_status.get()
        if status == 0:
            calculate = Tk()
            calculate.title('1')
            calculate.geometry('200x200')
            calculate.resizable(False, False)
            widgets = ONE(calculate)
        elif status == 1:
            calculate = Tk()
            calculate.title('2')
            calculate.geometry('200x200')
            calculate.resizable(False, False)
            widgets = TWO(calculate)
        elif status == 2:
            calculate = Tk()
            calculate.title('3')
            calculate.geometry('200x200')
            calculate.resizable(False, False)
            widgets = THREE(calculate)
        elif status == 3:
            calculate = Tk()
            calculate.title('4')
            calculate.geometry('275x200')
            calculate.resizable(False, False)
            widgets = FOUR(calculate)
        else:
            pass

        self.radio_status.set(-1)


class ONE:
    """
    Class for the first option
    """
    def __init__(self, window):
        """
        Initializes graphics
        """
        self.window = window

        self.frame_enter = Frame(self.window)

        self.label_enter = Label(self.frame_enter, text='Enter a Number: ')
        self.entry_enter = Entry(self.frame_enter, width=5)
        self.label_enter.pack(padx=5, side='left')
        self.entry_enter.pack(padx=5, side='left')
        self.frame_enter.pack(anchor='w', pady=5)

        self.frame_button = Frame(self.window)

        self.button_submit = Button(self.frame_button, text='SUBMIT', command=self.calculate)
        self.button_submit.pack(pady=5)
        self.frame_button.pack()

    def calculate(self):
        """
        calculates and displays result
        """
        num = int(self.entry_enter.get())

        self.frame_result = Frame(self.window)

        self.label_result = Label(self.frame_result, text=f'Result: {one(num)}')
        self.label_result.pack(padx=5)
        self.frame_result.pack(pady=5)


class TWO:
    """
    Class for the second option
    """
    def __init__(self, window):
        """
        Initializes graphics
        """
        self.window = window

        self.frame_base = Frame(self.window)

        self.label_base = Label(self.frame_base, text='Base')
        self.entry_base = Entry(self.frame_base, width=5)
        self.label_base.pack(padx=5, side='left')
        self.entry_base.pack(padx=5, side='left')
        self.frame_base.pack(anchor='w', pady=5)

        self.frame_exponent = Frame(self.window)

        self.label_exponent = Label(self.frame_exponent, text='Exponent')
        self.entry_exponent = Entry(self.frame_exponent, width=5)
        self.label_exponent.pack(padx=5, side='left')
        self.entry_exponent.pack(padx=5, side='left')
        self.frame_exponent.pack(pady=5, anchor='w')

        self.frame_button = Frame(self.window)

        self.button_submit = Button(self.frame_button, text='SUBMIT', command=self.calculate)
        self.button_submit.pack(pady=5)
        self.frame_button.pack()

    def calculate(self):
        """
        calculates and displays result
        """
        base = int(self.entry_base.get())
        exponent = int(self.entry_exponent.get())

        self.frame_result = Frame(self.window)

        self.label_result = Label(self.frame_result, text=f'Result: {base}^{exponent} = {two(base, exponent)}')
        self.label_result.pack(padx=5)
        self.frame_result.pack(pady=5)


class THREE:
    """
    Class for the second option
    """
    def __init__(self, window):
        """
        Initializes graphics
        """
        self.window = window

        self.frame_enter = Frame(self.window)

        self.label_enter = Label(self.frame_enter, text='Enter a Number: ')
        self.entry_enter = Entry(self.frame_enter, width=5)
        self.label_enter.pack(padx=5, side='left')
        self.entry_enter.pack(padx=5, side='left')
        self.frame_enter.pack(anchor='w', pady=5)

        self.frame_button = Frame(self.window)

        self.button_submit = Button(self.frame_button, text='SUBMIT', command=self.execute)
        self.button_submit.pack(pady=5)
        self.frame_button.pack()

    def execute(self):
        """
        displays result
        """
        num = int(self.entry_enter.get())

        self.frame_result = Frame(self.window)

        self.label_result = Label(self.frame_result, text=f'{three(num)}')
        self.label_result.pack(padx=5)
        self.frame_result.pack(pady=5)


class FOUR:
    """
    Class for the fourth option
    """
    def __init__(self, window):
        self.window = window

        self.frame_num1 = Frame(self.window)

        self.label_num1 = Label(self.frame_num1, text='First (Smaller) Number')
        self.entry_num1 = Entry(self.frame_num1, width=15)
        self.label_num1.pack(padx=5, side='left')
        self.entry_num1.pack(padx=5, side='left')
        self.frame_num1.pack(anchor='w', pady=5)

        self.frame_num2 = Frame(self.window)

        self.label_num2 = Label(self.frame_num2, text='Second (Larger) Number')
        self.entry_num2 = Entry(self.frame_num2, width=15)
        self.label_num2.pack(padx=5, side='left')
        self.entry_num2.pack(padx=5, side='left')
        self.frame_num2.pack(pady=5, anchor='w')

        self.frame_button = Frame(self.window)

        self.button_submit = Button(self.frame_button, text='SUBMIT', command=self.calculate)
        self.button_submit.pack(pady=5)
        self.frame_button.pack()

    def calculate(self):
        """
        calculates and displays result
        """
        num1 = int(self.entry_num1.get())
        num2 = int(self.entry_num2.get())

        self.frame_result = Frame(self.window)

        self.label_result = Label(self.frame_result, text=f'The sum of sums from {num1} to {num2} is {four(num1, num2)}')
        self.label_result.pack(padx=5)
        self.frame_result.pack(pady=5)
