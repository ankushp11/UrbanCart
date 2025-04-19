#! /bin/bash

echo "Running the migration script..."
DIRECTORY=/urbancart/app/migrations
echo "Starting Migration..."
if [ ! -d "$DIRECTORY" ]; then
  echo "$DIRECTORY does not exist."
  echo "Creating migration folder..."
  flask init_database
  echo "Migration folder created..."
fi
echo "Checking for available migrations..."
flask migrate_database
flask upgrade_database
echo "Done. Migration script completed successfully."
