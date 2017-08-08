#Ferdinand Cruz
#One of the Basic Data Type HackerRank problems
#Decided to go with an unorthodox way of solving it just for fun

#First input is how many numbers there are
#Grab next raw input (the numbers) and then sort the array
#each input is split
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    high = 0
    sec = 0
	
#loop for amount of first number input
#Because it's sorted, it's ordered from lowest to highest
#first number becomes current highest
#if the next number isn't a duplicate, it's now the highest;
#last number is now the second highest
for i in range(n):
    if i == 0:
        high = arr[i]
    elif arr[i] != high:
        sec = high
        high = arr[i]

#print second highest
print(sec)