class oddt_traj(nglview.Structure, nglview.Trajectory):
    
    ext = "pdb"  # or gro, cif, mol2, sdf
    params = {}  # loading options passed to NGL
    
    def __init__(self, protein, initial, conformations):
        self.p = protein
        self.i = initial
        self.c = conformations
        
    def __getattribute__(self, name):
        if name == 'n_frames':
            return self.n_frames

    def get_structure_string(self):
        return self.p.write('pdb') + self.i.write('pdb')

    def get_coordinates(self, index):
        return self.p.coords + self.c[index].coords
        
    def n_frames(self):
        return len(self.c)
    
nglview.ODDTTrajectory = oddt_traj
