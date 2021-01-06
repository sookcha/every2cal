# Every2Cal

[![Build Status](https://travis-ci.com/sookcha/every2cal.svg?branch=master)](https://travis-ci.com/sookcha/every2cal)

![](https://i.imgur.com/O098TZc.png)

Every2Cal은 Everytime 시간표를 .ics 형식으로 내보내주는 Python 프로그램입니다.

Everytime 앱 보다 캘린더로 일정을 관리하는게 편한 마음에 항상 Everytime 시간표를 수기로 캘린더에 적곤 했습니다.
 
그 수고로움을 덜고자 개발했습니다.

## 어떻게 사용하나요?

`python every2cal.py --begin 학기가 시작하는 날짜 --end 학기가 끝나는 날짜`

로 사용합니다.

Every2Cal은 Everytime 내부의 AJAX로 불러와지는 .xml 형식 시간표를 활용하고 있습니다.

추후에 이미지 기반 시간표 읽어오기도 지원 예정입니다.
