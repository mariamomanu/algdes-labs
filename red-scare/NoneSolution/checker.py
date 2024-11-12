import difflib

#this file was used to compare results while running two different versions of code

# Load the files
with open('./NoneSolution/answer.txt', 'r') as file1, open('./NoneSolution/answers.txt', 'r') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
i = 0
# Compare the files and get the differences
diff = difflib.unified_diff(
    file1_lines, 
    file2_lines, 
    fromfile='answer.txt', 
    tofile='answers.txt', 
    lineterm=''

)
i = 0
# Print the differences
for line in diff:
    i+=1
    print(line)

print(i)
