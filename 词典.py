import tkinter as tk
from tkinter import messagebox, simpledialog
import sys

class menu2_work:
    def EXIT():
        with open("单词本.txt", "w", encoding="utf-8") as file:
            for word, translation in dictionary.items():
                file.write(f"{word}\\{translation}\n")
        sys.exit()
    
    def save():
        messagebox.showinfo(lang_dict['save_title'], lang_dict['save_message'])
    
    def ABOUT():
        messagebox.showinfo(lang_dict['about_title'], lang_dict['about_message'])

    def OPEN():
        messagebox.showinfo(lang_dict['error_title'], lang_dict['error_message'])

def load_dictionary():
    try:
        with open("单词本.txt", "r", encoding="utf-8") as file:
            dictionary = {}
            for line in file:
                word, translation = line.strip().split("\\")
                dictionary[word] = translation
        return dictionary
    except FileNotFoundError:
        messagebox.showerror(lang_dict['error_title'], lang_dict['file_not_found_message'])

def lookup_word(lang_dict):
    global dictionary
    search_option = search_var.get()  # 获取选择的查询方式
    if search_option == lang_dict['word']:
        word = entry_word.get().lower()  # 获取输入的单词，并转换为小写
        if word in dictionary:
            translation = dictionary[word]
            messagebox.showinfo(lang_dict['result_title'], f"{word} {lang_dict['translation_is']} {translation}")
        else:
            add_translation(word)
    elif search_option == lang_dict['translation']:
        translation = entry_word.get()
        if translation in dictionary.values():
            word = [key for key, value in dictionary.items() if value == translation][0]
            messagebox.showinfo(lang_dict['result_title'], f"{translation} {lang_dict['word_is']} {word}")
        else:
            add_word(translation)

def add_translation(word):
    translation = simpledialog.askstring(lang_dict['translation_not_found'], f"{lang_dict['enter_translation_for']} '{word}':")
    if translation:
        with open("单词本.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}\\{translation}\n")
        messagebox.showinfo(lang_dict['add_success'], f"{lang_dict['word']} '{word}' {lang_dict['translation']} '{translation}' {lang_dict['added_to_dictionary']}")
        dictionary[word] = translation  # 更新内存中的字典

def add_word(translation):
    word = simpledialog.askstring(lang_dict['word_not_found'], f"{lang_dict['enter_word_for']} '{translation}':")
    if word:
        with open("单词本.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}\\{translation}\n")
        messagebox.showinfo(lang_dict['add_success'], f"{lang_dict['word']} '{word}' {lang_dict['translation']} '{translation}' {lang_dict['added_to_dictionary']}")
        dictionary[word] = translation  # 更新内存中的字典

def change_language(*args):
    global lang_dict
    lang = lang_var.get()
    old_lang_dict = lang_dict
    lang_dict = languages[lang]

    # 更新所有控件的文本
    root.title(lang_dict['title'])
    label_word.config(text=lang_dict['enter_query'])
    button_search.config(text=lang_dict['search_button'])
    Exit_Button.config(text=lang_dict['exit_button'])

    # 更新about按钮的文本
    about_menu.entryconfigure(0, label=lang_dict['about_menu'])
    about_menu.entryconfigure(1, label=lang_dict['file_menu'])

    # 更新file_menu2的标签
    file_menu2.entryconfigure(0, label=lang_dict['save_menu'])
    file_menu2.entryconfigure(1, label=lang_dict['open_menu'])
    file_menu2.entryconfigure(3, label=lang_dict['exit_menu'])

    # 更新search_option_menu的标签
    search_option_menu['menu'].entryconfig(0, label=lang_dict['word'])
    search_option_menu['menu'].entryconfig(1, label=lang_dict['translation'])
    if search_var.get() == old_lang_dict['word']:
        search_var.set(lang_dict['word'])
    else:
        search_var.set(lang_dict['translation'])

