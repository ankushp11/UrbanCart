# Register the commands with Flask CLI
def register_migration_commands(app, migration_manager):
    """Register all migration commands with the Flask CLI."""
    app.cli.add_command(migration_manager.drop_database)
    app.cli.add_command(migration_manager.init_database)
    app.cli.add_command(migration_manager.migrate_database)
    app.cli.add_command(migration_manager.upgrade_database)
    app.cli.add_command(migration_manager.downgrade_database)
