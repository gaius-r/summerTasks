window.onload = () => {
    document.getElementsByClassName("input")[0].focus();
};
const cmdhistory = [];
var pos = 0;
var cmd = '';
function readInput(el, e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        cmd = el.value;
        cmdhistory.push(cmd);
        dockercon(cmd)
        pos = cmdhistory.length;
    }

    else if (e.keyCode == 38 && cmdhistory.length) {
        e.preventDefault();
        temp =  (pos - 1)%(cmdhistory.length);
        pos = (temp < 0)? 0 : temp;   
        cmd = cmdhistory[pos];
        el.value = cmd;
    }

    else if (e.keyCode == 40 && cmdhistory.length) {
        e.preventDefault();
        temp = (pos + 1)%(cmdhistory.length);
        pos = (temp == 0)? cmdhistory.length-1 : temp;
        cmd = cmdhistory[pos];
        el.value = cmd;
    }
}

function dockercon(cmd) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://192.168.0.132/cgi-bin/docker-cgi.py?cmd="+cmd, true);
    xhr.send();
    xhr.onload = () => {
        response = xhr.responseText;
        output = document.getElementsByClassName("output")[0]
        output.innerHTML = response;
    }
}