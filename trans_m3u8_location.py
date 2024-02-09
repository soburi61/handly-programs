import os

for root, dirs, files in os.walk('.'):
    for file_name in files:
        if file_name.endswith(".m3u8"):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:  # encodingを指定
                file_content = file.read()
                modified_content = file_content.replace("primary/Music", "..")
            with open(file_path, 'w', encoding='utf-8') as file:  # encodingを指定
                file.write(modified_content)