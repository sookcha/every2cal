# Every2Cal

[![Build Status](https://travis-ci.com/sookcha/every2cal.svg?branch=master)](https://travis-ci.com/sookcha/every2cal)

![](https://i.imgur.com/O098TZc.png)

Every2Cal은 Everytime 시간표를 .ics 형식으로 내보내주는 Python 프로그램입니다.

Everytime 앱 보다 캘린더로 일정을 관리하는게 편한 마음에 항상 Everytime 시간표를 수기로 캘린더에 적곤 했습니다.
 
그 수고로움을 덜고자 개발했습니다.

## 어떻게 사용하나요?

모바일 에브리타임 앱의 시간표 공유 기능을 이용해서 동작합니다.

![Screenshot_20210911-021511_Everytime](https://user-images.githubusercontent.com/1160378/132894358-ab9aac60-7c1e-4a68-9c65-00fbd6400314.jpg)

1. 사진과 같이 본인이 공유할 시간표의 공개 URL을 가져옵니다
2. 공개 URL은 `https://everytime.kr/@id` 구조입니다. id 부분을 복사합니다.
3. `python every2cal.py --begin 학기가 시작하는 날짜 --end 학기가 끝나는 날짜` 로 프로그램을 실행합니다.
4. 2번 과정에서 만든 id를 붙여넣기 합니다.

내부적으로 해당 URL에 접근해 XML 파일을 읽어서 시간표를 .ics 파일로 변환해주고 있습니다.


## Update notes

이전에는 에브리타임 사이트에 프로그램이 자동으로 로그인해서 세션을 이용해서 시간표를 긁어왔는데요.
에브리타임이 크롤링 방지에 꽤 신경을 쓰시는 것 같아, 공유된 시간표의 id 를 이용해 긁어오는 방식으로
변경되었습니다.


# License

Copyright 2018 Hoseong Son

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
