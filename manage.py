from app import manager
from scripts import CreateUser, CreateTables

# manager
manager.add_command("create_user", CreateUser())
manager.add_command("create_tables", CreateTables())

manager.run()
