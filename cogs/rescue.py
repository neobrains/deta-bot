import discohook.discohook as discohook


class Help(discohook.Cog):
    @discohook.Cog.command(
        name="Help",
        category=discohook.AppCmdType.message,
    )
    async def rescue(self, magic: discohook.Interaction, message: dict):
        e = discohook.Embed(
            title="Deta Cat rescue service",
            description="`How to ask for help:` \n ** ** \n > **1.** Make sure you have checked #help or the [github discussions](https://github.com/deta/docs/discussions) for your error \n > **2.** If you couldn\’t find it create a new post and either staff or a member of the server will come and help you asap! \n ** ** \n\n **Thigns to keep in mind**  \n ⬩ If your question doesn\’t get answered instantly don\’t start trying to make people look at it by posting in #general \n ⬩ Provide code, if your code is too long paste it into a [codebin](https://codebin.deta.dev/) and send the link \n ⬩ Describe your issue as much as possible \n ⬩ Provide screenshots \n ⬩ Use the correct tags",
            color=0xEE4196,
        )
        return await magic.command.response(embed=e)


def setup(client: discohook.Client):
    client.add_cog(Help())
