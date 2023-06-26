#!/usr/bin/env python


import click
import requests


class API:
    def __init__(self, root, session):
        self.root = root
        self.session = session

    def mages(self):
        return self.session.get(f"{self.root}/mages/").json()

    def mage(self, id=None, value=None):
        if id:
            if not value:
                return self.session.get(f"{self.root}/mages/{id}/").json()
        else:
            return self.session.post(f"{self.root}/mages/", json=value)

    def spells(self):
        return self.session.get(f"{self.root}/spells/").json()

    def fight(self, mages):
        return self.session.post(f"{self.root}/fights/", json=mages).json()


@click.group()
@click.pass_context
def main(ctx):
    session = requests.Session()
    api = API("http://127.0.0.1:8000", session)
    ctx.ensure_object(dict)
    ctx.obj['api'] = api


@main.command()
@click.pass_context
def mage(ctx):
    api = ctx.obj['api']
    spells = api.spells()
    name = click.prompt("Name")
    click.echo("Spells:")
    for s in spells:
        click.echo(f"  {s['id']}) {s['name']}")
    spell = click.prompt("Choose a spell", type=int)
    r = api.mage(value={"name": name, "spells": [spell]}).json()
    mage = click.style(r["name"], fg="yellow")
    spell = click.style(r["spell_list"][0]["name"], fg="red")

    message = "Your mage, {}, has prepared {}!"
    click.echo(message.format(mage, spell))


@main.command()
@click.pass_context
def mages(ctx):
    api = ctx.obj['api']
    for mage in api.mages():
        spell = mage["spell_list"][0]
        click.echo(f"{mage['name']}  ({spell['name']})")


@main.command()
@click.pass_context
def fight(ctx):
    api = ctx.obj['api']
    mages = api.mages()
    click.echo("Mages:")
    for m in mages:
        click.echo(f"  {m['id']}) {m['name']}")
    first = click.prompt("Choose your first combatant", type=int)
    second = click.prompt("Choose your second combatant", type=int)

    fight = {
        "mages": [first, second]
    }
    r = api.fight(mages=fight)
    winner = click.style(r['winner']['name'], fg='green')
    spell = click.style(r["winner"]["spell_list"][0]["name"], fg="yellow")
    idx = [i for i in r["mages"] if i != r["winner"]["id"]][0]
    loser = click.style(api.mage(idx)["name"], fg="red")
    message = "{} has used {} to defeat {} in single mage combat!"
    click.echo(message.format(winner, spell, loser))


if __name__ == "__main__":
    main(obj={})
