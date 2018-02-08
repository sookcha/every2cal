# Every2Cal

![](https://i.imgur.com/O098TZc.png)

Every2Cal은 Everytime 시간표를 .ics 형식으로 내보내주는 Python 프로그램입니다.

Everytime 앱 보다 캘린더로 일정을 관리하는게 편한 마음에 항상 Everytime 시간표를 수기로 캘린더에 적곤 했습니다.
 
그 수고로움을 덜고자 개발했습니다

## 어떻게 사용하나요?

`python every2cal.py --xml 에브리타임 시간표 XML 파일 경로 --begin 학기가 시작하는 날짜 --end 학기가 끝나는 날짜`

로 사용합니다.

Every2Cal은 Everytime 내부의 AJAX로 불러와지는 .xml 형식 시간표를 활용하고 있습니다.

추후에 이미지 기반 시간표 읽어오기도 지원 예정입니다.

# License

Copyright 2018 Hoseong Son

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.