# 语言配置
languages = {
    'English': {
        'title': "Simple Dictionary",
        'enter_query': "Enter the word or translation to search:",
        'word': "Word",
        'translation': "Translation",
        'search_button': "Search",
        'exit_button': "Save and Exit",
        'save_menu': "Save",
        'open_menu': "Open",
        'exit_menu': "Exit",
        'file_menu': "File",
        'about_menu': "About 'Dictionary'",
        'save_title': "Save",
        'save_message': "File saved to '单词本.txt'",
        'about_title': "About",
        'about_message': "About 'Dictionary'\nv1.12\nFor more information, visit our website.",
        'result_title': "Result",
        'translation_is': "translation is",
        'word_is': "word is",
        'translation_not_found': "Translation not found",
        'word_not_found': "Word not found",
        'enter_translation_for': "Enter translation for",
        'enter_word_for': "Enter word for",
        'add_success': "Add Success",
        'added_to_dictionary': "added to dictionary"
    },
    '中文': {
        'title': "简易词典",
        'enter_query': "请输入要查询的单词或翻译：",
        'word': "单词",
        'translation': "翻译",
        'search_button': "查询",
        'exit_button': "保存并退出",
        'save_menu': "保存",
        'open_menu': "打开",
        'exit_menu': "退出",
        'file_menu': "文件",
        'about_menu': "关于‘词典’",
        'save_title': "保存",
        'save_message': "文件已保存到“单词本.txt”",
        'about_title': "关于",
        'about_message': "关于‘词典’\nv1.12\n更多信息请前往网站查看",
        'result_title': "结果",
        'translation_is': "的翻译是",
        'word_is': "的单词是",
        'translation_not_found': "翻译不存在",
        'word_not_found': "单词不存在",
        'enter_translation_for': "请输入单词",
        'enter_word_for': "请输入翻译",
        'add_success': "添加成功",
        'added_to_dictionary': "已添加到单词本"
    }
}

# 创建主窗口
root = tk.Tk()
root.title(languages['English']['title'])

# 加载单词本
dictionary = load_dictionary()

# 创建标签、输入框和选择查询方式的选项
label_word = tk.Label(root, text=languages['English']['enter_query'])
label_word.pack()
entry_word = tk.Entry(root)
entry_word.pack()
search_var = tk.StringVar(root)
search_var.set(languages['English']['word'])  # 默认选择单词查询
search_option_menu = tk.OptionMenu(root, search_var, languages['English']['word'], languages['English']['translation'])
search_option_menu.pack()

# 创建退出按钮
Exit_Button = tk.Button(root, text=languages['English']['exit_button'], width=50, height=2, command=menu2_work.EXIT, bg='green', fg='black')
Exit_Button.pack()

# 创建查询按钮
button_search = tk.Button(root, text=languages['English']['search_button'], width=50, height=2, command=lambda: lookup_word(lang_dict), bg='green', fg='black')
button_search.pack()

# 创建about按钮
about_menu = tk.Menu(root, tearoff=0)
about_menu.add_command(label=languages['English']['about_menu'], command=menu2_work.ABOUT)
root.config(menu=about_menu)

# 创建菜单栏和文件菜单
file_menu2 = tk.Menu(about_menu, tearoff=0)
about_menu.add_cascade(label=languages['English']['file_menu'], menu=file_menu2)
file_menu2.add_command(label=languages['English']['save_menu'], command=menu2_work.save)
file_menu2.add_command(label=languages['English']['open_menu'], command=menu2_work.OPEN)
file_menu2.add_separator()
file_menu2.add_command(label=languages['English']['exit_menu'], command=menu2_work.EXIT)

# 语言选项菜单
lang_var = tk.StringVar(value='English')
lang_option_menu = tk.OptionMenu(root, lang_var, *languages.keys(), command=change_language)
lang_option_menu.pack()

# 初始化当前语言
lang_dict = languages['English']

# 运行主事件循环
root.mainloop()
