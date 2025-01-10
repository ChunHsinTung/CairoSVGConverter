# CairoSVGConverter
Converting and resizing SVG file to PNG at the same time using CairoSVG library.

### Prerequisites
Install Cairo first on your machine, the the documentation as the [reference](https://cairosvg.org/documentation/).

### Instruction
I use the function `cairo.svg2png` to do the job, with the argument `file_obj`, `write_to`, `output_height`, `output_width`, `dpi` for specifying the <ins>original file path</ins>, <ins>destination path</ins>, <ins>output file height</ins>, <ins>output file width</ins> and <ins>output file dpi</ins> respectively.
