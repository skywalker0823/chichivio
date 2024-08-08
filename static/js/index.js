// console.log when DOM ready
let login_status = {ok: false};
let notification = document.getElementById('notifi');



document.addEventListener('DOMContentLoaded', async() => {
    document.getElementById("get_color_btn").click();
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
    login_display_control({ok: false, msg:"Login failed"});
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
    login_status = {ok: false,msg: "You are not logged in"};
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
        // status = await auto_login_status_check();
        // login_display_control(status);
        return;
    }
    console.log("register_error");
    
}

// document.getElementById('signup_btn').addEventListener('click', () => {
//     alert("Not available yet")
// });


document.getElementById('get_color_btn').addEventListener('click', () => {
    let wrapper = document.getElementById("wrapper")
    cube_total = 5;
    console.log("GET")
    for(let number = 1; number <= cube_total; number++){
        color = colorGenerator()
        document.getElementById("cube_"+number).style.backgroundColor = color
        document.getElementById("cube_"+number+"_color").innerHTML = color
        contrastColor = getContrast(color)
        document.getElementById("cube_"+number+"_color").style.color = contrastColor
    }
    wrapper.style.backgroundColor = "#f6f3ed";
});


// Random hex color code generator
const colorGenerator = () => {
    const letters = '0123456789ABCDEF' ;
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

const getContrast = (hexColor) => {
    hexColor = hexColor.replace("#", "");
  
    const r = parseInt(hexColor.substr(0, 2), 16);
    const g = parseInt(hexColor.substr(2, 2), 16);
    const b = parseInt(hexColor.substr(4, 2), 16);
  
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
  
    const contrastColor = brightness > 128 ? "#000000" : "#FFFFFF";
    console.log(contrastColor);
  
    return contrastColor;
};
  
const copied = (cube_id) => {
    let wrapper = document.getElementById("wrapper")
    let = document.getElementById("color_copy")
    let cube = document.getElementById(cube_id)
    // copy the color of this block
    let color = document.getElementById(cube_id+"_color").innerHTML;
    navigator.clipboard.writeText(color);
    color_copy.innerHTML = "Color copied!";

    // 點按複製之後 變化方塊
    cube.style.backgroundColor = "lightgray";
    // cube.style.transition = "0.5s";
    // cube.style.height = "120px";
    // cube.style.width = "120px";
    setTimeout(() => {
        cube.style.backgroundColor = current_cube_color;
        // cube.style.height = "100px";
        // cube.style.width = "100px";
    }, 200);


    
    // setTimeout(() => {
    //     color_copy.style.display = "none";
    // }, 2000);
    // wrapper.style.backgroundColor = color
}


const changeBackgroundColor = (cube_id) => {
    console.log("over!")
    current_cube_color = document.getElementById(cube_id+"_color").innerHTML;
    console.log(current_cube_color)
    document.getElementById("title").style.color = current_cube_color
}

const resetBackgroundColor = () => {
    document.getElementById("title").style.color = "black"
}