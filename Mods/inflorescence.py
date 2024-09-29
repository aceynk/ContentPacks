from pytocp import Mod, Entry, Entry_Curry, ContentFile

### INIT ###

m: Mod = Mod(
    name = "[CP] Inflorescence",
    author = "aceynk",
    version = "1.0.0",
    description = "Adds functionality related to flowers to Stardew Valley",
    uid = "aceynk.inflorescencecontent",
    update_key_nexus = 0,
    dependencies = [
        {
            "UniqueId": "selph.ExtraMachineConfig",
            "IsRequired": True
        },
        {
            "UniqueId": "leclair.bettercrafting",
            "IsRequired": True
        },
        {
            "UniqueId": "spacechase0.SpaceCore",
            "IsRequired": True
        }
    ]
)

m.AUTO_RELOAD = True
m.AUTO_REGISTER = True
m.PREFIX_WITH_MODID = False

m.output_fp = ['', "/home/aceynk/.local/share/Steam/steamapps/common/Stardew Valley/Mods"]

m.unpacked_content_fp = "../steamcommon/Stardew Valley/Content (unpacked)"

m.i18n_internal['default'] = {
    "Inflorescence_MailGold": "Congratulations, you won a gold medal! Enjoy some Gold Bouquets, you can spend them in the weekly shop! [#]TestingLetterGold",
    "Inflorescence_MailSilver": "Congratulations, you won a silver medal! Enjoy some Silver Bouquets, you can spend them in the weekly shop! [#]TestingLetterSilver",
    "Inflorescence_MailBronze": "Congratulations, you won a bronze medal! Enjoy some Bronze Bouquets, you can spend them in the weekly shop! [#]TestingLetterBronze",
    "Inflorescence_MailInitiation": "Hello @! We are Inflorescence, a local organization, and we run a farm flora competition. Plant some flowers on your farm and you may just win! We evaluate farms at the end of every week, and there is a prize stand on Tuesdays.^^Best of luck!^- Inflorescence[#]Flower Competition Invitation",
    "GoldBouquet_name": "Gold Bouquet",
    "GoldBouquet_desc": "A bouquet of golden flowers.",
    "SilverBouquet_name": "Silver Bouquet",
    "SilverBouquet_desc": "A bouquet of silver flowers.",
    "BronzeBouquet_name": "Bronze Bouquet",
    "BronzeBouquet_desc": "A bouquet of bronze flowers.",
    "PowerGro_name": "Power Gro",
    "PowerGro_desc": "Instantly grow a single flower.",
    "ScoreRadio_name": "Score Radio",
    "ScoreRadio_desc": "A radio that informs you of your current score in the Inflorescence flower competition.",
    "InformantEarpiece_name": "Informant Earpiece",
    "InformantEarpiece_desc": "Shhh... Maybe you can get information on your standings...",
    "AshFurnace_name": "Ash Furnace",
    "AshFurnace_desc": "Burns wood into ash.",
    "Ash_name": "Ash",
    "Ash_desc": "The remains of burnt wood...",
    "Bouquet_name": "Bouquet",
    "Bouquet_desc": "A cute bouquet of flowers.",
    "Lye_name": "Lye",
    "Lye_desc": "A strong alkaline solution.",
    "Soap_name": "Soap",
    "Soap_flavoredname": "%PRESERVED_DISPLAY_NAME Soap",
    "Soap_desc": "A fragrant bar of solid soap.",
    "SoapStation_name": "Soap Station",
    "SoapStation_desc": "A convenient station for soapmaking.",
    "SpaceCore_Bouquet": "Bouquet"
}

i18n = m.i18n

### CONTENTFILE ###

Mail = ContentFile("mail")
Objects = ContentFile("objects")
Recipes = ContentFile("recipes")
Machines = ContentFile("machines")
Shops = ContentFile("shops")

SpaceCore = ContentFile("spacecore")

### CURRIES ###

Mail_Curry = Entry_Curry(
    action = "EditData",
    target = "Data/Mail",
    register_with = Mail
)

ObjectCurry = Entry_Curry(
    action = "EditData",
    target = "Data/Objects",
    register_with = Objects
)

Flower_Currency = Entry_Curry(
    entry = {
        "Type": "Basic",
        "Category": -16,
        "Texture": "{{ModID}}/Objects"
    },
    to_curry = ObjectCurry
)

RecipeCurry = Entry_Curry(
    action = "EditData",
    target = "Data/CraftingRecipes",
    register_with = Recipes
)

MachineCurry = Entry_Curry(
    action = "EditData",
    target = "Data/Machines",
    register_with = Machines
)

BigCraftableCurry = Entry_Curry(
    action = "EditData",
    target = "Data/BigCraftables",
    entry = {
        "Texture": "{{ModID}}/Objects"
    },
    register_with = Machines
)

