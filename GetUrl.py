import googlesearch


# Perform a Google search & Get the URL of the first search result
def getUrlLink(query):
    search_results = googlesearch.search(query, num_results=1)
    return next(search_results, None)