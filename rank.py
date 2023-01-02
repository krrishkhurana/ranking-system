names=['krrish','karan','krish kumar','raj','vaibhav']
marks=[80,99,79,98,85]
updation=[10,-5,20,-10,56]
rank=1
previousRankMarks=100

for rank in range(1,6,1):
    currRankMarks =0
    currRankIndex =0
    for i in range(0,5):
        if ((marks[i] + updation[i] > currRankMarks) and ( marks[i]+updation[i] < previousRankMarks )):
            currRankMarks = marks[i] + updation[i]
            currRankIndex = i
    print("Rank",rank,"  ",names[currRankIndex],marks[currRankIndex]+updation[currRankIndex])
    previousRankMarks = marks[currRankIndex] + updation[currRankIndex]
