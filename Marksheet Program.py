# Made by SharjeelBaig0508
# A Marksheet Program

print("+" + "-" * 63 + "+")
print("|\t\t\tMark Sheet Program\t\t\t|")
print("+" + "-" * 63 + "+")

student_name = input("Enter Student's name >>> ")
print()

student_father = input("Enter Student's Father's name >>> ")
print()

print("+" + "-" * 63 +"+")
total_marks = 550

subject_total_marks = { 
	"English" : 75, 
	"Urdu" : 75, 
	"Maths" : 75, 
	"Physics" : 75, 
	"Chemistry" : 75, 
	"Computer" : 75, 
	"Pakistan Studies" : 50, 
	"Islamiat" : 50 
}

subject_obtained_marks = []

def set_subject_marks(subject, max_marks):
	marks = int(input("Enter Obtained Marks for " + subject + " (0 - " + str(max_marks) + ") >>> "))
	if marks <= max_marks:
		subject_obtained_marks.append(marks)
	else:
		subject_obtained_marks.append(max_marks)

for subject, marks in subject_total_marks.items():
	set_subject_marks(subject, marks)
	print()

obtained_marks = sum(subject_obtained_marks)

print("+" + "-" * 63 + "+")
print("Student Name :", student_name)
print("Father Name :", student_father)
print("+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")
print("|Subject\t|Obtained Marks\t|Total Marks\t|")
print("+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")
index = 0
for subject, marks in subject_total_marks.items():
	print("|" + subject[0 : 6] + "\t", subject_obtained_marks[index], marks, sep = "\t|\t", end = "\t|\n")
	index += 1
print("+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+")
print("Total Obtained Marks :", obtained_marks)
percentage = (obtained_marks / total_marks) * 100
if percentage >= 40:
	print("Student Passed with", percentage,"%")
else:
	print("Student Failed with", percentage, "%")
def grader(perc):
	if perc <= 100 and perc >= 90:
		return "A+"
	elif perc < 90 and perc >= 80:
		return "A"
	elif perc < 80 and perc >= 70:
		return "B"
	elif perc < 70 and perc >= 60:
		return "C"
	elif perc < 60 and perc >= 50:
		return "D"
	elif perc < 50 and perc >= 40:
		return "E"
	else:
		return "F"

print("Grade :", grader(percentage))
print("+" + "-" * 63 + "+")

