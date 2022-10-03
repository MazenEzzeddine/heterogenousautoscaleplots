# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math

import matplotlib.pyplot as plt
import csv

from numpy import double






def oldworkload():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 68:
                replicas.append(1)
            elif math.floor(double(row[0])) < 103:
                replicas.append(2)
            elif math.floor(double(row[0])) < 178:
                replicas.append(3)
            elif math.floor(double(row[0])) < 242:
                replicas.append(2)
            elif math.floor(double(row[0])) < 273:
                replicas.append(3)
            elif math.floor(double(row[0])) < 344:
                replicas.append(4)
            elif math.floor(double(row[0])) < 375:
                replicas.append(3)
            elif math.floor(double(row[0])) < 415:
                replicas.append(2)
            elif math.floor(double(row[0])) < 446:
                replicas.append(3)
            elif math.floor(double(row[0])) < 477:
                replicas.append(4)
            elif math.floor(double(row[0])) < 509:
                replicas.append(5)
            elif math.floor(double(row[0])) < 539:
                replicas.append(4)
            elif math.floor(double(row[0])) < 570:
                replicas.append(3)
            else:
                replicas.append(1)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    ax2.spines['left'].set_color('blue')
    ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Consumer replicas')

    plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    ax2.legend(loc=1)

    plt.show()

def oldHetero():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(1)
            elif math.floor(double(row[0])) < 103:
                replicas.append(2)
            elif math.floor(double(row[0])) < 178:
                replicas.append(3)
            elif math.floor(double(row[0])) < 242:
                replicas.append(2)
            elif math.floor(double(row[0])) < 273:
                replicas.append(3)
            elif math.floor(double(row[0])) < 344:
                replicas.append(4)
            elif math.floor(double(row[0])) < 375:
                replicas.append(3)
            elif math.floor(double(row[0])) < 415:
                replicas.append(2)
            elif math.floor(double(row[0])) < 446:
                replicas.append(3)
            elif math.floor(double(row[0])) < 477:
                replicas.append(4)
            elif math.floor(double(row[0])) < 509:
                replicas.append(5)
            elif math.floor(double(row[0])) < 539:
                replicas.append(4)
            elif math.floor(double(row[0])) < 570:
                replicas.append(3)
            else:
                replicas.append(1)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    ax2.spines['left'].set_color('blue')
    ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Consumer replicas')

    plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    ax2.legend(loc=1)

    plt.show()



def oldHetero1():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
            elif math.floor(double(row[0])) < 331:
                replicas.append(244+97)
            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
            elif math.floor(double(row[0])) < 450:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 507:
                replicas.append(244+244)
            elif math.floor(double(row[0])) < 524:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
            else:
                replicas.append(96)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax2.plot(t, replicas, '--r',  label='replicas')

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    ax2.spines['left'].set_color('blue')
    ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Consumer replicas')

    plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    ax2.legend(loc=1)

    plt.show()

def oldHetero2():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # font = {'family': 'normal',
    #         'weight': 'bold',
    #         'size': 22}


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
            elif math.floor(double(row[0])) < 331:
                replicas.append(244+97)
            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
            elif math.floor(double(row[0])) < 450:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 507:
                replicas.append(244+244)
            elif math.floor(double(row[0])) < 524:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
            else:
                replicas.append(96)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))

    #############################################################"
    # y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 75, 277, 855, 1094, 692, 246, 54, 0, 73, 82, 68, 81, 94, 175, 190, 93,
    #      181, 149, 80, 69, 150, 143, 162, 141, 159, 155, 133, 138, 144, 130, 143, 145
    #     , 146, 151, 154, 63, 168, 175, 191, 189, 205, 219, 240, 403, 235, 248, 264, 258, 262, 264, 267, 189, 100, 0, 0,
    #      39, 291, 475, 419, 188, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 117,
    #      113, 261, 133, 5, 191, 504, 1859, 2161,
    #      1596, 1062, 974, 819, 768, 537, 291, 74, 169, 1010, 2209, 1809, 1238, 972, 650, 418, 108, 43, 0, 357, 636, 540,
    #      179, 0, 0, 0, 0]
    #
    # t1 = 0
    # k = []
    # intt = []
    #
    # for i in range(len(y1)):
    #     k.append(t1)
    #     intt.append(float(y1[i]))
    #     t1 = t1 + 5

    ################################################

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax1.plot(t, replicas, '--r',  label='maximum consumption rate')
    # ax1.plot(k, intt,
    #          label="hetereogenous autoscaling lag")

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

   # ax2.set_ylabel('Consumer replicas')

    plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    #ax2.legend(loc=1)

    plt.show()

