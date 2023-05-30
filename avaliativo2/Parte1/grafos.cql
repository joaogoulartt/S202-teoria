// CRIANDO GRAFOS
CREATE (p:Pessoa:Estagiario {name:'João Victor', age:20, gender: 'M'});
CREATE (p:Pessoa:Gerente {name:'Sueli', age:47, gender: 'F'});
CREATE (p:Pessoa:Empresario {name:'Sandro', age:45, gender: 'M'} );
CREATE (p:Pessoa:Designer {name:'Christian', age:25, gender: 'M'} );
CREATE (p:Pessoa:Estagiario {name:'Laleska', age:27, gender: 'F'} );
CREATE (p:Pessoa:Advogado {name:'Karen', age:27, gender: 'F'} );
CREATE (p:Pessoa:Advogado {name:'Silvio', age:78, gender: 'M'} );
CREATE (p:Pessoa:Advogado {name:'Iracema', age:71, gender: 'F'} );
CREATE (p:Pessoa:Empresario {name:'João', age:67, gender: 'M'} );
CREATE (p:Pessoa:Aposentada {name:'Eunice', age:86, gender: 'F'} );

// CRIANDO RELAÇÕES
MATCH (p1:Pessoa {name:'João Victor'}), (p2:Pessoa {name:'Sueli'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'João Victor'}), (p2:Pessoa {name:'Sandro'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Sueli'}), (p2:Pessoa {name:'Eunice'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Sueli'}), (p2:Pessoa {name:'João'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Sandro'}), (p2:Pessoa {name:'Iracema'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Sandro'}), (p2:Pessoa {name:'Silvio'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Christian'}), (p2:Pessoa {name:'Sandro'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'Laleska'}), (p2:Pessoa {name:'Sandro'}) CREATE (p2)-[:PAI_DE]->(p1);
MATCH (p1:Pessoa {name:'João Victor'}), (p2:Pessoa {name:'Christian'}) CREATE (p2)-[:IRMAO_DE{mesma_mae: 'Não'}]->(p1);
MATCH (p1:Pessoa {name:'João Victor'}), (p2:Pessoa {name:'Laleska'}) CREATE (p2)-[:IRMAO_DE{mesma_mae: 'Não'}]->(p1);
MATCH (p1:Pessoa {name:'Christian'}), (p2:Pessoa {name:'Laleska'}) CREATE (p2)-[:IRMAO_DE{mesma_mae: 'Sim'}]->(p1);
MATCH (p1:Pessoa {name:'Christian'}), (p2:Pessoa {name:'Karen'}) CREATE (p2)-[:ESPOSA_DE]->(p1);
MATCH (p1:Pessoa {name:'João'}), (p2:Pessoa {name:'Eunice'}) CREATE (p2)-[:VIUVA_DE]->(p1);