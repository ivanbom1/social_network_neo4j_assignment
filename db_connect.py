from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", 
                              auth=("neo4j", "password"))
session = driver.session()

session.run("CREATE CONSTRAINT unique_user_id IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE")
session.run("CREATE CONSTRAINT unique_username IF NOT EXISTS FOR (u:User) REQUIRE u.username IS UNIQUE")

session.close()
driver.close()

print("Done")