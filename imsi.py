data = {}
data['영희'] = (80, 95, 90)
data['철수'] = (90, 80, 70)
data['혜영'] = (70, 100, 90)
print(data) # sorted(data.items(), key=lambda x: x[1][0], reverse=False) # sort(1, 2, 3) --> 1 번째 iteratable 파라미터가 하나씩 2번째 수식에 대입되어 돌아 간다. # key=lambda x: x[0] 은 key 로 소팅을 의미 x[1] 은 데이터를 의미 x[1][0] 은 데이터 중에 0번째 항목 print('tuple 의 1번째 항목으로 소팅') data2 = sorted(data.items(), key=lambda x: x[1][0], reverse=False) print(data2)

print('tuple 의 1번째 항목으로 소팅')
data2 = sorted(data.items(), key=lambda x: x[1][0], reverse=False)
print(data2)

