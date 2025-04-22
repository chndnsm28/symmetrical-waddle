import students,pickle


with open('student.data', 'rb') as f:
    for i in range(2):
        s = pickle.load(f)
        s.display()