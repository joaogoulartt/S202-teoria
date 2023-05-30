from database import Database
from family_db import FamilyDatabase

db = Database("bolt://3.236.192.43:7687", "neo4j", "tire-buildings-sled")

family_db = FamilyDatabase(db)

print("Família:")
print(family_db.get_family())
print("")
print("Quem da família é Advogado?")
print(family_db.get_lawyers())
print("")
print("Com quem Eunice foi casada?")
print(family_db.get_married("Eunice"))
print("")
print("Quem são os netos de Iracema?")
print(family_db.get_grandchildren("Iracema"))
print("")
print("De quem Karen é cunhada?")
print(family_db.get_siblings_in_law("Karen"))

db.close()