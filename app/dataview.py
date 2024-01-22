import tkinter as tk
from tkinter import filedialog, ttk
from collections import OrderedDict

def open_widget(temp):
    with open(temp, 'r', encoding='utf-8-sig') as file:
        view = file.readlines()
    data = file_format(view)
    return data


def file_format(entries):
    header = entries[0].strip().split(',')
    parameters = [param.strip() for param in header]
    result = {param: [] for param in parameters}
    for line in entries[1:]:
        values = [value.strip() for value in line.split(',')]
        for i, param in enumerate(parameters):
            result[param].append(values[i])
    print(result)
    return result


def update_filter(entry_text, label, data):
    # Получение текста из поля ввода и разделение его на аргументы
    filter_args = [arg.strip() for arg in entry_text.get().split(',')]

    # Фильтрация данных
    filtered_data = filter(data, filter_args)

    # Обновление данных с использованием отфильтрованных данных
    update_label_frame(label, filtered_data)


def filter(data, args):
    # Создаем упорядоченный словарь для хранения фильтрованных данных
    filtered_data = OrderedDict()

    # Проходим по каждому аргументу фильтрации
    for arg in args:
        if arg in data:
            # Добавляем фильтрованные данные в упорядоченный словарь
            filtered_data[arg] = data[arg]

    print(args, filtered_data)
    return filtered_data

def update_label_frame(label_frame, data):
    for widget in label_frame.winfo_children():
        widget.destroy()

    # Создаем столбцы для каждого параметра
    for col, (param, values) in enumerate(data.items()):
        tk.Label(label_frame, text=param).grid(row=0, column=col, padx=5, pady=5)
        for row, value in enumerate(values, start=1):
            var = tk.StringVar(value=value)
            tk.Entry(label_frame, textvariable=var, state='readonly').grid(row=row, column=col, padx=5, pady=5)


def open_file(window_label):
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = open_widget(file_path)
        update_label_frame(window_label, data)


def table_page(root):
    menu = root
    menu.title("Main Page")

    width_of_window = 800
    height_of_window = 800
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    menu.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

    # Создаем виджет Canvas для возможности прокрутки
    canvas = tk.Canvas(menu, bg='#E7F1FD')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Создаем скроллбар
    scrollbar = ttk.Scrollbar(menu, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Устанавливаем прокрутку виджета Canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    file = 'tempRainYearly.csv'
    data = open_widget(file)

    # Создаем фрейм, который будет внутри виджета Canvas
    inner_frame = tk.Frame(canvas, bg='#E7F1FD')

    # Добавляем виджет фрейма в виджет Canvas
    canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

    # Добавление поля ввода
    entry_widget = tk.Entry(inner_frame)
    entry_widget.grid(row=1, column=1, padx=(10, 10), pady=10)

    btn_main = tk.Button(inner_frame, text='Main', command=lambda: update_label_frame(window_label, data), width=15, height=2)
    btn_filter = tk.Button(inner_frame, text='Filter', command=lambda: update_filter(entry_widget, window_label, data), width=15,
                           height=2)
    btn_open_file = tk.Button(inner_frame, text='Open File', command=lambda: open_file(window_label),
                              width=15, height=2)
    window_label = tk.LabelFrame(inner_frame, text='Test')
    update_label_frame(window_label, data)

    btn_main.grid(row=0, column=0, sticky="w", padx=(10, 10), pady=10)
    btn_filter.grid(row=0, column=1, sticky="w", padx=(10, 10), pady=10)
    btn_open_file.grid(row=0, column=2, sticky="w", padx=(10, 10), pady=10)
    window_label.grid(row=2, column=0, columnspan=len(data), pady=10)


    def on_mouse_wheel(event):
        # Получаем текущую позицию скроллинга
        current_pos = canvas.canvasy(0)

        # Получаем границы inner_frame
        _, _, _, frame_bottom = canvas.bbox("all")

        # Если скроллим вверх и текущая позиция не равна 0, разрешаем скроллинг
        if event.delta < 0 or current_pos > 0:
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        # Если скроллим вниз и есть место, разрешаем скроллинг
        elif current_pos < frame_bottom:
            canvas.yview_moveto(current_pos/frame_bottom)

    # Добавляем обработчик события прокрутки для виджета Canvas
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    menu.mainloop()


# root = tk.Tk()
# table_page(root)
