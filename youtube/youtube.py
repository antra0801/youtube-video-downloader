from pytube import YouTube
import tkinter as tk
from tkinter import filedialog , messagebox , ttk

def download_vid(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highest_res  = streams.get_highest_resolution()
        highest_res.download(output_path = save_path)
        print("downloaded successfully")
        messagebox.showinfo("Success", "Download completed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# url = "https://www.youtube.com/watch?v=PeThw9Fjtz8"
# save_path = r"C:\Users\AntraGupta\OneDrive - Infusai Solutions Pvt. Ltd\Desktop\self_projects"
# "C:\Users\AntraGupta\OneDrive - Infusai Solutions Pvt. Ltd\Desktop\self_projects\yt_videos"

# download_vid(url,save_path)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        # output_entry.delete(0, tk.END)
        # folder.insert(0, folder )
        print(f"selected path : {folder}")
    return folder


window = tk.Tk()
window.title("YouTube Downloader")
window.iconbitmap(r"C:\Users\AntraGupta\Downloads\favicon.ico")

# Create style for buttons
style = ttk.Style()
style.configure('TButton', foreground='blue', font=('Arial', 10))

# Create labels and entry fields
url_label = ttk.Label(window, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

url_entry = ttk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

output_label = ttk.Label(window, text="Output directory:")
output_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

output_entry = ttk.Entry(window, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

output_button = ttk.Button(window, text="Select", command=open_file_dialog)
output_button.grid(row=1, column=2, padx=5, pady=5)

# Create the download button with custom style
download_button = ttk.Button(window, text="Download", command=download_vid)
download_button.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky="ns")

# Run the application
window.mainloop()
