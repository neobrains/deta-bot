import re
import requests


def render_content(text: str):
    # s = re.search(f"## {section}(.*) ##", str)
    t = (
        text.replace("####", ">")
        .replace("###", ">")
        .replace("##", ">")
        .replace("- ", "⬩ ")
    )
    a = re.sub("---.*?---", "", t, flags=re.DOTALL)
    r = re.sub("import.*?';", "", a, flags=re.DOTALL)
    if len(r) == 4096:
        return "Message to long!!"
    else:
        return r


def get_docs(section: str, doc_page: str, doc_query: str):
    url = f"https://raw.githubusercontent.com/deta/docs/master/docs/{section}/{doc_page}.md"
    contents = requests.get(url).text
    start_index = contents.find(doc_query)
    end_index = start_index + 1000
    return contents[start_index:end_index] + "..."
