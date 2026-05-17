from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------------- DATASET ----------------
crop_data = [
{"name":"Rice","soil":["Clay","Loamy"],"season":"Rainy","weather":"Rainy","yield":40,"cost":15000,"vehicle":"Tractor","irrigation":"Surface Irrigation","labour":"High"},
{"name":"Wheat","soil":["Loamy","Black"],"season":"Winter","weather":"Normal","yield":35,"cost":12000,"vehicle":"Tractor","irrigation":"Sprinkler","labour":"Medium"},
{"name":"Maize","soil":["Sandy","Loamy"],"season":"Rainy","weather":"Normal","yield":30,"cost":10000,"vehicle":"Seeder","irrigation":"Drip","labour":"Medium"},
{"name":"Millets","soil":["Sandy"],"season":"Summer","weather":"Hot","yield":20,"cost":8000,"vehicle":"Manual","irrigation":"Low","labour":"Low"},
{"name":"Sugarcane","soil":["Loamy"],"season":"Rainy","weather":"Rainy","yield":80,"cost":30000,"vehicle":"Harvester","irrigation":"Drip","labour":"High"},
{"name":"Cotton","soil":["Black"],"season":"Summer","weather":"Hot","yield":25,"cost":18000,"vehicle":"Tractor","irrigation":"Drip","labour":"High"},
{"name":"Groundnut","soil":["Sandy","Loamy"],"season":"Summer","weather":"Normal","yield":22,"cost":14000,"vehicle":"Tractor","irrigation":"Sprinkler","labour":"Medium"},
{"name":"Tomato","soil":["Loamy"],"season":"Winter","weather":"Normal","yield":50,"cost":20000,"vehicle":"Manual","irrigation":"Drip","labour":"High"},
{"name":"Potato","soil":["Loamy"],"season":"Winter","weather":"Normal","yield":45,"cost":16000,"vehicle":"Tractor","irrigation":"Sprinkler","labour":"Medium"},
{"name":"Onion","soil":["Loamy"],"season":"Winter","weather":"Normal","yield":30,"cost":12000,"vehicle":"Manual","irrigation":"Drip","labour":"High"},
{"name":"Chickpea","soil":["Sandy"],"season":"Winter","weather":"Normal","yield":18,"cost":9000,"vehicle":"Manual","irrigation":"Low","labour":"Low"},
{"name":"Banana","soil":["Loamy"],"season":"Rainy","weather":"Rainy","yield":90,"cost":25000,"vehicle":"Truck","irrigation":"Drip","labour":"High"},
{"name":"Tea","soil":["Acidic"],"season":"Rainy","weather":"Rainy","yield":60,"cost":35000,"vehicle":"Manual","irrigation":"Rainfed","labour":"High"},
{"name":"Coffee","soil":["Loamy"],"season":"Rainy","weather":"Normal","yield":55,"cost":30000,"vehicle":"Manual","irrigation":"Shade","labour":"Medium"},
{"name":"Barley","soil":["Loamy"],"season":"Winter","weather":"Normal","yield":28,"cost":10000,"vehicle":"Tractor","irrigation":"Low","labour":"Low"}
]

# ---------------- STYLE ----------------
def style(bg1, bg2):

    return f"""
    <!DOCTYPE html>
    <html>
    <head>

    <title>Smart Agriculture Expert System</title>

    <meta name="viewport"
    content="width=device-width, initial-scale=1.0">

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap"
    rel="stylesheet">

    <style>

    * {{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family:'Poppins',sans-serif;
    }}

    body {{
        min-height:100vh;
        background:linear-gradient(135deg,{bg1},{bg2});
        color:white;
        overflow-x:hidden;
    }}

    .navbar {{
        width:100%;
        padding:20px;
        text-align:center;
        font-size:30px;
        font-weight:bold;
        background:rgba(0,0,0,0.2);
        backdrop-filter:blur(10px);
    }}

    .container {{
        width:90%;
        max-width:850px;
        margin:40px auto;
        padding:40px;
        border-radius:25px;
        background:rgba(255,255,255,0.12);
        backdrop-filter:blur(15px);
        text-align:center;
        box-shadow:0 10px 40px rgba(0,0,0,0.3);
    }}

    h1 {{
        font-size:40px;
        margin-bottom:20px;
    }}

    h2 {{
        margin-bottom:20px;
    }}

    p {{
        font-size:20px;
        margin:12px 0;
    }}

    input, select {{
        width:90%;
        padding:15px;
        margin:15px;
        border:none;
        border-radius:15px;
        font-size:17px;
        outline:none;
    }}

    button {{
        padding:15px 35px;
        border:none;
        border-radius:15px;
        background:linear-gradient(45deg,#2d6a4f,#40916c);
        color:white;
        font-size:18px;
        font-weight:bold;
        cursor:pointer;
        transition:0.3s;
        margin-top:10px;
    }}

    button:hover {{
        transform:scale(1.05);
    }}

    .card {{
        background:rgba(255,255,255,0.15);
        padding:25px;
        border-radius:20px;
        margin-top:20px;
    }}

    a {{
        text-decoration:none;
        color:#ffe66d;
        font-size:22px;
        font-weight:bold;
    }}

    ul {{
        list-style:none;
        font-size:22px;
        line-height:2;
    }}

    .emoji {{
        font-size:60px;
        margin-bottom:10px;
    }}

    canvas {{
        width:100% !important;
        height:450px !important;
    }}

    @media(max-width:768px) {{

        .container {{
            width:95%;
            padding:25px;
        }}

        h1 {{
            font-size:30px;
        }}

        .navbar {{
            font-size:22px;
        }}

        button {{
            width:90%;
        }}
    }}

    </style>

    </head>
    """

