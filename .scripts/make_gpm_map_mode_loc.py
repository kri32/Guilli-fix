
input_file = "input.txt"
output_file = "gpm_map_mode_loc.txt"

with open(input_file, "r") as file:
    lines = [line.rstrip() for line in file]

with open(output_file, "w") as file:
    
    template_string = "defined_text = {{\n\tname = gpm_{}_list\n\ttext = {{ trigger = {{ owner = {{ has_relic = {} }} }} localization_key = {}_n }}\n\tdefault = gpm_empty_string\n}}"
    for line in lines:
        if line.startswith("#"):  # Check if the line is a comment
            result = line  # Keep the comment as-is
        elif line.strip():  # Check if the line is not empty
            # Replace all placeholders in the template string with the same value
            result = template_string.format(line, line, line)
        else:  # Keep empty lines as empty
            result = ""

        # Write the result to the output file
        file.write(result + "\n")


print(f"Results have been written to {output_file}")
