if __name__ == '__main__':
	student_marks = {}
	for _ in range(int(input())):
		name, *marks = input().split()
		marks = list(map(float,marks))
		student_marks[name]=marks
	query = input()
	print("{:.2f}".format(sum(student_marks[query])/len(student_marks[query])))

