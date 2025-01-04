from ..constants.services import Services


def run_migration(service_name):
    try:
        print(f"Checking for migrations for service: {service_name}")
        pass
    except Exception as e:
        print("Something went wrong!!")


def migrate_all_services():
    service_list = Services.SERVICES_LIST

    if not service_list:
        print("No services found to execute migrations!!")

    for service_name in service_list:
        run_migration(service_name)


def execute_all_migrations():
    try:
        migrate_all_services()
    except Exception as e:
        print("Something went wrong!!")


if __name__ == "__main__":
    execute_all_migrations()