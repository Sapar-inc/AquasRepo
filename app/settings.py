import tkinter as tk
from tkinter import ttk
from babel.support import Translations
import os

translations = {}


def load_translations():
    locales = ['en_US', 'ru_RU']

    for locale in locales:
        translation_path = os.path.join('locales', locale, 'LC_MESSAGES', 'messages.mo')

        try:
            translations[locale] = Translations.load(translation_path)
        except Exception as e:
            print(f"Error loading translations for {locale}: {e}")
            translations[locale] = Translations()

        print(f"Loaded translations for {locale} from {translation_path}")


def get_locale():
    return translations.get(lang_var.get(), Translations())


def update_translation():
    current_translation = get_locale()
    label_hello['text'] = current_translation.gettext('Hello, World!')
    label_locale['text'] = f"Locale: {lang_var.get()}"  #Обновляем Label с локалью
    print(current_translation.gettext('Hello, World!'))


def create_labels(parent):
    global label_hello, label_locale

    # Label для текста
    label_hello = tk.Label(parent, text='')
    label_hello.grid(row=1, column=0, padx=10, pady=10)

    # Label для локали
    label_locale = tk.Label(parent, text='')
    label_locale.grid(row=1, column=1, padx=10, pady=10)

    update_translation()  # Установим текст при создании меток


def on_language_change(*args):
    update_translation()


def settings_page(root):
    def create_language_dropdown(parent, lang_var):
        lang_switcher_combo = ttk.Combobox(parent, values=list(translations.keys()), textvariable=lang_var,
                                           state='readonly')
        lang_switcher_combo.grid(row=0, column=0, padx=10, pady=10)
        lang_switcher_combo.bind("<<ComboboxSelected>>", on_language_change)

    create_language_dropdown(root, lang_var)
    create_labels(root)


if __name__ == "__main__":
    load_translations()

    root = tk.Tk()
    lang_var = tk.StringVar()
    lang_var.set('ru_RU')

    settings_page(root)

    root.mainloop()