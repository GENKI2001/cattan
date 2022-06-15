import tkinter as tk
from turtle import color
from PIL import Image, ImageTk
import Cattan

class Application():
    def __init__(self, geology_colors) -> None:
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.canvas = tk.Canvas(self.root, background="white", width=600, height=600)
        self.geology_colors = geology_colors
        self.drawBlocks(100, 200)
        self.getImage()

        self.canvas.pack()

    def drawBlock(self, x, y, color="white"):
        scale = 20
        self.canvas.create_polygon(0 + x, 0 + y,
                            1.73 * scale + x, 1 * scale + y,
                            1.73 * scale + x, 3 * scale + y,
                            0 * scale + x, 4 * scale + y,
                            -1.73 * scale + x, 3 * scale + y,
                            -1.73 * scale + x, 1 * scale + y,
                            fill=color, outline="black", width=3)

    def drawBlocks(self, x, y):
        self.drawBlock(x=x+70+70*1, y=y-120, color=self.geology_colors[0])
        self.drawBlock(x=x+70+70*2, y=y-120, color=self.geology_colors[1])
        self.drawBlock(x=x+70+70*3, y=y-120, color=self.geology_colors[2])
        self.drawBlock(x=x+35+70*1, y=y-60, color=self.geology_colors[3])
        self.drawBlock(x=x+35+70*2, y=y-60, color=self.geology_colors[4])
        self.drawBlock(x=x+35+70*3, y=y-60, color=self.geology_colors[5])
        self.drawBlock(x=x+35+70*4, y=y-60, color=self.geology_colors[6])
        self.drawBlock(x=x+70*1, y=y, color=self.geology_colors[7])
        self.drawBlock(x=x+70*2, y=y, color=self.geology_colors[8])
        self.drawBlock(x=x+70*3, y=y, color=self.geology_colors[9])
        self.drawBlock(x=x+70*4, y=y, color=self.geology_colors[10])
        self.drawBlock(x=x+70*5, y=y, color=self.geology_colors[11])
        self.drawBlock(x=x+35+70*1, y=y+60, color=self.geology_colors[12])
        self.drawBlock(x=x+35+70*2, y=y+60, color=self.geology_colors[13])
        self.drawBlock(x=x+35+70*3, y=y+60, color=self.geology_colors[14])
        self.drawBlock(x=x+35+70*4, y=y+60, color=self.geology_colors[15])
        self.drawBlock(x=x+70+70*1, y=y+120, color=self.geology_colors[16])
        self.drawBlock(x=x+70+70*2, y=y+120, color=self.geology_colors[17])
        self.drawBlock(x=x+70+70*3, y=y+120, color=self.geology_colors[18])

    def getImage(self):
        self.img = Image.open("cattan_woods.png")
        self.img = self.img.resize((80, 90))

        # 森
        self.img_woods = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(200, 100 , anchor = tk.NW, image=self.img_woods)



