#!/usr/bin/env python3
#
# GlobalChem - Emerging PerfluoroAlkyls
#
# -------------------------------------

class EmergingPerFluoroAlkyls(object):

    def __init__(self):

        self.name = 'emerging_perfluoro_alkyls'

    @staticmethod
    def get_smiles():

        smiles = {
            'perfluorohexanoic acid': 'C(=O)(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluoroheptanoic acid': 'C(=O)(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluorononanoic acid': 'C(=O)(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluorodecanoic acid': 'C(=O)(C(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluorobutanesulfonic acid': 'C(C(C(F)(F)S(=O)(=O)O)(F)F)(C(F)(F)F)(F)F',
            'perfluorohexanesulfonic acid': 'C(C(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F)(C(C(F)(F)F)(F)F)(F)F',
            'perfluoroundecanoic acid': 'C(=O)(C(C(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            '2-(N-ethyl-perfluorooctane sulfanamido) acetic acid': 'CCN(CC(=O)O)S(=O)(=O)C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F',
            '2-(N-Methyl-perfluorooctane sulfanamido) acetic acid': 'CN(CC(=O)O)S(=O)(=O)C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F',
            'hexafluoropropylene Oxide Dimer Acid': 'C1(C(O1)(F)F)(C(F)(F)F)F',
            'perfluorotetradecanoic acid': 'C(=O)(C(C(C(C(C(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluorotridecanoic acid': 'C(=O)(C(C(C(C(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            '4,8-dioxa-3H-perfluorononanoic': 'C(C(C(=O)O)(F)F)(OC(C(C(OC(F)(F)F)(F)F)(F)F)(F)F)F',
            '6:2 chlorinated polyfluorinated ether sulfonic acid': 'FC(Cl)(C(F)(C(F)(F)C(F)(F)C(F)(F)OC(F)(F)C(F)(S(=O)(O[K])=O)F)F)F',
            # '8:2 chlorinated polyfluorinated ether sulfonic acid': '',
            'perfluorobutanoic acid': 'FC(F)(C(F)(C(O)=O)F)C(F)(F)F',
            'perfluoro-n-pentanoic acid': 'C(=O)(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)O',
            'nafion byproduct 2': 'C(C(F)(F)F)(OC(C(C(F)(F)F)(OC(C(F)(F)S(=O)(=O)O)(F)F)F)(F)F)F',
            'perfluoro-3,5,7,9-tetraoxadecanoic acid': 'C(=O)(C(OC(OC(OC(OC(F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            'perfluoro-3,5,7,9,11-pentaoxadodecanoic acid': 'C(=O)(C(OC(OC(OC(OC(OC(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)O',
            '2,2,3,3-tetrafluoro-3-((1,1,1,2,3,3-hexafluoro-3-(1,2,2,2-tetrafluoroethoxy)propan-2-yl)oxy)propanoic acid': 'C(=O)(C(C(F)(F)F)(OC(C(OC(C(C(F)(F)F)(F)F)(F)F)(F)F)(C(F)(F)F)F)F)O',
            'h,1h,2h,2h-perfluorooctanesulfonic acid': 'C(C(C(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F)(F)F)(C(C(C(F)(F)F)(F)F)(F)F)(F)F',
            '2-(perfluorooctyl)ethane-1-sulfonic acid': 'C(CS(=O)(=O)O)C(C(C(C(C(C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F)(F)F',
            'perfluoropentanesulfonic acid': 'C(C(C(F)(F)F)(F)F)(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F',
            'perfluoroheptanesulfonic acid': 'C(C(C(C(F)(F)F)(F)F)(F)F)(C(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F)(F)F',
            'perfluorononanesulfonic acid': 'C(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(C(C(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F)(F)F)(F)F',
            'perfluorodecanesulfonic acid': 'C(C(C(C(C(C(F)(F)S(=O)(=O)O)(F)F)(F)F)(F)F)(F)F)(C(C(C(C(F)(F)F)(F)F)(F)F)(F)F)(F)F',
            'hexafluoropropylene-oxide-trimer-acid': 'C(=O)(C(C(F)(F)F)(OC(C(C(F)(F)F)(OC(C(C(F)(F)F)(F)F)(F)F)F)(F)F)F)F',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'perfluorohexanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluoroheptanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluorononanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluorodecanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluorobutanesulfonic acid': '[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluorohexanesulfonic acid': '[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluoroundecanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            '2-(N-ethyl-perfluorooctane sulfanamido) acetic acid': '[#6]-[#6]-[#7](-[#6]-[#6](=[#8])-[#8])-[#16](=[#8])(=[#8])-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            '2-(N-Methyl-perfluorooctane sulfanamido) acetic acid': '[#6]-[#7](-[#6]-[#6](=[#8])-[#8])-[#16](=[#8])(=[#8])-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'hexafluoropropylene Oxide Dimer Acid': '[#6]1(-[#6](-[#8]-1)(-[#9])-[#9])(-[#6](-[#9])(-[#9])-[#9])-[#9]',
            'perfluorotetradecanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluorotridecanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            '4,8-dioxa-3H-perfluorononanoic': '[#6](-[#6](-[#6](=[#8])-[#8])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#6](-[#8]-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#9]',
            '6:2 chlorinated polyfluorinated ether sulfonic acid': '[#9]-[#6](-[#17])(-[#6](-[#9])(-[#6](-[#9])(-[#9])-[#6](-[#9])(-[#9])-[#6](-[#9])(-[#9])-[#8]-[#6](-[#9])(-[#9])-[#6](-[#9])(-[#16](=[#8])(-[#8]-[K])=[#8])-[#9])-[#9])-[#9]',
            'perfluorobutanoic acid': '[#9]-[#6](-[#9])(-[#6](-[#9])(-[#6](-[#8])=[#8])-[#9])-[#6](-[#9])(-[#9])-[#9]',
            'perfluoro-n-pentanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'nafion byproduct 2': '[#6](-[#6](-[#9])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])-[#9])(-[#9])-[#9])-[#9]',
            'perfluoro-3,5,7,9-tetraoxadecanoic acid': '[#6](=[#8])(-[#6](-[#8]-[#6](-[#8]-[#6](-[#8]-[#6](-[#8]-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            'perfluoro-3,5,7,9,11-pentaoxadodecanoic acid': '[#6](=[#8])(-[#6](-[#8]-[#6](-[#8]-[#6](-[#8]-[#6](-[#8]-[#6](-[#8]-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#8]',
            '2,2,3,3-tetrafluoro-3-((1,1,1,2,3,3-hexafluoro-3-(1,2,2,2-tetrafluoroethoxy)propan-2-yl)oxy)propanoic acid': '[#6](=[#8])(-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#8]-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#9])(-[#9])-[#9])-[#9])-[#9])-[#8]',
            'h,1h,2h,2h-perfluorooctanesulfonic acid': '[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            '2-(perfluorooctyl)ethane-1-sulfonic acid': '[#6](-[#6]-[#16](=[#8])(=[#8])-[#8])-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluoropentanesulfonic acid': '[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluoroheptanesulfonic acid': '[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluorononanesulfonic acid': '[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'perfluorodecanesulfonic acid': '[#6](-[#6](-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#16](=[#8])(=[#8])-[#8])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#6](-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9]',
            'hexafluoropropylene oxide trimer acid': '[#6](=[#8])(-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#8]-[#6](-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#9])-[#9])(-[#9])-[#9])-[#9])(-[#9])-[#9])-[#9])-[#9]',
        }

        return smarts
