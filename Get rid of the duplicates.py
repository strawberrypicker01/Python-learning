student_data = {'idi1': {'name':['Sara'],'class':}'['V'],'subject':['English, Math, Science']},
'idi2': {'name':['Sara'],'class':}'['V'],'subject':['English, Math, Science']},
'idi3': {'name':['Sara'],'class':}'['V'],'subject':['English, Math, Science']},
'idi4': {'name':['Sara'],'class':}'['V'],'subject':['English, Math, Science']},
}
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)