# import tkinter # 实现图形操作界面
from tkinter import messagebox # 对话框
from traceback import format_exc #用于精准的获取错误异常


if __name__ == '__main__':
    try:
        import program # 导入随机点名入口模块
    except:
        messagebox.showerror(
            title = '程序出错！',
            message='程序导入错误！\n%s' % (format_exc() ))
        print(format_exc())
    else: # 导入模块没有异常
        try:
            program.main.main() # 执行入口函数
        except:
                messagebox.showerror(
                    title = '程序出错！',
                    message='程序出现未知错误！\n%s' % (format_exc() ))
                print(format_exc())