# ---------------- LOGIN ----------------
@app.route('/')
def login():

    return render_template_string(style("#0f2027","#2c5364") + """

    <div class="navbar">
        🌾 Smart Agriculture Expert System
    </div>

    <div class="container">

        <div class="emoji">🌱</div>

        <h1>Welcome Farmer</h1>

        <p>AI Based Crop Recommendation System</p>

        <form action="/soil" method="post">

            <input type="text"
            name="username"
            placeholder="Enter Username"
            required>

            <input type="password"
            name="password"
            placeholder="Enter Password"
            required>

            <button type="submit">
                LOGIN
            </button>

        </form>

        <br>

        <p>
        Username : <b>admin</b><br>
        Password : <b>1234</b>
        </p>

    </div>

    </html>
    """)

# ---------------- SOIL ----------------
@app.route('/soil', methods=['POST'])
def soil():

    username = request.form['username']
    password = request.form['password']

    if username != "admin" or password != "1234":

        return render_template_string(style("#780000","#c1121f") + """

        <div class="container">

            <h1>❌ Invalid Login</h1>

            <br>

            <a href="/">Back</a>

        </div>

        </html>
        """)

    return render_template_string(style("#134e5e","#71b280") + """

    <div class="navbar">
        🌱 Soil Selection
    </div>

    <div class="container">

        <h1>Select Soil Type</h1>

        <form action="/weather" method="post">

            <select name="soil">

                <option>Loamy</option>
                <option>Sandy</option>
                <option>Clay</option>
                <option>Black</option>

            </select>

            <button type="submit">
                NEXT ➜
            </button>

        </form>

    </div>

    </html>
    """)

# ---------------- WEATHER ----------------
@app.route('/weather', methods=['POST'])
def weather():

    soil = request.form['soil']

    return render_template_string(style("#355c7d","#6c5b7b") + f"""

    <div class="navbar">
        ☁ Weather Selection
    </div>

    <div class="container">

        <h1>Select Weather</h1>

        <form action="/season" method="post">

            <input type="hidden"
            name="soil"
            value="{soil}">

            <select name="weather">

                <option>Normal</option>
                <option>Rainy</option>
                <option>Hot</option>

            </select>

            <button type="submit">
                NEXT ➜
            </button>

        </form>

    </div>

    </html>
    """)

# ---------------- SEASON ----------------
@app.route('/season', methods=['POST'])
def season():

    soil = request.form['soil']
    weather = request.form['weather']

    return render_template_string(style("#1d4350","#a43931") + f"""

    <div class="navbar">
        🌦 Season Selection
    </div>

    <div class="container">

        <h1>Select Season</h1>

        <form action="/result" method="post">

            <input type="hidden"
            name="soil"
            value="{soil}">

            <input type="hidden"
            name="weather"
            value="{weather}">

            <select name="season">

                <option>Rainy</option>
                <option>Winter</option>
                <option>Summer</option>

            </select>

            <button type="submit">
                ANALYZE ➜
            </button>

        </form>

    </div>

    </html>
    """)

