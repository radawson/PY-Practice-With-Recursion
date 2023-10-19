# Write code for algorithm 1 below

def count_down(n):

    # Base case
    if n==0:
        return
    
    # Recursive case
    else:
        print(n)
        count_down(n-1)


if __name__ == "__main__":
    n=8
    count_down(n)