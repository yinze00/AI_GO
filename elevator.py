from graphics import *
from math import *
WIDTH = 600
HEIGH = 400
op = ["先来先服务(FCFS)","短任务优先(SJF)", "最短剩余时间优先(SRTF)","优先级调度(HPF)",'时间片轮转(RR)']
def guiwin():
    win = GraphWin("A demo for Elevator Dispatching", WIDTH, HEIGH)
    option = []
    for i in range(5):
        tempopt = Text(Point(300, i * 50 + 100), op[i]);
        option.append(tempopt)
        tempopt.draw(win)    
    return win
def main():
    gamewin = guiwin()
    print("hello");
    


if __name__ == '__main__':
    main()
    