def oldHeteromulti():


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
            elif math.floor(double(row[0])) < 65:
                replicas.append(244+97)
            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
            elif math.floor(double(row[0])) < 331:
                replicas.append(244+97)
            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
            elif math.floor(double(row[0])) < 450:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 454:
                replicas.append(244 +244+97)
            elif math.floor(double(row[0])) < 507:
                replicas.append(244+244)
            elif math.floor(double(row[0])) < 511:
                replicas.append(244+96+244)
            elif math.floor(double(row[0])) < 524:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
            elif math.floor(double(row[0])) < 559:
                replicas.append(244+96)
            else:
                replicas.append(96)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))


    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    #ax1.plot(t, replicas, '--r',  label='maximum consumption rate')
    ax1.plot(t, replicas, 'r',  label='maximum consumption rate')

    # ax1.plot(k, intt,
    #          label="hetereogenous autoscaling lag")

    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

   # ax2.set_ylabel('Consumer replicas')

    #plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    #ax2.legend(loc=1)

    plt.show()

def oldHeterowithmultilag():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)




    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
            elif math.floor(double(row[0])) < 65:
                replicas.append(244 + 97)
            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
            elif math.floor(double(row[0])) < 331:
                replicas.append(244 + 97)
            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
            elif math.floor(double(row[0])) < 450:
                replicas.append(244 + 96)
            elif math.floor(double(row[0])) < 454:
                replicas.append(244 + 244 + 97)
            elif math.floor(double(row[0])) < 507:
                replicas.append(244 + 244)
            elif math.floor(double(row[0])) < 511:
                replicas.append(244 + 96 + 244)
            elif math.floor(double(row[0])) < 524:
                replicas.append(244 + 96)
            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
            elif math.floor(double(row[0])) < 559:
                replicas.append(244 + 96)
            else:
                replicas.append(96)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))

    #############################################################"
    y1 = [ 0,0,  0, 0, 0, 0, 0, 0, 0, 0, 77, 75, 277, 855, 1094, 692, 246, 54, 0, 73, 82, 68, 81, 94, 175, 190, 93,
         181, 149, 80, 69, 150, 143, 162, 141, 159, 155, 133, 138, 144, 130, 143, 145
        , 146, 151, 154, 63, 168, 175, 191, 189, 205, 219, 240, 403, 235, 248, 264, 258, 262, 264, 267, 189, 100, 0, 0,
         39, 291, 475, 419, 188, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 117,
         113, 261, 133, 5, 191, 504, 1859, 2161,
         1596, 1062, 974, 819, 768, 537, 291, 74, 169, 1010, 2209, 1809, 1238, 972, 650, 418, 108, 43, 0, 357, 636, 540,
         179, 0, 0, 0,0]

    t1 = 0
    k = []
    intt = []

    for i in range(len(y1)):
        k.append(t1)
        intt.append(float(y1[i]))
        t1 = t1 + 5

    ################################################


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    lns1 = ax1.plot(t, lamda, color='blue', label='workload')
    lns2 = ax1.plot(t, replicas, 'r',  label='maximum consumption rate')
    lns3= ax2.plot(k, intt,color= "green",
             label="hetereogenous autoscaling lag")
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)

    ax1.set_xlabel('Time (sec)', font=font, fontsize=12)
    ax1.set_ylabel('Event Arrivals Rate', font=font, fontsize=12)
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Event Lag', font=font, fontsize=12)

    #plt.title('Workload and corresponding consumer instances')
   # ax1.legend()
    #ax2.legend()

    plt.show()


