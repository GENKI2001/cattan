import random
import App

class Cattan:
    def __init__(self) -> None:
        self.geology = self.geo_randomDistribute()
        self.geology = self.setThievesCenter(self.geology)
        self.geology_colors = self.convertColor(self.geology)
        self.geology_nums = self.num_randomDistribute()

    def geo_randomDistribute(self):
        return random.sample(["鉄", "鉄", "鉄",
                             "麦", "麦", "麦", "麦",
                             "羊", "羊", "羊", "羊",
                             "木", "木", "木", "木",
                             "レンガ", "レンガ", "レンガ",
                             "盗賊"], 19)

    def setThievesCenter(self, mapList):
        for i, l in enumerate(mapList):
            if l == "盗賊":
                break
        temp = mapList[9]
        mapList[9] = "盗賊"
        mapList[i] = temp
        return mapList

    def convertColor(self, list):
        temp = []
        for i, l in enumerate(list):
            if l == "鉄":
                temp.append("grey")
            if l == "麦":
                temp.append("yellow")
            if l == "羊":
                temp.append("palegreen")
            if l == "木":
                temp.append("darkgreen")
            if l == "レンガ":
                temp.append("brown")
            if l == "盗賊":
                temp.append("black")
        return temp

    def num_randomDistribute(self):
        return random.sample([2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12], 18)

def main():
    cattan = Cattan()
    app = App.Application(cattan.geology_colors)
    app.root.mainloop()

main()
