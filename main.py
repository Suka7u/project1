from gui import *


def main():
    window = Tk()
    window.title('Calculations')
    window.geometry('300x180')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()


