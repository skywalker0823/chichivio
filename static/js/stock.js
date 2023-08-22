document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed 🚀");
});

document.getElementById("btn_stock").addEventListener("click", async() => {
    let stock = document.getElementById("input_stock").value;
    let info = document.getElementById("info_stock");
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const response = await fetch('/api/stock?stock='+stock, options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("stock_ok");
        console.log(result.data);
        //key-value in to html        
        for(let key in result.data){
            info.innerHTML += key + " : " + result.data[key] + "<br>";
        }
        return;
    }
    console.log("stock_error");
    return;
});