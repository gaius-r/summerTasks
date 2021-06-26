window.onload = () => {
    document.getElementsByClassName("input")[0].focus();
};

function readInput(el, e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        //cmd = 'docker ' + el.value;
        cmd = el.value;
        console.log(cmd);
        dockercon(cmd)
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