#!./venv/bin/python

def main():
    gen = ((x,y) for x in range(-1, 2) for y in range(-1, 2) if not (x ==0 and y == 0))
    
    for (rowoffs,coloffs) in gen:
        print(rowoffs, coloffs)

if __name__ == "__main__":  
    main()