def oldHeteromultireplicas():
    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t = []
    lamda = []
    replicas = []

    replicas100 = []
    replicas250 = []
    replicast= []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
                replicas100.append(1)
                replicas250.append(0)
                #replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])
            elif math.floor(double(row[0])) < 65:
                replicas.append(244+97)
                replicas100.append(1)
                replicas250.append(1)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                #replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 331:
                replicas.append(244+97)
                replicas100.append(1)
                replicas250.append(1)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                #replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 450:
                replicas.append(244+96)
                replicas100.append(1)
                replicas250.append(1)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 454:
                replicas.append(244 +244+97)
                replicas100.append(1)
                replicas250.append(2)
                #replicast.append(3)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 507:
                replicas.append(244+244)
                replicas100.append(0)
                replicas250.append(2)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 511:
                replicas.append(244+96+244)
                replicas100.append(1)
                replicas250.append(2)
                #replicast.append(3)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 524:
                replicas.append(244+96)
                replicas100.append(1)
                replicas250.append(1)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                #replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 559:
                replicas.append(244+96)
                replicas100.append(1)
                replicas250.append(1)
                #replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            else:
                replicas.append(96)
                replicas100.append(1)
                replicas250.append(0)
                #replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])


    # for r in range(len(replicas)):
    #     print(t[r],lamda[r], replicas[r])
    # print(len(replicas))
    # print(len(t))


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    lns1=ax1.plot(t, lamda, color='blue', label='workload')
    #ax1.plot(t, replicas, 'r',  label='maximum consumption rate')
    lns2=ax2.plot(t, replicas100, color='red', label = "replicas of capacity 100 event/sec")
    lns3=ax2.plot(t, replicas250, color ='green', label = "replicas of capacity 250 event/sec")
    lns4=ax2.plot(t, replicast, color = 'brown', label = "total replicas")

    lns = lns1 + lns2 + lns3 +lns4
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)




    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrivals Rate')
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Event Consumer replicas')

    #plt.title('Workload and corresponding consumer instances')
    #ax1.legend()
    #ax2.legend()

    plt.show()

def oldHeterowithlag():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    font = {
            'weight': 'bold',
            'size': 9}

    plt.rc('font', **font)

    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.titlesize'] = 14


    t = []
    lamda = []
    replicas = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
            elif math.floor(double(row[0])) < 331:
                replicas.append(244+97)
            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
            elif math.floor(double(row[0])) < 450:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 507:
                replicas.append(244+244)
            elif math.floor(double(row[0])) < 524:
                replicas.append(244+96)
            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
            else:
                replicas.append(96)

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))

    #############################################################"
    y1 = [   0, 0, 0, 0, 0, 0, 0, 0, 77, 75, 277, 855, 1094, 692, 246, 54, 0, 73, 82, 68, 81, 94, 175, 190, 93,
         181, 149, 80, 69, 150, 143, 162, 141, 159, 155, 133, 138, 144, 130, 143, 145
        , 146, 151, 154, 63, 168, 175, 191, 189, 205, 219, 240, 403, 235, 248, 264, 258, 262, 264, 267, 189, 100, 0, 0,
         39, 291, 475, 419, 188, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 117,
         113, 261, 133, 5, 191, 504, 1859, 2161,
         1596, 1062, 974, 819, 768, 537, 291, 74, 169, 1010, 2209, 1809, 1238, 972, 650, 418, 108, 43, 0, 357, 636, 540,
         179, 0, 0, 0]

    t1 = 0
    k = []
    intt = []

    for i in range(len(y1)):
        k.append(t1)
        intt.append(float(y1[i]))
        t1 = t1 + 5

    ################################################

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(t, lamda, color='blue', label='workload')
    ax1.plot(t, replicas, '--r',  label='maximum consumption rate')
    ax2.plot(k, intt,color= "green",
             label="hetereogenous autoscaling lag")

    ax1.set_xlabel('Time (sec)', font=font, fontsize=12)
    ax1.set_ylabel('Event Arrivals Rate', font=font, fontsize=12)
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

    ax2.set_ylabel('Event Lag', font=font, fontsize=12)

    #plt.title('Workload and corresponding consumer instances')
    ax1.legend()
    ax2.legend(loc=2)

    plt.show()

