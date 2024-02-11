import json
from typing import List, Dict, Any

SPRAVOCHNIK_FILE: str = "spravochnik.txt"

def load_spravochnik() -> List[Dict[str, Any]]:
    """
    Загружает справочник из файла.

    Returns:
        List[Dict[str, Any]]: Справочник в виде списка словарей.
    """
    try:
        with open(SPRAVOCHNIK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_spravochnik(spravochnik: List[Dict[str, Any]]) -> None:
    """
    Сохраняет справочник в файл.

    Args:
        spravochnik (List[Dict[str, Any]]): Справочник в виде списка словарей.
    """
    with open(SPRAVOCHNIK_FILE, 'w') as file:
        json.dump(spravochnik, file)

def add_record(spravochnik: List[Dict[str, Any]], record: Dict[str, Any]) -> None:
    """
    Добавляет новую запись в справочник.

    Args:
        spravochnik (List[Dict[str, Any]]): Справочник в виде списка словарей.
        record (Dict[str, Any]): Новая запись в виде словаря.
    """
    spravochnik.append(record)
    save_spravochnik(spravochnik)

def edit_record(spravochnik: List[Dict[str, Any]], index: int, new_record: Dict[str, Any]) -> None:
    """
    Редактирует запись в справочнике.

    Args:
        spravochnik (List[Dict[str, Any]]): Справочник в виде списка словарей.
        index (int): Индекс записи, которую нужно отредактировать.
        new_record (Dict[str, Any]): Новая запись в виде словаря.
    """
    spravochnik[index] = new_record
    save_spravochnik(spravochnik)

def search_records(spravochnik: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    """
    Ищет записи в справочнике по заданным критериям.

    Args:
        spravochnik (List[Dict[str, Any]]): Справочник в виде списка словарей.
        **criteria: Критерии поиска в виде именованных аргументов.

    Returns:
        List[Dict[str, Any]]: Список найденных записей.
    """
    results = []
    for record in spravochnik:
        match = True
        for key, value in criteria.items():
            if key not in record or record[key] != value:
                match = False
                break
        if match:
            results.append(record)
    return results

def display_records(records: List[Dict[str, Any]], page_size: int = 5) -> None:
    """
    Выводит записи справочника постранично.

    Args:
        records (List[Dict[str, Any]]): Справочник в виде списка словарей.
        page_size (int, optional): Размер страницы. Defaults to 5.
    """
    for i in range(0, len(records), page_size):
        print("\n".join(str(record) for record in records[i:i+page_size]))
        input("Press Enter to continue...")

def main() -> None:
    """
    Основная функция программы.
    """
    spravochnik = load_spravochnik()
    while True:
        print("\n1. Display Records\n2. Add Record\n3. Edit Record\n4. Search Records\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_records(spravochnik)
        elif choice == '2':
            record = {
                'surname': input("Enter surname: "),
                'name': input("Enter name: "),
                'patronymic': input("Enter patronymic: "),
                'organization': input("Enter organization: "),
                'phone_work': input("Enter work phone: "),
                'phone_personal': input("Enter personal phone: ")
            }
            add_record(spravochnik, record)
        elif choice == '3':
            index = int(input("Enter index of record to edit: "))
            new_record = {
                'surname': input("Enter surname: "),
                'name': input("Enter name: "),
                'patronymic': input("Enter patronymic: "),
                'organization': input("Enter organization: "),
                'phone_work': input("Enter work phone: "),
                'phone_personal': input("Enter personal phone: ")
            }
            edit_record(spravochnik, index, new_record)
        elif choice == '4':
            criteria = {}
            field = input("Enter field to search (surname, name, organization, phone_work, phone_personal): ")
            value = input("Enter value to search: ")
            criteria[field] = value
            results = search_records(spravochnik, **criteria)
            if results:
                display_records(results)
            else:
                print("No records found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
