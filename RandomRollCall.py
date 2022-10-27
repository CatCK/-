from tkinter import messagebox
from traceback import format_exc


if __name__ == '__main__':
    try:
        import program
    except:
        messagebox.showerror(
            title = '程序出错！',
            message='程序导入错误！\n%s' % (format_exc() ))
        print(format_exc())
    else:
        try:
            program.main.main()
        except:
                messagebox.showerror(
                    title = '程序出错！',
                    message='程序出现未知错误！\n%s' % (format_exc() ))
                print(format_exc())
