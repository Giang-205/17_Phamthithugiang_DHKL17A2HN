import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chương trình xem ảnh")

# Mở và xử lý ảnh
try:
    image = Image.open("xe.jpg")  # Đảm bảo file ảnh tồn tại
    new_size = (400, 400)  # Kích thước mới
    image = image.resize(new_size, Image.LANCZOS)  # Thay Image.ANTIALIAS bằng Image.LANCZOS

    # Chuyển ảnh thành định dạng Tkinter
    img = ImageTk.PhotoImage(image)

    # Hiển thị ảnh trong Label
    label = tk.Label(window, image=img)
    label.image = img  # Giữ tham chiếu tới ảnh để tránh bị xóa bộ nhớ
    label.pack()

except FileNotFoundError:
    error_label = tk.Label(window, text="Không tìm thấy file ảnh 'xe.jpg'", fg="red")
    error_label.pack()

# Chạy giao diện
window.mainloop()