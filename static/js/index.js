// console.log when DOM ready
// let login_status = {ok: false};
let notification = document.getElementById('notifi');



document.addEventListener('DOMContentLoaded', async() => {
    document.getElementById("get_color_btn").click();
    // login_status = await auto_login_status_check();
    // login_display_control(login_status);
    // turn url to root
});



document.getElementById('get_color_btn').addEventListener('click', () => {
    let wrapper = document.getElementById("wrapper")
    cube_total = 5;
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