def lag():
    y= [0,0,0,0,0,0,0,0,0,0,77,75,277,855,1094,692,246,54,0,73,82,68,81,94,175,190,93,181,149,80,69,150,143,162,141,159,155,133,138,144,130,143,145
,146,151,154,63,168,175,191,189,205,219,240,403,235,248,264,258,262,264,267,189,100,0,0,39,291,475,419,188,0,0,0,0,0,0,0,0,0,0,0,0,101,117,
        113,261,133,5,191,504,1859,2161,
        1596,1062,974,819,768,537,291,74,169,1010,2209,1809,1238,972,650,418,108,43,0,357,636,540,179,0,0,0,0]

    t = 0
    k = []
    intt = []
    inttunaware = []

    for i in range(len(y)):
        k.append(t)
        intt.append(float(y[i]))
        t = t + 5

    plt.plot(k, intt,
             label="hetereogenous autoscaling lag")


    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events lag')
    plt.title('Events lag during autoscaling')
    # plt.grid()
    plt.legend()
    plt.show()

def oldHeteromulti2plots():


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t = []
    lamda = []
    replicas = []
    replicas100 = []
    replicas250 = []
    replicast = []

    with open('defaultArrivalRatesm1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(math.floor(double(row[0])))
            lamda.append(double(row[1]))
            if math.floor(double(row[0])) < 61:
                replicas.append(97)
                replicas100.append(1)
                replicas250.append(0)
                # replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])
            elif math.floor(double(row[0])) < 65:
                replicas.append(244 + 97)
                replicas100.append(1)
                replicas250.append(1)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 267:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                # replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 331:
                replicas.append(244 + 97)
                replicas100.append(1)
                replicas250.append(1)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 428:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                # replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 450:
                replicas.append(244 + 96)
                replicas100.append(1)
                replicas250.append(1)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 454:
                replicas.append(244 + 244 + 97)
                replicas100.append(1)
                replicas250.append(2)
                # replicast.append(3)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 507:
                replicas.append(244 + 244)
                replicas100.append(0)
                replicas250.append(2)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 511:
                replicas.append(244 + 96 + 244)
                replicas100.append(1)
                replicas250.append(2)
                # replicast.append(3)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 524:
                replicas.append(244 + 96)
                replicas100.append(1)
                replicas250.append(1)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 555:
                replicas.append(244)
                replicas100.append(0)
                replicas250.append(1)
                # replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            elif math.floor(double(row[0])) < 559:
                replicas.append(244 + 96)
                replicas100.append(1)
                replicas250.append(1)
                # replicast.append(2)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

            else:
                replicas.append(96)
                replicas100.append(1)
                replicas250.append(0)
                # replicast.append(1)
                replicast.append(replicas250[math.floor(double(row[0]))] + replicas100[math.floor(double(row[0]))])

    for r in range(len(replicas)):
        print(t[r],lamda[r], replicas[r])
    print(len(replicas))
    print(len(t))

    fig, axs = plt.subplots(2, 1)


    #fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx()
    axs[0].plot(t, lamda, color='blue', label='workload')
    #ax1.plot(t, replicas, '--r',  label='maximum consumption rate')
    axs[0].plot(t, replicas, 'r',  label='maximum consumption rate')

    # ax1.plot(k, intt,
    #          label="hetereogenous autoscaling lag")

    #axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Event Arrivals Rate')
    # ax2.spines['left'].set_color('blue')
    # ax2.spines['right'].set_color('red')

    axs[1].plot(t, replicas100, color='green', label='replicas 100 events/sec')
    # ax1.plot(t, replicas, '--r',  label='maximum consumption rate')
    axs[1].plot(t, replicas250, color = 'brown', label='replicas 250 events/sec')

    axs[1].set_ylabel('Consumer replicas')
    axs[1].set_xlabel('Time (sec)')


   # ax2.set_ylabel('Consumer replicas')

    #plt.title('Workload and corresponding consumer instances')
    axs[0].legend()
    axs[1].legend()

    #ax2.legend(loc=1)

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #oldHetero1()
    #oldHeterowithlag()
    #oldHetero2()



    ################################################
    # oldHeteromulti()
    # oldHeterowithmultilag()
    # oldHeteromultireplicas()

    oldHeteromulti2plots()

    ###################################################
    #lag()

