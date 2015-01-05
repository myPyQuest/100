""" #21 **Limit Calculator**
    Ask the user to enter f(x) and the limit value, then return the value of the limit statement
    *Optional: Make the calculator capable of supporting infinite limits.*
"""














# from tkinter import *
#
#
# class Calculator(Frame):
#
#     def frame(self, side):
#         w = Frame(self)
#         w.pack(side=side, expand=YES, fill=BOTH)
#         return w
#
#     def button(self, root, side, text, command=None):
#         w = Button(root, text=text, command=command)
#         w.pack(side=side, expand=YES, fill=BOTH)
#         return w
#
#     need_clr = False
#
#     def digit(self, digit):
#         if self.need_clr:
#             self.display.set('')
#             self.need_clr = False
#         self.display.set(self.display.get() + digit)
#
#     def sign(self):
#         need_clr = False
#         cont = self.display.get()
#         if len(cont) > 0 and cont[0] == '-':
#             self.display.set(cont[1:])
#         else:
#             self.display.set('-' + cont)
#
#     def oper(self, op):
#         self.display.set(self.display.get() + ' ' + op + ' ')
#         self.need_clr = False
#
#     def calc(self):
#         try:
#             self.display.set(eval(self.display.get()))
#             self.need_clr = True
#         except:
#             showerror('Operation Error', 'Illegal Operation')
#             self.display.set('')
#             self.need_clr = False
#
#     def equals(self):
#         try:
#             result = eval(self.display.get())
#             if result >= 1000:
#                 result(calc)
#         except:
#             results("ERROR")
#         display.delete(0, END)
#         display.insert(0, display)
#
#     def __init__(self):
#         Frame.__init__(self)
#         self.option_add('*Font', 'Dotum 15')
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title('Simple Calculator')
#
#         self.display = StringVar()
#         e = Entry(self, relief=SUNKEN, textvariable=self.display)
#         e.pack(side=TOP, expand=YES, fill=BOTH)
#
#         for key in ("123", "456", "789"):
#             keyF = self.frame(TOP)
#             for char in key:
#                 self.button(keyF, LEFT, char,
#                             lambda c=char: self.digit(c))
#
#         keyF = self.frame(TOP)
#         self.button(keyF, LEFT, '0', lambda ch='0': self.digit(ch))
#
#         opsF = self.frame(TOP)
#         for char in "+-=":
#             if char == '=':
#                 btn = self.button(opsF, LEFT, char, self.calc)
#             else:
#                 btn = self.button(opsF, LEFT, char,
#                                   lambda w=self, s=char: w.oper(s))
#
#         clearF = self.frame(BOTTOM)
#         self.button(clearF, LEFT, 'Clr', lambda w=self.display: w.set(''))
#
# if __name__ == '__main__':
#     Calculator().mainloop()