def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, got {type(attendees).__name__}")
        return

    # Check if any items in the list aren't dictionaries
    if attendees and any(not isinstance(attendee, dict) for attendee in attendees):
        print("Error: All attendees must be dictionaries")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Create a copy of the template to modify
        processed_template = template

        # Replace placeholders with values or "N/A" if missing
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:  # Handle None values
                value = "N/A"
            processed_template = processed_template.replace(f"{{{placeholder}}}", str(value))

        # Write to output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
