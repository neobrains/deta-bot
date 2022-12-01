import discohook
from algoliasearch.search_client import SearchClient


def get_data(query: str, results_per_page: int = 10, page_num: int = 0):
    client = SearchClient.create("BH4D9OD16A", "4b3aaec0466a855ce8ec420d3baedde3")
    index = client.init_index("deta")
    response = index.search(query, {"hitsPerPage": results_per_page, "page": page_num})
    return response["hits"]


class Docs(discohook.Cog):
    @discohook.Cog.command(
        name="docs",
        description="Search deta.sh docs",
        options=[
            discohook.StringOption(
                name="query",
                description="Search query",
                required=True,
                auto_complete=True,
            )
        ],
    )
    async def docs(self, magic: discohook.Interaction, *, query: str):
        url = discohook.Button(
            "Deta docs",
            url=query,
            emoji=discohook.emoji.PartialEmoji(name="deta", id="1014580844813352980"),
            style=discohook.ButtonStyle.link,
        )
        c = discohook.View()
        c.add_button_row(url)
        e = discohook.Embed(
            description=f"> [`{query}`]({query})",
            color=0xEE4196,
        )
        e.author(name=f"{magic.author} picked", icon_url=magic.author.avatar_url)
        await magic.command.response(embed=e, components=c)

    @docs.autocomplete_callback
    async def autocomplete(magic: discohook.Interaction, name: str, value: str):
        dsc = []
        for i in get_data(value):
            n = ""
            for a in range(6):
                if i["hierarchy"][f"lvl{a}"] != None:
                    n += " > " + f"{i['hierarchy'][f'lvl{a}']}".replace("&#x27;", "'")
            dsc.append({"name": n, "url": i["url"]})
        await magic.send_autocomplete(
            [discohook.Choice(name=r["name"], value=r["url"]) for r in dsc]
        )


def setup(client: discohook.Client):
    client.add_cog(Docs())
