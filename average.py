
k=0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for j in student_marks[query_name]:
        k=k+j
    f=k/3.00
    print('%.2f'%f) 
