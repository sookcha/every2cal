let sessionParser = require('express-session');

function getTableXML(userid, password, semester, year) {
    var xmlHttp = new XMLHttpRequest()
    var payForm = new FormData();
    var semesForm = new FormData();
    var tabelFrom = new FormData();

    console.log("Call getTableXML function")

    xmlHttp.onreadystatechange = function () {
      if (this.status === 200 && this.readyState === this.DONE) {
        console.log(xmlHttp.responseText)
      }
    }

    // xmlHttp.open('CONNECT','https://everytime.kr', true)

    xmlHttp.open('POST', 'https://everytime.kr/user/login', true)
    payForm.append('userid', userid);
    payForm.append('password', password);
    payForm.append('redirect', '/');
    console.debug(document.cookie)
    xmlHttp.send(payForm)

    xmlHttp.open('POST', 'https://api.everytime.kr/find/timetable/table/list/semester', true)
    semesForm.append('semester', semester);
    semesForm.append('year', year);
    xmlHttp.send(semesForm)

    // xmlHttp.open('POST', 'https://api.everytime.kr/find/timetable/table', true)
    // tabelFrom.append()
    // xmlHttp.send(tabelFrom)

}
