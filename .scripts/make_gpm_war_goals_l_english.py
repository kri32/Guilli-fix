
input_file = "input.txt"
output_file = "gpm_war_goals_l_english.yml"

with open(input_file, "r") as file:
    lines = [line.rstrip() for line in file]

with open(output_file, "w", encoding="utf-8-sig") as file:
    file.write("### This file is generated by script and does not need any translation. ###\n")
    file.write("l_english:\n")
    
    template_string_r = " war_goal_wg_gpm_{}: \"${}$\"\n war_goal_wg_gpm_{}_desc: \"$gpm_relic_wg_desc$ ${}$\""
    template_string_gpm = " war_goal_wg_{}: \"${}$\"\n war_goal_wg_{}_desc: \"$gpm_relic_wg_desc$ ${}$\""
    for line in lines:
        if line.startswith("#"):
            result = line
        elif line.startswith("gpm_r"): #gpm relics already have the gpm prefix
            result = template_string_gpm.format(line, line, line, line)
        elif line.strip():
            result = template_string_r.format(line, line, line, line)
        else:
            result = ""

        file.write(result + "\n")

print(f"Results have been written to {output_file}")