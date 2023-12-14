import csv
import json

class PhoneBookDatabase:
    def __init__(self):
        self.phone_book = []

    def read_from_csv(self, file_path):
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                self.phone_book = list(csv_reader)
            return True, "Read successful"
        except FileNotFoundError:
            return False, f"File not found: {file_path}"
        except Exception as e:
            return False, f"Error reading from CSV: {str(e)}"

    def read_from_json(self, file_path):
        try:
            with open(file_path, 'r') as json_file:
                self.phone_book = json.load(json_file)
            return True, "Read successful"
        except FileNotFoundError:
            return False, f"File not found: {file_path}"
        except Exception as e:
            return False, f"Error reading from JSON: {str(e)}"

    def execute_query(self, query):
        query_tokens = query.split()
        command = query_tokens[0].upper()

        if command == 'SELECT':
            return self._select_records(query_tokens)
        elif command == 'INSERT':
            return self._insert_record(query_tokens)
        elif command == 'DELETE':
            return self._delete_record(query_tokens)
        else:
            return False, "Invalid query"

    def _select_records(self, query_tokens):
        try:
            if len(query_tokens) > 3 and query_tokens[3].upper() == 'FROM' and query_tokens[4].lower() == 'phone_records':
                # Implement SELECT operation based on query_tokens
                # For simplicity, this example assumes all records are selected.
                selected_records = self.phone_book[:10]  # Select the first 10 records
                self._print_records(selected_records)
                return True, selected_records
            else:
                return False, "Invalid SELECT query"
        except Exception as e:
            return False, f"Error executing SELECT query: {str(e)}"

    def _insert_record(self, query_tokens):
        try:
            if len(query_tokens) > 8 and query_tokens[1].upper() == 'INTO' and query_tokens[2].lower() == 'phone_records' \
                    and query_tokens[3].upper() == 'VALUES':
                # Implement INSERT operation based on query_tokens
                # For simplicity, this example assumes a fixed format for the query.
                new_record = {
                    'Name': query_tokens[4][1:-1],  # Remove quotes around the value
                    'Email': query_tokens[6][1:-1],
                    'Phone1': query_tokens[8][1:-1],
                    'Phone2': query_tokens[10][1:-1]
                }
                self.phone_book.append(new_record)
                print("Record inserted successfully")
                return True, "Record inserted successfully"
            else:
                return False, "Invalid INSERT query"
        except Exception as e:
            return False, f"Error executing INSERT query: {str(e)}"

    def _delete_record(self, query_tokens):
        try:
            if len(query_tokens) > 6 and query_tokens[1].upper() == 'FROM' and query_tokens[2].lower() == 'phone_records' \
                    and query_tokens[3].upper() == 'WHERE' and query_tokens[4].lower() == 'name':
                # Implement DELETE operation based on query_tokens
                # For simplicity, this example assumes a fixed format for the query.
                name_to_delete = query_tokens[6][1:-1]  # Remove quotes around the value
                self.phone_book = [record for record in self.phone_book if record['Name'] != name_to_delete]
                print(f"Record(s) with name '{name_to_delete}' deleted successfully")
                return True, f"Record(s) with name '{name_to_delete}' deleted successfully"
            else:
                return False, "Invalid DELETE query"
        except Exception as e:
            return False, f"Error executing DELETE query: {str(e)}"

    def _print_records(self, records):
        for record in records:
            print(record)


# Example usage:
database = PhoneBookDatabase()

# Read from CSV file
read_csv_result, read_csv_message = database.read_from_csv(r"C:\Data Science\Assignments\Vengage\New Microsoft Excel Worksheet.csv")
if not read_csv_result:
    print(f"Error: {read_csv_message}")

# Read from JSON file
read_json_result, read_json_message = database.read_from_json(r"C:\Data Science\Assignments\Vengage\New Text Document.json")
if not read_json_result:
    print(f"Error: {read_json_message}")

# SQL-like queries
select_query = "SELECT * FROM phone_records;"
insert_query = "INSERT INTO phone_records(Name, Email, Phone1, Phone2) VALUES('Test', 'test@test.xyz', '1234456', '1233233');"
delete_query = "DELETE FROM phone_records WHERE name='John';"
select_with_condition_query = "SELECT * FROM phone_records WHERE name='Doe';"

# Execute queries
select_result, _ = database.execute_query(select_query)
insert_result, _ = database.execute_query(insert_query)
delete_result, _ = database.execute_query(delete_query)
select_with_condition_result, _ = database.execute_query(select_with_condition_query)
