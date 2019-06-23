# Made by SharjeelBaig0508
# A Marksheet Program

def set_subject_marks(subject, max_marks):
	marks = int(input("Enter Obtained Marks for " + subject + " (0 - " + str(max_marks) + ") >>> "))
	if marks <= max_marks:
		subject_obtained_marks.append(marks)
	else:
		subject_obtained_marks.append(max_marks)

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

file_path = "Mark Sheet.txt"
with open(file_path, "w") as f:
	print("+" + "-" * 71 + "+")
	print("|\t\t\t\tMark Sheet Program\t\t\t|")
	print("+" + "-" * 71 + "+")
	student_name = input("Enter Student's name >>> ")
	print()
	student_father = input("Enter Student's Father's name >>> ")
	print()
	print("+" + "-" * 71 +"+")
	total_marks = 550
	subject_total_marks = { 
	"English Compulsory" : 75, 
	"Urdu Compulsory" : 75, 
	"Mathematics Comp." : 75, 
	"Physics Inter XI" : 75, 
	"Chemistry Inter XI" : 75, 
	"Computer Science" : 75, 
	"Pakistan Studies" : 50, 
	"Islamiat Studies" : 50 
	}
	subject_obtained_marks = []
	for subject, marks in subject_total_marks.items():
			set_subject_marks(subject, marks)
			print()
	obtained_marks = sum(subject_obtained_marks)
	f.write("+" + "-" * 71 + "+\n")
	f.write("Student Name : "+ student_name)
	f.write("\nFather Name : "+ student_father)
	f.write("\n+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+\n")
	f.write("|Subject\t\t|Obtained Marks\t|Total Marks\t|Grade\t\t|\n")
	f.write("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+\n")
	index = 0
	for subject, marks in subject_total_marks.items():
			percent = (subject_obtained_marks[index] / marks) * 100
			f.write("|" + subject + "\t|\t" +  str(subject_obtained_marks[index]) + "\t|\t" + str(marks) + "\t|\t" + grader(percent) + "\t|\n")
			index += 1
	f.write("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+\n")
	percentage = (obtained_marks / total_marks) * 100
	f.write("|Total :\t"+ "\t|\t" + str(obtained_marks) + "\t|\t" + str(total_marks) + "\t|\t" + grader(percentage) + "\t|\n")
	f.write("+" + "-" * 23 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+\n")
	if percentage >= 40:
		f.write("Student Passed with " + str(round(percentage, 2)) + " %\n")
	else:
		f.write("Student Failed with " +  str(round(percentage, 2)) + " %\n")
	f.write("Grade : " + grader(percentage))
	f.write("\n+" + "-" * 71 + "+\n")
print("+" + "-" * 71 + "+")
print("Your File", file_path, "has been written")
print("Open it and check your marksheet")
print("+" + "-" * 71 + "+")


