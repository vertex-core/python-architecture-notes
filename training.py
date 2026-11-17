from pathlib import Path

# * Выносим путь к файлу в константу, чтобы не дублировать строку в нескольких местах
NOTES_FILE = Path("notes.txt")


def add_note(filepath: Path, note: str) -> None:
    """Добавляет новую заметку в конец файла."""
    # * strip() убирает случайные пробелы/переносы, добавляем один четкий \n в конце
    clean_note = note.strip()
    if not clean_note:
        return

    with filepath.open("a", encoding="utf-8") as file:
        file.write(f"{clean_note}\n")


def print_notes(filepath: Path) -> None:
    """Выводит все заметки с порядковыми номерами."""
    if not filepath.exists():
        print(f"Файл '{filepath}' пока не создан.")
        return

    try:
        with filepath.open("r", encoding="utf-8") as file:
            print("--- Список заметок ---")
            for index, line in enumerate(file, start=1):
                print(f"{index}. {line.strip()}")
    except OSError as e:
        print(f"Ошибка при чтении файла: {e}")


if __name__ == "__main__":
    # * 1. Добавляем заметку
    add_note(NOTES_FILE, "Купить корм")

    # * 2. Читаем и красиво выводим заметки
    print_notes(NOTES_FILE)
