from data_input import get_fruit_data
from storage import store_data_to_csv
from summary import print_fruits_summary
from logger import record_job
from utils import reset_inventory_file


def main():
    # Optional: reset file on start
    reset_inventory_file()

    while True:
        print("\nInventory Management")
        print("1. Add New Fruit Item")
        print("2. View Fruit Items Summary")
        print("3. Exit")

        choice = input("Choose an Option: ")

        if choice == '1':
            data = get_fruit_data()
            store_data_to_csv(data)
            record_job(job_description=f"Added Fruit Item: {data}")
            print("Fruit Item Added Successfully!")

        elif choice == '2':
            print_fruits_summary()

        elif choice == '3':
            print("Exiting The Program.")
            break

        else:
            print("Invalid Choice, Please Try Again")


if __name__ == "__main__":
    main()