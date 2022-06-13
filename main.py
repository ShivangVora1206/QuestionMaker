class Process():
    def main(self, sample):
        self.sample = sample
        from random import randrange
        import os
        f = open(str(self.sample),"r")
        print(self.sample)
        restricted = [',', ' ', 'the', 'if', 'of', 'a', '.', ';', '', 'by', 'and', 'or', 'v.', 'for', '(', ')', 'adj', 'n.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '0.', 'to', 'in', 'an', 'as', 'that', 'on', 'at']
        for statement in f:
            statement = f.readlines()
        if os.getcwd() != r"C:\Users\shang\Desktop\python\Question_Maker_proj\static":
            os.chdir(r"C:\Users\shang\Desktop\python\Question_Maker_proj\static")
        q = open(self.sample[:-4] + "_questions" +".txt","a")
        a = open(self.sample[:-4] + "_answers" +".txt","a")
        for i in statement:
            state = i[2:]
            answers = state.split(" ")
            print(answers)
            length = len(answers)
            r = randrange(0,length)
            answer = answers[r]
            while answer in restricted:
                r = randrange(0,length)
                answer = answers[r]
            else:
                answer = answer.strip('\n')
                question = i.replace(answer, "-"*len(answer))

            print(question)
            q.write(question)
            print(answer)
            a.write(answer+"\n")

P = Process()
filename = "C:\\Users\\shang\\Desktop\\python\\Question_Maker_proj\\Uploads\\OUT.txt"
P.main(filename)