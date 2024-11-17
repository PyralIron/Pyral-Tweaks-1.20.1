import os
fruits = """banana, tfc
blackberry, tfc
blueberry, tfc
bunchberry, tfc
cherry, tfc
cloudberry, tfc
cranberry, tfc
elderberry, tfc
gooseberry, tfc
green_apple, tfc
lemon, tfc
melon_slice, tfc
olive, tfc
orange, tfc
peach, tfc
plum, tfc
pumpkin_chunks, tfc
raspberry, tfc
red_apple, tfc
snowberry, tfc
strawberry, tfc
wintergreen_berry, tfc
fig, firma
pineapple, firma
red_grapes, firma
white_grapes, firma"""
s = fruits.split("\n")
d = "C:/Users/admin/Twitch/Minecraft/Instances/New TFC 1.20.1/scripts/jam.zs"
f = open(d, "w")
template = """{
    "__comment__": "This file was automatically created by pyraltweaks",
    "type": "tfc:extra_products_shapeless_crafting",
    "extra_products": [
        {
        "item": "tfc:jar_lid"
        }
    ],
    "recipe": {
        "type": "tfc:damage_inputs_shapeless_crafting",
        "recipe": {
        "type": "tfc:advanced_shapeless_crafting",
        "ingredients": [
            {
            "type": "tfc:not_rotten",
            "ingredient": {
                "item": "namespace:jar/raspberry"
            }
            },
            {
            "tag": "tfc:knives"
            }
        ],
        "primary_ingredient": {
            "item": "namespace:jar/raspberry"
        },
        "result": {
            "stack": {
            "item": "namespace:jar/raspberry_unsealed"
            }
        }
        }
    }
}
"""
template_stomping = """{
  "__comment__": "This file was automatically created by pyraltweaks",
  "type": "tfc:damage_inputs_shaped_crafting",
  "recipe": {
    "type": "minecraft:crafting_shaped",
    "pattern": [
        "XGX",
        "XXX",
        "Z  "
    ],
    "key": {
        "X": {
            "item": "tfc:wood/lumber/acacia"
        },
        "G": {
            "item": "tfc:glue"
        },
        "Z": {
            "tag": "tfc:saws"
        }
    },
    "result": {
        "item": "firmalife:wood/stomping_barrel/acacia"
    }
  }
}"""

wood_types = [
    "acacia",
    "ash",
    "aspen",
    "birch",
    "blackwood",
    "chestnut",
    "douglas_fir",
    "hickory",
    "kapok",
    "mangrove",
    "maple",
    "oak",
    "palm",
    "pine",
    "rosewood",
    "sequoia",
    "spruce",
    "sycamore",
    "white_cedar",
    "willow"
]

removeTemplate = 'craftingTable.removeByName("tfc:crafting/unseal_raspberry_jar");'
removeTemplateFirma = 'craftingTable.removeByName("firmalife:crafting/unseal_fig_jar");'
# firmalife:crafting/unseal_fig_jar
for fff in s:
    sss = fff.split(", ")
    ff = sss[0]
    rr = template.replace("raspberry",ff)
    rr2 = ""
    if sss[1] == "tfc":
        rr2 = removeTemplate.replace("raspberry",ff)
        rr = rr.replace("namespace","tfc")
    elif sss[1] == "firma":
        rr2 = removeTemplateFirma.replace("fig",ff)
        rr = rr.replace("namespace","firmalife")
    # print(rr,rr2)
    f.write(rr2+"\n")
    f2 = open("C:/Users/admin/Twitch/Minecraft/Instances/New TFC 1.20.1/saves/Test World/datapacks/pyraltweaks/data/pyral/recipes/jars/unseal_"+ff+"_jar.json","w")
    f2.write(rr)
    f2.close()
for wood_type in wood_types:
    recipe = template_stomping.replace("acacia",wood_type)
    filepath = "C:/Users/admin/Twitch/Minecraft/Instances/New TFC 1.20.1/saves/Test World/datapacks/pyraltweaks/data/firmalife/recipes/crafting/wood/"+wood_type+"_stomping_barrel.json"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    f2 = open(filepath,"w")
    f2.write(recipe)
    f2.close()
f.close()