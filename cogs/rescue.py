import discohook

delete = discohook.Button(
    "Say thanks to deta cat",
    emoji=discohook.emoji.PartialEmoji(name="deta_heart", id="1025397955420770314"),
    style=discohook.ButtonStyle.grey,
)


@delete.on_click
async def delete_callback(inter: discohook.Interaction):
    return await inter.component.delete_original()


class Help(discohook.Cog):
    @discohook.Cog.command(
        name="Help",
        category=discohook.AppCmdType.message,
    )
    async def rescue(self, magic: discohook.Interaction, message: dict):
        c = discohook.View()
        c.add_button_row(delete)
        e = discohook.Embed(
            description="`How to ask for help:` \n > **1.** Make sure you have checked <#1022777815852130304> or the [github discussions](https://github.com/deta/docs/discussions) for your error \n > **2.** If you couldn\’t find it create a new post and either staff or a member of the server will come and help you asap! \n ** ** \n\n **Thigns to keep in mind**  \n ⬩ If your question doesn\’t get answered instantly don\’t start trying to make people look at it by posting in <#827546555669413919> \n ⬩ Provide code, if your code is too long paste it into a [codebin](https://codebin.deta.dev/) and send the link \n ⬩ Describe your issue as much as possible \n ⬩ Provide screenshots \n ⬩ Use the correct tags \n ⬩ [Discord threads](https://support.discord.com/hc/en-us/articles/4403205878423-Threads-FAQ)",
            color=0xEE4196,
        )
        e.author(
            name="Deta cat rescue service",
            icon_url="https://alpha.deta.space/assets/spinning_cat.aa434bc8.gif",
        )
        await magic.command.response(embed=e, components=c)


def setup(client: discohook.Client):
    client.add_cog(Help())
