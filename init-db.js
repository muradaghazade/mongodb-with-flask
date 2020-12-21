// db = db.getSiblingDB("mongo-database")
db.createUser(
    {
        user: "muradaghazada",
        pwd: "885522",
        roles: [
            {
                role: "readWrite",
                db: "mongo-database"
            }
        ]
    }
)