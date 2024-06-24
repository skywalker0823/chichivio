let container = document.querySelector("#container");
let inputField = document.querySelector("#input-field");
let leftArrow = document.querySelector("#left");
let rightArrow = document.querySelector("#right");
let lowTemp = document.querySelector("#temp-low");
let highTemp = document.querySelector("#temp-high");
let comfort = document.querySelector("#comfort");
let weatherStatus = document.querySelector("#status");
let rainStatus = document.querySelector("#rain-status-value");

let warmIcon = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/24.svg";
let sunnyIcon = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/27.svg";
let cloudyIcon = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/28.svg";
let rainyIcon = "https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/12.svg"
function iconUrl(weatherStatus) {
    return `https://www.cwa.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/${weatherStatus}.svg`
}

let enMonth={
    1:"JAN",
    2:"FEB",
    3:"MAR",
    4:"APR",
    5:"MAY",
    6:"JUN",
    7:"JUL",
    8:"AUG",
    9:"SEP",
    10:"OCT",
    11:"NOV",
    12:"DEC"
}

let background={
    sunny:"https://i.pinimg.com/originals/f8/42/6b/f8426bf4f6892dfed16b2e0f583d5670.gif",
    cloudy:"./img/cloudy.gif",
    rainy:"https://archive.org/download/ezgifresize1/ezgif%20resize1.gif"
}

let date;
let month;
let day;
// 抓現在時間
function getDate() {
    date = new Date();
    month=date.getMonth()+1;
    day=date.getDate();
    document.querySelector("#month").innerHTML=enMonth[month];
    document.querySelector("#day").innerHTML=day;
}

// 抓明天時間
function getTomorrow() {
    let tomorrow = new Date(date);
    tomorrow.setDate(tomorrow.getDate() + 1)
    let tomorrowMonth=tomorrow.getMonth()+1;
    let tomorrowDay=tomorrow.getDate();
    document.querySelector("#month").innerHTML=enMonth[tomorrowMonth];
    document.querySelector("#day").innerHTML=tomorrowDay;
}

// 顯示對應的背景
function showBackground(wxParameterValue) {
    if(wxParameterValue == "1" || wxParameterValue == "2" || wxParameterValue == "24" || wxParameterValue == "25"){
        container.style.backgroundImage="url("+background["sunny"]+")";
    }
    else if(wxParameterValue == "3" || wxParameterValue == "4" || wxParameterValue == "5" || wxParameterValue == "6" || wxParameterValue == "7"
    || wxParameterValue == "26" || wxParameterValue == "27" || wxParameterValue == "28"){
        container.style.backgroundImage="url("+background["cloudy"]+")";
    }
    else{
        container.style.backgroundImage="url("+background["rainy"]+")";
    }
}

// 顯示天氣狀況圖示
function showWeatherIcon(wxParameterValue) {
    if(wxParameterValue == "1"){
        document.querySelector("#weather-icon").src=warmIcon
    }
    else if(wxParameterValue == "2" ||wxParameterValue == "3"){
        document.querySelector("#weather-icon").src=sunnyIcon
    }
    else if(wxParameterValue == "4" || wxParameterValue == "5" || wxParameterValue == "6" || wxParameterValue == "7" ){
        document.querySelector("#weather-icon").src=cloudyIcon
    }
    else if(wxParameterValue == "8" || wxParameterValue == "9"){
        document.querySelector("#weather-icon").src=rainyIcon
    }
    else{
        let icon = iconUrl(wxParameterValue)
        document.querySelector("#weather-icon").src=icon
    }
}

// render 畫面
function render(location, wxParameterName, wxParameterValue, popParameterName, mintParameterName, maxtParameterName, ciParameterName) {
    //地點
    document.querySelector("#place").innerHTML=location;
    //天氣現象
    weatherStatus.innerHTML=wxParameterName;
    //天氣現象圖示
    showWeatherIcon(wxParameterValue);
    // 降雨機率
    rainStatus.innerHTML=popParameterName;
    //最低溫
    lowTemp.innerHTML=mintParameterName;
    //最高溫
    highTemp.innerHTML=maxtParameterName;
    //舒適度
    comfort.innerHTML=ciParameterName;
    //背景圖
    showBackground(wxParameterValue);
}

/** fetch weather API  section  */
async function fetchWeather(county){
    const API_KEY = "CWB-2C0F8651-AA53-49B4-9F2D-7E7A3A3B1307";
    const url = `https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=${API_KEY}&locationName=${county}`
    try{
        let response = await fetch(url); 
        if(response.ok){
            let weatherData = await response.json();
            return weatherData;
        }else{
            throw "weather fetching fail";
        };                              
    }catch(error){
        console.log(error)
    };
};

//查看明天天氣
function goAfter(location, wxParameterNameAfter18, wxParameterValueAfter18, popParameterNameAfter18, mintParameterNameAfter18, maxtParameterNameAfter18, ciParameterNameAfter18, wxParameterNameBefore18, wxParameterValueBefore18, popParameterNameBefore18, mintParameterNameBefore18, maxtParameterNameBefore18, ciParameterNameBefore18){
    //讓右邊箭頭disabled
    rightArrow.setAttribute("class","disabled");
    leftArrow.removeAttribute("class","disabled");

    //顯示明天日期
    getTomorrow();
    
    //若現在時間是18:00後
    if (date.getHours() >= 18){
        render(location, wxParameterNameAfter18, wxParameterValueAfter18, popParameterNameAfter18, mintParameterNameAfter18, maxtParameterNameAfter18, ciParameterNameAfter18)
    }else{
        //若現在時間在18:00前
        render(location, wxParameterNameBefore18, wxParameterValueBefore18, popParameterNameBefore18, mintParameterNameBefore18, maxtParameterNameBefore18, ciParameterNameBefore18)
    }
}

