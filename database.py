import pymongo, json, os

with open("config.json") as e:
    infos = json.load(e)
    db_token = infos["dbtoken"]


lardb = pymongo.MongoClient(db_token)
bancodb = lardb["economia"]
usuarios = bancodb["usuarios"]

async def novo_user(usuario):
    filtro = {"discord_id" : usuario.id}
    if usuarios.count_documents(filtro) == 0:
        objeto = {
            "discord_id":usuario.id,
            "carteira":20
        }
        usuario.insert_one(objeto)
        return objeto
    else:
        return False

async def check_eco(usuario):
    await novo_user(usuario)
    filtro = {"discord_id" : usuario.id}
    result = usuario.find(filtro)

    return  result.__getitem__(0)["carteira"]

async def alterar_saldo(usuario,quantidade):
    await novo_user(usuario)

    atual = await check_eco(usuario)

    filtro = {"discord_id" : usuario.id}
    resular= {
        "$set": {
            "carteira": atual+quantidade
        }
    }
    usuarios.update_one(filtro, resular)