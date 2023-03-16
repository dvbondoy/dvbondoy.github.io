function setVal(){
    const d = new Date();
    var str = d.toISOString().slice(0, -14)
    var url = 'https://sourceforge.net/projects/flickos/files/stats/json?start_date=2023-03-08&end_date='+str;
    
    const stat = fetch(url)
        .then((response) => response.json())
        .then((json) => {
            return json;
        });
    
    const status = () => {
        stat.then((a) => {
            document.getElementById("total").innerHTML = a.total;
        });
    }
    
    status();
}

window.onload = function() {
    setVal();
}


