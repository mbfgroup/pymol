# Create a simple name for the moving atoms
select mov_atoms /0413_mode_0010_all///UNK`42/N or /0413_mode_0010_all///UNK`14/N or /0413_mode_0010_all///UNK`5/N or /0413_mode_0010_all///UNK`10/N

# Create a simple name for the target atoms
select tar_atoms /cpc_a84_WT_qm/CYC/C/CYC`300/N*
python
for i in range(1, 11):
    print(f"Aligning state {i}...")
    cmd.do(f"set_state /0413_mode_0010_all, {i}")
    cmd.pair_fit("mov_atoms", "tar_atoms")
python end
