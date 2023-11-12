class Video:
    views = 0
    likes = 100
    subscribers = []
    is_published = True
    def __init__(self, video_name, is_published =True)
        self.name = video_name
        self.is_published = is_published
    def watch(self):
        self.views += 1
    def subscriber(self, human_objekt):
        self.subscribers.append(human_objekt)
class Human:
    def __init__(self, name, age):
        self.age - name
        self.age = age
    def __repr__(self):
        return self.name
    
i_am_at_zoo = Video("Я в зоопарке")
video_2 = Video("Урок 16. Конструктор")

asan = Human("Asan", 17)
janar = Human("JAnar", 17)
bekzat = Human("Bekzat", 18)

print(i_am_at_zoo.subscribers)
i_am_at_zoo.subscriber(asan)
i_am_at_zoo.subscriber(bekzat)


