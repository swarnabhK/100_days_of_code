# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height+=height
average_height = total_height/len(student_heights)
print(int(round(average_height,0)))