# Given list of students and grades. Print two second dummest
# Use 4_test.txt

if __name__ == '__main__':
    scores = list()
    for _ in range(int(input())):
        name = input()
        sc = float(input())
        scores.append([name, sc])

    set_scores = {sc[1] for sc in scores}
    list_scores = sorted(list(set_scores))
    min_score = list_scores[1]

    for x in sorted(scores):
        if x[1] == min_score:
            print(x[0])
    