//回去看今天天氣
function goBefore(location, wxParameterNameToday, wxParameterValueToday, popParameterNameToday, mintParameterNameToday, maxtParameterNameToday, ciParameterNameToday){
    //讓左邊箭頭disabled
    leftArrow.setAttribute("class","disabled");
    rightArrow.removeAttribute("class","disabled");
    //顯示明天日期
    document.querySelector("#day").innerHTML=day;
    render(location, wxParameterNameToday, wxParameterValueToday, popParameterNameToday, mintParameterNameToday, maxtParameterNameToday, ciParameterNameToday);
}

//抓使用者搜尋的縣市
function getSearchText(){
    let searchText=inputField.value;
    fetchWeather(searchText)
    .then((weatherData)=>{
    /**這邊做資料處理&畫面render*/
        //地點
        let location = weatherData.records.location[0].locationName;

        //資料類型有五種
        let wx = weatherData.records.location[0].weatherElement[0];
        let pop = weatherData.records.location[0].weatherElement[1];
        let mint = weatherData.records.location[0].weatherElement[2];
        let ci = weatherData.records.location[0].weatherElement[3];
        let maxt = weatherData.records.location[0].weatherElement[4];

        //Wx section 天氣現象
        //time1 今日18:00~隔日06:00
        //Wx-parameterName1
        let wxParameterName1 = wx.time[0].parameter.parameterName;
        //Wx-parameterValue1
        let wxParameterValue1=wx.time[0].parameter.parameterValue;

        //time2 隔日06:00~隔日18:00
        //Wx-parameterName2
        let wxParameterName2 = wx.time[1].parameter.parameterName;
        //Wx-parameterValue2
        let wxParameterValue2 = wx.time[1].parameter.parameterValue;

        //time3 隔日18:00~後天06:00
        //Wx-parameterName3
        let wxParameterName3 = wx.time[2].parameter.parameterName;
        //Wx-parameterValue3
        let wxParameterValue3 = wx.time[2].parameter.parameterValue;


        //PoP section 降雨機率 
        //time1 今日18:00~隔日06:00
        //pop-parameterName1 (unit:%)
        let popParameterName1 = pop.time[0].parameter.parameterName;

        //time2 隔日06:00~隔日18:00
        //pop-parameterName2 (unit:%)
        let popParameterName2 = pop.time[1].parameter.parameterName;

        //time3 隔日18:00~後天06:00
        //pop-parameterName3 (unit:%)
        let popParameterName3 = pop.time[2].parameter.parameterName;


        //MinT section 最低溫度
        //time1 今日18:00~隔日06:00
        //mint-parameterName1 (unit:℃)
        let mintParameterName1 = mint.time[0].parameter.parameterName;

        //time2 隔日06:00~隔日18:00
        //mint-parameterName2 (unit:℃)
        let mintParameterName2 = mint.time[1].parameter.parameterName;

        //time3 隔日18:00~後天06:00
        //mint-parameterName3 (unit:℃)
        let mintParameterName3 = mint.time[2].parameter.parameterName;


        //MaxT section 最高溫度
        //time1 今日18:00~隔日06:00
        //maxt-parameterName1 (unit:℃)
        let maxtParameterName1 = maxt.time[0].parameter.parameterName;

        //time2 隔日06:00~隔日18:00
        //maxt-parameterName2 (unit:℃)
        let maxtParameterName2 = maxt.time[1].parameter.parameterName;

        //time3 隔日18:00~後天06:00
        //maxt-parameterName3 (unit:℃)
        let maxtParameterName3 = maxt.time[2].parameter.parameterName;


        //CI section 舒適度
        //time1 今日18:00~隔日06:00
        //ci-parameterName1
        let ciParameterName1 = ci.time[0].parameter.parameterName;

        //time2 隔日06:00~隔日18:00
        //ci-parameterName2
        let ciParameterName2 = ci.time[1].parameter.parameterName;

        //time3 隔日18:00~後天06:00
        //ci-parameterName3
        let ciParameterName3 = ci.time[2].parameter.parameterName;

        //畫面render
        render(location, wxParameterName1, wxParameterValue1, popParameterName1, mintParameterName1, maxtParameterName1, ciParameterName1);     

        //查看明天天氣
        rightArrow.addEventListener("click", () => {
            goAfter(location, wxParameterName2, wxParameterValue2, popParameterName2, mintParameterName2, maxtParameterName2, ciParameterName2, wxParameterName3, wxParameterValue3, popParameterName3, mintParameterName3, maxtParameterName3, ciParameterName3);
        });

        //回去看今天天氣
        leftArrow.addEventListener("click", () => {
            goBefore(location, wxParameterName1, wxParameterValue1, popParameterName1, mintParameterName1, maxtParameterName1, ciParameterName1);
        });
    })
    .catch((error)=>{
        console.log(error)
    });
    }

    
//頁面載入完成,先顯示臺北市天氣
window.addEventListener("load",()=>{
    getDate();
    inputField.value = "臺北市";
    getSearchText();
    //選擇不同縣市後,直接顯示該縣市天氣
    let county = inputField;
    county.addEventListener("change",()=>{
        // 讓箭頭回歸原本狀態，顯示當天天氣
        leftArrow.setAttribute("class","disabled");
        rightArrow.removeAttribute("class","disabled");
        getSearchText();
    })
});