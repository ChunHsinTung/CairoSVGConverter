import cairosvg, os
for i in range(0, 36):
    with open(os.path.join(os.path.join(os.path.expanduser("~"), "Desktop", "ReportV2", "weathericon"), f"icon_{i+1}.svg")) as file:
        cairosvg.svg2png(file_obj=file, write_to=os.path.join(os.path.join(os.path.expanduser("~"), "Desktop", "ReportV2", "weathericon"), f"icon_{i+1}.png"), output_width=100, output_height=100, dpi=120)
