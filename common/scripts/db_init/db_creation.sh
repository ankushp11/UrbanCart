#!/bin/bash
set -e

# Ensure the POSTGRES_MULTIPLE_DATABASES variable is set
if [ -z "$POSTGRES_MULTIPLE_DATABASES" ]; then
    echo "Error: POSTGRES_MULTIPLE_DATABASES is not set."
    exit 1
fi

# Split the database names into an array
IFS=',' read -r -a DATABASES <<< "$POSTGRES_MULTIPLE_DATABASES"

echo "Databases to create: ${DATABASES[*]}"

# Loop through the databases and create them if they do not exist
for DB in "${DATABASES[@]}"; do
    DB=$(echo $DB | xargs) # Trim whitespace
    echo "Checking database: $DB"
    if ! psql -U "$POSTGRES_USER" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname = '$DB'" | grep -q 1; then
        echo "Database $DB does not exist. Creating it now..."
        psql -U "$POSTGRES_USER" -d postgres -c "CREATE DATABASE $DB;"
    else
        echo "Database $DB already exists. Skipping creation."
    fi
done

echo "Database initialization complete."
