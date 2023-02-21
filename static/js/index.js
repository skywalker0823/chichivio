// console.log when DOM ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM ready');
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
    const response = await fetch('/api/db/login', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("log_in_ok");
        return {ok: true}
    }
    console.log("log_in_error");
    return {error: result.error}
}


logout = async() => {
    const options = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const response = await fetch('/api/db/login', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("log_out_ok");
        return {ok: true}
    }
    console.log("log_out_error");
    return {error: result.error}
}