ShopsCurry = Entry_Curry(
    action = "EditData",
    target = "Data/Shops",
    register_with = Shops
)

SCBouquet = Entry_Curry(
    action="EditData",
    target="spacechase0.SpaceCore/ObjectExtensionData",
    entry={
        "CategoryTextOverride": i18n("SpaceCore_Bouquet"),
        "CategoryColorOverride": {
            "R": 62,
            "G": 107,
            "B": 62,
            "A": 255
        }
    },
    register_with = SpaceCore
)

### MAIL ###

Mail_Curry(
    entry_id = "Inflorescence_MailGold",
    entry = i18n("Inflorescence_MailGold")
)

Mail_Curry(
    entry_id = "Inflorescence_MailSilver",
    entry = i18n("Inflorescence_MailSilver")
)

Mail_Curry(
    entry_id = "Inflorescence_MailBronze",
    entry = i18n("Inflorescence_MailBronze")
)

Mail_Curry(
    entry_id = "Inflorescence_MailInitiation",
    entry = i18n("Inflorescence_MailInitiation")
)

### CURRENCY ###

m.PREFIX_WITH_MODID = True

Gold = Flower_Currency(
    entry_id = "_GoldBouquet",
    entry = {
        "Name": "Gold Bouquet",
        "DisplayName": i18n("GoldBouquet_name"),
        "Description": i18n("GoldBouquet_desc"),
        "Price": 500,
        "SpriteIndex": 2,
        "ContextTags": [
            "color_gold"
        ]
    }
)

Silver = Flower_Currency(
    entry_id = "_SilverBouquet",
    entry = {
        "Name": "Silver Bouquet",
        "DisplayName": i18n("SilverBouquet_name"),
        "Description": i18n("SilverBouquet_desc"),
        "Price": 250,
        "SpriteIndex": 1,
        "ContextTags": [
            "color_iron"
        ]
    }
)

Bronze = Flower_Currency(
    entry_id = "_BronzeBouquet",
    entry = {
        "Name": "Bronze Bouquet",
        "DisplayName": i18n("BronzeBouquet_name"),
        "Description": i18n("BronzeBouquet_desc"),
        "Price": 100,
        "SpriteIndex": 0,
        "ContextTags": [
            "color_orange"
        ]
    }
)

### ITEMS ###

ObjectCurry(
    entry_id = "_PowerGro",
    entry = {
        "Name": "Power Gro",
        "DisplayName": i18n("PowerGro_name"),
        "Description": i18n("PowerGro_desc"),
        "Type": "Basic",
        "Category": -19,
        "Price": 200,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 3,
        "ContextTags": [
            "not_giftable",
            "prevent_loss_on_death"
        ]
    }
)

ObjectCurry(
    entry_id = "_ScoreRadio",
    entry = {
        "Name": "Score Radio",
        "DisplayName": i18n("ScoreRadio_name"),
        "Description": i18n("ScoreRadio_desc"),
        "Type": "Basic",
        "Category": -99,
        "Price": 25,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 4,
        "ContextTags": [
            "not_giftable",
            "prevent_loss_on_death"
        ]
    }
)

ObjectCurry(
    entry_id = "_InformantEarpiece",
    entry = {
        "Name": "Informant Earpiece",
        "DisplayName": i18n("InformantEarpiece_name"),
        "Description": i18n("InformantEarpiece_desc"),
        "Type": "Basic",
        "Category": -99,
        "Price": 15,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 5,
        "ContextTags": [
            "not_giftable",
            "prevent_loss_on_death"
        ]
    }
)

ObjectCurry(
    entry_id = "_Ash",
    entry = {
        "Name": "Ash",
        "DisplayName": i18n("Ash_name"),
        "Description": i18n("Ash_desc"),
        "Type": "Basic",
        "Category": -16,
        "Price": 1,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 10,
        "ContextTags": [
            "color_gray"
        ]
    }
)

ObjectCurry(
    entry_id = "_Bouquet",
    entry = {
        "Name": "{{ModID}}_Bouquet",
        "DisplayName": i18n("Bouquet_name"),
        "Description": i18n("Bouquet_desc"),
        "Type": "Basic",
        "Category": -26,
        "Price": 200,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 16,
        "ContextTags": [
            "color_green"
        ]
    }
)

ObjectCurry(
    entry_id = "_Lye",
    entry = {
        "Name": "Lye",
        "DisplayName": i18n("Lye_name"),
        "Description": i18n("Lye_desc"),
        "Type": "Basic",
        "Category": -26,
        "Price": 5,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 11,
        "ContextTags": [
            "color_sand"
        ]
    }
)

