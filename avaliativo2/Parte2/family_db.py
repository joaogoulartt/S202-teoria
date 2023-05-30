
class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    def get_family(self):
        query = "MATCH (n) RETURN n.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_lawyers(self):
        query = "MATCH (n:Advogado) RETURN n.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_married(self, name):
        query = "MATCH (n:Pessoa)-[:VIUVA_DE]->(m:Pessoa) WHERE n.name = $name RETURN m.name AS name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]
    
    def get_grandchildren(self, name):
        query = "MATCH (n:Pessoa)-[:PAI_DE]->(m:Pessoa)-[:PAI_DE]->(o:Pessoa) WHERE n.name = $name RETURN o.name AS name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]
    
    def get_siblings_in_law(self, name):
        query = "MATCH (n:Pessoa)-[:ESPOSA_DE]->(m:Pessoa)-[:IRMAO_DE]-(o:Pessoa) WHERE n.name = $name RETURN o.name AS name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]