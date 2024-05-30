from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('360x465+0+0')
        master.config(bg='#333333')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(width=20, bg='black', fg='white', font=('Tahoma', 50), textvariable=self.equation).place(x=0, y=2)

        # Button Definitions
        buttons = [
            ('(', 1, 90), (')', 91, 90), ('.', 181, 90), ('÷', 271, 90),
            ('7', 1, 165), ('8', 91, 165), ('9', 181, 165), ('x', 271, 165),
            ('4', 1, 240), ('5', 91, 240), ('6', 181, 240), ('-', 271, 240),
            ('1', 1, 315), ('2', 91, 315), ('3', 181, 315), ('+', 271, 315),
            ('0', 91, 390), ('=', 271, 390), ('⌫', 181, 390), ('C', 1, 390),
        ]

        for (text, x, y) in buttons:
            Button(
                width=11, height=4, text=text, relief='groove',
                bg='grey' if text not in ('=', 'C') else ('gold' if text == '=' else 'grey'),
                fg='white' if text not in ('=', 'C') else ('black' if text == '=' else 'white'),
                command=lambda t=text: self._process_button(t)
            ).place(x=x, y=y)

    def _process_button(self, text):
        if text == '=':
            self.solve()
        elif text == 'C':
            self.clear()
        elif text == '⌫':
            self.backspace()
        else:
            self.show(text)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            self.equation.set(str(eval(self.entry_value.replace('÷', '/').replace('x', '*'))))
        except Exception:
            self.equation.set('Invalid')

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

root = Tk()
calculator = Calculator(root)
root.mainloop()
