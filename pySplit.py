import tkinter as tk
from tkinter import filedialog
import os

def open_file_dialog(title="Select a file", filetypes=(('All files', '*.*'),)):
    # 創建一個隱藏的根窗口
    root = tk.Tk()
    root.withdraw()

    # 開啟檔案選擇對話框，並取得選擇的檔案路徑
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return file_path

def open_directory_dialog(title="Select a folder"):
    # 創建一個隱藏的根窗口
    root = tk.Tk()
    root.withdraw()

    # 打開資料夾選擇對話框，並取得選擇的資料夾路徑
    directory_path = filedialog.askdirectory(title=title)
    return directory_path

def split_file(file_path, output_folder, lines_per_file):
    # 檢查檔案路徑和輸出資料夾是否有效
    if not file_path or not output_folder:
        print("Invalid file or output folder.")
        return

    # 嘗試開啟檔案並分割
    try:
        with open(file_path, 'r') as file:
            count = 1
            current_content = []
            file_count = 1
            
            for line in file:
                current_content.append(line)
                if count % lines_per_file == 0:
                    output_file_path = os.path.join(output_folder, f'part_{file_count}.txt')
                    with open(output_file_path, 'w') as output_file:
                        output_file.writelines(current_content)
                    file_count += 1
                    current_content = []
                count += 1

            # 處理剩餘內容
            if current_content:
                output_file_path = os.path.join(output_folder, f'part_{file_count}.txt')
                with open(output_file_path, 'w') as output_file:
                    output_file.writelines(current_content)

        print("File split successfully.")
    except Exception as e:
        print(f"Error: {e}")

# 主邏輯
if __name__ == "__main__":
    selected_file = open_file_dialog("Select a file to split", (('Text files', '*.txt'),))
    if selected_file:
        output_directory = open_directory_dialog("Select output directory")
        if output_directory:
            split_file(selected_file, output_directory, 1000)  # 以1000行為每個檔案的行數
