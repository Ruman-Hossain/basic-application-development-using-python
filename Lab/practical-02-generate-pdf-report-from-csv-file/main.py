from csv_reader import read_csv_data
from formatter import format_table_data
from pdf_generator import generate_pdf
from logger import record_job
from utils import validate_data


def main():
    data = read_csv_data()

    if not validate_data(data):
        return

    table_data = format_table_data(data)

    generate_pdf(table_data)

    record_job(job_description="PDF report generated successfully")

    print("PDF report generated successfully!")


if __name__ == "__main__":
    main()