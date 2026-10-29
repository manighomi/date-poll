from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>دعوت به دیت ❤️</title>
<style>
body {
    background: linear-gradient(135deg,#180d20,#35152b);
    color: white;
    font-family: Tahoma, sans-serif;
    text-align: center;
    padding: 20px;
}
.card {
    max-width: 430px;
    margin: 30px auto;
    padding: 25px;
    background: #24152c;
    border: 1px solid #b44a85;
    border-radius: 22px;
}
h1 { color: #ff83bc; }
select, button {
    width: 100%;
    padding: 14px;
    margin: 10px 0;
    border-radius: 12px;
    font-size: 16px;
}
select {
    background: #392441;
    color: white;
    border: 1px solid #bd70a7;
}
button {
    border: none;
    cursor: pointer;
    font-weight: bold;
}
#yes { background: #19c777; color: white; }
#no {
    background: #ff4165;
    color: white;
    position: relative;
}
#result { color: #ff9dcc; margin-top: 20px; }
</style>
</head>
<body>
<div class="card">
    <h1>💌 دعوت‌نامه دیت ❤️</h1>
    <p>خانم خوشگله! 🥹🌹</p>
    <p>پایه‌ای با من بریم بیرون؟ 😏</p>

    <form id="poll">
        <label>📍 کجا بریم؟</label>
        <select id="place" required>
            <option value="منیریه؛ بریم غذا بخوریم">🍔 منیریه؛ بریم غذا بخوریم</option>
            <option value="تجریش؛ بریم دور بزنیم">🌆 تجریش؛ بریم دور بزنیم</option>
            <option value="کافه">☕ بریم کافه</option>
        </select>

        <label>🕓 چه ساعتی؟</label>
        <select id="time" required>
            <option value="۴ عصر">۴ عصر</option>
            <option value="۵ عصر">۵ عصر</option>
            <option value="۶ عصر">۶ عصر</option>
        </select>

        <p>خب، پایه‌ای بریم دیت؟ ❤️</p>

        <button type="button" id="yes" onclick="accept()">
            آره، بریم! 😍❤️
        </button>

        <button type="button" id="no">
            نه، نمیام! 😂
        </button>
    </form>

    <div id="result"></div>
</div>

<script>
const no = document.getElementById('no');

function escapeButton() {
    no.style.position = 'fixed';
    no.style.left = Math.random() * Math.max(10, innerWidth - 150) + 'px';
    no.style.top = Math.random() * Math.max(10, innerHeight - 70) + 'px';
}

no.addEventListener('pointerenter', escapeButton);
no.addEventListener('click', escapeButton);
no.addEventListener('touchstart', function(e) {
    e.preventDefault();
    escapeButton();
}, {passive: false});

function accept() {
    const place = document.getElementById('place').value;
    const time = document.getElementById('time').value;

    document.getElementById('result').innerHTML =
        '😍 یــــس! قرارمون انتخاب شد! ❤️<br><br>' +
        '📍 ' + place + '<br>' +
        '🕓 ساعت ' + time +
        '<br><br>🌹 منتظر یه روز قشنگ باش!';
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

