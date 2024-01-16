import tkinter as tk
from PIL import ImageTk, Image

class SplashScreen:
    def __init__(self, root):
        self.splash = root
        self.splash.title("Splash Screen")

        width_of_window = 450
        height_of_window = 450
        screen_width = self.splash.winfo_screenwidth()
        screen_height = self.splash.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.splash.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

        frame = tk.Frame(self.splash, width=450, height=450, bg='#E7F1FD')
        frame.place(x=0, y=0)

        # Text label
        title_label = tk.Label(frame, text='NAME OF PROJECT', fg='black', bg='#E7F1FD',
                               font=("Game of Squids", 24, "bold"))
        title_label.place(x=80, y=150)

        labels = []
        for i in range(4):
            label = tk.Label(frame, border=0, relief=tk.FLAT, bg='#E7F1FD')  # Transparent background
            label.place(x=180 + i * 20, y=250)
            labels.append(label)

        image_paths = ['./images/stage_1.png', './images/stage_2.png', './images/stage_2.png', './images/stage_2.png']
        images = [ImageTk.PhotoImage(Image.open(path).resize((10, 10))) for path in image_paths]

        self.animate_images(labels, images, 0)

        # Close the splash screen after a delay (adjust delay time as needed)
        self.splash.after(4000, self.close_splash)

    def animate_images(self, labels, images, index):
        for i, label in enumerate(labels):
            label.config(image=images[(index + i) % len(images)])
        labels[0].after(500, lambda: self.animate_images(labels, images, (index + 1) % len(images)))

    def close_splash(self):
        self.splash.destroy()

    def show(self):
        self.splash.mainloop()