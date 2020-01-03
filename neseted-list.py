if __name__ == '__main__':
    finalist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        finalist.append([name,score])
    second_min = sorted(list(set([y for x,y in finalist])))[1]
    print("\n".join(sorted([name for name,score in finalist if score == second_min])))
