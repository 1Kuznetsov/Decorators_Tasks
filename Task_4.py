import json


# data = json.loads(input())
data = [('ptr', 4), ('lst', 2), ('num', 10), ('int', 5)]

data.sort(key=lambda x: x[1], reverse=True)

print(data)