# ---------------- RESULT ----------------
@app.route('/result', methods=['POST'])
def result():

    soil = request.form['soil']
    weather = request.form['weather']
    season = request.form['season']

    results = []

    for c in crop_data:

        score = 0

        if soil in c["soil"]:
            score += 3

        if season == c["season"]:
            score += 2

        if weather == c["weather"]:
            score += 2

        results.append((c, score))

    results.sort(key=lambda x: x[1], reverse=True)

    top = results[:3]

    html = """

    <div class="navbar">
        🌾 Recommended Crops
    </div>

    <div class="container">

    <h1>Top Crop Suggestions</h1>
    """

    for c, s in top:

        html += f"""

        <div class="card">

            <h2>{c['name']}</h2>

            <p>Recommendation Score : <b>{s}</b></p>

            <form action="/detail" method="post">

                <input type="hidden"
                name="crop"
                value="{c['name']}">

                <button type="submit">
                    View Analysis
                </button>

            </form>

        </div>
        """

    html += "</div></html>"

    return render_template_string(
        style("#1d4350","#a43931") + html
    )

# ---------------- DETAIL ----------------
@app.route('/detail', methods=['POST'])
def detail():

    name = request.form['crop']

    for c in crop_data:

        if c["name"] == name:

            if c['yield'] >= 70:
                area = "5 - 10 Acres"
            elif c['yield'] >= 40:
                area = "3 - 5 Acres"
            else:
                area = "1 - 3 Acres"

            return render_template_string(style("#355c7d","#6c5b7b") + f"""

            <div class="navbar">
                🌾 Crop Analysis
            </div>

            <div class="container">

                <h1>{c['name']} Analysis</h1>

                <div class="card">

                    <p><b>Yield :</b> {c['yield']} kg</p>

                    <p><b>Estimated Cost :</b> ₹{c['cost']}</p>

                    <p><b>Vehicle :</b> {c['vehicle']}</p>

                    <p><b>Irrigation :</b> {c['irrigation']}</p>

                    <p><b>Labour :</b> {c['labour']}</p>

                    <p><b>Suggested Area :</b> {area}</p>

                </div>

                <br><br>

                <h2>Crop Performance Graph</h2>

                <div style="
                    background:white;
                    padding:25px;
                    border-radius:20px;
                ">

                    <canvas id="chart"></canvas>

                </div>

                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

                <script>

                new Chart(document.getElementById('chart'), {{

                    type: 'bar',

                    data: {{

                        labels: [
                            'Yield (kg)',
                            'Cost (₹ in Thousands)'
                        ],

                        datasets: [{{
                            label: '{c["name"]} Statistics',

                            data: [
                                {c["yield"]},
                                {c["cost"]/1000}
                            ],

                            backgroundColor: [
                                '#2d6a4f',
                                '#40916c'
                            ],

                            borderRadius: 10
                        }}]

                    }},

                    options: {{
                        responsive:true,
                        maintainAspectRatio:false
                    }}

                }});

                </script>

                <br><br>

                <a href="/gov">
                    ➜ Government Schemes
                </a>

            </div>

            </html>
            """)

# ---------------- GOV ----------------
@app.route('/gov')
def gov():

    return render_template_string(style("#0f2027","#203a43") + """

    <div class="navbar">
        🌾 Government Schemes
    </div>

    <div class="container">

        <h1>Farmer Welfare Schemes</h1>

        <ul>

            <li>✅ PM-Kisan</li>
            <li>✅ Fasal Bima Yojana</li>
            <li>✅ Soil Health Card</li>
            <li>✅ Kisan Credit Card</li>
            <li>✅ PM Krishi Sinchai Yojana</li>

        </ul>

        <br>

        <a href="/final">
        ➜ Final Page
        </a>

    </div>

    </html>
    """)

# ---------------- FINAL ----------------
@app.route('/final')
def final():

    return render_template_string(style("#11998e","#38ef7d") + """

    <div class="navbar">
        🌾 Smart Agriculture Expert System
    </div>

    <div class="container">

        <h1>🎉 Analysis Completed</h1>

        <p>
        Thank you for using the AI Agriculture Expert System
        </p>

        <br><br>

        <a href="/">
        🏠 HOME
        </a>

        <br><br>

        <button onclick="exitWebsite()">
            ❌ EXIT
        </button>

    </div>

    <script>

    function exitWebsite() {

        let confirmExit =
        confirm("Are you sure you want to exit?");

        if(confirmExit) {

            document.body.innerHTML = `

            <div style="
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction:column;
            background:linear-gradient(135deg,#0f2027,#203a43);
            color:white;
            font-family:Poppins;
            ">

                <h1 style="
                font-size:55px;
                margin-bottom:20px;
                ">
                    🌾 Thank You
                </h1>

                <p style="
                font-size:24px;
                text-align:center;
                width:80%;
                ">
                    You have successfully exited the
                    Smart Agriculture Expert System
                </p>

            </div>

            `;

            window.history.pushState(
                null,
                null,
                window.location.href
            );

            window.onpopstate = function () {

                history.go(1);

            };
        }
    }

    </script>

    </html>
    """)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)