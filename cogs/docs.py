import discohook.discohook as discohook
from algoliasearch.search_client import SearchClient

url = discohook.Button(
    "Deta docs",
    url="https://docs.deta.sh/docs/home",
    emoji=discohook.emoji.PartialEmoji(name="deta", id="1014580844813352980"),
    style=discohook.ButtonStyle.link,
)

delete = discohook.Button(
    "Delete",
    style=discohook.ButtonStyle.red,
)


@delete.on_click
async def delete_callback(inter: discohook.Interaction):
    return await inter.component.delete_original()


def get_data(index, query: str, results_per_page: int = 10, page_num: int = 0):
    response = index.search(query, {"hitsPerPage": results_per_page, "page": page_num})
    return response["hits"]


class Docs(discohook.Cog):
    @discohook.Cog.command(
        name="docs",
        description="Search deta.sh docs",
        options=[
            discohook.StringOption(
                name="query", description="Search query", required=True
            )
        ],
    )
    async def docs(self, magic: discohook.Interaction, *, query: str):
        c = discohook.View()
        c.add_button_row(url, delete)
        client = SearchClient.create("BH4D9OD16A", "4b3aaec0466a855ce8ec420d3baedde3")
        index = client.init_index("deta")
        dsc = ""
        for i in get_data(index, query):
            name = ""
            for a in range(6):
                if i["hierarchy"][f"lvl{a}"] != None:
                    name += (
                        f"{i['hierarchy'][f'lvl{a}']}".replace("&#x27;", "'") + " > "
                    )
            dsc += f"> [`{name}`]({i['url']}) \n ** ** \n"
        e = discohook.Embed(
            description=dsc,
            color=0xEE4196,
        )
        e.author(name=f"Search results")
        await magic.command.response(embed=e, components=c)


def setup(client: discohook.Client):
    client.add_cog(Docs())
