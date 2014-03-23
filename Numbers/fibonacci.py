def fibonacci(n):
    series = [1]
    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    return series

def main():
    n = int(raw_input('How many numbers do you need? '))
    fibb = fibonacci(n)
    print fibb

if __name__ == '__main__':
    main()
