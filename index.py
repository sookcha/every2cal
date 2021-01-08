from flask import Flask
from flask import send_file
from flask import request
from flask import render_template

from every2cal import DownCal

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/dwn_cal', methods=['GET', 'POST'])
def dwn_cal():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    user_id = request.args.get('user_id')
    user_password = request.args.get('user_password')

    try:
        cal = DownCal(start_date, end_date, user_id, user_password)
        return send_file(cal,
                        start_date + end_date + 'csv',
                        as_attachment=True)
    except:
        return'''
        <h1>로그인 정보 혹은 시간표 존재 유무를 다시 확인해주세요.</h1>
        '''

    # file_name = f"static/results/file_path.csv"
    # return send_file(file_name,
    #                  mimetype='text/csv',
    #                  attachment_filename='downloaded_file_name.csv',# 다운받아지는 파일 이름. 
    #                  as_attachment=True)

app.run(debug=True, host='0.0.0.0')
