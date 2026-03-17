# 파일이름 :
# 작 성 자 : 60261941 박성원
name1 = input("이름을 입력하시오: ")
writing1 = int(input("당신의 글쓰기 점수를 입력하시오: "))
python1 = int(input("당신의 파이썬 점수를 입력하시오: "))
last_avg1 = float(input("당신의 지낙학기 평균을 입력하시오: "))
sum = writing1 + python1
average1 = sum / 2
print(f"{name1} 학생의 글쓰기 점수는 {writing1}, 파이썬 점수는 {python1} 입니다")
print(f"평균은 {average1} 이고, 지난 학기와 차이는 {average1 - last_avg1} 입니다.")
