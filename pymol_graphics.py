# fun commands to play around with for rendering
bg_color white # so you can get ray tracing in black outline
set ambient, 0.5 # better PyMol lighting
set cartoon_color, hydrogen # I like this color for cartoons
set cartoon_transparency, 0.7
set ray_trace_disco_factor, 0.3 # can play around with this, 0 = strong, 1 = off
# disco only has an effect with ray trace values of 1 - 3
# I like having disco on, you can see kinks/bends in structures better for sticks
set field_of_view, 70 # can play around with this to change perspective
ray # renders the ray image
png filename.png # to save
#  sometimes the waters mess up the surface rendering, so you need to remove waters before trying to render the protein
show surface, polymer # to show surface for the protein
set transparency, 0.7 # 0 is opaque, 1 is fully transparent
# for coloring custom carbons within a selection:
util.cnc("within_5")
color grey50, within_5 and elem c
# for selecting residues within cutoff distance of a selection:
select within_5, byres all within 5 of /cpc_a84_WT_qm/CYC/C/CYC`300