ObjectCurry(
    entry_id = "_Soap",
    entry = {
        "Name": "Soap",
        "DisplayName": i18n("Soap_name"),
        "Description": i18n("Soap_desc"),
        "Type": "Basic",
        "Category": -26,
        "Price": 100,
        "Texture": "{{ModID}}/Objects",
        "SpriteIndex": 26,
        "ContextTags": [
            "color_sand"
        ]
    }
)

### RECIPES ###

RecipeCurry(
    entry_id = "_AshFurnace",
    entry = "388 25 390 100 335 15 337 1/Home/{{ModID}}_AshFurnace/true/"
)

RecipeCurry(
    entry_id = "_Bouquet",
    entry = "597 1 591 1 421 1/Home/{{ModID}}_Bouquet/false/"
)

RecipeCurry(
    entry_id = "_SoapStation",
    entry = "335 10 343 10 370 2/Home/{{ModID}}_SoapStation/true/"
)

### BIG CRAFTABLES ###

BigCraftableCurry(
    entry_id = "_AshFurnace",
    entry = {
        "SpriteIndex": 10,
        "Name": "{{ModID}}_AshFurnace",
        "DisplayName": i18n("AshFurnace_name"),
        "Description": i18n("AshFurnace_desc"),
    }
)

BigCraftableCurry(
    entry_id = "_SoapStation",
    entry = {
        "SpriteIndex": 11,
        "Name": "{{ModID}}_SoapStation",
        "DisplayName": i18n("SoapStation_name"),
        "Description": i18n("SoapStation_desc"),
    }
)

### MACHINES ###

m.PREFIX_WITH_MODID = False

MachineCurry(
    targetfield = [ "(BC)20", "OutputRules" ],
    entry = {
        "Id": "{{ModID}}_Ash",
        "Triggers": [
            {
                "RequiredItemId": "(O){{ModID}}_Ash",
                "RequiredCount": 10
            }
        ],
        "OutputItem": [
            {
                "ItemId": "(O){{ModID}}_Lye",
                "MinStack": 1
            }
        ],
        "MinutesUntilReady": 1600
    }
)

MachineCurry(
    entry_id = "(BC){{ModID}}_SoapStation",
    entry = {
        "LoadEffects": [
            {
                "Sounds": [
                    {
                        "Id": "bubbles",
                        "Delay": 0
                    }
                ]
            }
        ],
        "WobbleWhileWorking": True,
        "OutputRules": [
            {
                "Id": "{{ModID}}_Soap",
                "Triggers": [
                    {
                        "RequiredTags": [ "inflor_flower_item" ],
                        "RequiredCount": 1
                    }
                ],
                "OutputItem": [
                    {
                        "ItemId": "selph.ExtraMachineConfig_FLAVORED_ITEM {{ModID}}_Soap DROP_IN_ID",
                        "PriceModifiers": [
                            {
                                "Modification": "Add",
                                "Amount": 100
                            },
                            {
                                "Modification": "Multiply",
                                "Amount": 2
                            }
                        ],
                        "ObjectDisplayName": i18n("Soap_flavoredname"),
                        "PreserveId": "DROP_IN",
                        "MinStack": 1,
                        "CopyColor": True
                    }
                ],
                "MinutesUntilReady": 100
            }
        ],
        "AdditionalConsumedItems": [
            {
                "ItemId": "(O){{ModID}}_Lye",
                "RequiredCount": 1
            },
            {
                "ItemId": "(O)247",
                "RequiredCount": 1
            }
        ]
    }
)

MachineCurry(
    entry_id = "(BC){{ModID}}_AshFurnace",
    entry = {
        "LoadEffects": [
            {
                "Sounds": [
                    {
                        "Id": "furnace",
                        "Delay": 0
                    }
                ]
            }
        ],
        "WobbleWhileWorking": True,
        "OutputRules": [
            {
                "Id": "{{ModID}}_Ash",
                "Triggers": [
                    {
                        "RequiredItemId": "388",
                        "RequiredCount": 5
                    }
                ],
                "OutputItem": [
                    {
                        "ItemId": "{{ModID}}_Ash",
                        "MinStack": 5
                    }
                ],
                "MinutesUntilReady": 200
            }
        ]
    }
)

m.PREFIX_WITH_MODID = True

### SHOP ###

