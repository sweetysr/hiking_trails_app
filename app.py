from flask import Flask, request 

app = Flask(__name__)

trails = [
    {
        "name": "Pine Ridge Loop",
        "location": "Mountain Valley",
        "difficulty": "Easy",
        "distance": "4.2 km",
        "time": "1.5 hours",
        "best_for": "Beginners and families",
    },


    {
        "name": "Lakeview Summit",
        "location": "Blue Lake Park",
        "difficulty": "Moderate",
        "distance": "8.5 km",
        "time": "3 hours",
        "best_for": "Lake views and photos",
     },
    
    {
        "name": "Granite Peak Trail",
        "location": "North Ridge",
        "difficulty": "Hard",
        "distance": "14 km",
        "time": "6 hours",
        "best_for": "Experienced hikers",
    },
]


@app.route("/")
def home():
    search_text = request.args.get("search", "").lower()
    selected_difficulty = request.args.get("difficulty", "All")
    trail_items = ""

    for trail in trails:
        matches_search = (
            search_text == ""
            or search_text in trail["name"].lower()
            or search_text in trail["location"].lower()
        )

        matches_difficulty = (
            selected_difficulty == "All"
            or selected_difficulty == trail["difficulty"]
        )

        if matches_search and matches_difficulty:
            trail_items = trail_items + f"""
            <li style="margin-bottom: 20px;">
                <strong>{trail["name"]}</strong><br>
                Location: {trail["location"]}<br>
                Difficulty: <span class="badge {trail["difficulty"]}">{trail["difficulty"]}</span><br>
                Distance: {trail["distance"]}<br>
                Time: {trail["time"]}<br>
                Best for: {trail["best_for"]}
            </li>
            """

    if trail_items == "":
        trail_items = """
        <p>No trails found. Try another search or difficulty.</p>
        """

    return f"""

    <style>

        ul {{
            list-style: none;
            padding-left: 0;
        }}
    
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f7f1;
            color: #243024;
            margin: 40px;
        }}

        h1 {{
            color: #1f4d36;
        }}

        li {{
            background-color: white;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid #d8e2d0;
        }}

        .badge {{
                display: inline-block;
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 14px;
                font-weight: bold;
               }}

        .Easy {{
                background-color: #d7f5dc;
                color: #176127;
              }}

        .Moderate {{
                    background-color: #fff0c2;
                    color: #705100;
                  }}

        .Hard {{
                background-color: #ffd7d7;
                color: #8b1e1e;
              }}
    </style>

    <h1>TrailWise</h1>
    <p>Find beautiful hiking trails for your next adventure.</p>

    <form method="get">
        <input type="text" name="search" placeholder="Search trails..." value="{search_text}">
        
        <select name="difficulty">
            <option value="All" {"selected" if selected_difficulty == "All" else ""}>All</option>
            <option value="Easy" {"selected" if selected_difficulty == "Easy" else ""}>Easy</option>
            <option value="Moderate" {"selected" if selected_difficulty == "Moderate" else ""}>Moderate</option>
            <option value="Hard" {"selected" if selected_difficulty == "Hard" else ""}>Hard</option>
        </select> 
        
        <button type="submit">Search</button>
    </form>

    <h2>Search Results</h2>
        <ul>
            {trail_items}
        </ul>
    """

def home():
    search_text = request.args.get("search", "").lower()
    selected_difficulty = request.args.get("difficulty", "All")
    trail_items = ""



