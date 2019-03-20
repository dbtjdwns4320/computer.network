
def main():
 arr = []
 import sys
 count = 1
 sys.argv[1]
 sys.argv[2]
 sys.argv[3]
 for i in range(4,int(len(sys.argv))):
     arr.append(int(sys.argv[i]))
     count = count + 1
 if sys.argv[1] == '-o':
     if sys.argv[2] == 'A':
         if sys.argv[3] =='arr' :
            quick_up(arr,0,count-2)
            for x in arr:
                print(x, end=" ")
     elif sys.argv[2] =='D':
         if sys.argv[3] == 'arr' :
            quick_Down(arr,0,count-2)
            for y in arr:
                print(y, end = " ")
def quick_up(arr,left,right) :
    L = left
    R = right
    box = int((left + right) / 2)
    pivot = arr[box]
    while L <= R:
        while arr[L] < pivot:
            L=L+1
        while arr[R] > pivot:
            R=R-1
        if L <= R:
            if L != R:
                temp = arr[L]
                arr[L] = arr[R]
                arr[R] = temp
            L = L+1
            R = R-1
    if left < R:
        quick_up(arr,left,R)
    if L < right:
        quick_up(arr,L,right)

def quick_Down(arr,left,right) :
    L = int(left)
    R = int(right)
    box = int((left + right) / 2)
    pivot = arr[box]
    while L <= R:
        while arr[L] > pivot:
            L = L+1
        while arr[R] < pivot:
            R = R-1
        if L <= R:
            if L != R:
                temp = arr[L]
                arr[L] = arr[R]
                arr[R] = temp
            L = L+1
            R = R-1
    if left < R:
        quick_Down(arr,left,R)
    if L < right:
        quick_Down(arr,L,right)
main()

