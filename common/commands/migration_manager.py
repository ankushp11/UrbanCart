from flask.cli import click, with_appcontext
from flask_migrate import init, migrate, upgrade, downgrade


class DatabaseMigrationManager:
    def __init__(self, db):
        self.db = db

    @click.command(name="drop_database")
    @with_appcontext
    def drop_database(self):
        self.db.drop_all()

    @staticmethod
    @click.command(name="init_database")
    @with_appcontext
    def init_database():
        print("hello")
        init(directory="migrations", multidb=False)

    @staticmethod
    @click.command(name="migrate_database")
    @with_appcontext
    def migrate_database():
        migrate(
            directory="migrations",
            message=None,
            sql=False,
            head="head",
            splice=False,
            branch_label=None,
            version_path=None,
            rev_id=None,
        )

    @staticmethod
    @click.command(name="upgrade_database")
    @with_appcontext
    def upgrade_database():
        upgrade(directory="migrations", revision="head", sql=False, tag=None)

    @staticmethod
    @click.command(name="downgrade_database")
    @with_appcontext
    def downgrade_database():
        downgrade(directory="migrations", revision="-1", sql=False, tag=None)
