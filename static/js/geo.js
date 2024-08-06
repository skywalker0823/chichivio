let current_ans
let name

const countyTranslations = {
    "Taipei City": "台北市",
    "New Taipei City": "新北市",
    "Taoyuan City": "桃園市",
    "Taichung City": "台中市",
    "Tainan City": "台南市",
    "Kaohsiung City": "高雄市",
    "Keelung City": "基隆市",
    "Hsinchu City": "新竹市",
    "Chiayi City": "嘉義市",
    "Hsinchu County": "新竹縣",
    "Miaoli County": "苗栗縣",
    "Changhua County": "彰化縣",
    "Nantou County": "南投縣",
    "Yunlin County": "雲林縣",
    "Chiayi County": "嘉義縣",
    "Pingtung County": "屏東縣",
    "Yilan County": "宜蘭縣",
    "Hualien County": "花蓮縣",
    "Taitung County": "台東縣",
    "Penghu County": "澎湖縣",
    "Kinmen County": "金門縣",
    "Lienchiang County": "連江縣"
};


document.addEventListener("DOMContentLoaded", async() => {
    button_generate();
});

get_img = async() => {
    current_ans = null;
    name = null;
    // delete old images
    display_area = document.getElementById("display_area")
    display_area.innerHTML = "";

    console.log("try get img")
    const response = await fetch('/api/geo');
    const result = await response.json();
    console.log(result);

    current_ans = result.ans;
    name = result.name;

    // post img
    const img = document.createElement('img');
    img.src = result.photo_url; // 设置图片的 URL
    img.alt = 'Loaded from photo_url';
    display_area.appendChild(img);
    console.log("done")
}

check_ans = async(county) => {
    console.log("正確答案:",current_ans);
    console.log("使用者答案",county);
    if (current_ans == null) {
        alert("請先請求圖片");
        return;
    }

    if(current_ans in countyTranslations){
        console.log("in! start translation",current_ans,county)
        current_ans = countyTranslations[current_ans];
        console.log("done translation", current_ans)
    }
    

    let user_ans = county;

    if (user_ans == current_ans) {
        alert("正確! 這裡是: "+ current_ans + "的 " + name);
        await get_img();
    } else {
        alert("錯了~ 正確答案是: " + current_ans);
    }
}



button_generate = async() => {
    const counties = [
        "台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市", 
        "基隆市", "新竹市", "嘉義市", "新竹縣", "苗栗縣", "彰化縣", 
        "南投縣", "雲林縣", "嘉義縣", "屏東縣", "宜蘭縣", "花蓮縣", 
        "台東縣", "澎湖縣", "金門縣", "連江縣"
    ];

    const buttonsContainer = document.getElementById('county_buttons');

    counties.forEach(county => {
        const button = document.createElement('button');
        button.innerText = county;
        button.onclick = () => check_ans(county);
        buttonsContainer.appendChild(button);
    });

}