import webbrowser

from voice import speak


# ==========================================
# WEB SEARCH
# ==========================================

def google_search(query):

    speak(f"Searching Google for {query}, sir.")

    url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)


def youtube_search(query):

    speak(f"Searching YouTube for {query}, sir.")

    url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)