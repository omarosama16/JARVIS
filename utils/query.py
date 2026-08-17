def extract_search_query(command, platform):
    """
    Extracts the search query from a Google or YouTube command.
    """

    command = command.lower().strip()

    patterns = []

    if platform == "google":
        patterns = [
            "search google for",
            "search google",
            "google"
        ]

    elif platform == "youtube":
        patterns = [
            "search youtube for",
            "search youtube",
            "find on youtube",
            "youtube"
        ]

    for pattern in patterns:

        if command.startswith(pattern):

            query = command[len(pattern):].strip()

            if query:
                return query

    return None