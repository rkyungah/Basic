#전체가 정렬되지 않은 키와 값의 쌍으로 구성


bans = { '잎새반':'찬영이',
         '열매반':'예영이',
         '햇살반':'준영이',
         '열매반':'채영이', }

print(type(bans))
print('반의수 : ', len(bans))      #키 값은 중복되지 않는 유일한 값

# 읽기
print('잎새반 : ', bans['잎새반'])
print('열매반 : ', bans['열매반'])
print('bans 읽기 :', bans)

# 추가
bans['꽃잎반'] = '희영이'
print('bans 추가 :', bans)

# 변경
bans['잎새반'] = '서영이'     #이미 존재하는 값은 변경이 되고, 없는 값은 추가가 된다.
print('bans 변경 :', bans)

# 삭제 del
del bans['잎새반']
print('bans 삭제 :', bans)

del bans['햇살반']
print('bans 삭제2: ', bans)

bans['튤립반'] = '라헬이'
print('bans 추가2: ', bans)


