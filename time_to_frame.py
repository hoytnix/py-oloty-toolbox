time = '38:58'

fps = 30

def main():
    times = [int(n) for n in time.split(':')]
    
    seconds = 0
    seconds += times[0] * 60
    seconds += times[1]

    print(seconds * fps)

if __name__ == '__main__':
    main()