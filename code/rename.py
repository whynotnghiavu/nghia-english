import os

# Đường dẫn đến folder cha
parent_folder = r"C:\Users\vvn20206205\Desktop\ChuyenDe"
parent_folder = r"C:\Users\vvn20206205\Desktop\KhoaHoc"

# Lấy danh sách các folder con
subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]

# Đổi tên các folder con thành các số thứ tự
for index, subfolder in enumerate(subfolders, start=1):
    new_name = str(index)
    old_path = os.path.join(parent_folder, subfolder)
    new_path = os.path.join(parent_folder, new_name)
    os.rename(old_path, new_path)

print("Đổi tên thành công!")
