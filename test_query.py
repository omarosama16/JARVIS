from utils.query import extract_search_query


test_queries = [

    # ==========================================
    # GOOGLE
    # ==========================================

    ("search google for python tutorials", "google"),
    ("google python tutorials", "google"),
    ("google how to learn python", "google"),
    ("search google python tutorials", "google"),

    # ==========================================
    # YOUTUBE
    # ==========================================

    ("search youtube for coding music", "youtube"),
    ("search youtube coding music", "youtube"),
    ("find on youtube coding music", "youtube"),
    ("youtube coding music", "youtube"),
]


for command, platform in test_queries:

    query = extract_search_query(command, platform)

    print(f"{command:<45} -> {query}")