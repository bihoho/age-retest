drive = input('請問你有沒有開過車:')
if drive != '有' and drive != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
age = input('請輸入年齡:')
age = int(age)
if drive == '有':
	if age >= 18:
		print('哇，那你有駕照嗎')
	else:
		print('哦，身分證字號交出來')
elif drive == '沒有':
	if age >= 18: 
		print('你可以考駕照了哦')
	else:
		print('再等幾年就可以考駕照了哦!')

