def avg_marks_from_list(marks):
    if len(marks) == 0:
        return 0
    
    avg = sum(marks) / len(marks)
    return avg

marks = [85, 90, 78, 92, 88]
print("The Average marks is ", avg_marks_from_list(marks))