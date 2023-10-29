class Question :
    def __init__ (self,qw,ans,wrong1,wrong2,wrong3):
        self.qw = qw
        self.ans = ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.count = 0
        self.count_right = 0
    def right_ans (self):
        self.count +=1
        self.count_right +=1
    def wrong_ans (self):
        self.count +=1


qw1 = Question("Скільки ніг у риби?","0","4","3","8")
qw2 = Question("Скільки років живуть кактуси?","200-300","10-20","50-150","80")
qw3 = Question("Якого розміру у страуса мозок?","Як горішок","Як у людини","Як у собаки","Як у комп'ютера")
qw4 = Question("Який птах може літати задом наперед?","Колібрі","Голуб","Гуска","Пингвин")
qw_list = [qw1,qw2,qw3,qw4]


