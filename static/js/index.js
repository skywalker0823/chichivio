// console.log when DOM ready
document.addEventListener('DOMContentLoaded', async() => {
    console.log('DOM ready');
    let login_status = await auto_login_status_check();
    login_display_control(login_status);

});

login = async() => {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: username, password: password})
    };
    const response = await fetch('/api/login/', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("log_in_ok");
        login_display_control({ok: true,username: username});
        return;
    }
    console.log("log_in_error");
    login_display_control({ok: false});
}


logout = async() => {
    const options = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const response = await fetch('/api/login/', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("log_out_ok");
        login_display_control({ok: false});
        return;
    }
    console.log("log_out_error, not supposed to happen");
}



auto_login_status_check = async() => {
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const response = await fetch('/api/login/', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("You are already logged in");
        return {ok: true,username: result.username}
    }
    console.log("You are not logged in");
    return {error: result.error}
}

login_display_control = (login_status) => {
    if(login_status.ok){
        document.getElementById('login_container').style.display = 'none';
        document.getElementById('login_message').style.display = 'block';
        document.getElementById('login_message').innerHTML = "Hello, " + login_status.username;
    }else{
        document.getElementById('login_container').style.display = 'block';
        document.getElementById('login_message').style.display = 'none';
    }
}