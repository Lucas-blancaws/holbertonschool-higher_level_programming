def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_content = template

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = "{" + key + "}"
            value = attendee.get(key)

            if value is None or value == "":
                output_content = output_content.replace(placeholder, "N/A")
            else:
                output_content = output_content.replace(placeholder, str(value))
    
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated: {output_filename}")
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")
