import tkinter
import tkinter.messagebox

def main():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello,World!') \
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg,fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('warnning','make sure that you want to quit?'):
            top.quit()

    top = tkinter.Tk()


    top.geometry('240x160')

    top.title('small game')

    label = tkinter.Label(top, text='Hello,World!', font='Arial -32', fg='red')
    label.pack(expand=1)

    panel = tkinter.Frame(top)

    button1 = tkinter.Button(panel, text='edit', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()