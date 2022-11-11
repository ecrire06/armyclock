# 짭 군돌이(armyclock)
# 일단 육군 기준으로 만들고, 다 만들면 육군/해군/공군 선택 구현하기

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

input = sys.stdin.readline


# 현재 시각
current_time = datetime.now()

# 현재일
today_date = format(current_time, '%Y-%m-%d')

# 입대일
s_year, s_month, s_day = map(int, input().split())
start_date = datetime(s_year, s_month, s_day)

# 전역일
end_date = start_date + relativedelta(months = 18) - relativedelta(days = 1)
print("전역일: {}".format(end_date))

# 계급 별 진급시기
grade_1 = start_date
grade_2 = (grade_1 + relativedelta(months = 3)).replace(day = 1) # 매월 1일에 진급하니까!
grade_3 = grade_2 + relativedelta(months = 6)
grade_4 = grade_3 + relativedelta(months = 6)

print("일병 진급: {}".format(grade_2))
print("상병 진급: {}".format(grade_3))
print("병장 진급: {}".format(grade_4))
