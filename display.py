import tkinter as tk
from tkinter import filedialog, messagebox
import time
from Miller import RunnigCode

def main():
    def load_file():
        try:
            # Выбор файла
            filepath = filedialog.askopenfilename(
                title="Выберите файл с разрядностью числа",
                filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
            )
            if not filepath:
                return
            
            # Чтение разрядности из файла с явной кодировкой utf-8
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content.isdigit():
                    raise ValueError("Файл должен содержать только целое число.")
                app_data["raz"] = int(content)  # Сохраняем разрядность для дальнейшей генерации

            # Отображаем информацию, что файл загружен
            file_label.config(text=f"Загружен файл с разрядностью: {app_data['raz']}")

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def generate_prime():
        try:
            if "raz" not in app_data:
                messagebox.showinfo("Информация", "Сначала загрузите файл с разрядностью числа.")
                return
            
            raz = app_data["raz"]
            start_time = time.time()
            is_prime = False
            iterations = 0

            # Генерация простого числа
            while not is_prime:
                iterations += 1
                num, is_prime = RunnigCode(raz)

            elapsed_time = time.time() - start_time

            # Результаты
            results = (
                f"Сгенерированное простое число: {num}\n"
                f"Разрядность числа: {raz}\n"
                f"Время выполнения: {elapsed_time:.10f} секунд\n"
                f"Количество итераций: {iterations}"
            )
            result_label.config(text=results)

            # Сохранение результатов в памяти для сохранения в файл
            app_data["results"] = results

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def save_results():
        if "results" not in app_data:
            messagebox.showinfo("Информация", "Сначала выполните генерацию числа.")
            return

        filepath = filedialog.asksaveasfilename(
            title="Сохранить результаты",
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if not filepath:
            return
        
        try:
            # Сохраняем результаты в файл с кодировкой utf-8
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(app_data["results"])
            messagebox.showinfo("Успех", "Результаты успешно сохранены.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    # Инициализация приложения
    app_data = {"results": None}  # Хранение результата для сохранения

    root = tk.Tk()
    root.title("Miller-Rabin Prime Generator")

    # Устанавливаем размер окна
    root.geometry("500x400")

    # Элементы интерфейса
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(expand=True, fill=tk.BOTH)

    # Кнопка для загрузки файла с разрядностью
    load_button = tk.Button(frame, text="Загрузить файл", command=load_file)
    load_button.pack(pady=5)

    # Метка для отображения информации о загруженном файле
    file_label = tk.Label(frame, text="Загрузите файл с разрядностью числа", justify=tk.LEFT, anchor="w", padx=5, pady=5)
    file_label.pack(fill=tk.BOTH, pady=10)

    # Кнопка для генерации простого числа
    generate_button = tk.Button(frame, text="Сгенерировать простое число", command=generate_prime)
    generate_button.pack(pady=5)

    # Кнопка для сохранения результатов
    save_button = tk.Button(frame, text="Сохранить результаты", command=save_results)
    save_button.pack(pady=5)

    # Метка для отображения результатов
    result_label = tk.Label(frame, text="Результаты появятся здесь.", justify=tk.LEFT, anchor="w", padx=5, pady=5)
    result_label.pack(fill=tk.BOTH, pady=10)

    # Запуск главного цикла
    root.mainloop()

if __name__ == "__main__":
    main()
