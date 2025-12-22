
class Image:
    def __init__(self, imageWidth=0, imageHeight=0, colorCode=""):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.colorCode = colorCode

    def get_imageWidth(self):
        return self.imageWidth

    def get_imageHeight(self):
        return self.imageHeight

    def get_colorCode(self):
        return self.colorCode

    def set_imageWidth(self, imageWidth):
        self.imageWidth = imageWidth

    def set_imageHeight(self, imageHeight):
        self.imageHeight = imageHeight

    def set_colorCode(self, colorCode):
        self.colorCode = colorCode

    def __str__(self):
        return f"Image Width: {self.imageWidth}, Image Height: {self.imageHeight}, Color Code: {self.colorCode}"

img1 = Image(1920, 1080, "#FFFFFF")
img2 = Image()
print("Image 1 -", img1)
print("Image 2 -", img2)
img2.set_imageWidth(1280)
img2.set_imageHeight(720)
img2.set_colorCode("#000000")
print("Updated Image 2 -", img2)
