from pathlib import Path

MATERIALS_DIR = Path("materials")
files = []


for folder in MATERIALS_DIR.iterdir():
    if folder.is_dir():
        print(f"\nКатегория: {folder.name}")

        for file in folder.iterdir():
            if file.is_file() and file.suffix == ".pdf":
                files.append((folder.name, file.name))
                print(file.name)


print("\nТолько учебники:")

for category, filename in files:
    if category == "textbooks":
        print(filename)

def get_materials(category):
    result = []

    for folder, filename in files:
        if folder == category:
            result.append(Path("materials") / folder / filename)
    
    return result  

for path in get_materials("textbooks"):
    print("Путь: ", path)
    print("Файл существует:", path.exists())

print(get_materials("textbooks"))
print("Учебники: ", get_materials("textbooks"))
print("Справочники: ", get_materials("reference_books"))
print("Методички: ", get_materials ("guides"))