from discord.ext import commands
import discord
from object_classes.heroes import Hero
from object_classes.inventory import Inventory
import pandas as pd
#LINK START: If user has 'player' role, disable them from having permission to use this command again
#Pandas Read Player Stats
ps = pd.read_csv('playerstatistics.csv')
pe = pd.read_csv('inventory.csv')

class start(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command(name='start')
        async def start(ctx):
            role = discord.utils.get(ctx.guild.roles, name='Player')
            if role not in ctx.author.roles:
                await ctx.author.send("Thank you for participating. Enjoy yourself.")
                await ctx.send(
                    f"Link connection has been established. Say hello to your new room {ctx.author.display_name}")
                await ctx.author.add_roles(role)
                self.pend(ctx.author.id, ctx.author.display_name)
                self.pendt(ctx.author.id,ctx.author.display_name)
            elif role in ctx.author.roles:
                await ctx.author.send("You're already a player!")
            pass

    def pend(self, id, display_name):
        hero = Hero(id, display_name)
        basis = {
            'userID': [hero.userID],
            'name': [hero.name],
            'HP': [hero.HP],
            'STR': [hero.STR],
            'DEX': [hero.DEX],
            'SPD': [hero.SPD],
            'MPE': [hero.MPE],
            'HIT': [hero.HIT]
        }
        columns = ['userID', 'name', 'HP', 'STR', 'DEX', 'SPD', 'MPE', 'HIT']
        heropend = pd.DataFrame(basis, columns=columns)
        print(f'\n\nNEW PLAYER: {hero.name}\n{heropend}')
        global ps
        ps = ps.append(heropend, ignore_index=True)
        ps.to_csv('playerstatistics.csv', index=False)

    def pendt(self, id, display_name):
        inventory = Inventory(id, display_name)
        basis = {
            'userID': [inventory.userID],
            'name': [inventory.name],
            'slot1': [inventory.slot1],
            'slotfav1': [inventory.slotfav1],
            'slot2': [inventory.slot2],
            'slotfav2': [inventory.slotfav2],
            'slot3': [inventory.slot3],
            'slotfav3': [inventory.slotfav3],
            'slot4': [inventory.slot4],
            'slotfav4': [inventory.slotfav4],
            'slot5': [inventory.slot5],
            'slotfav5': [inventory.slotfav5],
            'slot6': [inventory.slot6],
            'slotfav6': [inventory.slotfav6],
            'slot7': [inventory.slot7],
            'slotfav7': [inventory.slotfav7],
            'slot8': [inventory.slot8],
            'slotfav8': [inventory.slotfav8],
            'slot9': [inventory.slot9],
            'slotfav9': [inventory.slotfav9],
            'slot10': [inventory.slot10],
            'slotfav10': [inventory.slotfav10],
            'slot11': [inventory.slot11],
            'slotfav11': [inventory.slotfav11],
            'slot12': [inventory.slot12],
            'slotfav12': [inventory.slotfav12],
            'slot13': [inventory.slot13],
            'slotfav13': [inventory.slotfav13],
            'slot14': [inventory.slot14],
            'slotfav14': [inventory.slotfav14],
            'slot15': [inventory.slot15],
            'slotfav15': [inventory.slotfav15],
            'slot16': [inventory.slot16],
            'slotfav16': [inventory.slotfav16],
            'slot17': [inventory.slot17],
            'slotfav17': [inventory.slotfav17],
            'slot18': [inventory.slot18],
            'slotfav18': [inventory.slotfav18],
            'slot19': [inventory.slot19],
            'slotfav19': [inventory.slotfav19],
            'slot20': [inventory.slot20],
            'slotfav20': [inventory.slotfav20],
            'slot21': [inventory.slot21],
            'slotfav21': [inventory.slotfav21],
            'slot22': [inventory.slot22],
            'slotfav22': [inventory.slotfav22],
            'slot23': [inventory.slot23],
            'slotfav23': [inventory.slotfav23],
            'slot24': [inventory.slot24],
            'slotfav24': [inventory.slotfav24],
            'slot25': [inventory.slot25],
            'slotfav25': [inventory.slotfav25],
            'slot26': [inventory.slot26],
            'slotfav26': [inventory.slotfav26],
            'slot27': [inventory.slot27],
            'slotfav27': [inventory.slotfav27],
            'slot28': [inventory.slot28],
            'slotfav28': [inventory.slotfav28],
            'slot29': [inventory.slot29],
            'slotfav29': [inventory.slotfav29],
            'slot30': [inventory.slot30],
            'slotfav30': [inventory.slotfav30],
            'slot31': [inventory.slot31],
            'slotfav31': [inventory.slotfav31],
            'slot32': [inventory.slot32],
            'slotfav32': [inventory.slotfav32],
            'slot33': [inventory.slot33],
            'slotfav33': [inventory.slotfav33],
            'slot34': [inventory.slot34],
            'slotfav34': [inventory.slotfav34],
            'slot35': [inventory.slot35],
            'slotfav35': [inventory.slotfav35],
            'slot36': [inventory.slot36],
            'slotfav36': [inventory.slotfav36],
            'slot37': [inventory.slot37],
            'slotfav37': [inventory.slotfav37],
            'slot38': [inventory.slot38],
            'slotfav38': [inventory.slotfav38],
            'slot39': [inventory.slot39],
            'slotfav39': [inventory.slotfav39],
            'slot40': [inventory.slot40],
            'slotfav40': [inventory.slotfav40],
            'slot41': [inventory.slot41],
            'slotfav41': [inventory.slotfav41],
            'slot42': [inventory.slot42],
            'slotfav42': [inventory.slotfav42],
            'slot43': [inventory.slot43],
            'slotfav43': [inventory.slotfav43],
            'slot44': [inventory.slot44],
            'slotfav44': [inventory.slotfav44],
            'slot45': [inventory.slot45],
            'slotfav45': [inventory.slotfav45],
            'slot46': [inventory.slot46],
            'slotfav46': [inventory.slotfav46],
            'slot47': [inventory.slot47],
            'slotfav47': [inventory.slotfav47],
            'slot48': [inventory.slot48],
            'slotfav48': [inventory.slotfav48],
            'slot49': [inventory.slot49],
            'slotfav49': [inventory.slotfav49],
            'slot50': [inventory.slot50],
            'slotfav50': [inventory.slotfav50],
        }
        columns = ['userID', 'name','slot1', 'slotfav1','slot2', 'slotfav2','slot3', 'slotfav3','slot4', 'slotfav4','slot5', 'slotfav5','slot6', 'slotfav6','slot7', 'slotfav7','slot8', 'slotfav8','slot9', 'slotfav9','slot10', 'slotfav10','slot11', 'slotfav11','slot12', 'slotfav12','slot13', 'slotfav13','slot14', 'slotfav14','slot15', 'slotfav15','slot16', 'slotfav16','slot17', 'slotfav17','slot18', 'slotfav18','slot19', 'slotfav19','slot20', 'slotfav20','slot21', 'slotfav21','slot22', 'slotfav22','slot23', 'slotfav23','slot24', 'slotfav24','slot25', 'slotfav25','slot26', 'slotfav26','slot27', 'slotfav27','slot28', 'slotfav28','slot29', 'slotfav29','slot30', 'slotfav30','slot31', 'slotfav31','slot32', 'slotfav32','slot33', 'slotfav33','slot34', 'slotfav34','slot35', 'slotfav35','slot36', 'slotfav36','slot37', 'slotfav37','slot38', 'slotfav38','slot39', 'slotfav39','slot40', 'slotfav40','slot41', 'slotfav41','slot42', 'slotfav42','slot43', 'slotfav43','slot44', 'slotfav44','slot45', 'slotfav45','slot46', 'slotfav46','slot47', 'slotfav47','slot48', 'slotfav48','slot49', 'slotfav49','slot50', 'slotfav50']
        global pe
        invenpend = pd.DataFrame(basis, columns=columns)
        pe = pe.append(invenpend, ignore_index=True)
        pe.to_csv('inventory.csv', index=False)

def setup(client):
    client.add_cog(start(client))