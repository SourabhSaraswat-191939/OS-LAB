def findWaitingTime(n, bt, wt):
	wt[0] = 0
	print(bt)
	for i in range(1, n):
		wt[i] = bt[i - 1][1] + wt[i - 1] - bt[i-1][0]


def findTurnAroundTime(n,bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i][1] + wt[i]


def findAllProcessTime(n, bt):
	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0
	findWaitingTime(n, bt, wt)
	findTurnAroundTime(n,bt, wt, tat)
	print( "Processes  Arrival time  Burst time " +
				" Waiting time " +
				" Turn around time")


	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t|" +str(bt[i][0]) + "\t\t|" +str(bt[i][1]) + "\t |" +str(wt[i]) + "\t\t |" +str(tat[i]))


n = int(input("Enter Number of processes => "))

print("Enter burst time for each process")
burst_time = []
for i in range(n):
	arrival_burst = tuple(map(int,input().split()))
	burst_time.append(arrival_burst)

burst_time.sort()
findAllProcessTime(n,burst_time)