// console.log when DOM ready
let login_status = {ok: false};

document.addEventListener('DOMContentLoaded', async() => {
    console.log('DOM ready');
    login_status = await auto_login_status_check();
    login_display_control(login_status);
    // turn url to root
});

login = async() => {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    if(username == "" || password == ""){
        console.log("log_in_error, empty username or password");
        return;
    }
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
        login_status = {ok: true,username: username};
        console.log("log_in_ok");
        login_display_control(login_status);
        return;
    }
    console.log("log_in_error");
    login_display_control({ok: false});
}

logout = async() => {
    console.log(login_status);
    if(login_status.ok == false){
        console.log("log_out_error, not logged in");
        return;
    }
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
        login_status = {ok: false};
        console.log(login_status);
        login_display_control(login_status);
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
        login_status = {ok: true,username: result.username};
        return {ok: true,username: result.username}
    }
    console.log("You are not logged in");
    login_status = {ok: false};
    console.log(login_status);
    return login_status;
}

login_display_control = (login_status) => {
    let login_container = document.getElementById('login_container');
    let login_message = document.getElementById('login_message');
    let logout_btn = document.getElementById('logout_btn');
    if(login_status.ok == true){
        login_container.style.display = 'none';
        login_message.style.display = 'block';
        login_message.innerHTML = "Hello, " + login_status.username;
        logout_btn.style.display = 'block';
    }else{
        login_container.style.display = 'block';
        login_message.style.display = 'none';
        logout_btn.style.display = 'none';
        window.location.href="/"
    }
}

register = async() => {
    console.log("register");
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    if(username == "" || password == ""){
        console.log("register_error, empty username or password");
        return;
    }
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: username, password: password})
    };
    const response = await fetch('/api/signup/', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("register_ok");
        return;
    }
    console.log("register_error");
    
}

// document.getElementById('signup_btn').addEventListener('click', () => {
//     alert("Not available yet")
// });