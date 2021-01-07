from flask import Flask
from flask import send_file

from every2cal import DownCal

app = Flask(__name__)

@app.route("/file_download")
def hello():
    return '''
    <a href="/dwn_cal">Click me.</a>
    
    <form method="get" action="dwn_cal">
        <button type="submit">Download!</button>
    </form>
    '''


@app.route('/dwn_cal')
def dwn_cal():
    try:
        DownCal()
        # print("test")
    except:
        return'''
        <h1>로그인 정보 혹은 시간표 존재 유무를 다시 확인해주세요.</h1>
        '''

    # file_name = f"static/results/file_path.csv"
    # return send_file(file_name,
    #                  mimetype='text/csv',
    #                  attachment_filename='downloaded_file_name.csv',# 다운받아지는 파일 이름. 
    #                  as_attachment=True)

app.run(debug=True)
