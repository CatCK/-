import json

import time

import hashlib
'hashlib.md5(string.encode()).hexdigest()'

import sys
'print(sys.argv)'

import os.path

from tkinter import *

from tkinter import messagebox

def check_code(dat):
    # 浅拷贝，防止源数据效验码丢失
    data = dat.copy()
    '生成校验码'
    # 尝试删除数据文件原先的校验码
    try:
        data.pop('check_code')
    except:
        pass
    # 将数据改为以字符串格式
    data = repr(data)
    # 校验码是MD5加密后的结果
    check = hashlib.md5(data.encode()).hexdigest()
    # 返回校验码
    return check
def test_check(data):
    '检验校验码是否正确,返回bool值'
    # 尝试获取原校验码
    try:
        checkcode = data['check_code']
    except:
        return False
    # 获取校验码
    check = check_code(data)
    if checkcode == check:
        return True
    else:
        return False
def save_data(data, json_data_file):
    '保存数据到文件'
    # 更新校验码
    data['check_code'] = check_code(data)
    # 写入 JSON 数据
    with open(json_data_file, 'w') as f:
        json.dump(data, f)
    return data

def read_data(data, json_data_file):
    '读数据'
    # 判断数据文件是否存在
    if os.path.isfile(json_data_file):
        with open(json_data_file, 'r') as f:
            try: # 尝试把json转换成Python的数据类型
                new_data = json.load(f)
                # print(new_data)
                if test_check(new_data):
                    # print(new_data)
                    return new_data
                else:
                    top = Tk()
                    top.withdraw()#为了防止弹出对话框时出现白框框--隐藏窗口
                    
                    messagebox.showerror(
                        title = '数据错误，无法读取！',
                        message='数据错误，无法读取！\n请不要修改数据！\n已恢复默认数据')
                    top.destroy()# 销毁临时窗口
                    del top
                    
                    save_data(data, json_data_file)
            except:
                top = Tk()
                top.withdraw()#为了防止弹出对话框时出现白框框--隐藏窗口
                
                messagebox.showerror(
                    title = '数据损坏，无法读取！',
                    message='数据损坏，无法读取！\n已恢复默认数据')
                top.destroy() # 销毁临时窗口
                del top
            return data
    else:
        # print("文件")
        save_data(data, json_data_file)
        return data
def change_data(new_data, old_data):
    '改变数据'
    # 浅拷贝
    data = new_data.copy()
    # 获取旧数据的所有键
    old_keys = list(old_data.keys())
    
    # 如果没有则加上
    for key in old_keys:
        if key not in data:
            data[key] = old_data[key]
    
    return data



json_data_file = 'data.json'

data = {
    'program_name': 'Python program',
    'program_path': sys.argv[0],
    'verson': [0, 0, 0, 0],
    'autor': 'mm',
    'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    'check_code': '',
}


if __name__ == '__main__':
    # json_str = json.dumps(data)
    # print ("Python 原始数据：", repr(data))
    # print ("JSON 对象：", json_str)
    
    '''
    "文件操作"
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(data, f)
    '''
    data = read_data(data, json_data_file)
    data = save_data(data, json_data_file)
    # 读取数据
    with open('data.json', 'r') as f:
        data = json.load(f)
    

    print(data)
    print(test_check(data))
