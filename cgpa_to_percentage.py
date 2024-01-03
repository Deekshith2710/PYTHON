def cgpa_to_percentage(cgpa):
    # Conversion formula: CGPA * 9.5
    percentage = cgpa * 9.5
    return percentage

# Get CGPA from user input
cgpa = float(input("Enter your CGPA: "))

# Convert CGPA to percentage
percentage = cgpa_to_percentage(cgpa)

print(f"Your CGPA {cgpa} is equivalent to {percentage}% in percentage.")
