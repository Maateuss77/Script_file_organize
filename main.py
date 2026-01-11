import os
import shutil

CATEGORY = {
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg"
    ],
    "Imagens": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"
    ],
    "Áudios": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus"
    ],
    "Documentos": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".odt", ".ods", ".odp", ".txt", ".rtf", ".md", ".csv"
    ],
    "Compactados": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"
    ],
    "Executáveis": [
        ".exe", ".msi", ".bat", ".sh", ".run", ".apk", ".appimage"
    ],
    "Code": [
        ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".go", ".rs",
        ".swift", ".kt", ".ts", ".tsx"
    ],
    "Scripts":[
        ".py", ".sh"
    ],
    "Torrents": [
        ".torrent"
    ],
}

def create_new_category():
    while True:
        category = input("Nome da nova categoria: ").strip()

        if category == "/t":
            break

        extensions_input = input("Extensões (separe com vírgula, ex: .exe,.msi,.bat): ").strip()
        if extensions_input == "/t":
            break

        extensions = [ext.strip().lower() for ext in extensions_input.split(",")]

        CATEGORY[category] = extensions

        print(f"Categoria '{category}' criada com extensões: {extensions}")



DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


for file_name in os.listdir(DOWNLOAD_DIR):
    file_path = os.path.join(DOWNLOAD_DIR, file_name)

    # ignorar diretórios
    if os.path.isdir(file_path):
        continue

    # pega a extensão
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    # procura categoria correspondente
    for category, extensions in CATEGORY.items():
        if ext in extensions:
            # cria pasta se não existir
            category_folder = os.path.join(DOWNLOAD_DIR, category)
            os.makedirs(category_folder, exist_ok=True)

            # move o arquivo
            shutil.move(file_path, os.path.join(category_folder, file_name))
            break


