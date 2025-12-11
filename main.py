
from pyodide.ffi import to_js
from js import document


clubs = {
    "Ado signing Club": {
        "description": "SING LIKE ADO IN UNDER 1 NANOSECOND!!!",
        "meeting": "EVERYDAY 2-5 PM",
        "location": "ADO SIGNING HEADQUARTERS",
        "advisor": "MS. ADO",
        "members": "3223142",
        "category": "ACADEMIC!!!"
    },
    "Ado dancing Club": {
        "description": "DANCE LIKE ADO IN UNDER 1 SECOND (not 1 nanosecond sadly).",
        "meeting": "EVERYDAY 6-8 PM",
        "location": "ADO DANCING BUILDING",
        "advisor": "MS. ADO",
        "members": "349587",
        "category": "ACADEMIC!!!"
    },
    "Ado meme Club": {
        "description": "FIND MEMES RELATED TO ADO!!! (kinda boring tho lowkey)",
        "meeting": "EVERYDAY 6-7 AM",
        "location": "YOUR HOUSE!!!",
        "advisor": "MS. ADO",
        "members": "3231",
        "category": "SPCECIAL!!"
    },
    "Ado voice Club 2": {
        "description": "ANOTHER CLUB SO YOU CAN SING LIKE ADO BUT FOR THE PROS!!!",
        "meeting": "EVERYDAY 8-11:59 PM",
        "location": "ADO SIGNING HQ FOR PROS",
        "advisor": "MS. ADO",
        "members": "1 (just 1 person...)",
        "category": "VERY SPECIAL!!!!"
    }
}

def show_info(event):
    club = document.getElementById("ado_clubs_select").value
    info = clubs[club]

    text = (
        f"{club}\n"
        f"Description: {info['description']}\n"
        f"Meeting Time: {info['meeting']}\n"
        f"Location: {info['location']}\n"
        f"Advisor: {info['advisor']}\n"
        f"Number of Members: {info['members']}\n"
        f"Category: {info['category']}"
    )

    document.getElementById("result").innerText = text
