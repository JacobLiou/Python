x = []
y = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x.append([row[i] for row in y for i in range(len(row))])

# 列表推导等同于下面
# result = []
# for row in y:
#     for i in range(len(row)):
#         result.append(row[i])
# x.append(result)

print(x)