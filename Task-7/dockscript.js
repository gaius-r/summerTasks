window.onload = () => {
    document.getElementsByClassName("input")[0].focus();
};

function readInput(el, e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        cmd = 'docker ' + el.value;
        console.log(cmd);
        el.blur()
    }
}

function dockercon() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://192.168.0.132/cgi-bin/sample.py", false);
    xhr.send();
    response = xhr.responseText;
    output = document.getElementsByClassName("output")[0]
    output.innerHTML = "> Hello world";
}