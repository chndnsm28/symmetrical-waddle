import students,pickle

studs = [students.Students(10,'chandan','CSE'),students.Students(13,'Ashish','CSE')]

with open('student.data', 'wb') as f:
    for s in studs:
        pickle.dump(s,f)


