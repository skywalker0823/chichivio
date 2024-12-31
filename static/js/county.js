document.addEventListener('DOMContentLoaded', () => {
    // 目標 API URL
    const county = document.getElementById('county_id').innerHTML;
    const apiUrl = `/api/county/?county=${county}`;

    // 發送 GET 請求，取得夜市資料
    fetch(apiUrl, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': get_cookie('csrf_access_token')
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === '0') {
            // 成功獲得資料，顯示夜市資料
            const nightMarkets = data.night_markets;
            const container = document.getElementById('block-container');
            nightMarkets.forEach(market => {
                const marketDiv = document.createElement('div');
                marketDiv.classList.add('block');
                marketDiv.innerHTML = `
                    <h3>${market.name}</h3>
                    <p><strong>縣市:</strong> ${market.county}</p>
                    <p><strong>地點:</strong> ${market.location}</p>
                    <p><strong>營業時間:</strong> ${market.operating_days}</p>
                `;
                container.appendChild(marketDiv);
            });
        } else {
            // 出現錯誤或無資料
            alert('無法獲取夜市資料');
        }
    })
    .catch(error => {
        console.error('Error fetching night market data:', error);
        alert('請求夜市資料時發生錯誤');
    });
});


get_cookie = (name) => {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}