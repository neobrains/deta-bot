from algoliasearch.search_client import SearchClient


def get_data(index, query: str, results_per_page: int = 10, page_num: int = 0):
    response = index.search(query, {"hitsPerPage": results_per_page, "page": page_num})
    return response["hits"]


client = SearchClient.create("BH4D9OD16A", "4b3aaec0466a855ce8ec420d3baedde3")
index = client.init_index("deta")

dsc = ""
for i in get_data(index, "deta base"):
    name = ""
    for a in range(6):
        if i["hierarchy"][f"lvl{a}"] != None:
            if a == 6:
                name += f"{i['hierarchy'][f'lvl{a}']}"
                break
            else:
                name += f"{i['hierarchy'][f'lvl{a}']} > "
    dsc += f"> [`{name}`]({i['url']}) \n ** ** \n"
