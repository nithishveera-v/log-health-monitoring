ERROR_LIMIT = 4
LOGIN_LIMIT = 2

errors = 0
warnings = 0
logins = 0

try:
    with open("input_logs.txt") as file:
        for line in file:
            line = line.lower()

            if "error" in line:
                errors += 1
            if "warning" in line:
                warnings += 1
            if "login failed" in line:
                logins += 1

except FileNotFoundError:
    print("Log file not found.")
    

with open("summary_report.txt", "w") as report:
    report.write("LOG SUMMARY\n")
    report.write("-----------\n") 
    report.write(f"Errors   : {errors}\n")
    report.write(f"Warnings : {warnings}\n")
    report.write(f"Logins   : {logins}\n\n")

    if errors > ERROR_LIMIT:
        report.write("Warning: High error count\n")
    if logins > LOGIN_LIMIT:
        report.write("Security alert: Login failures\n")

print("Log analysis completed.")