ShopsCurry(
    entry_id = "_Inflor_Shop",
    entry = {
        "Owners": [
            {
                "Name": "AnyOrNone",
                "Dialogues": [
                    {
                        "Id": "{{ModID}}_Inflor_Silent",
                        "Dialogue": "..."
                    },
                    {
                        "Id": "{{ModID}}_Inflor_Cold",
                        "Condition": "SEASON winter",
                        "Dialogue": "It's so cold..."
                    }
                ]
            }
        ],
        "Items": [

            ### SPRINKLERS ###

            {
                "Id": "{{ModID}}_Sprinkler",
                "ItemId": "(O)599",
                "TradeItemId": Bronze.entry_id,
                "TradeItemAmount": 1,
                "AvailableStock": 3
            },
            {
                "Id": "{{ModID}}_QualitySprinkler",
                "ItemId": "(O)621",
                "TradeItemId": Bronze.entry_id,
                "TradeItemAmount": 3,
                "AvailableStock": 5
            },
            {
                "Id": "{{ModID}}_IridiumSprinkler",
                "ItemId": "(O)645",
                "TradeItemId": Silver.entry_id,
                "TradeItemAmount": 2,
                "AvailableStock": 3
            },

            ### SEEDS ###

            {
                "Id": "{{ModID}}_MixedSeeds",
                "ItemId": "(O)770",
                "Price": 150,
                "AvailableStock": 10
            },

            {
                "Id": "{{ModID}}_MixedFlowerSeeds",
                "ItemId": "MixedFlowerSeeds",
                "Price": 100,
                "AvailableStock": 5
            },

            {
                "Id": "{{ModID}}_MixedSeeds2",
                "ItemId": "(O)770",
                "TradeItemId": Bronze.entry_id,
                "TradeItemAmount": 1,
                "AvailableStock": 5,
                "MinStack": 5
            },

            {
                "Id": "{{ModID}}_MixedFlowerSeeds2",
                "ItemId": "MixedFlowerSeeds",
                "TradeItemId": Bronze.entry_id,
                "TradeItemAmount": 1,
                "AvailableStock": 10,
                "MinStack": 5
            },

            {
                "Id": "{{ModID}}_FairySeeds",
                "ItemId": "(O)425",
                "TradeItemId": Silver.entry_id,
                "TradeItemAmount": 1,
                "Condition": "Season winter"
            },

            ### BOUQUETS ###

            {
                "Id": "{{ModID}}_SilverBouquet",
                "ItemId": Silver.entry_id,
                "TradeItemId": Bronze.entry_id,
                "TradeItemAmount": 5
            },

            {
                "Id": "{{ModID}}_GoldBouquet",
                "ItemId": Gold.entry_id,
                "TradeItemId": Silver.entry_id,
                "TradeItemAmount": 5
            },

            {
                "Id": "{{ModID}}_SilverBouquet2",
                "ItemId": Silver.entry_id,
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 1,
                "MinStack": 3
            },

            {
                "Id": "{{ModID}}_BronzeBouquet2",
                "ItemId": Bronze.entry_id,
                "TradeItemId": Silver.entry_id,
                "TradeItemAmount": 1,
                "MinStack": 3
            },

            ### SPECIAL ###

            {
                "Id": "{{ModID}}_InformantEarpiece",
                "ItemId": "(O){{ModID}}_InformantEarpiece",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 5,
                "Condition": "TIME 2200"
            },

            {
                "Id": "{{ModID}}_ScoreRadio",
                "ItemId": "(O){{ModID}}_ScoreRadio",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 1
            },

            {
                "Id": "{{ModID}}_StardropTea",
                "ItemId": "(O)StardropTea",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 20,
                "AvailableStock": 1,
                "Condition": "Season fall"
            },

            {
                "Id": "{{ModID}}_PowerGro",
                "ItemId": "(O){{ModID}}_PowerGro",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 3,
                "AvailableStock": 5
            },

            ### RECIPES ###

            {
                "Id": "{{ModID}}_AshFurnace",
                "ItemId": "(BC){{ModID}}_AshFurnace",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 10,
                "AvailableStock": 1,
                "IsRecipe": True
            },

            {
                "Id": "{{ModID}}_Bouquet",
                "ItemId": "(O){{ModID}}_Bouquet",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 5,
                "AvailableStock": 1,
                "IsRecipe": True
            },

            {
                "Id": "{{ModID}}_SoapStation",
                "ItemId": "(BC){{ModID}}_SoapStation",
                "TradeItemId": Gold.entry_id,
                "TradeItemAmount": 3,
                "AvailableStock": 1,
                "IsRecipe": True
            }
        ]
    }
)

### SPACECORE ###

SCBouquet(
    entry_id = "_BronzeBouquet"
)

SCBouquet(
    entry_id = "_SilverBouquet"
)

SCBouquet(
    entry_id = "_GoldBouquet"
)

### ASSETS ###

m.FetchImage("../assets/inflorescence/objects.png", "{{ModID}}/Objects")
m.FetchImage("../assets/inflorescence/shop.png", "{{ModID}}/Shop")

### BUILD ###

m.Create()