 results = []
    for language in languages:
        if keyword.lower() in language.lower():
            results.append(language)
    return results
