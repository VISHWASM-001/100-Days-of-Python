def gradingStudents(grades):
    ans = []

    for grade in grades:
        if grade < 38:
            ans.append(grade)

        else:
            nextmultiple = 0

            for i in range(grade, grade + 5):
                if i % 5 == 0:
                    nextmultiple = i
                    break

            if nextmultiple - grade < 3:
                ans.append(nextmultiple)
            else:
                ans.append(grade)

    return ans

# approach 2 : simply adding the remainder
def gradingStudents(grades):
    ans = []

    for grade in grades:
        if grade < 38:
            ans.append(grade)
        else:
            remainder = grade % 5

            if remainder >= 3:
                grade += 5 - remainder

            ans.append(grade)

    return ans
