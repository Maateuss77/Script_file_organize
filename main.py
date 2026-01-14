from pathlib import Path
import json
import shutil


CATEGORIES_FILE = Path("categories.json")


def load_categories() -> dict:
    if not CATEGORIES_FILE.exists():
        raise FileNotFoundError("categories.json não encontrado.")

    with CATEGORIES_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_categories(categories: dict):
    with CATEGORIES_FILE.open("w", encoding="utf-8") as file:
        json.dump(categories, file, indent=4, ensure_ascii=False)

def create_json():
    path("categories.json").touch()

def create_new_category():
    categories = load_categories()

    while True:
        print("Digite /t para sair")

        category = input("Nome da nova categoria: ").strip()
        if category == "/t":
            break

        extensions_input = input("Extensões separadas por vírgula (.exe,.bat,.msi): ").strip()
        if extensions_input == "/t":
            break

        extensions = [ext.strip().lower() for ext in extensions_input.split(",")]

        categories[category] = extensions
        save_categories(categories)

        print(f"Categoria '{category}' criada com extensões: {extensions}")


def choose_directory() -> Path:
    print("Digite o caminho da pasta (pode usar ~):")
    raw = input("> ").strip()

    path = Path(raw).expanduser()

    if not path.exists():
        raise FileNotFoundError("Diretório não encontrado.")

    return path


def organize_directory(directory: Path):
    categories = load_categories()

    for item in directory.iterdir():
        if item.is_dir():
            continue

        ext = item.suffix.lower()

        moved = False

        for category, extensions in categories.items():
            if ext in extensions:
                target_dir = directory / category
                target_dir.mkdir(exist_ok=True)

                shutil.move(str(item), str(target_dir / item.name))
                moved = True
                break

        if not moved:
            other = directory / "Outros"
            other.mkdir(exist_ok=True)
            shutil.move(str(item), str(other / item.name))


def main():
    print("1 - Organizar diretório")
    print("2 - Criar nova categoria")
    choice = input("> ")

    if choice == "1":
        dir_path = choose_directory()
        organize_directory(dir_path)
        print("Organização concluída!")
    elif choice == "2":
        create_new_category()
    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()
