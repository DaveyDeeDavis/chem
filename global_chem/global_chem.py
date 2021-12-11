#!/usr/bin/env python3
#
# GlobalChem - Content Variable Store
#
# -----------------------------------


class GlobalChem(object):

    __version__ = "0.9.3"
    __allow_update__ = True

    """

    GlobalChem will be the master class of all variables, as the content store grows we can use this as the parent class.

    """
    
    def _get_common_regex_patterns():
                
        regex_patterns = {
            'mol2': '^@<\w+?>\w+?\n[COMPOUND_ID]\n(.|\n)*?@<TRIPOS>SUBSTRUCTURE\n.*?\n'
        }
        
        return regex_patterns

    def _get_amino_acids():

        amino_acids_smiles = {
            "alanine": "C",  
            "arginine": "CCCCNC(N)=N",
            "asparagine": "CCC(N)=O",
            "aspartic acid": "CC(O)=O",
            "cysteine": "CS",
            "glutamic acid": "CCC(O)=O",
            "glutamine": "CCC(N)=O",
            "glycine": "[H]",
            "histidine": "CC1=CNC=N1",
            "isoleucine": "C(CC)([H])C",
            "leucine": "CC(C)C", 
            "lysine": "CCCCN",
            "methionine": "CCSC",
            "phenylalanine": "CC1=CC=CC=C1", 
            "proline": "C2CCCN2",
            "serine": "CO",
            "threonine": "C(C)([H])O",
            "tryptophan": "CCC1=CNC2=C1C=CC=C2",
            "tyrosine": "CC1=CC=C(O)C=C1",
            "valine": "C(C)C"
        }

        amino_acids_smarts = {
            'alanine':'[#6]',
            'arginine':'[#6]-[#6]-[#6]-[#6]-[#7]-[#6](-[#7])=[#7]',
            'asparagine':'[#6]-[#6]-[#6](-[#7])=[#8]',
            'aspartic acid':'[#6]-[#6](-[#8])=[#8]',
            'cysteine':'[#6]-[#16]',
            'glutamic acid':'[#6]-[#6]-[#6](-[#8])=[#8]',
            'glutamine':'[#6]-[#6]-[#6](-[#7])=[#8]',
            'glycine':'[H]',
            'histidine':'[#6]-[#6]1:[#6]:[#7H]:[#6]:[#7]:1',
            'isoleucine':'[#6H](-[#6]-[#6])-[#6]',
            'leucine':'[#6]-[#6](-[#6])-[#6]',
            'lysine':'[#6]-[#6]-[#6]-[#6]-[#7]',
            'methionine':'[#6]-[#6]-[#16]-[#6]',
            'phenylalanine':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'proline':'[#6]1-[#6]-[#6]-[#6]-[#7]-1',
            'serine':'[#6]-[#8]',
            'threonine':'[#6H](-[#6])-[#8]',
            'tryptophan':'[#6]-[#6]-[#6]1:[#6]:[#7H]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'tyrosine':'[#6]-[#6]1:[#6]:[#6]:[#6](-[#8]):[#6]:[#6]:1',
            'valine':'[#6](-[#6])-[#6]',
        }

        return amino_acids_smiles, amino_acids_smarts

    def _get_common_organic_solvents():

        common_organic_solvents_smiles = {
            'acetic acid': 'CC(=O)O',
            'acetone' : 'CC(=O)C',
            'acetonitrile': 'CC#N',
            'benzene': 'C1=CC=CC=C1',
            'tert-butyl alcohol': 'CC(C)(C)O',
            'tert-butyl methyl ether': 'CC(C)(C)OC',
            'butylated hydroxytoluene': 'CC1=CC(=C(C(=C1)C(C)(C)C)O)C(C)(C)C',
            'chloroform': 'C(Cl)(Cl)Cl',
            '18-crown-6': 'C1COCCOCCOCCOCCOCCO1',
            'cyclohexane': 'C1CCCCC1',
            '1,2-dichloroethane': 'C(CCl)Cl',
            'dichloromethane': 'C(Cl)Cl',
            'diethyl ether': 'CCOCC',
            'diglyme': 'COCCOCCOC',
            '1,2-dimethoxyethane': 'COCCOC',
            'dimethylacetamide': 'CC(=O)N(C)C',
            'dimethylformamide': 'CN(C)C=O',
            'dimethyl sulfoxide': 'CS(=O)C',
            'dioxane': 'C1COCCO1',
            'ethanol': 'CCO',
            'ethyl acetate': 'CCOC(=O)C',
            'ethyl methyl ketone': 'CCC(=O)C',
            'ethylene': 'C=C',
            'ethylene glycol': 'C(CO)O',
            'grease': 'C(C(F)(F)F)OCC(F)(F)F',
            'n-hexane': 'CCCCCC',
            'hexamethylbenzene': 'CC1=C(C(=C(C(=C1C)C)C)C)C',
            'hexamethylphosphoramide': 'CN(C)P(=O)(N(C)C)N(C)C',
            'hexamethyldisiloxane': 'O([Si](C)(C)C)[Si](C)(C)C',
            'methanol': 'CO',
            'nitromethane': 'C[N+](=O)[O-]',
            'n-pentane': 'CCCCC',
            'propylene': 'CC=C',
            '2-propanol': 'CC(C)O',
            'pyridine': 'C1=CC=NC=C1',
            'pyrrole': 'C1=CNC=C1',
            'pyrrolidine': 'C1CCNC1',
            'silicon grease': 'C[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)C',
            'tetrahydrofuran': 'C1CCOC1',
            'toluene': 'CC1=CC=CC=C1',
            'triethylamine': 'CCN(CC)CC',
        }

        common_organic_solvents_smarts = {
            'acetic acid': '[#6]-[#6](=[#8])-[#8]',
            'acetone': '[#6]-[#6](=[#8])-[#6]',
            'acetonitrile': '[#6]-[#6]#[#7]',
            'benzene': '[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tert-butyl alcohol': '[#6]-[#6](-[#6])(-[#6])-[#8]',
            'tert-butyl methyl ether': '[#6]-[#6](-[#6])(-[#6])-[#8]-[#6]',
            'butylated hydroxytoluene': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6](:[#6]:1)-[#6](-[#6])(-[#6])-[#6])-[#8])-[#6](-[#6])(-[#6])-[#6]',
            'chloroform': '[#6](-[#17])(-[#17])-[#17]',
            '18-crown-6': '[#6]1-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-1',
            'cyclohexane': '[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '1,2-dichloroethane': '[#6](-[#6]-[#17])-[#17]',
            'dichloromethane': '[#6](-[#17])-[#17]',
            'diethyl ether': '[#6]-[#6]-[#8]-[#6]-[#6]',
            'diglyme': '[#6]-[#8]-[#6]-[#6]-[#8]-[#6]-[#6]-[#8]-[#6]',
            '1,2-dimethoxyethane': '[#6]-[#8]-[#6]-[#6]-[#8]-[#6]',
            'dimethylacetamide': '[#6]-[#6](=[#8])-[#7](-[#6])-[#6]',
            'dimethylformamide': '[#6]-[#7](-[#6])-[#6]=[#8]',
            'dimethyl sulfoxide': '[#6]-[#16](=[#8])-[#6]',
            'dioxane': '[#6]1-[#6]-[#8]-[#6]-[#6]-[#8]-1',
            'ethanol': '[#6]-[#6]-[#8]',
            'ethyl acetate': '[#6]-[#6]-[#8]-[#6](=[#8])-[#6]',
            'ethyl methyl ketone': '[#6]-[#6]-[#6](=[#8])-[#6]',
            'ethylene': '[#6]=[#6]',
            'ethylene glycol': '[#6](-[#6]-[#8])-[#8]',
            'grease': '[#6](-[#6](-[#9])(-[#9])-[#9])-[#8]-[#6]-[#6](-[#9])(-[#9])-[#9]',
            'n-hexane': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'hexamethylbenzene': '[#6]-[#6]1:[#6](:[#6](:[#6](:[#6](:[#6]:1-[#6])-[#6])-[#6])-[#6])-[#6]',
            'hexamethylphosphoramide': '[#6]-[#7](-[#6])-[#15](=[#8])(-[#7](-[#6])-[#6])-[#7](-[#6])-[#6]',
            'hexamethyldisiloxane': '[#8](-[Si](-[#6])(-[#6])-[#6])-[Si](-[#6])(-[#6])-[#6]',
            'methanol': '[#6]-[#8]',
            'nitromethane': '[#6]-[#7+](=[#8])-[#8-]',
            'n-pentane': '[#6]-[#6]-[#6]-[#6]-[#6]',
            'propylene': '[#6]-[#6]=[#6]',
            '2-propanol': '[#6]-[#6](-[#6])-[#8]',
            'pyridine': '[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'pyrrole': '[#6]1:[#6]:[#7H]:[#6]:[#6]:1',
            'pyrrolidine': '[#6]1-[#6]-[#6]-[#7]-[#6]-1',
            'silicon grease': '[#6]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#8]-[Si](-[#6])(-[#6])-[#6]',
            'tetrahydrofuran': '[#6]1-[#6]-[#6]-[#8]-[#6]-1',
            'toluene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'triethylamine': '[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]'
        }

        return common_organic_solvents_smiles, common_organic_solvents_smarts

    def _get_essential_vitamins():

        vitamins_smiles = {
            'vitamin A': 'CC1=C(C(CCC1)(C)C)C=CC(=CC=CC(=CCO)C)C',
            'vitamin C': 'C(C(C1C(=C(C(=O)O1)O)O)O)O',
            'vitamin D': 'CC(C)CCCC(C)C1CCC2C1(CCCC2=CC=C3CC(CCC3=C)O)C',
            'vitamin E': 'CC1=C(C2=C(CCC(O2)(C)CCCC(C)CCCC(C)CCCC(C)C)C(=C1O)C)C',
            'vitamin K': 'CC1=C(C(=O)C2=CC=CC=C2C1=O)CC=C(C)CCCC(C)CCCC(C)CCCC(C)C',
            'thiamine': 'OCCC1=C(C)[N+](CC2=CN=C(C)N=C2N)=CS1',
            'riboflavin': 'OC[C@H](O)[C@H](O)[C@H](O)CN(C(C=C1C)=C(C=C1C)N=C2C(N3)=O)C2=NC3=O',
            'niacin': 'C1=CC(=CN=C1)C(=O)O',
            'pantothenic acid': 'CC(C)(CO)C(C(=O)NCCC(=O)O)O',
            'biotin': 'C1C2C(C(S1)CCCCC(=O)O)NC(=O)N2',
            'b6': 'CC1=NC=C(C(=C1O)CO)CO',
            'b12': 'CC1=CC2=C(C=C1C)N(C=N2)C3C(C(C(O3)CO)OP(=O)(O)OC(C)CNC(=O)CCC4(C(C5C6(C(C(C(=C(C7=NC(=CC8=NC(=C(C4=N5)C)C(C8(C)C)CCC(=O)N)C(C7(C)CC(=O)N)CCC(=O)N)C)[N-]6)CCC(=O)N)(C)CC(=O)N)C)CC(=O)N)C)O',
            'folate': 'C1=CC(=CC=C1C(=O)NC(CCC(=O)O)C(=O)O)NCC2=CN=C3C(=N2)C(=O)NC(=N3)N',
        }

        vitamin_smarts = {
            'vitamin A':'[#6]-[#6]1=[#6](-[#6](-[#6]-[#6]-[#6]-1)(-[#6])-[#6])-[#6]=[#6]-[#6](=[#6]-[#6]=[#6]-[#6](=[#6]-[#6]-[#8])-[#6])-[#6]',
            'vitamin C':'[#6](-[#6](-[#6]1-[#6](=[#6](-[#6](=[#8])-[#8]-1)-[#8])-[#8])-[#8])-[#8]',
            'vitamin D':'[#6]-[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]1-[#6]-[#6]-[#6]2-[#6]-1(-[#6]-[#6]-[#6]-[#6]-2=[#6]-[#6]=[#6]1-[#6]-[#6](-[#6]-[#6]-[#6]-1=[#6])-[#8])-[#6]',
            'vitamin E':'[#6]-[#6]1:[#6](:[#6]2:[#6](-[#6]-[#6]-[#6](-[#8]-2)(-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]):[#6](:[#6]:1-[#8])-[#6])-[#6]',
            'vitamin K':'[#6]-[#6]1=[#6](-[#6](=[#8])-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1=[#8])-[#6]-[#6]=[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]-[#6]-[#6]-[#6](-[#6])-[#6]',
            'thiamine':'[#8]-[#6]-[#6]-[#6]1:[#6](-[#6]):[#7+](-[#6]-[#6]2:[#6]:[#7]:[#6](-[#6]):[#7]:[#6]:2-[#7]):[#6]:[#16]:1',
            'riboflavin':'[#8]-[#6]-[#6@H](-[#8])-[#6@H](-[#8])-[#6@H](-[#8])-[#6]-[#7]1:[#6]2:[#6]:[#6](-[#6]):[#6](:[#6]:[#6]:2:[#7]:[#6]2:[#6](:[#7H]:[#6](:[#7]:[#6]:1-2)=[#8])=[#8])-[#6]',
            'niacin':'[#6]1:[#6]:[#6](:[#6]:[#7]:[#6]:1)-[#6](=[#8])-[#8]',
            'pantothenic acid':'[#6]-[#6](-[#6])(-[#6]-[#8])-[#6](-[#6](=[#8])-[#7]-[#6]-[#6]-[#6](=[#8])-[#8])-[#8]',
            'biotin':'[#6]1-[#6]2-[#6](-[#6](-[#16]-1)-[#6]-[#6]-[#6]-[#6]-[#6](=[#8])-[#8])-[#7]-[#6](=[#8])-[#7]-2',
            'b6':'[#6]-[#6]1:[#7]:[#6]:[#6](:[#6](:[#6]:1-[#8])-[#6]-[#8])-[#6]-[#8]',
            'b12':'[#6]-[#6]1:[#6]:[#6]2:[#6](:[#6]:[#6]:1-[#6]):[#7](:[#6]:[#7]:2)-[#6]1-[#6](-[#6](-[#6](-[#8]-1)-[#6]-[#8])-[#8]-[#15](=[#8])(-[#8])-[#8]-[#6](-[#6])-[#6]-[#7]-[#6](=[#8])-[#6]-[#6]-[#6]1(-[#6](-[#6]2-[#6]3(-[#6](-[#6](-[#6](=[#6](-[#6]4=[#7]-[#6](=[#6]-[#6]5=[#7]-[#6](=[#6](-[#6]-1=[#7]-2)-[#6])-[#6](-[#6]-5(-[#6])-[#6])-[#6]-[#6]-[#6](=[#8])-[#7])-[#6](-[#6]-4(-[#6])-[#6]-[#6](=[#8])-[#7])-[#6]-[#6]-[#6](=[#8])-[#7])-[#6])-[#7-]-3)-[#6]-[#6]-[#6](=[#8])-[#7])(-[#6])-[#6]-[#6](=[#8])-[#7])-[#6])-[#6]-[#6](=[#8])-[#7])-[#6])-[#8]',
            'folate':'[#6]1:[#6]:[#6](:[#6]:[#6]:[#6]:1-[#6](=[#8])-[#7]-[#6](-[#6]-[#6]-[#6](=[#8])-[#8])-[#6](=[#8])-[#8])-[#7]-[#6]-[#6]1:[#6]:[#7]:[#6]2:[#6](:[#7]:1):[#6](=[#8]):[#7H]:[#6](:[#7]:2)-[#7]',
        }

        return vitamins_smiles, vitamin_smarts

    def _get_open_smiles_functional_groups():

        functional_groups_smiles = {
            "1,1,1-trifluoroethane": "CC(F)(F)F",
            "1,1'-biphenyl": "C1(C2=CC=CC=C2)=CC=CC=C1",
            "1H-indene": "C1(CC=C2)=C2C=CC=C1",
            "1H-pyrrole": "[NH]1CCCC1",
            "2-butyne": "CC#CC",
            "2-ethyl-1-butanol": "CCC(CC)CO",
            "2-methylpenta-2,3-diene": "CC=C=C(C)C",
            "(E)-1,2-dimethyldiazene": "C/N=N/C",
            "N,N-dimethylacetamide": "CC(N(C)C)=O",
            "N-methylpropan-2-imine": "C/C(C)=N/C",
            "(Z)-N,N,N'-trimethylacetimidamide": "C/C(N(C)C)=N/C",
            "acetic anydride": "CC(=O)OC(=O)C",
            "acyl bromide": "C(=O)Br",
            "acyl chloride": "C(=O)Cl",
            "acyl fluoride": "C(=O)F",
            "acyl iodide": "C(=O)I",
            "aldehyde": "CC=O",
            "amide": "C(=O)N",
            "amino": "*N",
            "anthracene": "C12=CC=CC=C1C=C3C(C=CC=C3)=C2",
            "azide": "C([N-][N+]#N)",
            "benzene": "C1=CC=CC=C1",
            "benzene thiol": "C1=CC=C(C=C1)S",
            "bicyclohexyl": "C1CCCCC1C1CCCCC1",
            "bromine": "Br",
            "but-1-ene": "CCC=C",
            "but-1-yne": "CCC#C",
            "carbon dioxide": "O=C=O",
            "carboxylic acid": "C(=O)O",
            "chlorine": "Cl",
            "chloromethyl methyl ether": "COCCl",
            "cyclobutadiene": "C1=CC=C1",
            "cyclobutane": "C1CCC1",
            "cycloheptane": "C1CCCCCC1",
            "cyclohexane": "C1CCCCC1",
            "cyclohexa-1,3-diene": "C1=CCCC=C1",
            "cyclohexa-1,4-diene": "C1=CCC=CC1",
            "cyclohexene": "C=1CCCCC=1",
            "cyclopentane": "C1CCCC1",
            "cyclopenta-1,3-diene": "C1=CCC=C1",
            "cyclopropane": "C1CC1",
            "cyclopropene": "C1=CC1",
            "deuteroethane": "[2H][CH2]C",
            "dimethyl ether": "COC",
            "diethyl ether": "CCOCC",
            "diisopropyl ether": "CC(C)OC(C)C",
            "diamond": "C&1&1&1&1",
            "diazomethane": "C=[N+]=[N-]",
            "diammonium thiosulfate": "[NH4+].[NH4+].[O-]S(=O)(=O)[S-]",
            "enamine": "N",
            "ethane": "CC",
            "ethanethiol": "CCS",
            "ethanol": "CCO",
            "ethene": "C=C",
            "ether": "COC",
            "ester": "C(=O)OC",
            "fluorine": "F",
            "formaldehyde": "C=O",
            "furan": "C1OC=CC=1",
            "graphite": "C&1&1&1",
            "hydrogen cyanide": "C#N",
            "hydroxide": "[OH-]",
            "hydroxyl amine": "NO",
            "indane": "C1=CC=CC(CCC2)=C12",
            "ketone": "CC(=O)C",
            "methane": "C",
            "methanethiol": "CS",
            "methyl acetate": "CC(OC)=O",
            "methyl pyrrole": "CN1CCCC1",
            "methyl tert-butyl ether": "CC(C)(C)OC",
            "naphthalene": "C12=CC=CC=C1C=CC=C2",
            "nitro": "[N+](=O)[O-]",
            "nitromethane": "C[N+]([O-])=O",
            "pentalene": "C12=CC=CC1=CC=C2",
            "perhydroisoquinoline": "N1CC2CCCC2CC1",
            "phenol": "OC1CCCCC1",
            "phenyl": "C=1(C=CC=CC1)",
            "polystyrene": "c1ccccc1C&1&1",
            "primary alcohol": "O",
            "primary amine": "N",
            "propan-2-one": "CC(C)=O",
            "propanol": "CCC=O",
            "prop-1-ene": "CC=C",
            "prop-1-yne": "CC#C",
            "pyridine": "N1CCCCC1",
            "pyridine-n-oxide": "O=N1CCCCC1",
            "secondary amine": "NC",
            "spiro[5.5]undecane": "C12(CCCCC1)CCCCC2",
            "sulfoxide": "S(=O)(=O)",
            "tetramethylammonium": "C[N+](C)(C)C",
            "thiol": "S",
            "thiosulfate": "OS(=O)(=S)O",
            "trimethylamine": "CN(C)C",
            "triphenylene": "C1(C=CC=C2)=C2C(C=CC=C3)=C3C4=C1C=CC=C4",
        }

        functional_groups_smarts = {
            "acetic anydride": "[CX3](=[OX1])[OX2][CX3](=[OX1])",
            "acetylenic carbon": "[$([CX2]#C)]",
            "acyl bromide": "[CX3](=[OX1])[Br]",
            "acyl chloride": "[CX3](=[OX1])[Cl]",
            "acyl fluoride": "[CX3](=[OX1])[F]",
            "acyl iodide": "[CX3](=[OX1])[I]",
            "aldehyde": "[CX3H1](=O)[#6]",
            "alkane": "[CX4]",
            "allenic carbon": "[$([CX2](=C)=C)]",
            "amide": "[NX3][CX3](=[OX1])[#6]",
            "amidium": "[NX3][CX3]=[NX3+]",
            "amino acid": "[$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-,N]",
            "azide": "[$(-[NX2-]-[NX2+]#[NX1]),$(-[NX2]=[NX2+]=[NX1-])]",
            "azo nitrogen": "[NX2]=N",
            "azole": "[$([nr5]:[nr5,or5,sr5]),$([nr5]:[cr5]:[nr5,or5,sr5])]",
            "azoxy nitrogen": "[$([NX2]=[NX3+]([O-])[#6]),$([NX2]=[NX3+0](=[O])[#6])]",
            "diazene": "[NX2]=[NX2]",
            "diazo nitrogen": "[$([#6]=[N+]=[N-]),$([#6-]-[N+]#[N])]",
            "bromine": "[Br]",
            "carbamate": "[NX3,NX4+][CX3](=[OX1])[OX2,OX1-]",
            "carbamic ester": "[NX3][CX3](=[OX1])[OX2H0]",
            "carbamic acid": "[NX3,NX4+][CX3](=[OX1])[OX2H,OX1-]",
            "carbo azosulfone": "[SX4](C)(C)(=O)=N",
            "carbo thiocarboxylate": "[S-][CX3](=S)[#6]",
            "carbo thioester": "S([#6])[CX3](=O)[#6]",
            "carboxylate ion": "[CX3](=O)[O-]",
            "carbonic acid": "[CX3](=[OX1])(O)O",
            "carbonic ester": "C[OX2][CX3](=[OX1])[OX2]C",
            "carbonyl group": "[$([CX3]=[OX1]),$([CX3+]-[OX1-])]",
            "carbonyl with carbon": "[CX3](=[OX1])C",
            "carbonyl with nitrogen": "[OX1]=CN",
            "carbonyl with oxygen": "[CX3](=[OX1])O",
            "carboxylic acid": "[CX3](=O)[OX1H0-,OX2H1]",
            "chlorine": "[Cl]",
            "cyanamide": "[NX3][CX2]#[NX1]",
            "di sulfide": "[#16X2H0][#16X2H0]",
            "enamine": "[NX3][CX3]=[CX3]",
            "enol": "[OX2H][#6X3]=[#6]",
            "ester": "[#6][CX3](=O)[OX2H0][#6]",
            "ether": "[OD2]([#6])[#6]",
            "fluorine": "[F]",
            "hydrogen": "[H]",
            "hydrazine": "[NX3][NX3]",
            "hydrazone": "[NX3][NX2]=[*]",
            "hydroxyl": "[OX2H]",
            "hydroxyl in alcohol": "[#6][OX2H]",
            "hydroxyl in carboxylic acid": "[OX2H][CX3]=[OX1]",
            "isonitrile": "[CX1-]#[NX2+]",
            "imide": "[CX3](=[OX1])[NX3H][CX3](=[OX1])",
            "imine": "[CX3;$([C]([#6])[#6]),$([CH][#6])]=[NX2][#6]",
            "iminium": "[NX3+]=[CX3]",
            "ketone": "[CX3]=[OX1]",
            "peroxide": "[OX2,OX1-][OX2,OX1-]",
            "phenol": "[OX2H][cX3]:[c]",
            "phosphoric acid": "[$(P(=[OX1])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)]),$([P+]([OX1-])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)])]",
            "phosphoric ester": "[$(P(=[OX1])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2][#6]),$([OX2]P)]),$([P+]([OX1-])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2][#6]),$([OX2]P)])]",
            "primary alcohol": "[OX2H]",
            "primary amine": "[NX3;H2;!$(NC=[!#6]);!$(NC#[!#6])][#6]",
            "proton": "[H+]",
            "mono sulfide": "[#16X2H0][!#16]",
            "nitrate": "[$([NX3](=[OX1])(=[OX1])O),$([NX3+]([OX1-])(=[OX1])O)]",
            "nitrile": "[NX1]#[CX2]",
            "nitro": "[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]",
            "nitroso": "[NX2]=[OX1]",
            "n-oxide": "[$([#7+][OX1-]),$([#7v5]=[OX1]);!$([#7](~[O])~[O]);!$([#7]=[#7])]",
            "secondary amine": "[NX3;H2,H1;!$(NC=O)]",
            "sulfate": "[$([#16X4](=[OX1])(=[OX1])([OX2H,OX1H0-])[OX2][#6]),$([#16X4+2]([OX1-])([OX1-])([OX2H,OX1H0-])[OX2][#6])]",
            "sulfamate": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2][#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2][#6])]",
            "sulfamic acid": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2H,OX1H0-]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2H,OX1H0-])]",
            "sulfenic acid": "[#16X2][OX2H,OX1H0-]",
            "sulfenate": "[#16X2][OX2H0]",
            "sulfide": "[#16X2H0]",
            "sulfonate": "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H0]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H0])]",
            "sulfinate": "[$([#16X3](=[OX1])[OX2H0]),$([#16X3+]([OX1-])[OX2H0])]",
            "sulfinic acid": "[$([#16X3](=[OX1])[OX2H,OX1H0-]),$([#16X3+]([OX1-])[OX2H,OX1H0-])]",
            "sulfonamide": "[$([#16X4]([NX3])(=[OX1])(=[OX1])[#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[#6])]",
            "sulfone": "[$([#16X4](=[OX1])(=[OX1])([#6])[#6]),$([#16X4+2]([OX1-])([OX1-])([#6])[#6])]",
            "sulfonic acid": "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H,OX1H0-]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H,OX1H0-])]",
            "sulfoxide": "[$([#16X3](=[OX1])([#6])[#6]),$([#16X3+]([OX1-])([#6])[#6])]",
            "sulfur": "[#16!H0]",
            "sulfuric acid ester": "[$([SX4](=O)(=O)(O)O),$([SX4+2]([O-])([O-])(O)O)]",
            "sulfuric acid diester": "[$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6]),$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6])]",
            "thioamide": "[NX3][CX3]=[SX1]",
            "thiol": "[#16X2H]",
            "vinylic carbon": "[$([CX3]=[CX3])]",
        }

        return functional_groups_smiles, functional_groups_smarts

    def _get_commonly_used_r_group_replacements():

        r_group_smiles = {
            'water': 'O',
            'methanol': 'OC',
            'ammonia': 'N',
            'hydrogen chloride': 'Cl',
            'hydrogen fluoride': 'F',
            'ethane': 'CC',
            'hydrogen cyanide': 'C#N',
            'formic acid': 'C(=O)O',
            'hydrogen bromide': 'Br',
            'fluroform': 'C(F)(F)F',
            'propane': 'C(C)C',
            'toulene': 'Cc1ccccc1',
            'pyridine': 'c1cccnc1',
            'dimethylamine': 'N(C)C',
            'ethanol': 'OCC',
            'formamide': 'C(N)=O',
            'morpholine': 'N1CCOCC1',
            'nitro': '[N+](=O)[O-]',
            'isobutane': 'C(C)(C)C',
            'anisole': 'c1ccc(OC)cc1',
            'flurobenzene': 'c1ccc(F)cc1',
            'cyclohexane': 'C1CCCCC1',
            'acetic acid': 'CC(=O)O',
            'methyl formate': 'C(=O)OC',
            'butane': 'CCCC',
            'acetamide': 'NC(C)=O',
            'methanamine': 'NC',
            'acetaldehyde': 'C(C)=O',
            'chlorobenzene': 'c1ccc(Cl)cc1',
            '1-methylpiperazine': 'N1CCN(C)CC1',
            'phenylmethanol': 'OCc1ccccc1',
            'ethylbenzene': 'CCc1ccccc1',
            'piperidine': 'N1CCCCC1',
            'thiophene': 'c1cccs1',
            'cyclopropane': 'C1CC1',
            'phenol': 'Oc1ccccc1',
            'aniline': 'Nc1ccccc1',
            'hydrosulfonylmethane': 'S(C)(=O)=O',
            'piperazine': 'N1CCNCC1',
            'pyrrolidine': 'N1CCCC1',
            '4-methylmorpholine': 'CN1CCOCC1',
            'hydrogen iodide': 'I',
            'ethyl formate': 'C(=O)OCC',
            'sulfonic amide': 'S(N)(=O)=O',
            'phenylmethanamine': 'NCc1ccccc1',
            'N-methylformamide': 'C(=O)NC',
            'trimethylamine': 'CN(C)C',
            'N,N-dimethylformamide': 'C(=O)N(C)C',
            'thiol': 'SC',
            'benzaldehyde': 'C(=O)c1ccccc1',
            '1-methylpiperidine': 'CN1CCCCC1',
            'cyclopentane': 'C1CCCC1',
            'N-hydroxyformamide': 'C(=O)NO',
            'pyrimidine': 'c1cncnc1',
            'furan': 'c1ccco1',
            'ethanamine': 'CCN',
            'benzonitrile': 'c1ccc(C#N)cc1',
            'propionic acid': 'CCC(=O)O',
            'propan-2-ol': 'OC(C)C',
            'methanesulfonamide': 'NS(C)(=O)=O',
            'pentane': 'CCCCC',
            'morpholine-4-carbaldehyde': 'C(=O)N1CCOCC1',
            'trifluoromethanol': 'OC(F)(F)F',
            'methoxymethane': 'COC',
            'cyclohexanamine': 'NC1CCCCC1',
            'formaldehyde': 'C=O',
            'N-phenylformamide': 'C(=O)Nc1ccccc1',
            'butan-1-ol': 'OCCCC',
            'pyrazine': 'c1cnccn1',
            'naphthalene': 'c1ccc2ccccc2c1',
            'propan-1-ol': 'OCCC',
            'benzamide': 'NC(=O)c1ccccc1',
            '1-methyl-1H-pyrazole': 'c1cnn(C)c1',
            'N-benzylformamide': 'C(=O)NCc1ccccc1',
            '1﻿H-imidazole': 'n1ccnc1',
            'propan-2-amine': 'NC(C)C',
            '1,3-Benzodioxole': 'c1ccc2c(c1)OCO2',
            '1-methylpyrrolidine': 'CN1CCCC1',
            'methylcyclohexane': 'CC1CCCCC1',
            'ethyne': 'C#C',
            '2-methoxypyridine': 'c1ccc(OC)nc1',
            'N,N-dimethylethanamine': 'CCN(C)C',
            'thiazole': 'c1nccs1',
            'bromobenzene': 'c1ccc(Br)cc1',
            '4-methylpyridine': 'Cc1ccncc1',
            '2-methoxyethan-1-ol': 'OCCOC',
            'hexane': 'CCCCCC',
            'Tetrahydropyran': 'C1CCOCC1',
            '1H-pyrazole': 'c1cn[nH]c1',
            '1-methyl-1H-imidazole': 'Cn1ccnc1',
            'benzoic acid': 'c1ccc(C(=O)O)cc1',
            'boronic acid': 'B(O)O',
            '2-hydroxyacetic acid': 'OCC(=O)O',
            'ethene': 'C=C',
            'piperidine-1-carbaldehyde': 'C(=O)N1CCCCC1',
            'styrene': 'C=Cc1ccccc1',
            '1-fluoro-4-methylbenzene': 'Cc1ccc(F)cc1',
            'ethylene glycol': 'OCCO',
            '2-(dimethylamino)ethan-1-ol': 'OCCN(C)C',
            '(trifluoromethyl)benzene': 'c1ccc(C(F)(F)F)cc1',
            'diethylamine': 'N(CC)CC',
            'N-cyclohexylformamide': 'C(=O)NC1CCCCC1',
            'benzothiazole': 'c1nc2ccccc2s1',
            'methylcyclopropane': 'CC1CC1',
            'N-ethyl-N-methylethanamine': 'CN(CC)CC',
            '1H-benzoimidazole': 'c1nc2ccccc2[nH]1',
            'N-isopropylformamide': 'C(=O)NC(C)C',
            '2-aminoethan-1-ol': 'NCCO',
            'N-(2-hydroxyethyl)formamide': 'C(=O)NCCO',
            '2,3-dihydrobenzo[b][1,4]dioxine': 'c1ccc2c(c1)OCCO2',
            'benzothiophene': 'c1cc2ccccc2s1',
            'propylbenzene': 'CCCc1ccccc1',
            'pyrrolidine-1-carbaldehyde': 'C(=O)N1CCCC1',
            '1,4-dimethylpiperazine': 'CN1CCN(C)CC1',
            'N-ethylformamide': 'C(=O)NCC',
            '2-morpholinoethan-1-ol': 'OCCN1CCOCC1',
            '4-ethylmorpholine': 'CCN1CCOCC1',
            'indole': 'c1c[nH]c2ccccc12',
            'quinoline': 'c1cnc2ccccc2c1',
            '3-(dimethylamino)propan-1-ol': 'OCCCN(C)C',
            '3-methylpyridine': 'Cc1cccnc1',
            'cyclobutane': 'C1CCC1',
            'formimidamide': 'C(=N)N',
            'benzofuran': 'c1cc2ccccc2o1',
            '1-methoxy-4-methylbenzene': 'Cc1ccc(OC)cc1',
            '2-methylpyridine': 'Cc1ccccn1',
            'acetonitrile': 'CC#N',
            '1,2-dichlorobenzene': 'c1ccc(Cl)c(Cl)c1',
            'N,N-dimethylaniline': 'c1ccc(N(C)C)cc1',
            'hydrosulfonylbenzene': 'S(=O)(=O)c1ccccc1',
            'N-methylacetamide': 'CNC(C)=O',
            'hydrogen sulfide': 'S',
            '2-phenylethan-1-amine': 'NCCc1ccccc1',
            '2-(pyrrolidin-1-yl)ethan-1-ol': 'OCCN1CCCC1',
            'methoxyethane': 'CCOC',
            '1,2-dimethoxybenzene': 'c1ccc(OC)c(OC)c1',
            'nitrobenzene': 'c1ccc([N+](=O)[O-])cc1',
            'ethynylbenzene': 'C#Cc1ccccc1',
            'N-(pyridin-3-yl)formamide': 'C(=O)Nc1cccnc1',
            '2-(piperidin-1-yl)ethan-1-ol': 'OCCN1CCCCC1',
            'benzenesulfonamide': 'c1ccc(S(N)(=O)=O)cc1',
            '1-ethylpyrrolidine': 'CCN1CCCC1',
            'pyrazole': 'c1cc[nH]n1',
            '3-(piperidin-1-yl)propan-1-ol': 'OCCCN1CCCCC1',
            'N,N-diethylformamide': 'C(=O)N(CC)CC',
            'acetophenone': 'c1ccc(C(C)=O)cc1',
            'benzooxazole': 'c1nc2ccccc2o1',
            '4-methylpiperazine-1-carbaldehyde': 'C(=O)N1CCN(C)CC1',
            'benzenethiol': 'Sc1ccccc1',
            'sulfuric diamide': 'NS(N)(=O)=O',
            '4-methoxyaniline': 'Nc1ccc(OC)cc1',
            '1-chloro-4-methylbenzene': 'Cc1ccc(Cl)cc1',
            'propan-1-amine': 'CCCN',
            'ethoxybenzene': 'c1ccc(OCC)cc1',
            '5-methylene-2-thioxothiazolidin-4-one': 'C=C1SC(=S)NC1=O',
            '1,3-difluorobenzene': 'c1ccc(F)cc1F',
            '(trifluoromethoxy)benzene': 'c1ccc(OC(F)(F)F)cc1',
            'heptane': 'CCCCCCC',
            'pyridin-2-amine': 'c1ccc(N)nc1',
            '1-ethylpiperidine': 'CCN1CCCCC1',
            'formohydrazide': 'C(=O)NN',
            '2-chlorothiophene': 'c1ccc(Cl)s1',
            'piperidin-4-ol': 'N1CCC(O)CC1',
            '2-methylthiazole': 'c1csc(C)n1',
            'N-cyclopropylformamide': 'C(=O)NC1CC1',
            'prop-2-en-1-ol': 'OCC=C',
            'cyclopentanamine': 'NC1CCCC1',
            'urea': 'NC(N)=O',
            'prop-1-ene': 'CC=C',
            '(methylsulfonyl)benzene': 'c1ccc(S(C)(=O)=O)cc1',
            'difluoromethanol': 'OC(F)F',
            '2-phenylacetamide': 'NC(=O)Cc1ccccc1',
            '4-fluorobenzaldehyde': 'C(=O)c1ccc(F)cc1',
            'N-propylformamide': 'C(=O)NCCC',
            'N-tert-butylformamide': 'C(=O)NC(C)(C)C',
            'tetrazole': 'c1nnn[nH]1',
            'pyrrolidin-3-ol': 'N1CCC(O)C1',
            'biphenyl': 'c1ccc(-c2ccccc2)cc1',
            'cyclopropanamine': 'NC1CC1',
            'formaldehyde oxime': 'C=NO',
            'furan-2-carboxamide': 'NC(=O)c1ccco1',
            '3-morpholinopropan-1-ol': 'OCCCN1CCOCC1',
            'propionamide': 'NC(=O)CC',
            '2-(piperazin-1-yl)ethan-1-ol': 'N1CCN(CCO)CC1',
            'pyridin-3-ylmethanamine': 'NCc1cccnc1',
            'N-hydroxyacrylamide': 'C=CC(=O)NO',
            'N-(2-methoxyethyl)formamide': 'C(=O)NCCOC',
            '2-methylthiophene': 'Cc1cccs1',
            'tert-butylbenzene': 'c1ccc(C(C)(C)C)cc1',
            'cyclohexanecarboxamide': 'NC(=O)C1CCCCC1',
            '4-fluorophenol': 'Oc1ccc(F)cc1',
            '2-ethynylpyridine': 'C#Cc1ccccn1',
            '(4-methoxyphenyl)methanamine': 'NCc1ccc(OC)cc1',
            'butyric acid': 'CCCC(=O)O',
            '1-Acetylpiperazine': 'N1CCN(C(C)=O)CC1',
            '3,5-dimethylisoxazole': 'c1c(C)noc1C',
            '2-methyl-1H-imidazole': 'n1ccnc1C',
            '1-ethylpiperazine': 'N1CCN(CC)CC1',
            'adamantane': 'C12CC3CC(CC(C3)C1)C2',
            '1-chloro-3-methylbenzene': 'Cc1cccc(Cl)c1',
            '1,2-difluorobenzene': 'c1ccc(F)c(F)c1',
            '1-phenylurea': 'NC(=O)Nc1ccccc1',
            '2-methylpropan-2-ol': 'OC(C)(C)C',
            '1-chloro-2-methylbenzene': 'Cc1ccccc1Cl',
            'N-phenethylformamide': 'C(=O)NCCc1ccccc1',
            'isonicotinamide': 'NC(=O)c1ccncc1',
            'N-methylcyclopentanamine': 'CNC1CCCC1',
            '2-methoxyethan-1-amine': 'NCCOC',
            'propionaldehyde': 'C(=O)CC',
            'N-(4-chlorophenyl)formamide': 'C(=O)Nc1ccc(Cl)cc1',
            '2-chloropyridine': 'c1ccc(Cl)nc1',
            'N,N-dimethylpropan-1-amine': 'CCCN(C)C',
            '5-methylenethiazolidine-2,4-dione': 'C=C1SC(=O)NC1=O',
            '3-methoxypyridine': 'c1cncc(OC)c1',
            '3-(trifluoromethyl)pyridine': 'c1ncccc1C(F)(F)F',
            '4-methylbenzenesulfonamide': 'NS(=O)(=O)c1ccc(C)cc1',
            '2-phenylethan-1-ol': 'OCCc1ccccc1',
            'N-cyclopentylformamide': 'C(=O)NC1CCCC1',
            'indazole': 'c1ccc2[nH]ncc2c1',
            'cyclopentanol': 'OC1CCCC1',
            'nicotinamide': 'NC(=O)c1cccnc1',
            'isopentane': 'CCC(C)C',
            'hydrosulfonylethane': 'S(=O)(=O)CC',
            'tert-butyl carbamate': 'NC(=O)OC(C)(C)C',
            '(tetrahydrofuran-2-yl)methanol': 'OCC1CCCO1',
            'N,N-dimethylacetamide': 'CC(=O)N(C)C',
            '1-phenylpiperazine': 'N1CCN(c2ccccc2)CC1',
            '2-methylpropan-1-ol': 'C(C)(C)CO',
            'N-methylethanamine': 'CCNC',
            '1,3-dichlorobenzene': 'c1ccc(Cl)cc1Cl',
            'tert-butyl formate': 'C(=O)OC(C)(C)C',
            'thiophene-2-carbaldehyde': 'C(=O)c1cccs1',
            '1-methyl-1,4-diazepane': 'N1CCCN(C)CC1',
            'N-phenylacetamide': 'c1ccc(NC(C)=O)cc1',
            'octane': 'CCCCCCCC',
            '1-methoxy-2-methylbenzene': 'Cc1ccccc1OC',
            '1H-pyrrole-2,5-dione': 'N1C(=O)C=CC1=O',
            'sulfamic acid': 'OS(N)(=O)=O',
            '2-methylisoindoline-1,3-dione': 'CN1C(=O)c2ccccc2C1=O',
            '(difluoromethyl)phosphonic acid': 'C(F)(F)P(=O)(O)O',
            'pyrimidin-2-amine': 'c1ccnc(N)n1',
            '1H-benzo[d]imidazole-5-carboxamide': 'c1nc2cc(C(N)=O)ccc2[nH]1',
            '2-methylpropan-2-amine': 'NC(C)(C)C',
            'N-(4-fluorophenyl)formamide': 'C(=O)Nc1ccc(F)cc1',
            'oxazole': 'c1cnco1',
            'pyridin-3-ylmethanol': 'OCc1cccnc1',
            'pyridin-3-ol': 'Oc1cccnc1',
            'picolinamide': 'NC(=O)c1ccccn1',
            'cyclopropylmethanol': 'OCC1CC1',
            'ethyl carbamate': 'NC(=O)OCC',
            '2-(diethylamino)ethan-1-ol': 'OCCN(CC)CC',
            'pyrocatechol': 'c1ccc(O)c(O)c1',
            'acrylamide': 'NC(=O)C=C',
            'azetidine': 'N1CCC1',
            'p-xylene': 'Cc1ccc(C)cc1',
            '1-methylpiperidin-4-ol': 'OC1CCN(C)CC1',
            '4-hydrosulfonylmorpholine': 'S(=O)(=O)N1CCOCC1',
            '4-methyl-1H-imidazole': 'Cc1c[nH]cn1',
            'N-(pyridin-4-yl)formamide': 'C(=O)Nc1ccncc1',
            '4-methoxyphenol': 'Oc1ccc(OC)cc1',
            'fluoromethane': 'CF',
            'N-methylbenzamide': 'CNC(=O)c1ccccc1',
            'pyridin-3-amine': 'Nc1cccnc1',
            'pyridin-4-ylmethanamine': 'NCc1ccncc1',
            'imidazole': 'c1ncc[nH]1',
            '3-chlorophenol': 'Oc1cccc(Cl)c1',
            '1-ethylurea': 'NC(=O)NCC',
            'methyl benzoate': 'c1ccc(C(=O)OC)cc1',
            '(aminomethylene)bis(phosphonic acid)': 'NC(P(=O)(O)O)P(=O)(O)O',
            'pyridin-4-amine': 'Nc1ccncc1',
            'pyrrole': 'n1cccc1',
            'N-methyl-2-phenylcyclopropan-1-amine': 'CNC1CC1c1ccccc1',
            '5-methoxy-3-methyl-1,3,4-oxadiazol-2(3H)-one': 'Cn1nc(OC)oc1=O',
            '(methylsulfonyl)methane': 'CS(C)(=O)=O',
            '1-(piperidin-1-yl)ethan-1-one': 'C1CCN(C(C)=O)CC1',
            'methyl acetate': 'CC(=O)OC',
            '4-chlorophenol': 'Oc1ccc(Cl)cc1',
            'ethane-1,2-diamine': 'NCCN',
            '4-methylpiperidine': 'N1CCC(C)CC1',
            'benzyl formate': 'C(=O)OCc1ccccc1',
            'N,N-dimethylsulfonic amide': 'S(=O)(=O)N(C)C',
            '4-methoxybenzaldehyde': 'C(=O)c1ccc(OC)cc1',
            'N-hydroxyacetamide': 'CC(=O)NO',
            '1H-1,2,4-triazole': 'n1cncn1',
            '2-fluoroethan-1-ol': 'OCCF',
            '2-aminobenzamide': 'Nc1ccccc1C(N)=O',
            'N-hydroxypropionamide': 'CCC(=O)NO',
            '2H-tetrazole': 'c1nn[nH]n1',
            'prop-2-yn-1-ol': 'OCC#C',
            'piperidin-4-ylmethanol': 'N1CCC(CO)CC1',
            '3-ethynylpyridine': 'C#Cc1cccnc1',
            '4-chlorobenzaldehyde': 'C(=O)c1ccc(Cl)cc1',
            'methylphosphonic acid': 'CP(=O)(O)O',
            'isobutyramide': 'NC(=O)C(C)C',
            'cyclopropylmethanamine': 'NCC1CC1',
            'N,N-dimethylpyrrolidin-3-amine': 'N1CCC(N(C)C)C1',
            '4,5-dihydrooxazol-2-amine': 'C1COC(N)=N1',
            '1,2,3,4-tetrahydroisoquinoline': 'N1CCc2ccccc2C1',
            '4-phenylmorpholine': 'c1ccc(N2CCOCC2)cc1',
            '4,5-dihydro-1H-imidazole': 'C1=NCCN1',
            '3-aminopropan-1-ol': 'NCCCO',
            '2,2,2-trifluoroacetaldehyde': 'C(=O)C(F)(F)F',
            'trifluoromethanethiol': 'SC(F)(F)F',
            'N-ethylacetamide': 'CCNC(C)=O',
            'N-methylaniline': 'N(C)c1ccccc1',
            'phenylmethanethiol': 'SCc1ccccc1',
            '4-(pyrrolidin-1-yl)piperidine': 'N1CCC(N2CCCC2)CC1',
            '4-(trifluoromethyl)pyrimidine': 'c1nccc(C(F)(F)F)n1',
            '1-methoxy-3-methylbenzene': 'Cc1cccc(OC)c1',
            'N-butylformamide': 'C(=O)NCCCC',
            '2,2,2-trifluoroethan-1-ol': 'OCC(F)(F)F',
            'p-toluidine': 'Nc1ccc(C)cc1',
            '1,3-dimethoxybenzene': 'c1cc(OC)cc(OC)c1',
            'N,N-dimethyl-1-phenylmethanamine': 'CN(C)Cc1ccccc1',
            '2-methylnaphthalene': 'Cc1ccc2ccccc2c1',
            'tetrahydrofuran': 'C1CCCO1',
            'acrylic acid': 'C=CC(=O)O',
            '2-(methylamino)ethan-1-ol': 'CNCCO',
            '4-methylbenzaldehyde': 'C(=O)c1ccc(C)cc1',
            '3,4-dimethyl-1H-pyrazole-5-carboxylic acid': 'Cc1c(C)n[nH]c1C(=O)O',
            'chloromethane': 'CCl',
            'butyramide': 'NC(=O)CCC',
            '1-chloro-4-hydrosulfonylbenzene': 'S(=O)(=O)c1ccc(Cl)cc1',
            'difluoromethane': 'C(F)F',
            '3-(pyrrolidin-1-yl)propan-1-ol': 'OCCCN1CCCC1',
            'cyclopropylbenzene': 'C1CC1c1ccccc1',
            'cumene': 'c1ccc(C(C)C)cc1',
            '2-methyltetrahydrofuran': 'CC1CCCO1',
            'N-methylpropan-2-amine': 'CNC(C)C',
            'alanine': 'CC(N)C(=O)O',
            '1,2,3,6-tetrahydropyridine': 'C1=CCNCC1',
            '2-(trifluoromethyl)pyridine': 'c1ccc(C(F)(F)F)nc1',
            'hydroquinone': 'Oc1ccc(O)cc1',
            '4-fluoroaniline': 'Nc1ccc(F)cc1',
            '1-fluoro-2-methoxybenzene': 'c1ccc(OC)c(F)c1',
            '2-ethylidenehydrazine-1-carbothioamide': 'C(C)=NNC(N)=S',
            'furan-2-carbaldehyde': 'C(=O)c1ccco1',
            'butan-1-amine': 'NCCCC',
            'triaza-1,2-dien-2-ium': 'N=[N+]=N',
            'pyridin-2-ylmethanol': 'OCc1ccccn1',
            'resorcinol': 'c1cc(O)cc(O)c1',
            'piperidin-3-ol': 'N1CCCC(O)C1',
            'cyclopropanecarboxamide': 'NC(=O)C1CC1',
            '1-methyl-1H-1,2,4-triazole': 'Cn1cncn1',
            '4-chlorobenzene-1,2-diol': 'Oc1ccc(Cl)cc1O',
            'N-methyl-1-phenylmethanamine': 'N(C)Cc1ccccc1',
            'pyrazin-2-amine': 'c1cnc(N)cn1',
            'thiophen-2-ylmethanamine': 'NCc1cccs1',
            '2-morpholinoethan-1-amine': 'NCCN1CCOCC1',
            'thiomorpholine 1,1-dioxide': 'N1CCS(=O)(=O)CC1',
            '2-isopropoxypyridine': 'c1ccc(OC(C)C)nc1',
            'pyridazine': 'c1ccnnc1',
            '3-fluoropyridine': 'c1ccc(F)cn1',
            'isoquinoline': 'c1cncc2ccccc12',
            '4-chloroaniline': 'Nc1ccc(Cl)cc1',
            'pyrrolidin-2-one': 'N1CCCC1=O',
            '5-methyloctahydropyrrolo[3,4-b]pyrrole': 'N1CCC2CN(C)CC21',
            '4-methoxybenzamide': 'NC(=O)c1ccc(OC)cc1',
            'm-cresol': 'Oc1cccc(C)c1',
            '4,4,5,5-tetramethyl-1,3,2-dioxaborolane': 'B1OC(C)(C)C(C)(C)O1',
            'N1,N1-dimethylethane-1,2-diamine': 'NCCN(C)C',
            '1-phenylthiourea': 'NC(=S)Nc1ccccc1',
            '1-methyl-4-(trifluoromethyl)benzene': 'Cc1ccc(C(F)(F)F)cc1',
            'isopropoxybenzene': 'c1ccc(OC(C)C)cc1',
            '4-methoxypiperidine': 'N1CCC(OC)CC1',
            '1,2-dichloro-4-methylbenzene': 'Cc1ccc(Cl)c(Cl)c1',
            '1-(4-chlorophenyl)urea': 'NC(=O)Nc1ccc(Cl)cc1',
            'thiazol-2-amine': 'Nc1nccs1',
            'o-xylene': 'c1ccc(C)c(C)c1',
            '2-methyl-1,3,4-oxadiazole': 'c1nnc(C)o1',
            '1-fluoro-3-methylbenzene': 'Cc1cccc(F)c1',
            '(methoxymethyl)benzene': 'COCc1ccccc1',
            'hydrazine': 'NN',
            '1-cyclohexylurea': 'NC(=O)NC1CCCCC1',
            'ethanethiol': 'SCC',
            'N-hydroxypentanamide': 'CCCCC(=O)NO',
            'thiophene-2-carboxamide': 'NC(=O)c1cccs1',
            'N-(cyclopropylmethyl)formamide': 'C(=O)NCC1CC1',
            '1-ethyl-2-methylpyrrolidine': 'CCN1CCCC1C',
            'pyridin-4-ylmethanol': 'OCc1ccncc1',
            'triethylamine': 'CCN(CC)CC',
            '4-hydroxy-2-oxobut-3-enoic acid': 'C(O)=CC(=O)C(=O)O',
            'isonicotinaldehyde': 'C(=O)c1ccncc1',
            '1,1,1-trifluoroethane': 'CC(F)(F)F',
            'isothiocyanic acid': 'N=C=S',
            'phosphonic acid': 'P(=O)(O)O',
            '2-hydroxy-4-oxobut-2-enoic acid': 'C(=O)C=C(O)C(=O)O',
            'N,N-dimethylpiperidin-4-amine': 'CN(C)C1CCNCC1',
            '1-(pyridin-2-yl)piperazine': 'N1CCN(c2ccccn2)CC1',
        }

        r_group_smarts = {
            'water': '[#8]',
            'methanol': '[#8]-[#6]',
            'ammonia': '[#7]',
            'hydrogen chloride': '[#17]',
            'hydrogen fluoride': '[#9]',
            'ethane': '[#6]-[#6]',
            'hydrogen cyanide': '[#6]#[#7]',
            'formic acid': '[#6](=[#8])-[#8]',
            'hydrogen bromide': '[#35]',
            'fluroform': '[#6](-[#9])(-[#9])-[#9]',
            'propane': '[#6](-[#6])-[#6]',
            'toulene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridine': '[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'dimethylamine': '[#7](-[#6])-[#6]',
            'ethanol': '[#8]-[#6]-[#6]',
            'formamide': '[#6](-[#7])=[#8]',
            'morpholine': '[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'nitro': '[#7+](=[#8])-[#8-]',
            'isobutane': '[#6](-[#6])(-[#6])-[#6]',
            'anisole': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'flurobenzene': '[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            'cyclohexane': '[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'acetic acid': '[#6]-[#6](=[#8])-[#8]',
            'methyl formate': '[#6](=[#8])-[#8]-[#6]',
            'butane': '[#6]-[#6]-[#6]-[#6]',
            'acetamide': '[#7]-[#6](-[#6])=[#8]',
            'methanamine': '[#7]-[#6]',
            'acetaldehyde': '[#6](-[#6])=[#8]',
            'chlorobenzene': '[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            '1-methylpiperazine': '[#7]1-[#6]-[#6]-[#7](-[#6])-[#6]-[#6]-1',
            'phenylmethanol': '[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'ethylbenzene': '[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'piperidine': '[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'thiophene': '[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'cyclopropane': '[#6]1-[#6]-[#6]-1',
            'phenol': '[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'aniline': '[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'hydrosulfonylmethane': '[#16](-[#6])(=[#8])=[#8]',
            'piperazine': '[#7]1-[#6]-[#6]-[#7]-[#6]-[#6]-1',
            'pyrrolidine': '[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            '4-methylmorpholine': '[#6]-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'hydrogen iodide': '[#53]',
            'ethyl formate': '[#6](=[#8])-[#8]-[#6]-[#6]',
            'sulfonic amide': '[#16](-[#7])(=[#8])=[#8]',
            'phenylmethanamine': '[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N-methylformamide': '[#6](=[#8])-[#7]-[#6]',
            'trimethylamine': '[#6]-[#7](-[#6])-[#6]',
            'N,N-dimethylformamide': '[#6](=[#8])-[#7](-[#6])-[#6]',
            'thiol': '[#16]-[#6]',
            'benzaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1-methylpiperidine': '[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'cyclopentane': '[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'N-hydroxyformamide': '[#6](=[#8])-[#7]-[#8]',
            'pyrimidine': '[#6]1:[#6]:[#7]:[#6]:[#7]:[#6]:1',
            'furan': '[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'ethanamine': '[#6]-[#6]-[#7]',
            'benzonitrile': '[#6]1:[#6]:[#6]:[#6](-[#6]#[#7]):[#6]:[#6]:1',
            'propionic acid': '[#6]-[#6]-[#6](=[#8])-[#8]',
            'propan-2-ol': '[#8]-[#6](-[#6])-[#6]',
            'methanesulfonamide': '[#7]-[#16](-[#6])(=[#8])=[#8]',
            'pentane': '[#6]-[#6]-[#6]-[#6]-[#6]',
            'morpholine-4-carbaldehyde': '[#6](=[#8])-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'trifluoromethanol': '[#8]-[#6](-[#9])(-[#9])-[#9]',
            'methoxymethane': '[#6]-[#8]-[#6]',
            'cyclohexanamine': '[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'formaldehyde': '[#6]=[#8]',
            'N-phenylformamide': '[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'butan-1-ol': '[#8]-[#6]-[#6]-[#6]-[#6]',
            'pyrazine': '[#6]1:[#6]:[#7]:[#6]:[#6]:[#7]:1',
            'naphthalene': '[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:1',
            'propan-1-ol': '[#8]-[#6]-[#6]-[#6]',
            'benzamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1-methyl-1H-pyrazole': '[#6]1:[#6]:[#7]:[#7](-[#6]):[#6]:1',
            'N-benzylformamide': '[#6](=[#8])-[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'propan-2-amine': '[#7]-[#6](-[#6])-[#6]',
            '1,3-Benzodioxole': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#8]-[#6]-[#8]-2',
            '1-methylpyrrolidine': '[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            'methylcyclohexane': '[#6]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'ethyne': '[#6]#[#6]',
            '2-methoxypyridine': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#7]:[#6]:1',
            'N,N-dimethylethanamine': '[#6]-[#6]-[#7](-[#6])-[#6]',
            'thiazole': '[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'bromobenzene': '[#6]1:[#6]:[#6]:[#6](-[#35]):[#6]:[#6]:1',
            '4-methylpyridine': '[#6]-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '2-methoxyethan-1-ol': '[#8]-[#6]-[#6]-[#8]-[#6]',
            'hexane': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'Tetrahydropyran': '[#6]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            '1H-pyrazole': '[#6]1:[#6]:[#7]:[#7H]:[#6]:1',
            '1-methyl-1H-imidazole': '[#6]-[#7]1:[#6]:[#6]:[#7]:[#6]:1',
            'benzoic acid': '[#6]1:[#6]:[#6]:[#6](-[#6](=[#8])-[#8]):[#6]:[#6]:1',
            'boronic acid': '[#5](-[#8])-[#8]',
            '2-hydroxyacetic acid': '[#8]-[#6]-[#6](=[#8])-[#8]',
            'ethene': '[#6]=[#6]',
            'piperidine-1-carbaldehyde': '[#6](=[#8])-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'styrene': '[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1-fluoro-4-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            'ethylene glycol': '[#8]-[#6]-[#6]-[#8]',
            '2-(dimethylamino)ethan-1-ol': '[#8]-[#6]-[#6]-[#7](-[#6])-[#6]',
            '(trifluoromethyl)benzene': '[#6]1:[#6]:[#6]:[#6](-[#6](-[#9])(-[#9])-[#9]):[#6]:[#6]:1',
            'diethylamine': '[#7](-[#6]-[#6])-[#6]-[#6]',
            'N-cyclohexylformamide': '[#6](=[#8])-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'benzothiazole': '[#6]1:[#7]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#16]:1',
            'methylcyclopropane': '[#6]-[#6]1-[#6]-[#6]-1',
            'N-ethyl-N-methylethanamine': '[#6]-[#7](-[#6]-[#6])-[#6]-[#6]',
            '1H-benzoimidazole': '[#6]1:[#7]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7H]:1',
            'N-isopropylformamide': '[#6](=[#8])-[#7]-[#6](-[#6])-[#6]',
            '2-aminoethan-1-ol': '[#7]-[#6]-[#6]-[#8]',
            'N-(2-hydroxyethyl)formamide': '[#6](=[#8])-[#7]-[#6]-[#6]-[#8]',
            '2,3-dihydrobenzo[b][1,4]dioxine': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#8]-[#6]-[#6]-[#8]-2',
            'benzothiophene': '[#6]1:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#16]:1',
            'propylbenzene': '[#6]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyrrolidine-1-carbaldehyde': '[#6](=[#8])-[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            '1,4-dimethylpiperazine': '[#6]-[#7]1-[#6]-[#6]-[#7](-[#6])-[#6]-[#6]-1',
            'N-ethylformamide': '[#6](=[#8])-[#7]-[#6]-[#6]',
            '2-morpholinoethan-1-ol': '[#8]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            '4-ethylmorpholine': '[#6]-[#6]-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'indole': '[#6]1:[#6]:[#7H]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2',
            'quinoline': '[#6]1:[#6]:[#7]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:1',
            '3-(dimethylamino)propan-1-ol': '[#8]-[#6]-[#6]-[#6]-[#7](-[#6])-[#6]',
            '3-methylpyridine': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'cyclobutane': '[#6]1-[#6]-[#6]-[#6]-1',
            'formimidamide': '[#6](=[#7])-[#7]',
            'benzofuran': '[#6]1:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#8]:1',
            '1-methoxy-4-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            '2-methylpyridine': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'acetonitrile': '[#6]-[#6]#[#7]',
            '1,2-dichlorobenzene': '[#6]1:[#6]:[#6]:[#6](-[#17]):[#6](-[#17]):[#6]:1',
            'N,N-dimethylaniline': '[#6]1:[#6]:[#6]:[#6](-[#7](-[#6])-[#6]):[#6]:[#6]:1',
            'hydrosulfonylbenzene': '[#16](=[#8])(=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N-methylacetamide': '[#6]-[#7]-[#6](-[#6])=[#8]',
            'hydrogen sulfide': '[#16]',
            '2-phenylethan-1-amine': '[#7]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '2-(pyrrolidin-1-yl)ethan-1-ol': '[#8]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            'methoxyethane': '[#6]-[#6]-[#8]-[#6]',
            '1,2-dimethoxybenzene': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#8]-[#6]):[#6]:1',
            'nitrobenzene': '[#6]1:[#6]:[#6]:[#6](-[#7+](=[#8])-[#8-]):[#6]:[#6]:1',
            'ethynylbenzene': '[#6]#[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N-(pyridin-3-yl)formamide': '[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            '2-(piperidin-1-yl)ethan-1-ol': '[#8]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'benzenesulfonamide': '[#6]1:[#6]:[#6]:[#6](-[#16](-[#7])(=[#8])=[#8]):[#6]:[#6]:1',
            '1-ethylpyrrolidine': '[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            'pyrazole': '[#6]1:[#6]:[#6]:[#7H]:[#7]:1',
            '3-(piperidin-1-yl)propan-1-ol': '[#8]-[#6]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'N,N-diethylformamide': '[#6](=[#8])-[#7](-[#6]-[#6])-[#6]-[#6]',
            'acetophenone': '[#6]1:[#6]:[#6]:[#6](-[#6](-[#6])=[#8]):[#6]:[#6]:1',
            'benzooxazole': '[#6]1:[#7]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#8]:1',
            '4-methylpiperazine-1-carbaldehyde': '[#6](=[#8])-[#7]1-[#6]-[#6]-[#7](-[#6])-[#6]-[#6]-1',
            'benzenethiol': '[#16]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'sulfuric diamide': '[#7]-[#16](-[#7])(=[#8])=[#8]',
            '4-methoxyaniline': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            '1-chloro-4-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'propan-1-amine': '[#6]-[#6]-[#6]-[#7]',
            'ethoxybenzene': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]-[#6]):[#6]:[#6]:1',
            '5-methylene-2-thioxothiazolidin-4-one': '[#6]=[#6]1-[#16]-[#6](=[#16])-[#7]-[#6]-1=[#8]',
            '1,3-difluorobenzene': '[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1-[#9]',
            '(trifluoromethoxy)benzene': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6](-[#9])(-[#9])-[#9]):[#6]:[#6]:1',
            'heptane': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'pyridin-2-amine': '[#6]1:[#6]:[#6]:[#6](-[#7]):[#7]:[#6]:1',
            '1-ethylpiperidine': '[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'formohydrazide': '[#6](=[#8])-[#7]-[#7]',
            '2-chlorothiophene': '[#6]1:[#6]:[#6]:[#6](-[#17]):[#16]:1',
            'piperidin-4-ol': '[#7]1-[#6]-[#6]-[#6](-[#8])-[#6]-[#6]-1',
            '2-methylthiazole': '[#6]1:[#6]:[#16]:[#6](-[#6]):[#7]:1',
            'N-cyclopropylformamide': '[#6](=[#8])-[#7]-[#6]1-[#6]-[#6]-1',
            'prop-2-en-1-ol': '[#8]-[#6]-[#6]=[#6]',
            'cyclopentanamine': '[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'urea': '[#7]-[#6](-[#7])=[#8]',
            'prop-1-ene': '[#6]-[#6]=[#6]',
            '(methylsulfonyl)benzene': '[#6]1:[#6]:[#6]:[#6](-[#16](-[#6])(=[#8])=[#8]):[#6]:[#6]:1',
            'difluoromethanol': '[#8]-[#6](-[#9])-[#9]',
            '2-phenylacetamide': '[#7]-[#6](=[#8])-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '4-fluorobenzaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            'N-propylformamide': '[#6](=[#8])-[#7]-[#6]-[#6]-[#6]',
            'N-tert-butylformamide': '[#6](=[#8])-[#7]-[#6](-[#6])(-[#6])-[#6]',
            'tetrazole': '[#6]1:[#7]:[#7]:[#7]:[#7H]:1',
            'pyrrolidin-3-ol': '[#7]1-[#6]-[#6]-[#6](-[#8])-[#6]-1',
            'biphenyl': '[#6]1:[#6]:[#6]:[#6](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:1',
            'cyclopropanamine': '[#7]-[#6]1-[#6]-[#6]-1',
            'formaldehyde oxime': '[#6]=[#7]-[#8]',
            'furan-2-carboxamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            '3-morpholinopropan-1-ol': '[#8]-[#6]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'propionamide': '[#7]-[#6](=[#8])-[#6]-[#6]',
            '2-(piperazin-1-yl)ethan-1-ol': '[#7]1-[#6]-[#6]-[#7](-[#6]-[#6]-[#8])-[#6]-[#6]-1',
            'pyridin-3-ylmethanamine': '[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'N-hydroxyacrylamide': '[#6]=[#6]-[#6](=[#8])-[#7]-[#8]',
            'N-(2-methoxyethyl)formamide': '[#6](=[#8])-[#7]-[#6]-[#6]-[#8]-[#6]',
            '2-methylthiophene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'tert-butylbenzene': '[#6]1:[#6]:[#6]:[#6](-[#6](-[#6])(-[#6])-[#6]):[#6]:[#6]:1',
            'cyclohexanecarboxamide': '[#7]-[#6](=[#8])-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '4-fluorophenol': '[#8]-[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            '2-ethynylpyridine': '[#6]#[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            '(4-methoxyphenyl)methanamine': '[#7]-[#6]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'butyric acid': '[#6]-[#6]-[#6]-[#6](=[#8])-[#8]',
            '1-Acetylpiperazine': '[#7]1-[#6]-[#6]-[#7](-[#6](-[#6])=[#8])-[#6]-[#6]-1',
            '3,5-dimethylisoxazole': '[#6]1:[#6](-[#6]):[#7]:[#8]:[#6]:1-[#6]',
            '1-ethylpiperazine': '[#7]1-[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]-1',
            'adamantane': '[#6]12-[#6]-[#6]3-[#6]-[#6](-[#6]-[#6](-[#6]-3)-[#6]-1)-[#6]-2',
            '1-chloro-3-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#17]):[#6]:1',
            '1,2-difluorobenzene': '[#6]1:[#6]:[#6]:[#6](-[#9]):[#6](-[#9]):[#6]:1',
            '1-phenylurea': '[#7]-[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '2-methylpropan-2-ol': '[#8]-[#6](-[#6])(-[#6])-[#6]',
            '1-chloro-2-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'N-phenethylformamide': '[#6](=[#8])-[#7]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'isonicotinamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'N-methylcyclopentanamine': '[#6]-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            '2-methoxyethan-1-amine': '[#7]-[#6]-[#6]-[#8]-[#6]',
            'propionaldehyde': '[#6](=[#8])-[#6]-[#6]',
            'N-(4-chlorophenyl)formamide': '[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            '2-chloropyridine': '[#6]1:[#6]:[#6]:[#6](-[#17]):[#7]:[#6]:1',
            'N,N-dimethylpropan-1-amine': '[#6]-[#6]-[#6]-[#7](-[#6])-[#6]',
            '5-methylenethiazolidine-2,4-dione': '[#6]=[#6]1-[#16]-[#6](=[#8])-[#7]-[#6]-1=[#8]',
            '3-methoxypyridine': '[#6]1:[#6]:[#7]:[#6]:[#6](-[#8]-[#6]):[#6]:1',
            '3-(trifluoromethyl)pyridine': '[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1-[#6](-[#9])(-[#9])-[#9]',
            '4-methylbenzenesulfonamide': '[#7]-[#16](=[#8])(=[#8])-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            '2-phenylethan-1-ol': '[#8]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N-cyclopentylformamide': '[#6](=[#8])-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'indazole': '[#6]1:[#6]:[#6]:[#6]2:[#7H]:[#7]:[#6]:[#6]:2:[#6]:1',
            'cyclopentanol': '[#8]-[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'nicotinamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'isopentane': '[#6]-[#6]-[#6](-[#6])-[#6]',
            'hydrosulfonylethane': '[#16](=[#8])(=[#8])-[#6]-[#6]',
            'tert-butyl carbamate': '[#7]-[#6](=[#8])-[#8]-[#6](-[#6])(-[#6])-[#6]',
            '(tetrahydrofuran-2-yl)methanol': '[#8]-[#6]-[#6]1-[#6]-[#6]-[#6]-[#8]-1',
            'N,N-dimethylacetamide': '[#6]-[#6](=[#8])-[#7](-[#6])-[#6]',
            '1-phenylpiperazine': '[#7]1-[#6]-[#6]-[#7](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2)-[#6]-[#6]-1',
            '2-methylpropan-1-ol': '[#6](-[#6])(-[#6])-[#6]-[#8]',
            'N-methylethanamine': '[#6]-[#6]-[#7]-[#6]',
            '1,3-dichlorobenzene': '[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1-[#17]',
            'tert-butyl formate': '[#6](=[#8])-[#8]-[#6](-[#6])(-[#6])-[#6]',
            'thiophene-2-carbaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            '1-methyl-1,4-diazepane': '[#7]1-[#6]-[#6]-[#6]-[#7](-[#6])-[#6]-[#6]-1',
            'N-phenylacetamide': '[#6]1:[#6]:[#6]:[#6](-[#7]-[#6](-[#6])=[#8]):[#6]:[#6]:1',
            'octane': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            '1-methoxy-2-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]',
            '1H-pyrrole-2,5-dione': '[#7]1-[#6](=[#8])-[#6]=[#6]-[#6]-1=[#8]',
            'sulfamic acid': '[#8]-[#16](-[#7])(=[#8])=[#8]',
            '2-methylisoindoline-1,3-dione': '[#6]-[#7]1-[#6](=[#8])-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1=[#8]',
            '(difluoromethyl)phosphonic acid': '[#6](-[#9])(-[#9])-[#15](=[#8])(-[#8])-[#8]',
            'pyrimidin-2-amine': '[#6]1:[#6]:[#6]:[#7]:[#6](-[#7]):[#7]:1',
            '1H-benzo[d]imidazole-5-carboxamide': '[#6]1:[#7]:[#6]2:[#6]:[#6](-[#6](-[#7])=[#8]):[#6]:[#6]:[#6]:2:[#7H]:1',
            '2-methylpropan-2-amine': '[#7]-[#6](-[#6])(-[#6])-[#6]',
            'N-(4-fluorophenyl)formamide': '[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            'oxazole': '[#6]1:[#6]:[#7]:[#6]:[#8]:1',
            'pyridin-3-ylmethanol': '[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridin-3-ol': '[#8]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'picolinamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'cyclopropylmethanol': '[#8]-[#6]-[#6]1-[#6]-[#6]-1',
            'ethyl carbamate': '[#7]-[#6](=[#8])-[#8]-[#6]-[#6]',
            '2-(diethylamino)ethan-1-ol': '[#8]-[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]',
            'pyrocatechol': '[#6]1:[#6]:[#6]:[#6](-[#8]):[#6](-[#8]):[#6]:1',
            'acrylamide': '[#7]-[#6](=[#8])-[#6]=[#6]',
            'azetidine': '[#7]1-[#6]-[#6]-[#6]-1',
            'p-xylene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            '1-methylpiperidin-4-ol': '[#8]-[#6]1-[#6]-[#6]-[#7](-[#6])-[#6]-[#6]-1',
            '4-hydrosulfonylmorpholine': '[#16](=[#8])(=[#8])-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            '4-methyl-1H-imidazole': '[#6]-[#6]1:[#6]:[#7H]:[#6]:[#7]:1',
            'N-(pyridin-4-yl)formamide': '[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '4-methoxyphenol': '[#8]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'fluoromethane': '[#6]-[#9]',
            'N-methylbenzamide': '[#6]-[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridin-3-amine': '[#7]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridin-4-ylmethanamine': '[#7]-[#6]-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'imidazole': '[#6]1:[#7]:[#6]:[#6]:[#7H]:1',
            '3-chlorophenol': '[#8]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#17]):[#6]:1',
            '1-ethylurea': '[#7]-[#6](=[#8])-[#7]-[#6]-[#6]',
            'methyl benzoate': '[#6]1:[#6]:[#6]:[#6](-[#6](=[#8])-[#8]-[#6]):[#6]:[#6]:1',
            '(aminomethylene)bis(phosphonic acid)': '[#7]-[#6](-[#15](=[#8])(-[#8])-[#8])-[#15](=[#8])(-[#8])-[#8]',
            'pyridin-4-amine': '[#7]-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'N-methyl-2-phenylcyclopropan-1-amine': '[#6]-[#7]-[#6]1-[#6]-[#6]-1-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '5-methoxy-3-methyl-1,3,4-oxadiazol-2(3H)-one': '[#6]-[#7]1:[#7]:[#6](-[#8]-[#6]):[#8]:[#6]:1=[#8]',
            '(methylsulfonyl)methane': '[#6]-[#16](-[#6])(=[#8])=[#8]',
            '1-(piperidin-1-yl)ethan-1-one': '[#6]1-[#6]-[#6]-[#7](-[#6](-[#6])=[#8])-[#6]-[#6]-1',
            'methyl acetate': '[#6]-[#6](=[#8])-[#8]-[#6]',
            '4-chlorophenol': '[#8]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'ethane-1,2-diamine': '[#7]-[#6]-[#6]-[#7]',
            '4-methylpiperidine': '[#7]1-[#6]-[#6]-[#6](-[#6])-[#6]-[#6]-1',
            'benzyl formate': '[#6](=[#8])-[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N,N-dimethylsulfonic amide': '[#16](=[#8])(=[#8])-[#7](-[#6])-[#6]',
            '4-methoxybenzaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'N-hydroxyacetamide': '[#6]-[#6](=[#8])-[#7]-[#8]',
            '2-fluoroethan-1-ol': '[#8]-[#6]-[#6]-[#9]',
            '2-aminobenzamide': '[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6](-[#7])=[#8]',
            'N-hydroxypropionamide': '[#6]-[#6]-[#6](=[#8])-[#7]-[#8]',
            '2H-tetrazole': '[#6]1:[#7]:[#7]:[#7H]:[#7]:1',
            'prop-2-yn-1-ol': '[#8]-[#6]-[#6]#[#6]',
            'piperidin-4-ylmethanol': '[#7]1-[#6]-[#6]-[#6](-[#6]-[#8])-[#6]-[#6]-1',
            '3-ethynylpyridine': '[#6]#[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            '4-chlorobenzaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'methylphosphonic acid': '[#6]-[#15](=[#8])(-[#8])-[#8]',
            'isobutyramide': '[#7]-[#6](=[#8])-[#6](-[#6])-[#6]',
            'cyclopropylmethanamine': '[#7]-[#6]-[#6]1-[#6]-[#6]-1',
            'N,N-dimethylpyrrolidin-3-amine': '[#7]1-[#6]-[#6]-[#6](-[#7](-[#6])-[#6])-[#6]-1',
            '4,5-dihydrooxazol-2-amine': '[#6]1-[#6]-[#8]-[#6](-[#7])=[#7]-1',
            '1,2,3,4-tetrahydroisoquinoline': '[#7]1-[#6]-[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1',
            '4-phenylmorpholine': '[#6]1:[#6]:[#6]:[#6](-[#7]2-[#6]-[#6]-[#8]-[#6]-[#6]-2):[#6]:[#6]:1',
            '4,5-dihydro-1H-imidazole': '[#6]1=[#7]-[#6]-[#6]-[#7]-1',
            '3-aminopropan-1-ol': '[#7]-[#6]-[#6]-[#6]-[#8]',
            '2,2,2-trifluoroacetaldehyde': '[#6](=[#8])-[#6](-[#9])(-[#9])-[#9]',
            'trifluoromethanethiol': '[#16]-[#6](-[#9])(-[#9])-[#9]',
            'N-ethylacetamide': '[#6]-[#6]-[#7]-[#6](-[#6])=[#8]',
            'N-methylaniline': '[#7](-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenylmethanethiol': '[#16]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '4-(pyrrolidin-1-yl)piperidine': '[#7]1-[#6]-[#6]-[#6](-[#7]2-[#6]-[#6]-[#6]-[#6]-2)-[#6]-[#6]-1',
            '4-(trifluoromethyl)pyrimidine': '[#6]1:[#7]:[#6]:[#6]:[#6](-[#6](-[#9])(-[#9])-[#9]):[#7]:1',
            '1-methoxy-3-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:1',
            'N-butylformamide': '[#6](=[#8])-[#7]-[#6]-[#6]-[#6]-[#6]',
            '2,2,2-trifluoroethan-1-ol': '[#8]-[#6]-[#6](-[#9])(-[#9])-[#9]',
            'p-toluidine': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            '1,3-dimethoxybenzene': '[#6]1:[#6]:[#6](-[#8]-[#6]):[#6]:[#6](-[#8]-[#6]):[#6]:1',
            'N,N-dimethyl-1-phenylmethanamine': '[#6]-[#7](-[#6])-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '2-methylnaphthalene': '[#6]-[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:1',
            'tetrahydrofuran': '[#6]1-[#6]-[#6]-[#6]-[#8]-1',
            'acrylic acid': '[#6]=[#6]-[#6](=[#8])-[#8]',
            '2-(methylamino)ethan-1-ol': '[#6]-[#7]-[#6]-[#6]-[#8]',
            '4-methylbenzaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            '3,4-dimethyl-1H-pyrazole-5-carboxylic acid': '[#6]-[#6]1:[#6](-[#6]):[#7]:[#7H]:[#6]:1-[#6](=[#8])-[#8]',
            'chloromethane': '[#6]-[#17]',
            'butyramide': '[#7]-[#6](=[#8])-[#6]-[#6]-[#6]',
            '1-chloro-4-hydrosulfonylbenzene': '[#16](=[#8])(=[#8])-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'difluoromethane': '[#6](-[#9])-[#9]',
            '3-(pyrrolidin-1-yl)propan-1-ol': '[#8]-[#6]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-1',
            'cyclopropylbenzene': '[#6]1-[#6]-[#6]-1-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cumene': '[#6]1:[#6]:[#6]:[#6](-[#6](-[#6])-[#6]):[#6]:[#6]:1',
            '2-methyltetrahydrofuran': '[#6]-[#6]1-[#6]-[#6]-[#6]-[#8]-1',
            'N-methylpropan-2-amine': '[#6]-[#7]-[#6](-[#6])-[#6]',
            'alanine': '[#6]-[#6](-[#7])-[#6](=[#8])-[#8]',
            '1,2,3,6-tetrahydropyridine': '[#6]1=[#6]-[#6]-[#7]-[#6]-[#6]-1',
            '2-(trifluoromethyl)pyridine': '[#6]1:[#6]:[#6]:[#6](-[#6](-[#9])(-[#9])-[#9]):[#7]:[#6]:1',
            'hydroquinone': '[#8]-[#6]1:[#6]:[#6]:[#6](-[#8]):[#6]:[#6]:1',
            '4-fluoroaniline': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#6]:1',
            '1-fluoro-2-methoxybenzene': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6](-[#9]):[#6]:1',
            '2-ethylidenehydrazine-1-carbothioamide': '[#6](-[#6])=[#7]-[#7]-[#6](-[#7])=[#16]',
            'furan-2-carbaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'butan-1-amine': '[#7]-[#6]-[#6]-[#6]-[#6]',
            'triaza-1,2-dien-2-ium': '[#7]=[#7+]=[#7]',
            'pyridin-2-ylmethanol': '[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'resorcinol': '[#6]1:[#6]:[#6](-[#8]):[#6]:[#6](-[#8]):[#6]:1',
            'piperidin-3-ol': '[#7]1-[#6]-[#6]-[#6]-[#6](-[#8])-[#6]-1',
            'cyclopropanecarboxamide': '[#7]-[#6](=[#8])-[#6]1-[#6]-[#6]-1',
            '1-methyl-1H-1,2,4-triazole': '[#6]-[#7]1:[#6]:[#7]:[#6]:[#7]:1',
            '4-chlorobenzene-1,2-diol': '[#8]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1-[#8]',
            'N-methyl-1-phenylmethanamine': '[#7](-[#6])-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyrazin-2-amine': '[#6]1:[#6]:[#7]:[#6](-[#7]):[#6]:[#7]:1',
            'thiophen-2-ylmethanamine': '[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            '2-morpholinoethan-1-amine': '[#7]-[#6]-[#6]-[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'thiomorpholine 1,1-dioxide': '[#7]1-[#6]-[#6]-[#16](=[#8])(=[#8])-[#6]-[#6]-1',
            '2-isopropoxypyridine': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6](-[#6])-[#6]):[#7]:[#6]:1',
            'pyridazine': '[#6]1:[#6]:[#6]:[#7]:[#7]:[#6]:1',
            '3-fluoropyridine': '[#6]1:[#6]:[#6]:[#6](-[#9]):[#6]:[#7]:1',
            'isoquinoline': '[#6]1:[#6]:[#7]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2',
            '4-chloroaniline': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'pyrrolidin-2-one': '[#7]1-[#6]-[#6]-[#6]-[#6]-1=[#8]',
            '5-methyloctahydropyrrolo[3,4-b]pyrrole': '[#7]1-[#6]-[#6]-[#6]2-[#6]-[#7](-[#6])-[#6]-[#6]-1-2',
            '4-methoxybenzamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'm-cresol': '[#8]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]):[#6]:1',
            '4,4,5,5-tetramethyl-1,3,2-dioxaborolane': '[#5]1-[#8]-[#6](-[#6])(-[#6])-[#6](-[#6])(-[#6])-[#8]-1',
            'N1,N1-dimethylethane-1,2-diamine': '[#7]-[#6]-[#6]-[#7](-[#6])-[#6]',
            '1-phenylthiourea': '[#7]-[#6](=[#16])-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1-methyl-4-(trifluoromethyl)benzene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#6](-[#9])(-[#9])-[#9]):[#6]:[#6]:1',
            'isopropoxybenzene': '[#6]1:[#6]:[#6]:[#6](-[#8]-[#6](-[#6])-[#6]):[#6]:[#6]:1',
            '4-methoxypiperidine': '[#7]1-[#6]-[#6]-[#6](-[#8]-[#6])-[#6]-[#6]-1',
            '1,2-dichloro-4-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6](-[#17]):[#6]:1',
            '1-(4-chlorophenyl)urea': '[#7]-[#6](=[#8])-[#7]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'thiazol-2-amine': '[#7]-[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'o-xylene': '[#6]1:[#6]:[#6]:[#6](-[#6]):[#6](-[#6]):[#6]:1',
            '2-methyl-1,3,4-oxadiazole': '[#6]1:[#7]:[#7]:[#6](-[#6]):[#8]:1',
            '1-fluoro-3-methylbenzene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#9]):[#6]:1',
            '(methoxymethyl)benzene': '[#6]-[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'hydrazine': '[#7]-[#7]',
            '1-cyclohexylurea': '[#7]-[#6](=[#8])-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'ethanethiol': '[#16]-[#6]-[#6]',
            'N-hydroxypentanamide': '[#6]-[#6]-[#6]-[#6]-[#6](=[#8])-[#7]-[#8]',
            'thiophene-2-carboxamide': '[#7]-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'N-(cyclopropylmethyl)formamide': '[#6](=[#8])-[#7]-[#6]-[#6]1-[#6]-[#6]-1',
            '1-ethyl-2-methylpyrrolidine': '[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-1-[#6]',
            'pyridin-4-ylmethanol': '[#8]-[#6]-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'triethylamine': '[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]',
            '4-hydroxy-2-oxobut-3-enoic acid': '[#6](-[#8])=[#6]-[#6](=[#8])-[#6](=[#8])-[#8]',
            'isonicotinaldehyde': '[#6](=[#8])-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '1,1,1-trifluoroethane': '[#6]-[#6](-[#9])(-[#9])-[#9]',
            'isothiocyanic acid': '[#7]=[#6]=[#16]',
            'phosphonic acid': '[#15](=[#8])(-[#8])-[#8]',
            '2-hydroxy-4-oxobut-2-enoic acid': '[#6](=[#8])-[#6]=[#6](-[#8])-[#6](=[#8])-[#8]',
            'N,N-dimethylpiperidin-4-amine': '[#6]-[#7](-[#6])-[#6]1-[#6]-[#6]-[#7]-[#6]-[#6]-1',
            '1-(pyridin-2-yl)piperazine': '[#7]1-[#6]-[#6]-[#7](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#7]:2)-[#6]-[#6]-1',

        }

        return r_group_smiles, r_group_smarts

    def _get_iupac_blue_book_common_functional_groups():
        
        radical_smiles = {
            'acetamido': 'O=C(N)C',
            'acetoacetyl': 'O=C(C)CC(=O)O',
            'acetyl': 'C(C)=O',
            'acryloyl': 'C=CC(C)=O',
            'alanyl': 'N[CH](C)C(C)=O',
            'beta-alanyl': 'NCCC(C)=O',
            'allyl': '[CH2]C=C',
            'allylidene': '[CH]C=C',
            'amidino': 'NC=N',
            'amino': 'N',
            'amyl': '[CH2]CCCC',
            'anilino': 'NC1=CC=CC=C1',
            'anisidino': 'NC1=CC=C(OC)C=C1',
            'anthranoyl': 'NC1=CC=CC=C1[C](C)=O',
            'arsino': '[AsH3]',
            'azelaoyl': 'O=CCCCCCCCC=O',
            'azido': '[N]=[N+]=[N-]',
            'azo': 'C/N=N/C',
            'azoxy': 'C/N=[N+]([O-])/C',
            'benzal': '[CH]C1=CC=CC=C1',
            'benzamido': 'O=C(N)C1=CC=CC=C1',
            'benzhydrol': 'OC(C1=CC=CC=C1)C2=CC=CC=C2',
            'benzoxy': '[O]CC1=CC=CC=C1',
            'benzoyl': 'O=[C]C1=CC=CC=C1',
            'benzyl': '[CH2]C1=CC=CC=C1',
            'benzylidene': '[CH]C1=CC=CC=C1',
            'benzylidyne': '[C]C1=CC=CC=C1',
            'biphenylyl': 'C1(C2=CC=CC=C2)=CC=CC=[C]1',
            'biphenylene': 'C12=C3C=CC=CC3=C1C=CC=C2',
            'butoxy': '[O]CCCC',
            'sec-butoxy': '[O]C(C)CC',
            'tert-butoxy': '[O]C(C)(C)C',
            'butyl': '[CH2]CCC',
            'sec-butyl': 'CC[CH]C',
            'tert-butyl': 'C[C](C)C',
            'butyryl': 'O=[C]CCC',
            'caproyl': 'CCCCC[C]=O',
            'capryl': 'CCCCCCCC',
            'capryloyl': 'CCCCCCC[C]=O',
            'carbamido': 'C(=O)(N)N',
            'carbamoyl': 'N[C]=O',
            'carbamyl': 'N[C]=O',
            'carbazoyl': 'NN[C]=O',
            'carbethoxy': 'O=[C]OCC',
            'carbonyl': '[CH]=O',
            'carboxy': 'O=[C]O',
            'cetyl': '[CH2]CCCCCCCCCCCCCCC',
            'chloroformyl': 'O=[C]Cl',
            'cinnamoyl': 'O=[C]C=CC1=CC=CC=C1',
            'cinnamyl': '[CH2]C=CC1=CC=CC=C1',
            'cinnamylidene': '[CH]C=CC1=CC=CC=C1',
            'cresyl': 'OC1=CC=C(C)C=C1',
            'crotonoyl': 'C/C=C/[C]=O',
            'crotyl': '[CH2]/C=C/C',
            'cyanamido': '[NH]C#N',
            'cyanato': '[O]C#N',
            'cyano': '[C]#N',
            'decanedioyl': 'O=[C]CCCCCCCC[C]=O',
            'decanoyl': 'CCCCCCCCC[C]=O',
            'diazo': '[N+]=[N-]',
            'diazoamino': 'N=NN',
            'disilanyl': '[SiH2][SiH3]',
            'disiloxanyloxy': '[O][SiH2]O[SiH3]',
            'disulfinyl': 'O=[S]S=O',
            'dithio': '[S]S',
            'enanthoyl': 'CCCCCC[C]=O',
            'epoxy': '[O]',
            'ethenyl': '[CH]=C',
            'ethynyl': '[C]#C',
            'ethoxy': '[O]CC',
            'ethyl': '[CH2]C',
            'ethylene': 'C=C',
            'ethylidene': '[CH]C',
            'ethylthio': '[S]CC',
            'formamido': 'O=C[NH]',
            'formyl': '[CH]=O',
            'furmaroyl': 'O=CO',
            'furfuryl': '[CH2]C1=CC=CO1',
            'furfurylidene': '[CH]C1=CC=CO1',
            'glutamoyl': 'N[C@@H](CC[C]=O)[C]=O',
            'glutaryl': 'O=[C]CCC[C]=O',
            'glycylamino': '[NH]C(CN)=O',
            'glycoloyl': 'OC[C]=O',
            'glycyl': 'NC[C]=O',
            'glyoxyoyl': 'O=[C]C=O',
            'guanidino': '[NH]C(N)=N',
            'guanyl': 'N=[C]N',
            'heptadecanoyl': 'CCCCCCCCCCCCCCCC[C]=O',
            'heptanamido': 'CCCCCCC([NH])=O',
            'heptanoyl': 'CCCCCC[C]=O.CCCCCCC([NH])=O',
            'hexadecanoyl': 'CCCCCCCCCCCCCCC[C]=O.CCCCCC[C]=O.CCCCCCC([NH])=O',
            'hexamethylene': 'CCCCCC',
            'hexanedioyl': 'O=[C]CCCC[C]=O',
            'hippuryl': '[CH2]CNC(C1=CC=CC=C1)=O',
            'hydrazino': 'N[NH]',
            'hydrazo': 'NN',
            'hydrocinnamoyl': 'O=[C]CCC1=CC=CC=C1',
            'hydroperoxy': '[O]O',
            'hydroxyamino': '[NH]O',
            'imino': '[NH]',
            'iodoso': 'I=O',
            'iodyl': 'O=I=O',
            'isoamyl': '[CH2]CC(C)C',
            'isobutenyl': '[CH]=C(C)C',
            'isobutoxy': '[O]CC(C)C',
            'isobutyl': '[CH2]C(C)C',
            'isobutylidene': '[CH]C(C)C',
            'isobutyryl': 'O=[C]C(C)C',
            'isocyanato': '[N]=C=O',
            'isocyano': '[N+]#[C-]',
            'isohexyl': '[CH2]CCC(C)C',
            'isoleucyl': 'N[C@@H]([C@@H](C)CC)[C]=O',
            'isonitroso': '[N]O',
            'isopentyl': '[CH2]CC(C)C',
            'isopentylidene': '[CH]CC(C)C',
            'isopropenyl': 'C=[C]C',
            'isopropoxy': '[O]C(C)C',
            'isopropyl': 'C[CH]C',
            'isopropylidene': 'C[C]C',
            'isothiocynato': 'N=C=S',
            'isovaleryl': 'O=[C]CC(C)C',
            'lactoyl': 'OC(C)[C]=O',
            'lauroyl': 'CCCCCCCCCCC[C]=O',
            'lauryl': '[CH2]CCCCCCCCCCC',
            'leucyl': 'N[C@@H](CC(C)C)[C]=O',
            'levulinoyl': 'O=C(C)CC[C]=O',
            'malonyl': 'O=[C]C[C]=O',
            'mandeloyl': 'OC(C1=CC=CC=C1)[C]=O',
            'mercapto': '[SH]',
            'mesityl': 'CC1=CC(C)=CC(C)=[C]1',
            'methacryloyl': 'CC([C]=O)=C',
            'methallyl': '[CH2]C(C)=C',
            'methionyl': 'N[C@@H](CCSC)[C]=O',
            'methoxy': '[O]C',
            'methyl': '[CH3]',
            'methylene': '[CH2]',
            'methylthio': '[S]C',
            'myristoyl': 'CCCCCCCCCCCCC[C]=O',
            'myristyl': '[CH2]CCCCCCCCCCCCC',
            'naphthyl': 'C12=CC=C[C]=C1C=CC=C2',
            'naphthylene': 'C12=CC=CC=C1C=CC=C2',
            'neopentyl': '[CH2]C(C)(C)C',
            'nitramino': '[NH][N+]([O-])=O',
            'nitro': 'O=[N+][O-]',
            'nitrosamino': '[NH]N=O',
            'nitroso': '[N]=O',
            'nonanoyl': 'CCCCCCCC[C]=O',
            'oleoyl': 'CCCCCCCC/C=C\CCCCCCC[C]=O',
            'oxalyl': 'O=[C]C=O',
            'oxo': '[O]',
            'palmitoyl': 'CCCCCCCCCCCCCCC[C]=O',
            'pentamethylene': 'O=C1C(C=C)[C@@]2([H])SCCN12',
            'pentyl': '[CH2]CCCC',
            'tert-pentyl': 'CC[C](C)C',
            'phenacyl': '[CH2]C(C1=CC=CC=C1)=O',
            'phenacylidene': '[CH]C(C1=CC=CC=C1)=O',
            'phenethyl': '[CH2]CC1=CC=CC=C1',
            'phenoxy': '[O]C1=CC=CC=C1',
            'phenyl': '[C]1=CC=CC=C1',
            'phenylene': 'C1=C[C]=CC=[C]1',
            'phosphino': '[PH2]',
            'phosphinyl': '[PH2]=O',
            'phospho': 'O=[P](O)O',
            'phosphono': 'O=[P](O)O',
            'phthaloyl': 'O=[C]C1=CC=CC=C1[C]=O',
            'picryl': '[O-][N+](C1=CC([N+]([O-])=O)=CC([N+]([O-])=O)=[C]1)=O',
            'pimeloyl': 'O=[C]CCCCC[C]=O',
            'piperidino': '[N]1CCCCC1',
            'pivaloyl': 'CC(C)(C)[C]=O',
            'prenyl': '[CH2]/C=C(C)\C',
            'propargyl': '[CH2]C#C',
            '1-propenyl': '[CH]=CC',
            '2-propenyl': '[CH2]C=C',
            'propionyl': 'O=[C]CC',
            'propoxy': '[O]CCC',
            'propyl': '[CH2]CC',
            'propylidene': '[CH]CC',
            'pyrryl': 'N1[C]=CC=C1',
            'salicyloyl': 'OC1=CC=CC=C1[C]=O',
            'selenyl': '[SeH]',
            'seryl': 'N[C@@H](CO)[C]=O',
            'siloxy': '[O][SiH3]',
            'silyl': '[SiH3]',
            'silyene': '[SiH2]',
            'sorboyl': 'CC=CC=CC(O)=O',
            'stearoyl': 'CCCCCCCCCCCCCCCCC[C]=O',
            'stearyl': '[CH2]CCCCCCCCCCCCCCCCC',
            'styryl': '[CH]=CC1=CC=CC=C1',
            'suberoyl': 'O=[C]CCCCCC[C]=O',
            'succinyl': 'O=[C]CC[C]=O',
            'sulfamino': '[NH]S(=O)(O)=O',
            'sulfamoyl': 'O=[S](N)=O',
            'sulfanilyl': 'O=[S](C1=CC=C(N)C=C1)=O',
            'sulfeno': '[S]O',
            'sulfhydryl': '[SH]',
            'sulfinyl': 'S=O',
            'sulfo': 'O=[S](O)=O',
            'sulfonyl': 'O=S=O',
            'terephthaloyl': 'O=[C]C1=CC=C([C]=O)C=C1',
            'tetramethylene': 'CCCC',
            'thienyl': '[C]1=CC=CS1',
            'thiocarbonyl': '[CH]=S',
            'thiocarboxy': 'S=[C]O',
            'thiocyanato': '[S]C#N',
            'thionyl': 'S=O',
            'threonyl': 'N[C@@H]([C@H](O)C)[C]=O',
            'toluidino': '[NH]C1=CC=C(C)C=C1',
            'toluoyl': 'CC1=CC=C([C]=O)C=C1',
            'tolyl': 'CC1=CC=[C]C=C1',
            'alpha-tolyl': '[C]C1=CC=CC=C1',
            'tolylene': '[CH]C1=CC=CC=C1',
            'tosyl': 'O=[S](C1=CC=C(C)C=C1)=O',
            'triazano': '[NH]N[NH]',
            'trimethylene': 'CCC',
            'trityl': '[C](C1=CC=CC=C1)(C2=CC=CC=C2)C3=CC=CC=C3',
            'valeryl': 'O=[C]CCCC',
            'valyl': 'N[C@@H](C(C)C)[C]=O',
            'vinyl': '[CH]=C',
            'vinylidene': '[C]=C',
            'xylidino': '[NH]C1=CC=C(C)C=C1C',
            'xylyl': 'CC1=CC=[C]C(C)=C1',
            'xylylene': 'NCC1=CC=CC(CN)=C1',
        }

        radical_smarts = {
            'acetamido':'[#8]=[#6](-[#7])-[#6]',
            'acetoacetyl':'[#8]=[#6](-[#6])-[#6]-[#6](=[#8])-[#8]',
            'acetyl':'[#6](-[#6])=[#8]',
            'acryloyl':'[#6]=[#6]-[#6](-[#6])=[#8]',
            'alanyl':'[#7]-[#6H](-[#6])-[#6](-[#6])=[#8]',
            'beta-alanyl':'[#7]-[#6]-[#6]-[#6](-[#6])=[#8]',
            'allyl':'[#6H2]-[#6]=[#6]',
            'allylidene':'[#6H]-[#6]=[#6]',
            'amidino':'[#7]-[#6]=[#7]',
            'amino':'[#7]',
            'amyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]',
            'anilino':'[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'anisidino':'[#7]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'anthranoyl':'[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6](-[#6])=[#8]',
            'arsino':'[AsH3]',
            'azelaoyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'azido':'[#7]=[#7+]=[#7-]',
            'azo':'[#6]/[#7]=[#7]/[#6]',
            'azoxy':'[#6]/[#7]=[#7+](\[#8-])-[#6]',
            'benzal':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzamido':'[#8]=[#6](-[#7])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzhydrol':'[#8]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzoxy':'[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzoyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzyl':'[#6H2]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzylidene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzylidyne':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'biphenylyl':'[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'biphenylene':'[#6]12=[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3=[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'butoxy':'[#8]-[#6]-[#6]-[#6]-[#6]',
            'sec-butoxy':'[#8]-[#6](-[#6])-[#6]-[#6]',
            'tert-butoxy':'[#8]-[#6](-[#6])(-[#6])-[#6]',
            'butyl':'[#6H2]-[#6]-[#6]-[#6]',
            'sec-butyl':'[#6]-[#6]-[#6H]-[#6]',
            'tert-butyl':'[#6]-[#6](-[#6])-[#6]',
            'butyryl':'[#8]=[#6]-[#6]-[#6]-[#6]',
            'caproyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'capryl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'capryloyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'carbamido':'[#6](=[#8])(-[#7])-[#7]',
            'carbamoyl':'[#7]-[#6]=[#8]',
            'carbamyl':'[#7]-[#6]=[#8]',
            'carbazoyl':'[#7]-[#7]-[#6]=[#8]',
            'carbethoxy':'[#8]=[#6]-[#8]-[#6]-[#6]',
            'carbonyl':'[#6H]=[#8]',
            'carboxy':'[#8]=[#6]-[#8]',
            'cetyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'chloroformyl':'[#8]=[#6]-[#17]',
            'cinnamoyl':'[#8]=[#6]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cinnamyl':'[#6H2]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cinnamylidene':'[#6H]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cresyl':'[#8]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            'crotonoyl':'[#6]/[#6]=[#6]/[#6]=[#8]',
            'crotyl':'[#6H2]/[#6]=[#6]/[#6]',
            'cyanamido':'[#7H]-[#6]#[#7]',
            'cyanato':'[#8]-[#6]#[#7]',
            'cyano':'[#6]#[#7]',
            'decanedioyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'decanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'diazo':'[#7+]=[#7-]',
            'diazoamino':'[#7]=[#7]-[#7]',
            'disilanyl':'[SiH2]-[SiH3]',
            'disiloxanyloxy':'[#8]-[SiH2]-[#8]-[SiH3]',
            'disulfinyl':'[#8]=[#16]-[#16]=[#8]',
            'dithio':'[#16]-[#16]',
            'enanthoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'epoxy':'[#8]',
            'ethenyl':'[#6H]=[#6]',
            'ethynyl':'[#6]#[#6]',
            'ethoxy':'[#8]-[#6]-[#6]',
            'ethyl':'[#6H2]-[#6]',
            'ethylene':'[#6]=[#6]',
            'ethylidene':'[#6H]-[#6]',
            'ethylthio':'[#16]-[#6]-[#6]',
            'formamido':'[#8]=[#6]-[#7H]',
            'formyl':'[#6H]=[#8]',
            'furmaroyl':'[#8]=[#6]-[#8]',
            'furfuryl':'[#6H2]-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'furfurylidene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'glutamoyl':'[#7]-[#6@@H](-[#6]-[#6]-[#6]=[#8])-[#6]=[#8]',
            'glutaryl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'glycylamino':'[#7H]-[#6](-[#6]-[#7])=[#8]',
            'glycoloyl':'[#8]-[#6]-[#6]=[#8]',
            'glycyl':'[#7]-[#6]-[#6]=[#8]',
            'glyoxyoyl':'[#8]=[#6]-[#6]=[#8]',
            'guanidino':'[#7H]-[#6](-[#7])=[#7]',
            'guanyl':'[#7]=[#6]-[#7]',
            'heptadecanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'heptanamido':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'heptanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'hexadecanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'hexamethylene':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'hexanedioyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'hippuryl':'[#6H2]-[#6]-[#7]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'hydrazino':'[#7]-[#7H]',
            'hydrazo':'[#7]-[#7]',
            'hydrocinnamoyl':'[#8]=[#6]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'hydroperoxy':'[#8]-[#8]',
            'hydroxyamino':'[#7H]-[#8]',
            'imino':'[#7H]',
            'iodoso':'[#53]=[#8]',
            'iodyl':'[#8]=[#53]=[#8]',
            'isoamyl':'[#6H2]-[#6]-[#6](-[#6])-[#6]',
            'isobutenyl':'[#6H]=[#6](-[#6])-[#6]',
            'isobutoxy':'[#8]-[#6]-[#6](-[#6])-[#6]',
            'isobutyl':'[#6H2]-[#6](-[#6])-[#6]',
            'isobutylidene':'[#6H]-[#6](-[#6])-[#6]',
            'isobutyryl':'[#8]=[#6]-[#6](-[#6])-[#6]',
            'isocyanato':'[#7]=[#6]=[#8]',
            'isocyano':'[#7+]#[#6-]',
            'isohexyl':'[#6H2]-[#6]-[#6]-[#6](-[#6])-[#6]',
            'isoleucyl':'[#7]-[#6@@H](-[#6@@H](-[#6])-[#6]-[#6])-[#6]=[#8]',
            'isonitroso':'[#7]-[#8]',
            'isopentyl':'[#6H2]-[#6]-[#6](-[#6])-[#6]',
            'isopentylidene':'[#6H]-[#6]-[#6](-[#6])-[#6]',
            'isopropenyl':'[#6]=[#6]-[#6]',
            'isopropoxy':'[#8]-[#6](-[#6])-[#6]',
            'isopropyl':'[#6]-[#6H]-[#6]',
            'isopropylidene':'[#6]-[#6]-[#6]',
            'isothiocynato':'[#7]=[#6]=[#16]',
            'isovaleryl':'[#8]=[#6]-[#6]-[#6](-[#6])-[#6]',
            'lactoyl':'[#8]-[#6](-[#6])-[#6]=[#8]',
            'lauroyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'lauryl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'leucyl':'[#7]-[#6@@H](-[#6]-[#6](-[#6])-[#6])-[#6]=[#8]',
            'levulinoyl':'[#8]=[#6](-[#6])-[#6]-[#6]-[#6]=[#8]',
            'malonyl':'[#8]=[#6]-[#6]-[#6]=[#8]',
            'mandeloyl':'[#8]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]=[#8]',
            'mercapto':'[#16H]',
            'mesityl':'[#6]-[#6]1:[#6]:[#6](-[#6]):[#6]:[#6](-[#6]):[#6]:1',
            'methacryloyl':'[#6]-[#6](-[#6]=[#8])=[#6]',
            'methallyl':'[#6H2]-[#6](-[#6])=[#6]',
            'methionyl':'[#7]-[#6@@H](-[#6]-[#6]-[#16]-[#6])-[#6]=[#8]',
            'methoxy':'[#8]-[#6]',
            'methyl':'[#6H3]',
            'methylene':'[#6H2]',
            'methylthio':'[#16]-[#6]',
            'myristoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'myristyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'naphthyl':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'naphthylene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'neopentyl':'[#6H2]-[#6](-[#6])(-[#6])-[#6]',
            'nitramino':'[#7H]-[#7+](-[#8-])=[#8]',
            'nitro':'[#8]=[#7+]-[#8-]',
            'nitrosamino':'[#7H]-[#7]=[#8]',
            'nitroso':'[#7]=[#8]',
            'nonanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'oleoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]/[#6]=[#6]\[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'oxalyl':'[#8]=[#6]-[#6]=[#8]',
            'oxo':'[#8]',
            'palmitoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'pentamethylene':'[#8]=[#6]1-[#6](-[#6]=[#6])-[#6@H]2-[#16]-[#6]-[#6]-[#7]-1-2',
            'pentyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]',
            'tert-pentyl':'[#6]-[#6]-[#6](-[#6])-[#6]',
            'phenacyl':'[#6H2]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'phenacylidene':'[#6H]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'phenethyl':'[#6H2]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenoxy':'[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenyl':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenylene':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phosphino':'[#15H2]',
            'phosphinyl':'[#15H2]=[#8]',
            'phospho':'[#8]=[#15](-[#8])-[#8]',
            'phosphono':'[#8]=[#15](-[#8])-[#8]',
            'phthaloyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]=[#8]',
            'picryl':'[#8-]-[#7+](-[#6]1:[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:1)=[#8]',
            'pimeloyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'piperidino':'[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'pivaloyl':'[#6]-[#6](-[#6])(-[#6])-[#6]=[#8]',
            'prenyl':'[#6H2]-[#6]=[#6](-[#6])-[#6]',
            'propargyl':'[#6H2]-[#6]#[#6]',
            '1-propenyl':'[#6H]=[#6]-[#6]',
            '2-propenyl':'[#6H2]-[#6]=[#6]',
            'propionyl':'[#8]=[#6]-[#6]-[#6]',
            'propoxy':'[#8]-[#6]-[#6]-[#6]',
            'propyl':'[#6H2]-[#6]-[#6]',
            'propylidene':'[#6H]-[#6]-[#6]',
            'pyrryl':'[#7H]1:[#6]:[#6]:[#6]:[#6]:1',
            'salicyloyl':'[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]=[#8]',
            'selenyl':'[SeH]',
            'seryl':'[#7]-[#6@@H](-[#6]-[#8])-[#6]=[#8]',
            'siloxy':'[#8]-[SiH3]',
            'silyl':'[SiH3]',
            'silyene':'[SiH2]',
            'sorboyl':'[#6]-[#6]=[#6]-[#6]=[#6]-[#6](-[#8])=[#8]',
            'stearoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'stearyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'styryl':'[#6H]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'suberoyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'succinyl':'[#8]=[#6]-[#6]-[#6]-[#6]=[#8]',
            'sulfamino':'[#7H]-[#16](=[#8])(-[#8])=[#8]',
            'sulfamoyl':'[#8]=[#16](-[#7])=[#8]',
            'sulfanilyl':'[#8]=[#16](-[#6]1:[#6]:[#6]:[#6](-[#7]):[#6]:[#6]:1)=[#8]',
            'sulfeno':'[#16]-[#8]',
            'sulfhydryl':'[#16H]',
            'sulfinyl':'[#16]=[#8]',
            'sulfo':'[#8]=[#16](-[#8])=[#8]',
            'sulfonyl':'[#8]=[#16]=[#8]',
            'terephthaloyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:1',
            'tetramethylene':'[#6]-[#6]-[#6]-[#6]',
            'thienyl':'[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'thiocarbonyl':'[#6H]=[#16]',
            'thiocarboxy':'[#16]=[#6]-[#8]',
            'thiocyanato':'[#16]-[#6]#[#7]',
            'thionyl':'[#16]=[#8]',
            'threonyl':'[#7]-[#6@@H](-[#6@H](-[#8])-[#6])-[#6]=[#8]',
            'toluidino':'[#7H]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            'toluoyl':'[#6]-[#6]1:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:1',
            'tolyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'alpha-tolyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tolylene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tosyl':'[#8]=[#16](-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1)=[#8]',
            'triazano':'[#7H]-[#7]-[#7H]',
            'trimethylene':'[#6]-[#6]-[#6]',
            'trityl':'[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'valeryl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]',
            'valyl':'[#7]-[#6@@H](-[#6](-[#6])-[#6])-[#6]=[#8]',
            'vinyl':'[#6H]=[#6]',
            'vinylidene':'[#6]=[#6]',
            'xylidino':'[#7H]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1-[#6]',
            'xylyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]):[#6]:1',
            'xylylene':'[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]-[#7]):[#6]:1',
        }
        
        rings_smiles = {
            'cyclopropane': 'C1CC1',
            'spiropentane': 'C1CC12CC2',
            'cyclobutane': 'C1CCC1',
            'cyclopentane': 'C1CCCC1',
            'furan': 'O1C=CC=C1',
            'thiophene': 'C1=CC=CS1',
            'pyrrole': 'N1C=CC=C1',
            '2H-pyrrole': 'N1=CC=CC1',
            '3H-pyrrole': 'N1=CCC=C1',
            'pyrazole': 'N1N=CC=C1',
            '2H-imidazole': 'C1N=CC=N1',
            '1,2,3-triazole': 'N1N=NC=C1',
            '1,2,4-triazole': 'N1N=CN=C1',
            '1,2-dithiole': 'S1SC=CC1',
            '1,3-dithiole': 'S1CSC=C1',
            '3H-1,2-oxathiole': 'O1SCC=C1',
            'isoxazole': 'O1N=CC=C1',
            'oxazole': 'O1C=NC=C1',
            'thiazole': 'S1C=NC=C1',
            'isothiazole': 'S1N=CC=C1',
            '1,2,3-oxadiazole': 'O1N=NC=C1',
            '1,2,4-oxadiazole': 'O1N=CN=C1',
            '1,2,5-oxadiazole': 'O1N=CC=N1',
            '1,3,4-oxadiazole': 'O1C=NN=C1',
            '1,2,3,4-oxatriazole': 'O1N=NN=C1',
            '1,2,3,5-oxatriazole': 'O1N=NC=N1',
            '3H-1,2,3-dioxazole': 'O1ONC=C1',
            '1,2,4-dioxazole': 'O1OC=NC1',
            '1,3,2-dioxazole': 'O1NOC=C1',
            '1,3,4-dioxazole': 'O1CON=C1',
            '5H-1,2,5-oxathiazole': 'O1SC=CN1',
            '1,3-oxathiole': 'O1CSC=C1',
            'benzene': 'C1=CC=CC=C1',
            'cyclohexane': 'C1CCCCC1',
            '2H-pyran': 'C1C=CC=CO1',
            '4H-pyran': 'C1=CCC=CO1',
            '2H-pyran-2-one': 'O=C1C=CC=CO1',
            '4H-pyran-4-one': 'O=C1C=COC=C1',
            '1,2-dioxin': 'O1OC=CC=C1',
            '1,3-dioxin': 'O1COC=CC1',
            'pyridine': 'C1=NC=CC=C1',
            'pyridazine': 'C1=NN=CC=C1',
            'pyrimidine': 'C1=NC=CC=N1',
            'pyrazine': 'C1=NC=CN=C1',
            'piperazine': 'N1CCNCC1',
            '1,3,5-triazine': 'N1=CN=CN=C1',
            '1,2,4-triazine': 'N1=NC=NC=C1',
            '1,2,3-triazine': 'N1=NN=CC=C1',
            '4H-1,2-Oxazine': 'O1N=CCC=C1',
            '2H-1,3-Oxazine': 'O1CN=CC=C1',
            '6H-1,3-Oxazine': 'O1C=NC=CC1',
            '6H-1,2-Oxazine': 'O1N=CC=CC1',
            '1,4-Oxazine': 'O1C=CN=CC1',
            '2H-1,2-Oxazine': 'O1NC=CC=C1',
            '4H-1,4-Oxazine': 'O1C=CNC=C1',
            '1,2,5-Oxathiazine': 'O1SC=CN=C1',
            '1,2,6-Oxathiazine': 'O1SC=CC=N1',
            '1,2,4-Oxadiazine': 'O1NC=NC=C1',
            '1,3,5-Oxadiazine': 'O1C=NC=NC1',
            'morpholine': 'N1CCOCC1',
            'azepine': 'N1C=CC=CC=C1',
            'oxepin': 'O1C=CC=CC=C1',
            'thiepin': 'S1C=CC=CC=C1',
            '4H-1,2-diazepine': 'N1=CC=CCC=N1',
            'indene': 'C12=C(CC=C2)C=CC=C1',
            '2H-indene': 'C12=CCC=C1C=CC=C2',
            'benzofuran': 'C12=CC=CC=C1C=CO2',
            'isobenzofuran': 'C12=COC=C1C=CC=C2',
            'benzo[b]thiophene': 'C12=CC=CC=C1C=CS2',
            'benzo[c]thiophene': 'C12=CSC=C1C=CC=C2',
            'indole': 'C12=C(NC=C2)C=CC=C1',
            '3H-indole': 'C12=C(N=CC2)C=CC=C1',
            '1H-indole': 'C12=C(NC=C2)C=CC=C1',
            'cyclopenta[b]pyridine': 'C12=CC=CC1=CC=CN2',
            'pyrano[3,4-b]-pyrrole': 'C12=COC=CC1=CC=N2',
            'indazole': 'C12=C(NN=C2)C=CC=C1',
            'benzisoxazole': 'C12=NOC=C1C=CC=C2',
            'benzoxazole': 'C12=CC=CC=C1OC=N2',
            '2,1-benzisoxazole': 'C12=CON=C1C=CC=C2',
            'naphthalene': 'C12=CC=CC=C1C=CC=C2',
            '1,2,3,4-tetrahydronaphthalene': 'C12=C(CCCC2)C=CC=C1',
            'octahydronaphthalene': 'C12CCCCC1=CCCC2',
            '2H-1-benzopyran': 'C12=CC=CC=C1OCC=C2',
            '2H-1-benzopyran-2-one': 'O=C1C=CC2=CC=CC=C2O1',
            '4H-1-benzopyran-4-one': 'O=C1C=COC2=CC=CC=C12',
            '1H-2-benzopyran-1-one': 'O=C1C2=CC=CC=C2C=CO1',
            '3H-2-benzopyran-1-one': 'O=C1C2=CC=CC=C2CCO1',
            'quinoline': 'C12=CC=CC=C1N=CC=C2',
            'isoquinoline': 'C12=C(C=NC=C2)C=CC=C1',
            'cinnoline': 'C12=CC=NN=C1C=CC=C2',
            'quinazoline': 'C12=CN=CN=C1C=CC=C2',
            '1,8-napthyhridine': 'C1=CC2=C(N=C1)N=CC=C2',
            '1,7-napththyridine': 'C1=CC2=C(C=NC=C2)N=C1',
            '1,5-napththridine': 'C1=CC2=C(C=CC=N2)N=C1',
            '1,6-napthyridine': 'C1=CC2=C(C=CN=C2)N=C1',
            '2H-1,3-benzoxazine': 'C12=CC=CC=C1OCN=C2',
            '2H-1,4-benzoxazine': 'C12=CC=CC=C1OCC=N2',
            '1H-2,3-benzoxazine': 'C12=CC=CC=C1CON=C2',
            '4H-3,1-benzoxazine': 'C12=CC=CC=C1N=COC2',
            '2H-1,2-benzoxazine': 'C12=CC=CC=C1ONC=C2',
            '4H-1,3-benzoxazine': 'C12=CC=CC=C1OC=NC2',
            'anthracene': 'C12=CC=CC=C1C=C3C=CC=CC3=C2',
            'phenanthrene': 'C12=CC=CC=C1C=CC3=CC=CC=C23',
            'phenalene': 'C12=C3C(CC=C2)=CC=CC3=CC=C1',
            'fluorene': 'C1(CC2=C3C=CC=C2)=C3C=CC=C1',
            'carbazole': 'C1(NC2=C3C=CC=C2)=C3C=CC=C1',
            'xanthene': 'C1(CC2=C(C=CC=C2)O3)=C3C=CC=C1',
            'acridine': 'C12=NC3=CC=CC=C3C=C1C=CC=C2',
            'norpinane': 'C1(C2)CCCC2C1',
            '7H-purine': 'C12=NC=NC=C1NC=N2',
            'steroid_ring_system': 'C12CCCCC1C3C(C(CCC4)C4CC3)CC2',
            
        }

        rings_smarts = {
            'cyclopropane':'[#6]1-[#6]-[#6]-1',
            'spiropentane':'[#6]1-[#6]-[#6]-12-[#6]-[#6]-2',
            'cyclobutane':'[#6]1-[#6]-[#6]-[#6]-1',
            'cyclopentane':'[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'furan':'[#8]1:[#6]:[#6]:[#6]:[#6]:1',
            'thiophene':'[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'pyrrole':'[#7H]1:[#6]:[#6]:[#6]:[#6]:1',
            '2H-pyrrole':'[#7]1=[#6]-[#6]=[#6]-[#6]-1',
            '3H-pyrrole':'[#7]1=[#6]-[#6]-[#6]=[#6]-1',
            'pyrazole':'[#7H]1:[#7]:[#6]:[#6]:[#6]:1',
            '2H-imidazole':'[#6]1-[#7]=[#6]-[#6]=[#7]-1',
            '1,2,3-triazole':'[#7H]1:[#7]:[#7]:[#6]:[#6]:1',
            '1,2,4-triazole':'[#7H]1:[#7]:[#6]:[#7]:[#6]:1',
            '1,2-dithiole':'[#16]1-[#16]-[#6]=[#6]-[#6]-1',
            '1,3-dithiole':'[#16]1-[#6]-[#16]-[#6]=[#6]-1',
            '3H-1,2-oxathiole':'[#8]1-[#16]-[#6]-[#6]=[#6]-1',
            'isoxazole':'[#8]1:[#7]:[#6]:[#6]:[#6]:1',
            'oxazole':'[#8]1:[#6]:[#7]:[#6]:[#6]:1',
            'thiazole':'[#16]1:[#6]:[#7]:[#6]:[#6]:1',
            'isothiazole':'[#16]1:[#7]:[#6]:[#6]:[#6]:1',
            '1,2,3-oxadiazole':'[#8]1:[#7]:[#7]:[#6]:[#6]:1',
            '1,2,4-oxadiazole':'[#8]1:[#7]:[#6]:[#7]:[#6]:1',
            '1,2,5-oxadiazole':'[#8]1:[#7]:[#6]:[#6]:[#7]:1',
            '1,3,4-oxadiazole':'[#8]1:[#6]:[#7]:[#7]:[#6]:1',
            '1,2,3,4-oxatriazole':'[#8]1:[#7]:[#7]:[#7]:[#6]:1',
            '1,2,3,5-oxatriazole':'[#8]1:[#7]:[#7]:[#6]:[#7]:1',
            '3H-1,2,3-dioxazole':'[#8]1-[#8]-[#7]-[#6]=[#6]-1',
            '1,2,4-dioxazole':'[#8]1-[#8]-[#6]=[#7]-[#6]-1',
            '1,3,2-dioxazole':'[#8]1-[#7]-[#8]-[#6]=[#6]-1',
            '1,3,4-dioxazole':'[#8]1-[#6]-[#8]-[#7]=[#6]-1',
            '5H-1,2,5-oxathiazole':'[#8]1-[#16]-[#6]=[#6]-[#7]-1',
            '1,3-oxathiole':'[#8]1-[#6]-[#16]-[#6]=[#6]-1',
            'benzene':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cyclohexane':'[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '2H-pyran':'[#6]1-[#6]=[#6]-[#6]=[#6]-[#8]-1',
            '4H-pyran':'[#6]1=[#6]-[#6]-[#6]=[#6]-[#8]-1',
            '2H-pyran-2-one':'[#8]=[#6]1:[#6]:[#6]:[#6]:[#6]:[#8]:1',
            '4H-pyran-4-one':'[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]:[#6]:1',
            '1,2-dioxin':'[#8]1-[#8]-[#6]=[#6]-[#6]=[#6]-1',
            '1,3-dioxin':'[#8]1-[#6]-[#8]-[#6]=[#6]-[#6]-1',
            'pyridine':'[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridazine':'[#6]1:[#7]:[#7]:[#6]:[#6]:[#6]:1',
            'pyrimidine':'[#6]1:[#7]:[#6]:[#6]:[#6]:[#7]:1',
            'pyrazine':'[#6]1:[#7]:[#6]:[#6]:[#7]:[#6]:1',
            'piperazine':'[#7]1-[#6]-[#6]-[#7]-[#6]-[#6]-1',
            '1,3,5-triazine':'[#7]1:[#6]:[#7]:[#6]:[#7]:[#6]:1',
            '1,2,4-triazine':'[#7]1:[#7]:[#6]:[#7]:[#6]:[#6]:1',
            '1,2,3-triazine':'[#7]1:[#7]:[#7]:[#6]:[#6]:[#6]:1',
            '4H-1,2-Oxazine':'[#8]1-[#7]=[#6]-[#6]-[#6]=[#6]-1',
            '2H-1,3-Oxazine':'[#8]1-[#6]-[#7]=[#6]-[#6]=[#6]-1',
            '6H-1,3-Oxazine':'[#8]1-[#6]=[#7]-[#6]=[#6]-[#6]-1',
            '6H-1,2-Oxazine':'[#8]1-[#7]=[#6]-[#6]=[#6]-[#6]-1',
            '1,4-Oxazine':'[#8]1-[#6]=[#6]-[#7]=[#6]-[#6]-1',
            '2H-1,2-Oxazine':'[#8]1-[#7]-[#6]=[#6]-[#6]=[#6]-1',
            '4H-1,4-Oxazine':'[#8]1-[#6]=[#6]-[#7]-[#6]=[#6]-1',
            '1,2,5-Oxathiazine':'[#8]1-[#16]-[#6]=[#6]-[#7]=[#6]-1',
            '1,2,6-Oxathiazine':'[#8]1-[#16]-[#6]=[#6]-[#6]=[#7]-1',
            '1,2,4-Oxadiazine':'[#8]1-[#7]-[#6]=[#7]-[#6]=[#6]-1',
            '1,3,5-Oxadiazine':'[#8]1-[#6]=[#7]-[#6]=[#7]-[#6]-1',
            'morpholine':'[#7]1-[#6]-[#6]-[#8]-[#6]-[#6]-1',
            'azepine':'[#7]1-[#6]=[#6]-[#6]=[#6]-[#6]=[#6]-1',
            'oxepin':'[#8]1-[#6]=[#6]-[#6]=[#6]-[#6]=[#6]-1',
            'thiepin':'[#16]1-[#6]=[#6]-[#6]=[#6]-[#6]=[#6]-1',
            '4H-1,2-diazepine':'[#7]1=[#6]-[#6]=[#6]-[#6]-[#6]=[#7]-1',
            'indene':'[#6]12:[#6](-[#6]-[#6]=[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            '2H-indene':'[#6]12=[#6]-[#6]-[#6]=[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'benzofuran':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#8]:2',
            'isobenzofuran':'[#6]12:[#6]:[#8]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'benzo[b]thiophene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#16]:2',
            'benzo[c]thiophene':'[#6]12:[#6]:[#16]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'indole':'[#6]12:[#6](:[#7H]:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:2',
            '3H-indole':'[#6]12:[#6](-[#7]=[#6]-[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            '1H-indole':'[#6]12:[#6](:[#7H]:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:2',
            'cyclopenta[b]pyridine':'[#6]12:[#6]:[#6]:[#6]:[#6]-1:[#6]:[#6]:[#6]:[#7H]:2',
            'pyrano[3,4-b]-pyrrole':'[#6]12:[#6]:[#8]:[#6]:[#6]:[#6]-1:[#6]:[#6]:[#7]:2',
            'indazole':'[#6]12:[#6](:[#7H]:[#7]:[#6]:1):[#6]:[#6]:[#6]:[#6]:2',
            'benzisoxazole':'[#6]12:[#7]:[#8]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'benzoxazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#8]:[#6]:[#7]:2',
            '2,1-benzisoxazole':'[#6]12:[#6]:[#8]:[#7]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'naphthalene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '1,2,3,4-tetrahydronaphthalene':'[#6]12:[#6](-[#6]-[#6]-[#6]-[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            'octahydronaphthalene':'[#6]12-[#6]-[#6]-[#6]-[#6]-[#6]-1=[#6]-[#6]-[#6]-[#6]-2',
            '2H-1-benzopyran':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]-[#6]=[#6]-2',
            '2H-1-benzopyran-2-one':'[#8]=[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#8]:1',
            '4H-1-benzopyran-4-one':'[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2',
            '1H-2-benzopyran-1-one':'[#8]=[#6]1:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:[#6]:[#8]:1',
            '3H-2-benzopyran-1-one':'[#8]=[#6]1-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-[#6]-[#8]-1',
            'quinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#6]:[#6]:2',
            'isoquinoline':'[#6]12:[#6](:[#6]:[#7]:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:2',
            'cinnoline':'[#6]12:[#6]:[#6]:[#7]:[#7]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'quinazoline':'[#6]12:[#6]:[#7]:[#6]:[#7]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '1,8-napthyhridine':'[#6]1:[#6]:[#6]2:[#6](:[#7]:[#6]:1):[#7]:[#6]:[#6]:[#6]:2',
            '1,7-napththyridine':'[#6]1:[#6]:[#6]2:[#6](:[#6]:[#7]:[#6]:[#6]:2):[#7]:[#6]:1',
            '1,5-napththridine':'[#6]1:[#6]:[#6]2:[#6](:[#6]:[#6]:[#6]:[#7]:2):[#7]:[#6]:1',
            '1,6-napthyridine':'[#6]1:[#6]:[#6]2:[#6](:[#6]:[#6]:[#7]:[#6]:2):[#7]:[#6]:1',
            '2H-1,3-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]-[#7]=[#6]-2',
            '2H-1,4-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]-[#6]=[#7]-2',
            '1H-2,3-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#8]-[#7]=[#6]-2',
            '4H-3,1-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#7]=[#6]-[#8]-[#6]-2',
            '2H-1,2-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#7]-[#6]=[#6]-2',
            '4H-1,3-benzoxazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]=[#7]-[#6]-2',
            'anthracene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:2',
            'phenanthrene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:2:1',
            'phenalene':'[#6]12:[#6]3:[#6](-[#6]-[#6]=[#6]-1):[#6]:[#6]:[#6]:[#6]:3:[#6]:[#6]:[#6]:2',
            'fluorene':'[#6]12-[#6]-[#6]3:[#6](:[#6]:[#6]:[#6]:[#6]:3)-[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'carbazole':'[#6]12:[#7H]:[#6]3:[#6](:[#6]:[#6]:[#6]:[#6]:3):[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'xanthene':'[#6]12-[#6]-[#6]3:[#6](:[#6]:[#6]:[#6]:[#6]:3)-[#8]-[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'acridine':'[#6]12:[#7]:[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'norpinane':'[#6]12-[#6]-[#6](-[#6]-[#6]-[#6]-1)-[#6]-2',
            '7H-purine':'[#6]12:[#7]:[#6]:[#7]:[#6]:[#6]:1:[#7H]:[#6]:[#7]:2',
            'steroid_ring_system':'[#6]12-[#6]-[#6]-[#6]-[#6]-[#6]-1-[#6]1-[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-1)-[#6]-[#6]-2',
        }
        
        return radical_smiles, radical_smarts, rings_smiles, rings_smarts

    def _get_rings_in_drugs():

        rings_in_drugs_smiles = {
            "benzene": "C1=CC=CC=C1",
            "pyridine": "C1=CC=CN=C1",
            "piperidine": "N1CCCCC1",
            "piperazine": "N1CCNCC1",
            "cyclohexane": "C1CCCCC1",
            "oxane": "O1CCCCC1",
            "imidazole": "C1=NC=CN1",
            "pyrrolidine": "C1CCNC1",
            "(R)-5-thia-1-azabicyclo[4.2.0]oct-2-en-8-one": "O=C1C[C@@H]2N1C=CCS2",
            "cyclopropane": "C1CC1",
            "tetrahydrofuran" : "C1CCOC1",
            "thiazole": "C1=NC=CS1",
            "indole": "C12=CC=CC=C1C=CN2",
            "diazine": "C1=NC=CC=N1",
            "(R)-4-thia-1-azabicyclo[3.2.0]heptan-7-one": "O=C1N2CCS[C@@H]2C1",
            "6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1C=CC(C2C[C@H](CCC3)C3CC2)C(CCC)=C1",
            "tetrazole": "N1=NN=C[N]1",
            "cyclopentane": "C1CCCC1",
            "thiophenyl" : "C1=CC=CS1",
            "naphthalene": "C12=CC=CC=C1C=CC=C2",
            "1H-benzo[d]imidazole" : "C12=CC=CC=C1N=CN2",
            "quinoline": "C12=CC=CC=C1C=CC=N2",
            "1H-purine": "C12=CNC=NC1=NC=N2",
            "1,2,6,7,8,9,10,11,12,13,14,15,16,17-tetradecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1CCC([C@@H]2C[C@H](CCC3)C3CC2)C(CCC)=C1",
            "furan" : "C1=CC=CO1",
            "1H-1,2,4-Triazole": "N1=CN=CN1",
            "10H-Phenothiazine" : "C12=CC=CC=C1NC3=C(C=CC=C3)S2",
            "quinazoline" : "C12=CC=CC=C1C=NC=N2",
            "morpholine": "C1CNCCO1",
            "pyrimidin-2(1H)-one" : "O=C1N=CC=CN1",
            "quinolin-4(1H)-one": "O=C1C2=C(C=CC=C2)NC=C1",
            "(9S,14R)-6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one": "O=C1C=CC([C@H]2CCC3[C@@H](CCC3)C2)C(CCC)=C1",
            "isoxazole": "C1=CC=NO1",
            "imidazoline": "C1=NCCN1",
            "1,4-dihydropyridine": "C1=CCC=CN1",
            "pyrimidine-2,4(1H,3H)-dione": "O=C(N1)NC=CC1=O",
            "3,4-dihydro-2H-benzo[e][1,4]diazepin-2-one": "O=C1N=C2C=CC=CC2=CNC1",
            "cyclohexene": "C1=CCCCC1",
            "pyrrolidin-2-one": "O=C1NCCC1",
            "imidazolidine-2,4-dione": "O=C(CN1)NC1=O",
            "1,2,3,4-tetrahydroisoquinoline": "C1(C=CC=C2)=C2CCNC1",
            "3,4-dihydro-2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide": "O=S1(NCNC2=C1C=CC=C2)=O",
            "7,8,9,11,12,13,14,15,16,17-decahydro-6H-cyclopenta[a]phenanthrene": "CCCC1=CC=CC=C1[C@@H]2C[C@H](CCC3)C3CC2",
            "1H-pyrazole": "N1=CC=CN1",
            "quinuclidine": "C1(CC2)CCN2CC1",
            "epoxide": "C1CO1",
            "pyrazine": "C1=CN=CC=N1",
            "oxazolidinone": "O=C1OCCN1",
            "tetrahydronaphthalene":"C1(C=CC=C2)=C2CCCC1",
            "adamantane": "C1(CC(C2)C3)CC2CC3C1",
            "1,8-naphthyridin-4(1H)-one":"O=C(C=CN1)C2=C1N=CC=C2",
            "3,7-dihydro-1H-purine-2,6-dione": "O=C(C(NC=N1)=C1N2)NC2=O",
            "hexadecahydro-1H-cyclopenta[a]phenanthrene": "CCC[C@H]1CCCCC1[C@@H]2C[C@H](CCC3)C3CC2",
            "7,8,9,10-tetrahydrotetracene-5,12-dione": "O=C(C(C=C(CCCC1)C1=C2)=C2C3=O)C4=C3C=CC=C4",
            "cyclobutane": "C1CCC1",
            "1,2-dihydro-3H-1,2,4-triazol-3-one": "O=C1NNC=N1",
            "1,3,4-thiadiazole": "C1=NN=CS1",
            "azepane": "C1NCCCCC1",
            "8-azabicyclo[3.2.1]octane": "C12CCCC(CC2)N1",
            "piperidine-2,6-dione":"O=C(N1)CCCC1=O",
            "2,3-dihydro-1H-indene":"O=C(N1)CCCC1=O",
            "benzo[d]isoxazole":"C12=CC=CC=C1C=NO2",
            "1,9-dihydro-6H-purin-6-one":"O=C1C2=C(NC=N2)N=CN1",
            "9H-fluorene":"C12=CC=CC=C1C3=C(C=CC=C3)C2",
            "10,11-dihydro-5H-dibenzo[b,f]azepine":"C12=CC=CC=C1CCC3=C(C=CC=C3)N2",
            "(6aR,10aR)-4,6,6a,7,8,9,10,10a-octahydroindolo[4,3-fg]quinoline":"C12=CC=CC3=C1C(C[C@@H]4[C@@H]2CCCN4)=CN3",
            "1H-pyrrole": "C1=CC=CN1",
            "1,3-dioxolane":"O1CCOC1",
            "(1R,5S)-3-azabicyclo[3.1.0]hexane": "[C@@H]1(C2)[C@H]2CNC1",
            "cyclopentanone": "O=C1CCCC1",
            "pyrrolidine-2,5-dione":"O=C(N1)CCC1=O",
            "pyrazolidine":"O=C(NN1)CC1=O",
            "(R)-1-azabicyclo[3.2.0]hept-2-en-7-one":"O=C1N2C=CC[C@@H]2C1",
            "thiazolidine-2,4-dione":"O=C(CS1)NC1=O",
            "benzofuran":"C12=CC=CC=C1C=CO2",
            "1H-indazole":"C12=CC=CC=C1C=NN2",
            "indolin-2-one":"O=C1NC2=CC=CC=C2C1",
            "benzo[b]thiophene":"C12=CC=CC=C1C=CS2",
            "(R)-1,2,3,7,8,8a-hexahydronaphthalene":"C12=CCCC[C@@H]1CCC=C2",
            "4,5,6,7-tetrahydrothieno[3,2-c]pyridine":"C1(C=CS2)=C2CCNC1",
            "4H-chromen-4-one":"O=C(C=CO1)C2=C1C=CC=C2",
            "3,4-dihydroquino-2(1H)-one":"O=C(CC1)NC2=C1C=CC=C2",
            "napthalene-1,4-dione": "O=C(C=CC1=O)C2=C1C=CC=C2",
            "2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide":"O=S(C1=C2C=CC=C1)(NC=N2)=O",
            "4H-benzo[f][1,2,4]triazolo[4,3-a][1,4]diazepine":"C1(N2C(CN=C3)=NN=C2)=C3C=CC=C1",
            "9H-thioxanthene":"C12=CC=CC=C1CC3=C(C=CC=C3)S2",
            "(5aR,8aR)-5,8,8a,9-tetrahydrofuro[3',4':6,7]naphtho[2,3-d][1,3]dioxol-6(5aH)-one":"O=C(OC1)[C@H]2[C@H]1CC3=CC4=C(C=C3C2)OCO4",
            "(3a1S,5aS,10bS)-3a,3a1,4,5,5a,6,11,12-octahydro-1H-indolizino[8,1-cd]carbazole":"C12=CC=CC=C1[C@@]34[C@H](CCC5[C@@H]3N(CC=C5)CC4)N2",
            "(4aR,5aR)-4a,5a,6,12a-tetrahydrotetracene-1,11(4H,5H)-dione":"O=C1C2=CC3[C@H](CC=CC3=O)C[C@@H]2CC4=CC=CC=C41",
            "1H-1,2,3-triazole": "N1=NC=CN1",
            "azetidin-2-one":"O=C1NCC1",
            "oxetan-2-one":"O=C1OCC1"
        }

        rings_in_drugs_smarts = {
            'benzene':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridine':'[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'piperidine':'[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'piperazine':'[#7]1-[#6]-[#6]-[#7]-[#6]-[#6]-1',
            'cyclohexane':'[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'oxane':'[#8]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'imidazole':'[#6]1:[#7]:[#6]:[#6]:[#7H]:1',
            'pyrrolidine':'[#6]1-[#6]-[#6]-[#7]-[#6]-1',
            '(R)-5-thia-1-azabicyclo[4.2.0]oct-2-en-8-one':'[#8]=[#6]1-[#6]-[#6@@H]2-[#7]-1-[#6]=[#6]-[#6]-[#16]-2',
            'cyclopropane':'[#6]1-[#6]-[#6]-1',
            'tetrahydrofuran':'[#6]1-[#6]-[#6]-[#8]-[#6]-1',
            'thiazole':'[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'indole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'diazine':'[#6]1:[#7]:[#6]:[#6]:[#6]:[#7]:1',
            '(R)-4-thia-1-azabicyclo[3.2.0]heptan-7-one':'[#8]=[#6]1-[#7]2-[#6]-[#6]-[#16]-[#6@@H]-2-[#6]-1',
            '6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]=[#6]-[#6](-[#6]2-[#6]-[#6@@H]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'tetrazole':'[#7]1=[#7]-[#7]=[#6]-[#7]-1',
            'cyclopentane':'[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'thiophenyl':'[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'naphthalene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '1H-benzo[d]imidazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#7H]:2',
            'quinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#7]:2',
            '1H-purine':'[#6]12:[#6]:[#7H]:[#6]:[#7]:[#6]-1:[#7]:[#6]:[#7]:2',
            '1,2,6,7,8,9,10,11,12,13,14,15,16,17-tetradecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]-[#6]-[#6](-[#6@@H]2-[#6]-[#6@@H]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'furan':'[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            '1H-1,2,4-Triazole':'[#7]1:[#6]:[#7]:[#6]:[#7H]:1',
            '10H-Phenothiazine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#7]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#16]-2',
            'quinazoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#6]:[#7]:2',
            'morpholine':'[#6]1-[#6]-[#7]-[#6]-[#6]-[#8]-1',
            'pyrimidin-2(1H)-one':'[#8]=[#6]1:[#7]:[#6]:[#6]:[#6]:[#7H]:1',
            'quinolin-4(1H)-one':'[#8]=[#6]1:[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2):[#7H]:[#6]:[#6]:1',
            '(9S,14R)-6,7,8,9,10,11,12,13,14,15,16,17-dodecahydro-3H-cyclopenta[a]phenanthren-3-one':'[#8]=[#6]1-[#6]=[#6]-[#6](-[#6@H]2-[#6]-[#6]-[#6]3-[#6@@H](-[#6]-[#6]-[#6]-3)-[#6]-2)-[#6](-[#6]-[#6]-[#6])=[#6]-1',
            'isoxazole':'[#6]1:[#6]:[#6]:[#7]:[#8]:1',
            'imidazoline':'[#6]1=[#7]-[#6]-[#6]-[#7]-1',
            '1,4-dihydropyridine':'[#6]1=[#6]-[#6]-[#6]=[#6]-[#7]-1',
            'pyrimidine-2,4(1H,3H)-dione':'[#8]=[#6]1:[#7H]:[#6](:[#6]:[#6]:[#7H]:1)=[#8]',
            '3,4-dihydro-2H-benzo[e][1,4]diazepin-2-one':'[#8]=[#6]1-[#7]=[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2=[#6]-[#7]-[#6]-1',
            'cyclohexene':'[#6]1=[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'pyrrolidin-2-one':'[#8]=[#6]1-[#7]-[#6]-[#6]-[#6]-1',
            'imidazolidine-2,4-dione':'[#8]=[#6]1-[#6]-[#7]-[#6](-[#7]-1)=[#8]',
            '1,2,3,4-tetrahydroisoquinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#7]-[#6]-2',
            '3,4-dihydro-2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide':'[#8]=[#16]1(-[#7]-[#6]-[#7]-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2)=[#8]',
            '7,8,9,11,12,13,14,15,16,17-decahydro-6H-cyclopenta[a]phenanthrene':'[#6]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6@@H]1-[#6]-[#6@@H]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-[#6]-1',
            '1H-pyrazole':'[#7]1:[#6]:[#6]:[#6]:[#7H]:1',
            'quinuclidine':'[#6]12-[#6]-[#6]-[#7](-[#6]-[#6]-1)-[#6]-[#6]-2',
            'epoxide':'[#6]1-[#6]-[#8]-1',
            'pyrazine':'[#6]1:[#6]:[#7]:[#6]:[#6]:[#7]:1',
            'oxazolidinone':'[#8]=[#6]1-[#8]-[#6]-[#6]-[#7]-1',
            'tetrahydronaphthalene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]-[#6]-2',
            'adamantane':'[#6]12-[#6]-[#6]3-[#6]-[#6](-[#6]-1)-[#6]-[#6](-[#6]-3)-[#6]-2',
            '1,8-naphthyridin-4(1H)-one':'[#8]=[#6]1:[#6]:[#6]:[#7H]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#7]:2',
            '3,7-dihydro-1H-purine-2,6-dione':'[#8]=[#6]1:[#6]2:[#7H]:[#6]:[#7]:[#6]:2:[#7H]:[#6](:[#7H]:1)=[#8]',
            'hexadecahydro-1H-cyclopenta[a]phenanthrene':'[#6]-[#6]-[#6]-[#6@H]1-[#6]-[#6]-[#6]-[#6]-[#6]-1-[#6@@H]1-[#6]-[#6@@H]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-[#6]-1',
            '7,8,9,10-tetrahydrotetracene-5,12-dione':'[#8]=[#6]1-[#6]2:[#6]:[#6]3-[#6]-[#6]-[#6]-[#6]-[#6]:3:[#6]:[#6]:2-[#6](=[#8])-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2',
            'cyclobutane':'[#6]1-[#6]-[#6]-[#6]-1',
            '1,2-dihydro-3H-1,2,4-triazol-3-one':'[#8]=[#6]1:[#7H]:[#7H]:[#6]:[#7]:1',
            '1,3,4-thiadiazole':'[#6]1:[#7]:[#7]:[#6]:[#16]:1',
            'azepane':'[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            '8-azabicyclo[3.2.1]octane':'[#6]12-[#6]-[#6]-[#6]-[#6](-[#6]-[#6]-1)-[#7]-2',
            'piperidine-2,6-dione':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-[#6]-1)=[#8]',
            '2,3-dihydro-1H-indene':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-[#6]-1)=[#8]',
            'benzo[d]isoxazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#8]:2',
            '1,9-dihydro-6H-purin-6-one':'[#8]=[#6]1:[#6]2:[#6](:[#7H]:[#6]:[#7]:2):[#7]:[#6]:[#7H]:1',
            '9H-fluorene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#6]-2',
            '10,11-dihydro-5H-dibenzo[b,f]azepine':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#7]-2',
            '(6aR,10aR)-4,6,6a,7,8,9,10,10a-octahydroindolo[4,3-fg]quinoline':'[#6]12:[#6]:[#6]:[#6]:[#6]3:[#6]:1:[#6](-[#6]-[#6@@H]1-[#6@@H]-2-[#6]-[#6]-[#6]-[#7]-1):[#6]:[#7H]:3',
            '1H-pyrrole':'[#6]1:[#6]:[#6]:[#6]:[#7H]:1',
            '1,3-dioxolane':'[#8]1-[#6]-[#6]-[#8]-[#6]-1',
            '(1R,5S)-3-azabicyclo[3.1.0]hexane':'[#6]1-[#6@@H]2-[#6@H]-1-[#6]-[#7]-[#6]-2',
            'cyclopentanone':'[#8]=[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'pyrrolidine-2,5-dione':'[#8]=[#6]1-[#7]-[#6](-[#6]-[#6]-1)=[#8]',
            'pyrazolidine':'[#8]=[#6]1-[#7]-[#7]-[#6](-[#6]-1)=[#8]',
            '(R)-1-azabicyclo[3.2.0]hept-2-en-7-one':'[#8]=[#6]1-[#7]2-[#6]=[#6]-[#6]-[#6@@H]-2-[#6]-1',
            'thiazolidine-2,4-dione':'[#8]=[#6]1-[#6]-[#16]-[#6](-[#7]-1)=[#8]',
            'benzofuran':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#8]:2',
            '1H-indazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#7H]:2',
            'indolin-2-one':'[#8]=[#6]1-[#7]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1',
            'benzo[b]thiophene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#16]:2',
            '(R)-1,2,3,7,8,8a-hexahydronaphthalene':'[#6]12=[#6]-[#6]-[#6]-[#6]-[#6@@H]-1-[#6]-[#6]-[#6]=[#6]-2',
            '4,5,6,7-tetrahydrothieno[3,2-c]pyridine':'[#6]12:[#6]:[#6]:[#16]:[#6]:1-[#6]-[#6]-[#7]-[#6]-2',
            '4H-chromen-4-one':'[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '3,4-dihydroquino-2(1H)-one':'[#8]=[#6]1-[#6]-[#6]-[#6]2:[#6](-[#7]-1):[#6]:[#6]:[#6]:[#6]:2',
            'napthalene-1,4-dione':'[#8]=[#6]1-[#6]=[#6]-[#6](=[#8])-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2',
            '2H-benzo[e][1,2,4]thiadiazine 1,1-dioxide':'[#8]=[#16]1(-[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2)-[#7]=[#6]-[#7]-1)=[#8]',
            '4H-benzo[f][1,2,4]triazolo[4,3-a][1,4]diazepine':'[#6]12-[#7]3:[#6](-[#6]-[#7]=[#6]-[#6]:1:[#6]:[#6]:[#6]:[#6]:2):[#7]:[#7]:[#6]:3',
            '9H-thioxanthene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]1:[#6](:[#6]:[#6]:[#6]:[#6]:1)-[#16]-2',
            "(5aR,8aR)-5,8,8a,9-tetrahydrofuro[3',4':6,7]naphtho[2,3-d][1,3]dioxol-6(5aH)-one":'[#8]=[#6]1-[#8]-[#6]-[#6@H]2-[#6@H]-1-[#6]-[#6]1:[#6](-[#6]-2):[#6]:[#6]2:[#6](:[#6]:1)-[#8]-[#6]-[#8]-2',
            '(3a1S,5aS,10bS)-3a,3a1,4,5,5a,6,11,12-octahydro-1H-indolizino[8,1-cd]carbazole':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6@@]13-[#6@H](-[#6]-[#6]-[#6]4-[#6@@H]-1-[#7](-[#6]-[#6]=[#6]-4)-[#6]-[#6]-3)-[#7]-2',
            '(4aR,5aR)-4a,5a,6,12a-tetrahydrotetracene-1,11(4H,5H)-dione':'[#8]=[#6]1-[#6]2=[#6]-[#6]3-[#6@H](-[#6]-[#6]=[#6]-[#6]-3=[#8])-[#6]-[#6@@H]-2-[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-1',
            '1H-1,2,3-triazole':'[#7]1:[#7]:[#6]:[#6]:[#7H]:1',
            'azetidin-2-one':'[#8]=[#6]1-[#7]-[#6]-[#6]-1',
            'oxetan-2-one':'[#8]=[#6]1-[#8]-[#6]-[#6]-1',
        }

        return rings_in_drugs_smiles, rings_in_drugs_smarts

    def _get_common_heterocyclic_rings_phase_2():

        rings_smiles = {
            'pyridine': 'C1=CC=NC=C1',
            'indole': 'C12=CC=CC=C1C=CN2',
            'imidazole': 'C1=CN=CN1',
            'thiazol-2-amine': 'NC1=NC=CS1',
            'tetrazole': 'C1=NN=NN1',
            '1,2,4-triazole': 'C1=NC=NN1',
            'thiophene': 'C1=CC=CS1',
            'cytosine': 'O=C1N=C(N)C=CN1',
            'adenine': 'NC1=NC=NC2=C1N=CN2',
            '5-methylindole': 'CC1=CC=C2C(C=CN2)=C1',
            'isocaffeine': 'O=C(N1C)NC2=C(N=CN2)C1=O',
            'tetrazolethiol': 'SN1N=NN=C1',
            '3-methylisoxazole': 'C1=CC=NO1',
            '1-methylimidazole': 'CN1C=NC=C1',
            '2-methylimidazole': 'CC1=NC=CN1',
            'guanine': 'NC(N1)=NC2=C(N=CN2)C1=O',
            'quinoline': 'C12=CC=CC=C1N=CC=C2',
            'furan': 'C1=CC=CO1',
            'tosufloxacin': 'NC1=C(F)C=C2C(NC=C(C(O)=O)C2=O)=N1'
        }

        rings_smarts = {
            'pyridine': '[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            'indole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'imidazole': '[#6]1:[#6]:[#7]:[#6]:[#7H]:1',
            'thiazol-2-amine': '[#7]-[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'tetrazole': '[#6]1:[#7]:[#7]:[#7]:[#7H]:1',
            '1,2,4-triazole': '[#6]1:[#7]:[#6]:[#7]:[#7H]:1',
            'thiophene': '[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'cytosine': '[#8]=[#6]1:[#7]:[#6](-[#7]):[#6]:[#6]:[#7H]:1',
            'adenine': '[#7]-[#6]1:[#7]:[#6]:[#7]:[#6]2:[#6]:1:[#7]:[#6]:[#7H]:2',
            '5-methylindole': '[#6]-[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:[#6]:[#7H]:2):[#6]:1',
            'isocaffeine': '[#8]=[#6]1:[#7](-[#6]):[#6](:[#6]2:[#6](:[#7H]:1):[#7H]:[#6]:[#7]:2)=[#8]',
            'tetrazolethiol': '[#16]-[#7]1:[#7]:[#7]:[#7]:[#6]:1',
            '3-methylisoxazole': '[#6]1:[#6]:[#6]:[#7]:[#8]:1',
            '1-methylimidazole': '[#6]-[#7]1:[#6]:[#7]:[#6]:[#6]:1',
            '2-methylimidazole': '[#6]-[#6]1:[#7]:[#6]:[#6]:[#7H]:1',
            'guanine': '[#7]-[#6]1:[#7H]:[#6](:[#6]2:[#6](:[#7]:1):[#7H]:[#6]:[#7]:2)=[#8]',
            'quinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#6]:[#6]:2',
            'furan': '[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'tosufloxacin': '[#7]-[#6]1:[#6](-[#9]):[#6]:[#6]2:[#6](:[#7H]:[#6]:[#6](-[#6](-[#8])=[#8]):[#6]:2=[#8]):[#7]:1',
        }

        return rings_smiles, rings_smarts

    def _get_common_privileged_scaffolds():

        privileged_functional_groups_smiles = {
            'indole': 'C12=CC=CC=C1C=CN2',
            'quinoline': 'C12=CC=CC=C1N=CC=C2',
            'isoquinoline': 'C12=C(C=NC=C2)C=CC=C1',
            'purine': 'C12=NC=NC=C1NC=N2',
            'quinoxaline': 'C12=CC=CC=C1N=CC=N2',
            'quinazolinone': 'O=C1NC2=C(C=CC=C2)C=N1',
            'tetrahydroisoquinoline': 'C12=C(CNCC2)C=CC=C1',
            'tetrahydraquinoline': 'C12=C(NCCC2)C=CC=C1',
            'benzoxazole': 'C12=CC=CC=C1OC=N2',
            'benzofuran': 'C12=CC=CC=C1C=CO2',
            '3,3-dimethylbenzopyran': 'CC1(C)C=CC2=CC=CC=C2O1',
            'chromone': 'O=C1C=COC2=C1C=CC=C2',
            'coumarin': 'O=C1OC2=C(C=CC=C2)C=C1',
            'carbohydrate': 'OCC1OC(O)C(O)C(O)C1O',
            'steroid': 'C12CCCCC1C3C(C(CCC4)C4CC3)CC2',
            'prostanoic acid': 'CCCCCCCC[C@@H]1[C@H](CCC1)CCCCCCC(O)=O',
            'benzodiazepine': 'O=C1CN=C(C2=CC=CC=C2)C3=C(C=CC=C3)N1',
            'arylpiperidine': 'C1(C2CCNCC2)=CC=CC=C1',
            'arylpiperizine': 'C1(N2CCNCC2)=CC=CC=C1',
            'benzylpiperidine': 'N1(CC2=CC=CC=C2)CCCCC1',
            'benzothiophene': 'C12=CC=CC=C1C=CS2',
            'dihydropyridine': 'C1CC=CC=N1',
            'benzimidazole': 'C12=CC=CC=C1NC=N2',
            'biphenyltetrazole': 'C1(C2=C(C3=CC=CC=C3)C=CC=C2)=NN=NN1',
            '3,3-hydroxy-2-oxindole': 'OC(C1=CC=CC=C1N2)C2=O',
            '5,7,5-lactone': 'C=C1C2CCCC3C(CC3)C2OC1=O',
            '6,6-spiroacetal': 'C1CCCC2(CCCCO2)O1',
            'dihydropyrimidone': 'O=C1NCC=CN1',
            'indolizine': 'N12C=CC=C1C=CC=C2',
            'biphenyl': 'C1(C2=CC=CC=C2)=CC=CC=C1',
            'triazaspirodecanone': 'O=C(NC1)C2(CCNCC2)N1C3=CC=CC=C3',
            'N-acylhydrazone': '[H]C(/N=N/CC)=O',
            'pyrrolinone': 'O=C1C=CNC1',
            'hydroxyamate': 'ONC(CCC(C)=O)=O',
            'trans-lactam': 'O=C1NC2CCCC2C1',
            'trans-lactone': 'O=C1OC2CCCC2C1',
            'hexahydroisoindole': 'C12CNCC1CCCC2',
            'benzimidazolone': 'O=C1N(C2CCNCC2)C3=CC=CC=C3N1',
            'indoline': 'C12=C(NCC2)C=CC=C1',
            '2-arylbenzothiazole': 'C12=CC=CC=C1N=C(C3=CC=CC=C3)S2',
            'imidazolequinoxaline': 'C1(NC2)=CC=CC=C1N3C2=CN=C3',
            'spiroindanylpiperidine': 'C12=CC=CC=C1C3(CCNCC3)CC2',
            'aminopyridazine': 'NC1=NN=CC=C1',
            '1,4-pyrazolodiazepin-8-one': 'O=C1NCCNC2=CNN=C21',
            'rhodanine': 'S=C(N1)SCC1=O',
            'pyranopyridone': 'O=C1C2=C(OCC=C2)C=CN1',
            'pyranoquinolone': 'O=C1C=CC2=CC=CC=C2N1'
        }

        privileged_functional_groups_smarts = {
            'indole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'quinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#6]:[#6]:2',
            'isoquinoline': '[#6]12:[#6](:[#6]:[#7]:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:2',
            'purine': '[#6]12:[#7]:[#6]:[#7]:[#6]:[#6]:1:[#7H]:[#6]:[#7]:2',
            'quinoxaline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#6]:[#7]:2',
            'quinazolinone': '[#8]=[#6]1:[#7H]:[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#7]:1',
            'tetrahydroisoquinoline': '[#6]12:[#6](-[#6]-[#7]-[#6]-[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            'tetrahydraquinoline': '[#6]12:[#6](-[#7]-[#6]-[#6]-[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            'benzoxazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#8]:[#6]:[#7]:2',
            'benzofuran': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#8]:2',
            '3,3-dimethylbenzopyran': '[#6]-[#6]1(-[#6])-[#6]=[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#8]-1',
            'chromone': '[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]2:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'coumarin': '[#8]=[#6]1:[#8]:[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:1',
            'carbohydrate': '[#8]-[#6]-[#6]1-[#8]-[#6](-[#8])-[#6](-[#8])-[#6](-[#8])-[#6]-1-[#8]',
            'steroid': '[#6]12-[#6]-[#6]-[#6]-[#6]-[#6]-1-[#6]1-[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-3-[#6]-[#6]-1)-[#6]-[#6]-2',
            'prostanoic acid': '[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6@@H]1-[#6@H](-[#6]-[#6]-[#6]-1)-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#8])=[#8]',
            'benzodiazepine': '[#8]=[#6]1-[#6]-[#7]=[#6](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2)-[#6]2:[#6](:[#6]:[#6]:[#6]:[#6]:2)-[#7]-1',
            'arylpiperidine': '[#6]1(-[#6]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'arylpiperizine': '[#6]1(-[#7]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzylpiperidine': '[#7]1(-[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2)-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'benzothiophene': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#16]:2',
            'dihydropyridine': '[#6]1-[#6]-[#6]=[#6]-[#6]=[#7]-1',
            'benzimidazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7H]:[#6]:[#7]:2',
            'biphenyltetrazole': '[#6]1(-[#6]2:[#6](-[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3):[#6]:[#6]:[#6]:[#6]:2):[#7]:[#7]:[#7]:[#7H]:1',
            '3,3-hydroxy-2-oxindole': '[#8]-[#6]1-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#7]-[#6]-1=[#8]',
            '5,7,5-lactone': '[#6]=[#6]1-[#6]2-[#6]-[#6]-[#6]-[#6]3-[#6](-[#6]-[#6]-3)-[#6]-2-[#8]-[#6]-1=[#8]',
            '6,6-spiroacetal': '[#6]1-[#6]-[#6]-[#6]-[#6]2(-[#6]-[#6]-[#6]-[#6]-[#8]-2)-[#8]-1',
            'dihydropyrimidone': '[#8]=[#6]1-[#7]-[#6]-[#6]=[#6]-[#7]-1',
            'indolizine': '[#7]12:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'biphenyl': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'triazaspirodecanone': '[#8]=[#6]1-[#7]-[#6]-[#7](-[#6]-12-[#6]-[#6]-[#7]-[#6]-[#6]-2)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'N-acylhydrazone': '[#6H](/[#7]=[#7]/[#6]-[#6])=[#8]',
            'pyrrolinone': '[#8]=[#6]1-[#6]=[#6]-[#7]-[#6]-1',
            'hydroxyamate': '[#8]-[#7]-[#6](-[#6]-[#6]-[#6](-[#6])=[#8])=[#8]',
            'trans-lactam': '[#8]=[#6]1-[#7]-[#6]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-1',
            'trans-lactone': '[#8]=[#6]1-[#8]-[#6]2-[#6]-[#6]-[#6]-[#6]-2-[#6]-1',
            'hexahydroisoindole': '[#6]12-[#6]-[#7]-[#6]-[#6]-1-[#6]-[#6]-[#6]-[#6]-2',
            'benzimidazolone': '[#8]=[#6]1:[#7](-[#6]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7H]:1',
            'indoline': '[#6]12:[#6](-[#7]-[#6]-[#6]-1):[#6]:[#6]:[#6]:[#6]:2',
            '2-arylbenzothiazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1):[#16]:2',
            'imidazolequinoxaline': '[#6]12-[#7]-[#6]-[#6]3:[#7](-[#6]:1:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#7]:[#6]:3',
            'spiroindanylpiperidine': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]1(-[#6]-[#6]-[#7]-[#6]-[#6]-1)-[#6]-[#6]-2',
            'aminopyridazine': '[#7]-[#6]1:[#7]:[#7]:[#6]:[#6]:[#6]:1',
            '1,4-pyrazolodiazepin-8-one': '[#8]=[#6]1-[#7]-[#6]-[#6]-[#7]-[#6]2:[#6]:[#7H]:[#7]:[#6]:2-1',
            'rhodanine': '[#16]=[#6]1-[#7]-[#6](-[#6]-[#16]-1)=[#8]',
            'pyranopyridone': '[#8]=[#6]1:[#6]2:[#6](-[#8]-[#6]-[#6]=[#6]-2):[#6]:[#6]:[#7H]:1',
            'pyranoquinolone': '[#8]=[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7H]:1',
        }

        return privileged_functional_groups_smiles, privileged_functional_groups_smarts

    def _get_major_warhead_functional_groups():

        functional_groups_smiles = {
            'propiolamide': 'C#CC(N)=O',
            'fumarate ester': 'NC(/C=C/CC(OC)=O)=O',
            'allenamide': 'NC(C=C=C)=O',
            'propiolonitrile': 'C#CC#N',
            'propargylamide': 'C#CCC(N)=O',
            'arylsulfonyl bicyclobutane': 'O=S(C12CC1C2)(C3=CC=CC=C3)=O',
            'haloalkane': 'CBr',
            'alpha-halomethyl': 'CC(CCl)=O',
            'alpha-haloamide': 'NC(CCl)=O',
            'alpha-haloester': 'O=C(CCl)OC',
            'epoxide': 'C1CO1',
            'aziridine': 'N1CC1',
            'nitroalkane': 'CC[N+]([O-])=O',
            'acrylamide': 'C=CC(N)=O',
            'cyanoenone': 'O=C(C)C(C#N)=C',
            'aldehyde': 'O=C(C)[H]',
            'ketone': 'O=C(C)C',
            'nitrile': 'N#CC',
            'cyanamide': 'NC#N',
            'isothicyanate': '[N-]=C=S',
            'sulfone': 'CS=O',
            'sulfonyl fluoride': 'O=S(F)=O',
            'sulfonimidoyl fluoride': 'N=S(F)(F)=O',
            'aryl fluorosulfate': 'O=S(OCCCCC)(F)=O',
            'ester': 'CC(OC)=O',
            'sulfonamide': 'O=S(N)=O',
            '2-carbonyl arylboronic acid': 'O=C(C1=CC=CC=C1B(O)O)C',
            'n-methyl isoxazolium': 'C[N+]1=CC=CO1',
            'oxaziridine': 'O1NC1',
        }

        functional_groups_smarts = {
            'propiolamide': '[#6]#[#6]-[#6](-[#7])=[#8]',
            'fumarate ester': '[#7]-[#6](/[#6]=[#6]/[#6]-[#6](-[#8]-[#6])=[#8])=[#8]',
            'allenamide': '[#7]-[#6](-[#6]=[#6]=[#6])=[#8]',
            'propiolonitrile': '[#6]#[#6]-[#6]#[#7]',
            'propargylamide': '[#6]#[#6]-[#6]-[#6](-[#7])=[#8]',
            'arylsulfonyl bicyclobutane': '[#8]=[#16](-[#6]12-[#6]-[#6]-1-[#6]-2)(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'haloalkane': '[#6]-[#35]',
            'alpha-halomethyl': '[#6]-[#6](-[#6]-[#17])=[#8]',
            'alpha-haloamide': '[#7]-[#6](-[#6]-[#17])=[#8]',
            'alpha-haloester': '[#8]=[#6](-[#6]-[#17])-[#8]-[#6]',
            'epoxide': '[#6]1-[#6]-[#8]-1',
            'aziridine': '[#7]1-[#6]-[#6]-1',
            'nitroalkane': '[#6]-[#6]-[#7+](-[#8-])=[#8]',
            'acrylamide': '[#6]=[#6]-[#6](-[#7])=[#8]',
            'cyanoenone': '[#8]=[#6](-[#6])-[#6](-[#6]#[#7])=[#6]',
            'aldehyde': '[#8]=[#6H]-[#6]',
            'ketone': '[#8]=[#6](-[#6])-[#6]',
            'nitrile': '[#7]#[#6]-[#6]',
            'cyanamide': '[#7]-[#6]#[#7]',
            'isothicyanate': '[#7-]=[#6]=[#16]',
            'sulfone': '[#6]-[#16]=[#8]',
            'sulfonyl fluoride': '[#8]=[#16](-[#9])=[#8]',
            'sulfonimidoyl fluoride': '[#7]=[#16](-[#9])(-[#9])=[#8]',
            'aryl fluorosulfate': '[#8]=[#16](-[#8]-[#6]-[#6]-[#6]-[#6]-[#6])(-[#9])=[#8]',
            'ester': '[#6]-[#6](-[#8]-[#6])=[#8]',
            'sulfonamide': '[#8]=[#16](-[#7])=[#8]',
            '2-carbonyl arylboronic acid': '[#8]=[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#5](-[#8])-[#8])-[#6]',
            'n-methyl isoxazolium': '[#6]-[#7+]1:[#6]:[#6]:[#6]:[#8]:1',
            'oxaziridine': '[#8]1-[#7]-[#6]-1',
        }

        return functional_groups_smiles, functional_groups_smarts

    def _get_common_polymer_repeating_units():

        functional_group_smiles = {
            '3′-bromo-2-chloro[1,1′:4′,1′′-terphenyl]-4,4′′': 'ClC1=CC=CC=C1C2=CC=C(C3=CC=CC=C3)C(Br)=C2',
            '[3,3′-biquinoline]-6,6′': 'C1(C2=CC3=CC=CC=C3N=C2)=CC4=CC=CC=C4N=C1',
            '[2,3′-bipyridine]-4,5′': 'C1(C2=CC=CN=C2)=NC=CC=C1',
            '(Z)-but-1-enel': 'C=CCC',
            'threo-(E)-3-(methoxycarbonyl)-4-methylbut-1-ene-1,4-diyl': '',
            'ethene-1,2-diyl': 'C=C',
            'propane-1,3-diyl': 'CCC',
            'methylmethylene': '[CH]C',
            '1-phenylethylene': 'C=CC1=CC=CC=C1',
            '1,2-dioxobutane': 'CCC(C=O)=O',
            '1,3-dioxohexane': 'CCCC(CC=O)=O',
            'oxyoxalyl': 'O=CC(O)=O',
            'oxysuccinyl': 'O=CCCC(O)=O',
            'naphthalene': 'C12=CC=CC=C1C=CC=C2',
            '2H-furo[3,2-b]pyran': 'C12=CCOC1=CC=CO2',
            'pyridine': 'C1=NC=CC=C1',
            '1-carboxylatoethylene': 'NC1(C(O)=O)CC1',
            'x-iminocyclopentane': 'N=C1CCCC1',
            'pyridine-3,5-diylpiperidine': 'N1(C2=CC3=CN=C2)C3CCCC1',
            '(4-chloro[3,3′-bipyridine])methylene': '[CH]C1=NC=CC(Cl)=C1C2=CC=CN=C2',
            'imino[1-oxo-2-(phenylsulfanyl)ethylene]': 'O=C=C(N)SC1=CC=CC=C1',
            'methylphenylsiloxane': '[H]O[SiH](C)C1=CC=CC=C1',
            'diethoxyphosphazene': 'CCO[PH2](N)OCC',
            'piperidine-3,5-diylideneethanediylidene': 'C/C=C1CNCCC1',
            'sulfanediylcarbonyl': 'O=[CH]S',
            'spiro[4.5]decane-2,8-diylmethylene': 'C1(CC(CC2)CC3)CC32CC1',
            '4H-1,2,4-triazole-3,5-diylmethylene': 'C1(C2)=NN=C2N1',
            '(2-phenyl-1,3-phenylene)ethylene': 'C1(C=C2)=CC=CC2=C1C3=CC=CC=C3',
            '(5′-chloro[1,2′-binaphthalene])methylene': 'CC1=CC=C2C=CC=CC2=C1C3=CC=C4C(Cl)=CC=CC4=C3',
            '(6-chlorocyclohex-1-ene)(1-bromoethylene)': 'ClC1C=CC(C(Br)C)CC1',
            'oxy{[3-(trifluoromethyl)phenyl]methylene}': 'FC(C1=CC([CH]O)=CC=C1)(F)F',
            '1,3-phenyleneethylene': 'C1(C=C2)=CC=CC2=C1',
            '(tetramethoxy-1,4-phenylene)(1,2-diphenylethene)': 'COC(C(OC)=CC(OC)=C1OC)=C1/C(C2=CC=CC=C2)=C/C3=CC=CC=C3',
            '(1,1′,3,3′-tetraoxo[5,5′-biisoindoline]-2,2′-diyl)biphenyl': 'O=C(C1=C2C=CC(C3=CC=C4C(OCN(C5=CC=C(C6=CC=CC=C6)C=C5)CO4)=C3)=C1)NC2=O',
            'morpholine-2,6-diylpyridine-3,5-diylthianthrene': 'C(C=C1S2)(C3=CN=CC(C4CNCCO4)=C3)=CC=C1SC5=C2C=CC=C5',
            'naphthalene-1,4-phenylenecyclohexane': 'C12=CC=CC=C1C=C(C3=CC=CC(C4CCCCC4)=C3)C=C2',
            'pyridine-1,4-phenylenecyclopentane': 'C1(C2=CC=CC(C3CCCC3)=C2)=CC=CN=C1',
            'pyridine-4H-1,2,4-triazole-3,5-diylmethylene': 'CC(N1)=NN=C1C2=NC=CC=C2',
            'oxyspiro[3.5]nona-2,5-diene-7,1-diylcyclohex-4-ene-1,3-diyl': 'OC1C=CC2(CCC2C3CC=CCC3)CC1',
            'piperidine-oxymethylene': 'COC1NCCCC1',
            'pyridine-methyleneoxy-1,4-phenylene': 'C1(OCC2=NC=CC=C2)=CC=CC=C1',
            'imino(1-chloro-2-oxoethylene)(4-nitro-1,3-phenylene)(3-bromopropane)': 'NC(C(C1=CC=C([N+]([O-])=O)C(CCBr)=C1)=O)Cl',
            'pyridine-acenaphthylene-3,8-diylpyrrole-diylacenaphthylene': 'C1(C2=C(C=C3)C(C3=C(C4=CNC=C4C5=C(C=C6)C(C6=CC=C7)=C7C=C5)C=C8)=C8C=C2)=CC=CN=C1',
            'pyridine-(phenylmethylene)iminocyclohexane': 'C1(C(NC2CCCCC2)C3=CC=CC=C3)=CC=CC=N1',
            '(methylimino)methyleneimino-1,3-phenylene': 'CNCNC1=CC=CC=C1',
            'pyridine-diyliminocyclohexane(phenylmethylene)': 'C1(NC2CCC(CC3=CC=CC=C3)CC2)=CC=CC=N1',
            'imino(1-oxoethylene)silanediylpropane': 'NC(C[Si](C)(C)C)=O',
            'pyridine-cyclohexane-oxypropane': 'CCCOC(CCC1)CC1C2=CC=CN=C2',
            'sulfaneethylenesulfanediyl(2-amino-4-carboxypentane)': 'SCCSC(N)CC(C)C(O)=O',
            'sulfaneethylenesulfanediyl(4-amino-1-carboxypentane)': 'SCCSC(C(O)=O)CC(N)C',
            'pyridine-methylenepyridine(tetrahydropyran)': 'C1(CC2=CN=CC(C3COCCC3)=C2)=CC=CN=C1',
            'sulfane(2-chloropropane)sulfanepropane': 'SCC(CSCCC)Cl',
            'pyridine-carbonyloxymethylene': 'O=C(OC)C1=CC=CN=C1',
            '1,3-phenylene(1-bromoethylene)cyclohexane(2-butylethylene)': 'BrC(C1CCCC(C(CCC)C)C1)C2=CC=CC=C2',
            'oxy(1,1-dichloroethylene)imino(1-oxoethylene)': 'OC(Cl)(CNCOC)Cl',
            'sulfane(1-chloroethylene)-1,3-phenylene(1-chloroethylene)': 'SC(CC1=CC(C(C)Cl)=CC=C1)Cl',
            'sulfane(1-iodoethylene)sulfane(5-bromo-3-chloropentane)': 'SC(CSCCC(CCBr)Cl)I',
            'oxymethylene-ONN-azoxy(chloromethylene)': 'OCN(O)-NCCl',
            '(3-chlorobiphenyl)methylene(3-chloro-1,4-phenylene)methylene': 'ClC1=CC(C2=CC=C(C3=CC=C(C)C(Cl)=C3)C=C2)=CC=C1',
            'imino(x-methyl-1,3-phenylene)iminomalonyl': 'NC1=CC(C)=CC(NC(CC=O)=O)=C1',
            'oxyhexane-oxycarbonylimino(methylphenylene)iminocarbonyl': 'OCCCCCCOC(NC1=CC(C)=C(NC=O)C=C1)=O',
            '2,4,8,10-tetraoxaspiro[5.5]undecane-oxyhexane-1,6-diyloxy': 'CC1OCC2(COC(OCCCCCCO)OC2)CO1',
            'pyridine-methylenepyrrole-oxymethylene': 'COC1=CNC=C1CC2=CC=CN=C2',
            'oxymethyleneiminocarbonylsulfane-1,3-phenyleneethylene': 'COCNC(SC1=CC=CC(CC)=C1)=O',
            'oxyiminomethylenehydrazine-methylene': 'ONCNNC',
            'piperidine-methylenepiperidine-4,2-diylcyclopentane-ethylenecyclopentane-1,2-diylmethylene': 'CC(C1)CCC1CC(C2)CCC2C(C3)NCCC3CC4NCCCC4',
            '1,3-dioxa-8-thia-5,10-diazadodecane': 'OCOCNCCSCNCC',
            'oxymethyleneoxymethyleneoxymethyleneimino-1,3-phenylenemethyleneiminomethylene': 'OCOCOCNC1=CC(CNC)=CC=C1',
            'pyridine-1,4-phenylenemethyleneoxymethyleneiminomethyleneoxy-1,4-phenylenemethylene': 'CC(C=C1)=CC=C1OCNCOCC(C=C2)=CC=C2C3=CC=CN=C3',
            'sulfinylmethylenesulfanediylpropane-1,3-diylsulfonyl-1,4-phenylene': 'SOCSCCCS(=O)(C1=CC=CC=C1)=O',
            'oxyterephthaloylhydrazine-terephthaloyl': 'OC(C1=CC=C(C(NNC(C2=CC=C(C=O)C=C2)=O)=O)C=C1)=O',
            'nitrilo-1,4-phenylenenitriloprop-2-en-3-yl-1-ylidene-1,4-phenyleneprop-1-en-1-yl-3-ylidene': 'NC1=CC=C(N=CC=CC2=CC=C(C=CCC)C=C2)C=C1',
            'oxycarbonylnitrilopropane-idenenitrilocarbonyl': 'OC(N=CCC=NC=O)=O',
            'oxyethyleneiminomethylenesulfanediylethyleneiminocyclohexane': 'OCCCNCSCCNC1CCCCC1',
            'iminomethyleneiminocarbonyl{2-[(2,4-dinitrophenyl)hydrazono]cyclopentane}carbonyl': 'OC(C1=CC=C(C(OCCCCCC)=O)C=C1)=O',
            'oxyterephthaloyloxyhexane': 'NCCNC(C1/C(C(C=O)CC1)=N/NC2=C([N+]([O-])=O)C=C([N+]([O-])=O)C=C2)=O',
            'nitrilocyclohexa-2,5-diene-idenenitrilo-1,4-phenyleneimino-1,4-phenyleneimino1,4-phenylene': 'N=C1C=CC(C=C1)=NC2=CC=C(NC3=CC=C(NC4=CC=CC=C4)C=C3)C=C2',
            'cyclohexane-methanylylidenecyclohexane-idenemethanylylidenecyclohexane-methylene': 'CC(CC1)CCC1C=C(CC2)CCC2=CC3CCCCC3'
        }

        functional_group_smarts = {
            '3′-bromo-2-chloro[1,1′:4′,1′′-terphenyl]-4,4′′': '[#17]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]1:[#6]:[#6]:[#6](-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6](-[#35]):[#6]:1',
            '[3,3′-biquinoline]-6,6′': '[#6]1(-[#6]2:[#6]:[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3:[#7]:[#6]:2):[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7]:[#6]:1',
            '[2,3′-bipyridine]-4,5′': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#7]:[#6]:2):[#7]:[#6]:[#6]:[#6]:[#6]:1',
            '(Z)-but-1-enel': '[#6]=[#6]-[#6]-[#6]',
            'threo-(E)-3-(methoxycarbonyl)-4-methylbut-1-ene-1,4-diyl': '',
            'ethene-1,2-diyl': '[#6]=[#6]',
            'propane-1,3-diyl': '[#6]-[#6]-[#6]',
            'methylmethylene': '[#6H]-[#6]',
            '1-phenylethylene': '[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1,2-dioxobutane': '[#6]-[#6]-[#6](-[#6]=[#8])=[#8]',
            '1,3-dioxohexane': '[#6]-[#6]-[#6]-[#6](-[#6]-[#6]=[#8])=[#8]',
            'oxyoxalyl': '[#8]=[#6]-[#6](-[#8])=[#8]',
            'oxysuccinyl': '[#8]=[#6]-[#6]-[#6]-[#6](-[#8])=[#8]',
            'naphthalene': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '2H-furo[3,2-b]pyran': '[#6]12=[#6]-[#6]-[#8]-[#6]-1=[#6]-[#6]=[#6]-[#8]-2',
            'pyridine': '[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1',
            '1-carboxylatoethylene': '[#7]-[#6]1(-[#6](-[#8])=[#8])-[#6]-[#6]-1',
            'x-iminocyclopentane': '[#7]=[#6]1-[#6]-[#6]-[#6]-[#6]-1',
            'pyridine-3,5-diylpiperidine': '[#7]12-[#6]3:[#6]:[#6](:[#6]:[#7]:[#6]:3)-[#6]-1-[#6]-[#6]-[#6]-[#6]-2',
            '(4-chloro[3,3′-bipyridine])methylene': '[#6H]-[#6]1:[#7]:[#6]:[#6]:[#6](-[#17]):[#6]:1-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'imino[1-oxo-2-(phenylsulfanyl)ethylene]': '[#8]=[#6]=[#6](-[#7])-[#16]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'methylphenylsiloxane': '[#8H]-[SiH](-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'diethoxyphosphazene': '[#6]-[#6]-[#8]-[#15H2](-[#7])-[#8]-[#6]-[#6]',
            'piperidine-3,5-diylideneethanediylidene': '[#6]-[#6]=[#6]1-[#6]-[#7]-[#6]-[#6]-[#6]-1',
            'sulfanediylcarbonyl': '[#8]=[#6H]-[#16]',
            'spiro[4.5]decane-2,8-diylmethylene': '[#6]12-[#6]-[#6]3-[#6]-[#6]-[#6](-[#6]-[#6]-3)(-[#6]-1)-[#6]-[#6]-2',
            '4H-1,2,4-triazole-3,5-diylmethylene': '[#6]12-[#6]-[#6](:[#7]:[#7]:1):[#7H]:2',
            '(2-phenyl-1,3-phenylene)ethylene': '[#6]12-[#6]=[#6]-[#6](:[#6]:[#6]:[#6]:1):[#6]:2-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '(5′-chloro[1,2′-binaphthalene])methylene': '[#6]-[#6]1:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:1-[#6]1:[#6]:[#6]:[#6]2:[#6](-[#17]):[#6]:[#6]:[#6]:[#6]:2:[#6]:1',
            '(6-chlorocyclohex-1-ene)(1-bromoethylene)': '[#17]-[#6]1-[#6]=[#6]-[#6](-[#6](-[#35])-[#6])-[#6]-[#6]-1',
            'oxy{[3-(trifluoromethyl)phenyl]methylene}': '[#9]-[#6](-[#6]1:[#6]:[#6](-[#6H]-[#8]):[#6]:[#6]:[#6]:1)(-[#9])-[#9]',
            '1,3-phenyleneethylene': '[#6]12-[#6]=[#6]-[#6](:[#6]:[#6]:[#6]:1):[#6]:2',
            '(tetramethoxy-1,4-phenylene)(1,2-diphenylethene)': '[#6]-[#8]-[#6]1:[#6](-[#8]-[#6]):[#6]:[#6](-[#8]-[#6]):[#6](-[#8]-[#6]):[#6]:1/[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#6]/[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '(1,1′,3,3′-tetraoxo[5,5′-biisoindoline]-2,2′-diyl)biphenyl': '[#8]=[#6]1-[#6]2:[#6](:[#6]:[#6]:[#6](-[#6]3:[#6]:[#6]:[#6]4:[#6](-[#8]-[#6]-[#7](-[#6]5:[#6]:[#6]:[#6](-[#6]6:[#6]:[#6]:[#6]:[#6]:[#6]:6):[#6]:[#6]:5)-[#6]-[#8]-4):[#6]:3):[#6]:2)-[#6](-[#7]-1)=[#8]',
            'morpholine-2,6-diylpyridine-3,5-diylthianthrene': '[#6]1(:[#6]:[#6]2-[#16]-[#6]3:[#6](-[#16]-[#6]:2:[#6]:[#6]:1):[#6]:[#6]:[#6]:[#6]:3)-[#6]1:[#6]:[#7]:[#6]:[#6](-[#6]2-[#6]-[#7]-[#6]-[#6]-[#8]-2):[#6]:1',
            'naphthalene-1,4-phenylenecyclohexane': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6](-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-[#6]-3):[#6]:1):[#6]:[#6]:2',
            'pyridine-1,4-phenylenecyclopentane': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6](-[#6]3-[#6]-[#6]-[#6]-[#6]-3):[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridine-4H-1,2,4-triazole-3,5-diylmethylene': '[#6]-[#6]1:[#7H]:[#6](:[#7]:[#7]:1)-[#6]1:[#7]:[#6]:[#6]:[#6]:[#6]:1',
            'oxyspiro[3.5]nona-2,5-diene-7,1-diylcyclohex-4-ene-1,3-diyl': '[#8]-[#6]1-[#6]=[#6]-[#6]2(-[#6]-[#6]-[#6]-2-[#6]2-[#6]-[#6]=[#6]-[#6]-[#6]-2)-[#6]-[#6]-1',
            'piperidine-oxymethylene': '[#6]-[#8]-[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-1',
            'pyridine-methyleneoxy-1,4-phenylene': '[#6]1(-[#8]-[#6]-[#6]2:[#7]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'imino(1-chloro-2-oxoethylene)(4-nitro-1,3-phenylene)(3-bromopropane)': '[#7]-[#6](-[#6](-[#6]1:[#6]:[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6](-[#6]-[#6]-[#35]):[#6]:1)=[#8])-[#17]',
            'pyridine-acenaphthylene-3,8-diylpyrrole-diylacenaphthylene': '[#6]1(-[#6]2:[#6]3-[#6]=[#6]-[#6]4:[#6]:3:[#6](:[#6]:[#6]:[#6]:4-[#6]3:[#6]:[#7H]:[#6]:[#6]:3-[#6]3:[#6]4-[#6]=[#6]-[#6]5:[#6]:4:[#6](:[#6]:[#6]:[#6]:5):[#6]:[#6]:3):[#6]:[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'pyridine-(phenylmethylene)iminocyclohexane': '[#6]1(-[#6](-[#7]-[#6]2-[#6]-[#6]-[#6]-[#6]-[#6]-2)-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#7]:1',
            '(methylimino)methyleneimino-1,3-phenylene': '[#6]-[#7]-[#6]-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pyridine-diyliminocyclohexane(phenylmethylene)': '[#6]1(-[#7]-[#6]2-[#6]-[#6]-[#6](-[#6]-[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3)-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'imino(1-oxoethylene)silanediylpropane': '[#7]-[#6](-[#6]-[Si](-[#6])(-[#6])-[#6])=[#8]',
            'pyridine-cyclohexane-oxypropane': '[#6]-[#6]-[#6]-[#8]-[#6]1-[#6]-[#6]-[#6]-[#6](-[#6]-1)-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfaneethylenesulfanediyl(2-amino-4-carboxypentane)': '[#16]-[#6]-[#6]-[#16]-[#6](-[#7])-[#6]-[#6](-[#6])-[#6](-[#8])=[#8]',
            'sulfaneethylenesulfanediyl(4-amino-1-carboxypentane)': '[#16]-[#6]-[#6]-[#16]-[#6](-[#6](-[#8])=[#8])-[#6]-[#6](-[#7])-[#6]',
            'pyridine-methylenepyridine(tetrahydropyran)': '[#6]1(-[#6]-[#6]2:[#6]:[#7]:[#6]:[#6](-[#6]3-[#6]-[#8]-[#6]-[#6]-[#6]-3):[#6]:2):[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfane(2-chloropropane)sulfanepropane': '[#16]-[#6]-[#6](-[#6]-[#16]-[#6]-[#6]-[#6])-[#17]',
            'pyridine-carbonyloxymethylene': '[#8]=[#6](-[#8]-[#6])-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            '1,3-phenylene(1-bromoethylene)cyclohexane(2-butylethylene)': '[#35]-[#6](-[#6]1-[#6]-[#6]-[#6]-[#6](-[#6](-[#6]-[#6]-[#6])-[#6])-[#6]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'oxy(1,1-dichloroethylene)imino(1-oxoethylene)': '[#8]-[#6](-[#17])(-[#6]-[#7]-[#6]-[#8]-[#6])-[#17]',
            'sulfane(1-chloroethylene)-1,3-phenylene(1-chloroethylene)': '[#16]-[#6](-[#6]-[#6]1:[#6]:[#6](-[#6](-[#6])-[#17]):[#6]:[#6]:[#6]:1)-[#17]',
            'sulfane(1-iodoethylene)sulfane(5-bromo-3-chloropentane)': '[#16]-[#6](-[#6]-[#16]-[#6]-[#6]-[#6](-[#6]-[#6]-[#35])-[#17])-[#53]',
            'oxymethylene-ONN-azoxy(chloromethylene)': '[#8]-[#6]-[#7](-[#8])-[#7]-[#6]-[#17]',
            '(3-chlorobiphenyl)methylene(3-chloro-1,4-phenylene)methylene': '[#17]-[#6]1:[#6]:[#6](-[#6]2:[#6]:[#6]:[#6](-[#6]3:[#6]:[#6]:[#6](-[#6]):[#6](-[#17]):[#6]:3):[#6]:[#6]:2):[#6]:[#6]:[#6]:1',
            'imino(x-methyl-1,3-phenylene)iminomalonyl': '[#7]-[#6]1:[#6]:[#6](-[#6]):[#6]:[#6](-[#7]-[#6](-[#6]-[#6]=[#8])=[#8]):[#6]:1',
            'oxyhexane-oxycarbonylimino(methylphenylene)iminocarbonyl': '[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#8]-[#6](-[#7]-[#6]1:[#6]:[#6](-[#6]):[#6](-[#7]-[#6]=[#8]):[#6]:[#6]:1)=[#8]',
            '2,4,8,10-tetraoxaspiro[5.5]undecane-oxyhexane-1,6-diyloxy': '[#6]-[#6]1-[#8]-[#6]-[#6]2(-[#6]-[#8]-[#6](-[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#8])-[#8]-[#6]-2)-[#6]-[#8]-1',
            'pyridine-methylenepyrrole-oxymethylene': '[#6]-[#8]-[#6]1:[#6]:[#7H]:[#6]:[#6]:1-[#6]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'oxymethyleneiminocarbonylsulfane-1,3-phenyleneethylene': '[#6]-[#8]-[#6]-[#7]-[#6](-[#16]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]-[#6]):[#6]:1)=[#8]',
            'oxyiminomethylenehydrazine-methylene': '[#8]-[#7]-[#6]-[#7]-[#7]-[#6]',
            'piperidine-methylenepiperidine-4,2-diylcyclopentane-ethylenecyclopentane-1,2-diylmethylene': '[#6]-[#6]1-[#6]-[#6](-[#6]-[#6]-1)-[#6]-[#6]1-[#6]-[#6](-[#6]-[#6]-1)-[#6]1-[#6]-[#6](-[#6]-[#6]-[#7]-1)-[#6]-[#6]1-[#7]-[#6]-[#6]-[#6]-[#6]-1',
            '1,3-dioxa-8-thia-5,10-diazadodecane': '[#8]-[#6]-[#8]-[#6]-[#7]-[#6]-[#6]-[#16]-[#6]-[#7]-[#6]-[#6]',
            'oxymethyleneoxymethyleneoxymethyleneimino-1,3-phenylenemethyleneiminomethylene': '[#8]-[#6]-[#8]-[#6]-[#8]-[#6]-[#7]-[#6]1:[#6]:[#6](-[#6]-[#7]-[#6]):[#6]:[#6]:[#6]:1',
            'pyridine-1,4-phenylenemethyleneoxymethyleneiminomethyleneoxy-1,4-phenylenemethylene': '[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#8]-[#6]-[#7]-[#6]-[#8]-[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#7]:[#6]:1',
            'sulfinylmethylenesulfanediylpropane-1,3-diylsulfonyl-1,4-phenylene': '[#16]-[#8]-[#6]-[#16]-[#6]-[#6]-[#6]-[#16](=[#8])(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'oxyterephthaloylhydrazine-terephthaloyl': '[#8]-[#6](-[#6]1:[#6]:[#6]:[#6](-[#6](-[#7]-[#7]-[#6](-[#6]2:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:2)=[#8])=[#8]):[#6]:[#6]:1)=[#8]',
            'nitrilo-1,4-phenylenenitriloprop-2-en-3-yl-1-ylidene-1,4-phenyleneprop-1-en-1-yl-3-ylidene': '[#7]-[#6]1:[#6]:[#6]:[#6](-[#7]=[#6]-[#6]=[#6]-[#6]2:[#6]:[#6]:[#6](-[#6]=[#6]-[#6]-[#6]):[#6]:[#6]:2):[#6]:[#6]:1',
            'oxycarbonylnitrilopropane-idenenitrilocarbonyl': '[#8]-[#6](-[#7]=[#6]-[#6]-[#6]=[#7]-[#6]=[#8])=[#8]',
            'oxyethyleneiminomethylenesulfanediylethyleneiminocyclohexane': '[#8]-[#6]-[#6]-[#6]-[#7]-[#6]-[#16]-[#6]-[#6]-[#7]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'iminomethyleneiminocarbonyl{2-[(2,4-dinitrophenyl)hydrazono]cyclopentane}carbonyl': '[#8]-[#6](-[#6]1:[#6]:[#6]:[#6](-[#6](-[#8]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6])=[#8]):[#6]:[#6]:1)=[#8]',
            'oxyterephthaloyloxyhexane': '[#7]-[#6]-[#6]-[#7]-[#6](-[#6]1/[#6](-[#6](-[#6]=[#8])-[#6]-[#6]-1)=[#7]/[#7]-[#6]1:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6]:1)=[#8]',
            'nitrilocyclohexa-2,5-diene-idenenitrilo-1,4-phenyleneimino-1,4-phenyleneimino1,4-phenylene': '[#7]=[#6]1-[#6]=[#6]-[#6](-[#6]=[#6]-1)=[#7]-[#6]1:[#6]:[#6]:[#6](-[#7]-[#6]2:[#6]:[#6]:[#6](-[#7]-[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3):[#6]:[#6]:2):[#6]:[#6]:1',
            'cyclohexane-methanylylidenecyclohexane-idenemethanylylidenecyclohexane-methylene': '[#6]-[#6]1-[#6]-[#6]-[#6](-[#6]-[#6]-1)-[#6]=[#6]1-[#6]-[#6]-[#6](-[#6]-[#6]-1)=[#6]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',

        }

        return functional_group_smiles, functional_group_smarts

    def _get_common_electrophilic_warheads_for_kinases():

        electrophilic_warheads_smiles = {
            'methylacrylamide': 'CNC(C=C)=O',
            'methyl acrylate': 'COC(C=C)=O',
            'methyl propiolate' :'COC(C#C)=O',
            '2-cyanoacrylamide': 'N#CC(C(N)=O)=C',
            'n-methylmaleimide' :'CN1C(C=CC1=O)=O',
            'n-ethylmaleimide' :'O=C(C=CC1=O)N1CC',
            'crotonamide': 'C/C=C/C(N)=O',
            'ethyl crotonate': 'C/C=C/C(OCC)=O',
            'crotononitrile' :'C/C=C/C#N',
            'methyl methylpropiolate': 'CC#CC(OC)=O',
            'isothiocyanatomethane': 'CN=C=S',
            'isothiocyanatoethane': 'CCN=C=S',
            'prop-1-ene': 'CC=C',
            'prop-1-yne': 'CC#C',
            'acetonitrile': 'CC#N',
            'tert-butyl (Z)-2-ethylidenehydrazine-1-carboxylate' : 'C/C=N/\/NC(OC(C)(C)C)=O',
            'n-methylchloroacetamide': 'CNC(CCl)=O',
            'n-methyl-2-chloropropanamide': 'CNC(C(C)Cl)=O',
            'n-methyl-2-bromopropanamide': 'CNC(C(C)Br)=O',
            'bromoacetone': 'CC(CBr)=O',
            '2-methyloxirane': 'CC1OC1',
            'fluoromethane': 'CF',
            'methylsulfane': 'CS',
            'aldehyde': 'CC=O'
        }

        electrophilic_warheads_smarts = {
            'methylacrylamide': '[#6]-[#7]-[#6](-[#6]=[#6])=[#8]',
            'methyl acrylate': '[#6]-[#8]-[#6](-[#6]=[#6])=[#8]',
            'methyl propiolate': '[#6]-[#8]-[#6](-[#6]#[#6])=[#8]',
            '2-cyanoacrylamide': '[#7]#[#6]-[#6](-[#6](-[#7])=[#8])=[#6]',
            'n-methylmaleimide': '[#6]-[#7]1-[#6](-[#6]=[#6]-[#6]-1=[#8])=[#8]',
            'n-ethylmaleimide': '[#8]=[#6]1-[#6]=[#6]-[#6](=[#8])-[#7]-1-[#6]-[#6]',
            'crotonamide': '[#6]/[#6]=[#6]/[#6](-[#7])=[#8]',
            'ethyl crotonate': '[#6]/[#6]=[#6]/[#6](-[#8]-[#6]-[#6])=[#8]',
            'crotononitrile': '[#6]/[#6]=[#6]/[#6]#[#7]',
            'methyl methylpropiolate': '[#6]-[#6]#[#6]-[#6](-[#8]-[#6])=[#8]',
            'isothiocyanatomethane': '[#6]-[#7]=[#6]=[#16]',
            'isothiocyanatoethane': '[#6]-[#6]-[#7]=[#6]=[#16]',
            'prop-1-ene': '[#6]-[#6]=[#6]',
            'prop-1-yne': '[#6]-[#6]#[#6]',
            'acetonitrile': '[#6]-[#6]#[#7]',
            'tert-butyl (Z)-2-ethylidenehydrazine-1-carboxylate': '[#6]/[#6]=[#7]\[#7]-[#6](-[#8]-[#6](-[#6])(-[#6])-[#6])=[#8]',
            'n-methylchloroacetamide': '[#6]-[#7]-[#6](-[#6]-[#17])=[#8]',
            'n-methyl-2-chloropropanamide': '[#6]-[#7]-[#6](-[#6](-[#6])-[#17])=[#8]',
            'n-methyl-2-bromopropanamide': '[#6]-[#7]-[#6](-[#6](-[#6])-[#35])=[#8]',
            'bromoacetone': '[#6]-[#6](-[#6]-[#35])=[#8]',
            '2-methyloxirane': '[#6]-[#6]1-[#8]-[#6]-1',
            'fluoromethane': '[#6]-[#9]',
            'methylsulfane': '[#6]-[#16]',
            'aldehyde': '[#6]-[#6]=[#8]',
        }

        return electrophilic_warheads_smiles, electrophilic_warheads_smarts

    def _get_privileged_scaffolds_for_kinase_inhibitors():

        kinase_inhibitor_smiles = {
            'indole': 'C12=CC=CC=C1C=CN2',
            'quinoline': 'C12=CC=CC=C1C=CC=N2',
            'phenylpiperazine': 'C1(N2CCNCC2)=CC=CC=C1',
            'biphenyl': 'C1(C2=CC=CC=C2)=CC=CC=C1',
            'benzimidazole': 'C12=CC=CC=C1NC=N2',
            'quinazoline': 'C12=CC=CC=C1C=NC=N2',
            'purine': 'C12=NC=NC=C1NC=N2',
            'indoline': 'C12=CC=CC=C1CCN2',
            'isoquinoline': 'C12=CC=CC=C1C=NC=C2',
            'benzylpiperidine': 'N1(CC2=CC=CC=C2)CCCCC1',
            'aminopyridazine': 'NC1=CC=CN=N1',
            '4-phenylpiperidine': 'C1(C2CCNCC2)=CC=CC=C1',
            'chromone': 'O=C1C=COC2=CC=CC=C21',
            '4-hydroxyquinazoline': 'O=C1NC=NC2=CC=CC=C21',
            'benzothiophene': 'C12=CC=CC=C1SC=C2',
            'benzofuran': 'C12=CC=CC=C1OC=C2',
            'quinoxaline': 'C12=CC=CC=C1N=CC=N2',
            'benzo[d]oxazole': 'C12=CC=CC=C1OC=N2',
            '1,2,3,4-tetrahydroisoquinoline': 'C12=CC=CC=C1CCNC2',
            'thiazolidine-2,4-dione': 'O=C(N1)SCC1=O',
            '1,2,3,4-tetrahydroquinoline': 'C12=CC=CC=C1CCCN2',
            '2H-chromen-2-one': 'O=C1OC2=CC=CC=C2C=C1',
            '1-(piperidin-4-yl)-1,3-dihydro-2H-benzo[d]imidazol-2-one': 'O=C1N(C2CCNCC2)C3=CC=CC=C3N1',
            '5H-dibenzo[b,e][1,4]diazepine': 'C1(C=CC=C2)=C2NC(C=CC=C3)=C3C=N1',
            '3,4-dihydropyrimidin-2(1H)-one': 'O=C1NC=CCN1',
            '3,4-dihydropyrimidine-2(1H)-thione': 'S=C1NC=CCN1',
            '6-(hydroxymethyl)tetrahydro-2H-pyran-2,3,4,5-tetraol': 'OCC1OC(O)C(O)C(O)C1O',
            '1-phenyl-1,3,8-triazaspiro[4.5]decan-4-one': 'O=C(NC1)C2(CCNCC2)N1C3=CC=CC=C3',
            '1,4-dihydropyridine': 'C1=CNC=CC1',
            '2-(tetrazol-5-yl)biphenyl': 'C1(C2=CC=CC=C2C3=NN=NN3)=CC=CC=C1'
        }

        kinase_inhibitor_smarts = {
            'indole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'quinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#7]:2',
            'phenylpiperazine': '[#6]1(-[#7]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'biphenyl': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzimidazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7H]:[#6]:[#7]:2',
            'quinazoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#6]:[#7]:2',
            'purine': '[#6]12:[#7]:[#6]:[#7]:[#6]:[#6]:1:[#7H]:[#6]:[#7]:2',
            'indoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#7]-2',
            'isoquinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#6]:[#6]:2',
            'benzylpiperidine': '[#7]1(-[#6]-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2)-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'aminopyridazine': '[#7]-[#6]1:[#6]:[#6]:[#6]:[#7]:[#7]:1',
            '4-phenylpiperidine': '[#6]1(-[#6]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'chromone': '[#8]=[#6]1:[#6]:[#6]:[#8]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2',
            '4-hydroxyquinazoline': '[#8]=[#6]1:[#7H]:[#6]:[#7]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2',
            'benzothiophene': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#16]:[#6]:[#6]:2',
            'benzofuran': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#8]:[#6]:[#6]:2',
            'quinoxaline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#6]:[#7]:2',
            'benzo[d]oxazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#8]:[#6]:[#7]:2',
            '1,2,3,4-tetrahydroisoquinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#7]-[#6]-2',
            'thiazolidine-2,4-dione': '[#8]=[#6]1-[#7]-[#6](-[#6]-[#16]-1)=[#8]',
            '1,2,3,4-tetrahydroquinoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]-[#7]-2',
            '2H-chromen-2-one': '[#8]=[#6]1:[#8]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6]:[#6]:1',
            '1-(piperidin-4-yl)-1,3-dihydro-2H-benzo[d]imidazol-2-one': '[#8]=[#6]1:[#7](-[#6]2-[#6]-[#6]-[#7]-[#6]-[#6]-2):[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#7H]:1',
            '5H-dibenzo[b,e][1,4]diazepine': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]=[#7]-2',
            '3,4-dihydropyrimidin-2(1H)-one': '[#8]=[#6]1-[#7]-[#6]=[#6]-[#6]-[#7]-1',
            '3,4-dihydropyrimidine-2(1H)-thione': '[#16]=[#6]1-[#7]-[#6]=[#6]-[#6]-[#7]-1',
            '6-(hydroxymethyl)tetrahydro-2H-pyran-2,3,4,5-tetraol': '[#8]-[#6]-[#6]1-[#8]-[#6](-[#8])-[#6](-[#8])-[#6](-[#8])-[#6]-1-[#8]',
            '1-phenyl-1,3,8-triazaspiro[4.5]decan-4-one': '[#8]=[#6]1-[#7]-[#6]-[#7](-[#6]-12-[#6]-[#6]-[#7]-[#6]-[#6]-2)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1,4-dihydropyridine': '[#6]1=[#6]-[#7]-[#6]=[#6]-[#6]-1',
            '2-(tetrazol-5-yl)biphenyl': '[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]2:[#7]:[#7]:[#7]:[#7H]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
        }

        return kinase_inhibitor_smiles, kinase_inhibitor_smarts

    def _get_braf_kinase_inhibitors_for_cancer():

        ribose_subpocket_smiles = {
            'imidazole': 'C1=CN=CN1',
            'pyrazole-1-ethanol': 'OCCN1N=CC=C1',
            'acetonitrile': 'C#N',
            '2-(tert-butyl)thiazole': 'CC(C)(C)C1=NC=CS1',
            'pyridine': 'C1=CC=NC=C1',
            '1-isopropyl-pyrazole': 'CC(C)N1N=CC=C1',
            'isoindoline' :'C12=CC=CC=C1CNC2',
            'pyrrolopyridine': 'C12=CC=CN=C1C=CN2',
        }

        ribose_subpocket_smarts = {
            'imidazole': '[#6]1:[#6]:[#7]:[#6]:[#7H]:1',
            'pyrazole-1-ethanol': '[#8]-[#6]-[#6]-[#7]1:[#7]:[#6]:[#6]:[#6]:1',
            'acetonitrile': '[#6]#[#7]',
            '2-(tert-butyl)thiazole': '[#6]-[#6](-[#6])(-[#6])-[#6]1:[#7]:[#6]:[#6]:[#16]:1',
            'pyridine': '[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '1-isopropyl-pyrazole': '[#6]-[#6](-[#6])-[#7]1:[#7]:[#6]:[#6]:[#6]:1',
            'isoindoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#7]-[#6]-2',
            'pyrrolopyridine': '[#6]12:[#6]:[#6]:[#6]:[#7]:[#6]:1:[#6]:[#6]:[#7H]:2',
        }

        adenine_subpocket_smiles = {
            'pyridine': 'C1=CC=NC=C1',
            '1H-pyrrolo[2,3-b]pyridine': 'C12=NC=CC=C1C=CN2',
            'pyrimidine': 'C1=CN=CN=C1',
            '3,4-dihydroquinazoline': 'C12=CC=CC=C1CNC=N2',
            '1,3,8-Triazanaphthalene': 'C12=NC=CC=C1C=NC=N2',
            'benzothiazole': 'C1(SC=N2)=C2C=CC=C1',
            '3,4-dihydropyrido[2,3-b]pyrazine':'C12=NC=CC=C1N=CCN2',
            'morpholine': 'C1COCCN1',
            '2-aminopyrimidine': 'NC1=NC=CC=N1',
            'benzoimidazole': 'C12=CC=CC=C1N=CN2',
            'pyridinyl imidazole': 'C1(C2=NC=CN2)=CC=CC=N1',
            'quinazoline': 'C12=NC=NC=C1C=CC=C2',
        }

        adenine_subpocket_smarts = {
            'pyridine': '[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '1H-pyrrolo[2,3-b]pyridine': '[#6]12:[#7]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#7H]:2',
            'pyrimidine': '[#6]1:[#6]:[#7]:[#6]:[#7]:[#6]:1',
            '3,4-dihydroquinazoline': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#7]-[#6]=[#7]-2',
            '1,3,8-Triazanaphthalene': '[#6]12:[#7]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#7]:[#6]:[#7]:2',
            'benzothiazole': '[#6]12:[#16]:[#6]:[#7]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            '3,4-dihydropyrido[2,3-b]pyrazine': '[#6]12:[#7]:[#6]:[#6]:[#6]:[#6]:1-[#7]=[#6]-[#6]-[#7]-2',
            'morpholine': '[#6]1-[#6]-[#8]-[#6]-[#6]-[#7]-1',
            '2-aminopyrimidine': '[#7]-[#6]1:[#7]:[#6]:[#6]:[#6]:[#7]:1',
            'benzoimidazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#7]:[#6]:[#7H]:2',
            'pyridinyl imidazole': '[#6]1(-[#6]2:[#7]:[#6]:[#6]:[#7H]:2):[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'quinazoline': '[#6]12:[#7]:[#6]:[#7]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
        }

        hydrophobic_subpocket_smiles = {
            'benzene': 'C1=CC=CC=C1',
            '1-methyleneindan': 'C=C1CCC2=C1C=CC=C2',
            'toluene': 'CC1=CC=CC=C1',
            'fluorobenzene': 'FC1=CC=CC=C1',
            'methyl(phenyl)sulfane': 'CSC1=CC=CC=C1',
            '2-methylpyridine': 'CC1=CC=CC=N1',
            '1a,6b-dihydro-1H-cyclopropa[b]benzofuran': 'C12=CC=CC=C1OC3C2C3',
            '1,2,3,4-tetrahydronaphthalene': 'C12=CC=CC=C1CCCC2',
            '1,3-difluorobenzene': 'FC1=CC(F)=CC=C1',
            '1-chloro-4-fluorobenzene': 'FC1=CC=C(Cl)C=C1',
            'benzoimidazole': 'C12=CC=CC=C1[N]C=N2',
        }

        hydrophobic_subpocket_smarts = {
            'benzene': '[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '1-methyleneindan': '[#6]=[#6]1-[#6]-[#6]-[#6]2:[#6]-1:[#6]:[#6]:[#6]:[#6]:2',
            'toluene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'fluorobenzene': '[#9]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'methyl(phenyl)sulfane': '[#6]-[#16]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '2-methylpyridine': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            '1a,6b-dihydro-1H-cyclopropa[b]benzofuran': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#8]-[#6]1-[#6]-2-[#6]-1',
            '1,2,3,4-tetrahydronaphthalene': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-[#6]-[#6]-[#6]-2',
            '1,3-difluorobenzene': '[#9]-[#6]1:[#6]:[#6](-[#9]):[#6]:[#6]:[#6]:1',
            '1-chloro-4-fluorobenzene': '[#9]-[#6]1:[#6]:[#6]:[#6](-[#17]):[#6]:[#6]:1',
            'benzoimidazole': '[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#7]-[#6]=[#7]-2',
        }

        type_1_subpocket_smiles = {
            'sulfonylpropane': 'O=S(CCC)=O',
            'methanesulfonamide': 'O=S(C)(N)=O',
            '1,3-difluoro-2-sulfonylbenzene' : 'O=S(C1=C(F)C=CC=C1F)=O',
            'N-ethyl-N-methylsulfonic amide': 'O=S(N(CC)C)=O',
            'propanesulfonamide': 'O=S(CCC)(N)=O',
            '1-hydrosulfonylpyrrolidine': 'O=S(N1CCCC1)=O',
        }

        type_1_subpocket_smarts = {
            'sulfonylpropane': '[#8]=[#16](-[#6]-[#6]-[#6])=[#8]',
            'methanesulfonamide': '[#8]=[#16](-[#6])(-[#7])=[#8]',
            '1,3-difluoro-2-sulfonylbenzene': '[#8]=[#16](-[#6]1:[#6](-[#9]):[#6]:[#6]:[#6]:[#6]:1-[#9])=[#8]',
            'N-ethyl-N-methylsulfonic amide': '[#8]=[#16](-[#7](-[#6]-[#6])-[#6])=[#8]',
            'propanesulfonamide': '[#8]=[#16](-[#6]-[#6]-[#6])(-[#7])=[#8]',
            '1-hydrosulfonylpyrrolidine': '[#8]=[#16](-[#7]1-[#6]-[#6]-[#6]-[#6]-1)=[#8]',
        }

        type_2_subpocket_smiles = {
            'toluene': 'CC1=CC=CC=C1',
            'prop-2-yn-1-ylbenzene': 'C#CCC1=CC=CC=C1',
            'neohexane': 'CCC(C)(C)C',
            '(trifluoromethyl)benzene': 'FC(F)(F)C1=CC=CC=C1',
            '3-chloro-4-(trifluoromethyl)pyridine': 'ClC1=CN=CC=C1C(F)(F)F',
            '1-phenyl-1H-pyrazole': 'C1(N2N=CC=C2)=CC=CC=C1',
            '4-(trifluoromethyl)pyridine': 'FC(F)(F)C1=CC=NC=C1',
            '2-phenylpropan-2-amine': 'CC(C)(N)C1=CC=CC=C1',
            '6-methyl-1H-benzoimidazole': 'CC1=CC=C(N=CN2)C2=C1',
            '5-(1,1,1-trifluoro-2-methylpropan-2-yl)isoxazole': 'CC(C(F)(F)F)(C)C1=CC=NO1',
        }

        type_2_subpocket_smarts = {
            'toluene': '[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'prop-2-yn-1-ylbenzene': '[#6]#[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'neohexane': '[#6]-[#6]-[#6](-[#6])(-[#6])-[#6]',
            '(trifluoromethyl)benzene': '[#9]-[#6](-[#9])(-[#9])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '3-chloro-4-(trifluoromethyl)pyridine': '[#17]-[#6]1:[#6]:[#7]:[#6]:[#6]:[#6]:1-[#6](-[#9])(-[#9])-[#9]',
            '1-phenyl-1H-pyrazole': '[#6]1(-[#7]2:[#7]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '4-(trifluoromethyl)pyridine': '[#9]-[#6](-[#9])(-[#9])-[#6]1:[#6]:[#6]:[#7]:[#6]:[#6]:1',
            '2-phenylpropan-2-amine': '[#6]-[#6](-[#6])(-[#7])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            '6-methyl-1H-benzoimidazole': '[#6]-[#6]1:[#6]:[#6]:[#6]2:[#7]:[#6]:[#7H]:[#6]:2:[#6]:1',
            '5-(1,1,1-trifluoro-2-methylpropan-2-yl)isoxazole': '[#6]-[#6](-[#6](-[#9])(-[#9])-[#9])(-[#6])-[#6]1:[#6]:[#6]:[#7]:[#8]:1',
        }

        exposed_to_solvent_smiles = {
            'N,N-dimethyl-2-phenoxyethan-1-amine': 'CN(C)CCOC1=CC=CC=C1',
            'cyclopropanecarboxamide': 'O=C(N)C1CC1',
            'chlorobenzene': 'ClC1=CC=CC=C1',
            'methyl tert-butylcarbamate': 'COC(NC(C)(C)C)=O',
            'tetrahydro-2H-pyran': 'C1CCCCO1',
            '2-cyclopropylpyrimidine': 'C1(C2CC2)=NC=CC=N1',
            '1-ethylpiperidine': 'CCN1CCCCC1'
        }

        exposed_to_solvent_smarts = {
            'N,N-dimethyl-2-phenoxyethan-1-amine': '[#6]-[#7](-[#6])-[#6]-[#6]-[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cyclopropanecarboxamide': '[#8]=[#6](-[#7])-[#6]1-[#6]-[#6]-1',
            'chlorobenzene': '[#17]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'methyl tert-butylcarbamate': '[#6]-[#8]-[#6](-[#7]-[#6](-[#6])(-[#6])-[#6])=[#8]',
            'tetrahydro-2H-pyran': '[#6]1-[#6]-[#6]-[#6]-[#6]-[#8]-1',
            '2-cyclopropylpyrimidine': '[#6]1(-[#6]2-[#6]-[#6]-2):[#7]:[#6]:[#6]:[#6]:[#7]:1',
            '1-ethylpiperidine': '[#6]-[#6]-[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
        }

        return  ribose_subpocket_smiles, ribose_subpocket_smarts, adenine_subpocket_smiles, adenine_subpocket_smarts, hydrophobic_subpocket_smiles, hydrophobic_subpocket_smarts, type_1_subpocket_smiles, type_1_subpocket_smarts, type_2_subpocket_smiles, type_2_subpocket_smarts, exposed_to_solvent_smiles, exposed_to_solvent_smarts

    def _get_common_amino_acid_protecting_groups():

        alpha_amino_removed_by_acid_smiles = {
            'tert-Butyloxycarbonyl': '',
            'trityl': '',
            '3,5-dimethoxyphenylisoproxycarbonyl': '',
            '2-(4-biphenyl)isopropoxycarbonyl': '',
            '2-nitrophenylsulfenyl': ''
        }

        alpha_amino_removed_by_acid_smarts = {

        }

        alpha_amino_removed_by_acid_acronym_smiles = {
            'boc': '',
            'trt': '',
            'ddz': '',
            'bpoc': '',
            'nps': ''
        }

        alpha_amino_removed_by_acid_acronym_smarts = {

        }

        alpha_amino_removed_by_base_smiles = {
            '9-fluorenylmethoxycarbonyl': '',
            '2-(4-nitrophenylsulfonyl)ethoxycarbonyl': '',
            '(1,1-dioxobenzo[b]thiophene-2-yl)methyloxycarbonyl': '',
            '(1,1-dioxonaptho[1,2-b]thiophene-2-yl)methyloxycarbonyl': '',
            '1-(4,4-dimethyl-2,6-dioxocyclohex-1-ylidene)-3-methylbutyl': '',
            '2,7-di-tert-butyl-fmoc': '',
            '2-fluoro-fmoc': '',
            '2-monoisooctyl-fmoc': '',
            '2,7-diisooctyl-fmoc': '',
            'tetrachlorophthaloyl': '',
            '2-[phenyl(methyl)sulfonio])ethyloxycarbonyltetrafluoroborate': '',
            'ethanesulfonylethoxycarbonyl': '',
            '2-(4-sulfophenylsulfonyl)ethoxycarbonyl': '',
        }

        alpha_amino_removed_by_base_smarts = {

        }

        alpha_amino_removed_by_base_acronym_smiles = {
            'fmoc': '',
            'nsc': '',
            'bsmoc': '',
            'alpha-nsmoc': '',
            'ivdde': '',
            'fmoc*': '',
            'fmoc(fmoc(2f))': '',
            'mio-fmoc': '',
            'dio-fmoc': '',
            'tcp': '',
            'pms': '',
            'esc': '',
            'sps': '',
        }

        alpha_amino_removed_by_base_acronym_smarts = {

        }

        other_alpha_amino_protect_groups_smiles = {
            'benzyloxycarbonyl': '',
            'allyloxycarbonyl': '',
            'o-nitrobenzenesulfonyl': '',
            '2,4-dinitrobenzenesulfonyl': '',
            'benzothiazole-2-sulfonyl': '',
            '2,2,2-trichloroethyloxycarbonyl': '',
            'dithiasuccinoyl': '',
            'p-nitrobenzyloxycarbonyl': '',
            'alpha-azidoacids': '',
            'proparglyoxycarbonyl': '',
            'o-nitrobenzylcarbonyl': '',
            '4-nitroveratryloxycarbonyl': '',
            '2-(2-nitrophenyl)propyloxycarbonyl': '',
            '2-(3,4-methylenedioxy-6-nitrophenyl)propyloxycarbonyl': '',
            '9-(4-bromophenyl)-9-fluorenyl': '',
            'azidomethoxycarbonyl': '',
            'hexafluoroacetone': '',
        }

        other_alpha_amino_protect_groups_smarts = {

        }

        other_alpha_amino_protect_groups_acronym_smiles = {
            'Z': '',
            'alloc': '',
            'onbs': '',
            'dnbs': '',
            'bts': '',
            'troc': '',
            'dts': '',
            'pnz': '',
            'poc': '',
            'onz': '',
            'nvoc': '',
            'nppoc': '',
            'mnppoc': '',
            'brphf': '',
            'azoc': '',
            'hfa': '',
        }

        other_alpha_amino_protect_groups_acronym_smarts = {

        }

        lys_orn_dap_dab_protecting_groups_removed_by_acid_smiles = {
            '2-chlorobenzyloxycarbonyl': '',
            'tert-butyloxycarbonyl': '',
            '4-methyltrityl': '',
        }

        lys_orn_dap_dab_protecting_groups_removed_by_acid_smarts = {

        }

        lys_orn_dap_dab_protecting_groups_removed_by_acid_acronym_smiles = {
            'cl-z': '',
            'boc': '',
            'mtt': '',
        }

        lys_orn_dap_dab_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        lys_orn_dap_dab_protecting_groups_removed_by_base_smiles = {
            '9-fluorenylmethoxycarbonyl': '',
            '1-(4,4-dimethyl-2,6-dioxocylohex-1-ylidene)-3-methylbutyl': '',
            'trifluoroacetyl': '',
            '2-(methylsulfonyl)ethoxycarbonyl': '',
            'tetrachlorophthaloyl': '',
        }

        lys_orn_dap_dab_protecting_groups_removed_by_base_smarts = {

        }

        lys_orn_dap_dab_protecting_groups_removed_by_base_acronym_smiles = {
            'fmoc': '',
            'ivdde': '',
            'tfa': '',
            'msc': '',
            'tcp': ''
        }

        lys_orn_dap_dab_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_lys_orn_dap_dab_protecting_groups_smiles = {
            'allyloxycarbonyl': '',
            'p-nitrobenzyloxycarbonyl': '',
            'phenyldisulphanylethyloxycarbonyl': '',
            '2-pyridyldisulphanylethyloxycarbonyl': '',
            'o-nitrobenzenesulfonyl': '',
        }

        other_lys_orn_dap_dab_protecting_groups_smarts = {

        }

        other_lys_orn_dap_dab_protecting_groups_acronym_smiles = {
            'alloc': '',
            'pnz': '',
            'phdec': '',
            'pydec': '',
            'o-nbs': ''
        }

        other_lys_orn_dap_dab_protecting_groups_acronym_smarts = {

        }

        alpha_carboxylic_acid_protecting_groups_removed_by_acid_smiles = {
            'tert-butyl': '',
            '2-chlorotrityl': '',
            '2-4-dimethyoxybenzyl': '',
            '2-phenylisopropyl': '',
            '5-phenyl-3,4-ethylenedioxythenyl': '',
        }

        alpha_carboxylic_acid_protecting_groups_removed_by_acid_smarts = {

        }

        alpha_carboxylic_acid_protecting_groups_removed_by_acid_acronym_smiles = {
            'bu': '',
            '2-cl-trt': '',
            'dmb': '',
            '2-ph-pr': '',
            'phenyl-edotn': '',
        }

        alpha_carboxylic_acid_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        alpha_carboxylic_acid_protecting_groups_removed_by_base_smiles = {
            '9-fluorenylmethyl': '',
            '4-(N-[1-(4,4-dimethyl-2,6-dioxocylocheylidene)-3-methylbutyl]-amino)benzyl': '',
            'methyl': '',
            'ethyl': '',
            'carbamoylmethyl': '',

        }

        alpha_carboxylic_acid_protecting_groups_removed_by_base_smarts = {

        }

        alpha_carboxylic_acid_protecting_groups_removed_by_base_acronym_smiles = {
            'fm': '',
            'dmab': '',
            'me': '',
            'et': '',
            'cam': '',
        }

        alpha_carboxylic_acid_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_alpha_carboxylic_acid_protecting_group_smiles = {
            'allyl': '',
            'benzyl': '',
            'phenacyl': '',
            'p-nitrobenzyl': '',
            '2-trimethylsilyethyl': '',
            '(2-phenyl-2-trimethylsilyl)ethyl': '',
            '2-(trimethylsilyl)isopropyl': '',
            '2,2,2-trichloroethyl': '',
            'p-hydroxyphenacyl': '',
            '4,5-dimethyoxy-2-nitrobenzyl': '',
            '1,1-dimethylallyl': '',
            'pentaaminecobalt_III': '',
        }

        other_alpha_carboxylic_acid_protecting_group_smarts = {

        }

        other_alpha_carboxylic_acid_protecting_group_acronym_smiles = {
            'al': '',
            'bn': '',
            'pac': '',
            'pnb': '',
            'tmse': '',
            'ptmse': '',
            'tmsi': '',
            'tce': '',
            'php': '',
            'dmnb': '',
            'dma': '',
        }

        other_alpha_carboxylic_acid_protecting_group_acronym_smarts = {

        }

        asp_glu_protecting_groups_removed_by_acid_smiles = {
            'benzyl': '',
            'cyclohexyl': '',
            'tert-butyl': '',
            'b-menthyl': '',
            'b-3-methylpent-3-yl': '',
            '2-phenylisopropyl': '',
            '4-(3,6,9-trioxadecyl)oxybenzyl': '',
        }

        asp_glu_protecting_groups_removed_by_acid_smarts = {

        }

        asp_glu_protecting_groups_removed_by_acid_acronym_smiles = {
            'bn': '',
            'chx': '',
            'bu': '',
            'men': '',
            'mpe': '',
            '2-ph-pr': '',
            'tegbz': '',

        }

        asp_glu_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        asp_glu_protecting_groups_removed_by_base_smiles = {
            '9-fluoroenylmethyl': '',
            '4-(N-[1-(4,4-dimethyl-2,6-dioxocyclohexylidene)-3-methyl-butyl]-amino)benzyl': '',
        }

        asp_glu_protecting_groups_removed_by_base_smarts = {

        }

        asp_glu_protecting_groups_removed_by_base_acronym_smiles = {
            'fm': '',
            'dmab': ''
        }

        asp_glu_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_asp_glu_protecting_groups_smiles = {
            'allyl': 'al',
            'p-nitrobenzyl': '',
            'trimethylsilylethyl': '',
            '(2-phenyl-2-trimethylsilyl)ethyl': '',
            '4,5-dimethoxy-2-nitrobenzyloxycarbonyl': '',
        }

        other_asp_glu_protecting_groups_smarts = {

        }

        other_asp_glu_protecting_groups_acronym_smiles = {
            'al': '',
            'pnb': '',
            'tmse': '',
            'ptmse': '',
            'dmnb': '',
        }

        other_asp_glu_protecting_groups_acronym_smarts = {

        }

        amide_backbone_protecting_group_removed_by_acid_smiles = {
            'pseudoprolines': '',
            '2-hydroxy-4-methoxybenzyl': '',
            '2,4-dimethoxybenzyl': '',
            '2,4,6-trimethoxybenzyl': '',
            '1-methyl-3-indolylmethyl': '',
            '3,4-ethylene-dioxy-2-thenyl': '',
        }

        amide_backbone_protecting_group_removed_by_acid_smarts = {

        }

        amide_backbone_protecting_group_removed_by_acid_acronym_smiles = {
            'hmb': '',
            'dmb': '',
            'tmob': '',
            'mim': '',
            'edot': '',
        }

        amide_backbone_protecting_group_removed_by_acid_acronym_smarts  = {

        }

        other_amide_backbone_protecting_group_smiles = {
            '4-methoxy-2-nitro-benzyl': '',
            '(6-hydroxy-3-oxido-1,3-benz[d]oxathiol-5-yl)methyl': '',
            '2-hydroxy-4-methoxy-5-(methylsulfinyl)benzyl': '',
            'n-boc-n-methyl[2-(methylamino)ethyl]carbamoyl-hmb': '',
        }

        other_amide_backbone_protecting_group_smarts = {

        }

        asn_gln_protecting_groups_removed_by_acid_smiles = {
            '9-xanthenyl': '',
            'trityl': '',
            '4-methyltrityl': '',
            'cyclopropyldimethylcarbinyl': '',
            '4,4-dimethoxybenzhydryl': '',
            '2,4,6-trimethoxybenzyl': '',
        }

        asn_gln_protecting_groups_removed_by_acid_smarts = {

        }

        asn_gln_protecting_groups_removed_by_acid_acronym_smiles = {
            'xan': '',
            'trt': '',
            'mtt': '',
            'cpd': '',
            'mbh': '',
            'tmob': '',
        }

        asn_gln_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        arg_protecting_groups_removed_by_acid_smiles = {
            'p-toluenesulfonyl': '',
            '2,2,5,7,8-pentamethylchroman-6-sulfonyl': '',
            '2,2,4,6,7-pentamethyl-2,3-dihydrobenzofuran-5-sulfonyl': '',
            'mesityl-2-sulfonyl': '',
            '4-methoxy-2,3,6-trimethylphenylsulfonyl': '',
            '1,2-dimethylindole-3-sulfonyl': '',
            'w,w-bis-tert-butyloxycarbonyl': '',
            '5-dibenzosuberenyl': '',
            '5-dibenzosuberyl': '',
            '2-methoxy-5-dibenzosuberyl': '',
            'nitro': ''
        }

        arg_protecting_groups_removed_by_acid_smarts = {

        }

        arg_protecting_groups_removed_by_acid_acronym_smiles = {
            'tos': '',
            'pmc': '',
            'pbf': '',
            'mts': '',
            'mtr': '',
            'mis': '',
            'bis-boc': '',
            'suben': '',
            'sub': '',
            'mesub': '',
            'no2': ''
        }

        arg_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        arg_protecting_groups_removed_by_base_smiles = {
            'trifluoroacetyl': ''
        }

        arg_protecting_groups_removed_by_base_smarts = {

        }

        arg_protecting_groups_removed_by_base_acronym_smiles = {
            'tfa': ''
        }

        arg_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_arg_protecting_groups_smiles = {
            'w,w-bis-benzyloxycarbonyl': '',
            'w,w-bis-allyloxycarbonyl': ''
        }

        other_arg_protecting_groups_smarts = {

        }

        other_arg_protecting_groups_acronym_smiles = {
            'z': '',
            'alloc': '',
        }

        other_arg_protecting_groups_acronym_smarts = {

        }

        cys_protecting_groups_removed_by_acid_smiles = {
            'p-methylbenzyl': '',
            'p-methoxybenzyl': '',
            'trityl': '',
            'monomethoxytrityl': '',
            'trimethoxybenzyl': '',
            '9-xanthenyl': '',
            '2,2,4,6,7-pentamethyl-5-dihydrobenzofuranylmethyl': '',
            'benzyl': '',
            'tert-butyl': '',
            '1-adamantyl': '',
        }

        cys_protecting_groups_removed_by_acid_smarts = {

        }

        cys_protecting_groups_removed_by_acid_acronym_smiles = {
            'meb': '',
            'mob': '',
            'trt': '',
            'mmt': '',
            'tmob': '',
            'xan': '',
            'pmbf': '',
            'bn': '',
            'bu': '',
            '1-ada': '',
        }

        cys_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        cys_protecting_groups_removed_by_base_smiles = {
            '9-fluorenylmethyl': '',
            '2-(2,4-dinitrophenyl)ethyl': '',
            '9-fluororenylmethoxycarbonyl': '',
        }

        cys_protecting_groups_removed_by_base_smarts = {

        }

        cys_protecting_groups_removed_by_base_acronym_smiles = {
            'fm': '',
            'dnpe': '',
            'fmoc': '',
        }

        cys_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_cys_protecting_groups_smiles = {
            'acetamidomethyl': '',
            'phenylacetamidomethyl': '',
            '5-tert-butylmercapto': '',
            '3-nitro-2-pyridinesulfenyl': '',
            '2-pyridinesulfenyl': '',
            'allyloxycarbonyl': '',
            'N-allyloxycarbonyl-N-[2,3,5,6-tetrafluoro-4-(phenylthio)phenyl]]aminomethyl': '',
            'o-nitrobenzyl': '',
            '4-picolyl': '',
            'ninhydrin': '',
        }

        other_cys_protecting_groups_smarts = {

        }

        other_cys_protecting_groups_acronym_smiles = {
            'acm': '',
            'phacm': '',
            'sbu': '',
            'npys': '',
            's-pyr': '',
            'alloc': '',
            'fsam': '',
            'onb': '',
            'nin': ''
        }

        other_cys_protecting_groups_acronym_smarts = {

        }

        his_protecting_groups_removed_by_acid_smiles = {
            'n-tosyl': '',
            'n-trityl': '',
            'n-monomethoxytrityl': '',
            'n-methyltrityl': '',
            'n-tert-butyloxycarbonyl': '',
            'n-2,4-dimethylpent-3-yloxycarbonyl': '',
            'n-benzyloxymethyl': '',
            'n-tert-butoxymethyl': '',
        }

        his_protecting_groups_removed_by_acid_smarts = {

        }

        his_protecting_groups_removed_by_acid_acronym_smiles = {
            'tos': '',
            'trt': '',
            'mtt': '',
            'mmt': '',
            'boc': '',
            'doc': '',
            'bom': '',
            'bum': '',
        }

        his_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        his_protecting_groups_removed_by_base_smiles = {
            '9-fluorenylmethoxycarbonyl': '',
            '2,6-dimethoxybenzoyl': '',
        }

        his_protecting_groups_removed_by_base_smarts = {

        }

        his_protecting_groups_removed_by_base_acronym_smiles = {
            'fmoc': '',
            'dmbz': '',
        }

        his_protecting_groups_removed_by_base_acronym_smarts = {

        }

        other_his_protecting_groups_smiles = {
            'N-2,4-dinitrophenyl': '',
        }

        other_his_protecting_groups_smarts = {

        }

        other_his_protecting_groups_acronym_smiles = {
            'dnp': ''
        }

        other_his_protecting_groups_acronym_smarts = {

        }

        ser_thr_hyp_protecting_groups_removed_by_acid_smiles = {
            'benzyl': '',
            'cyclohexyl;': '',
            'tert-butyl': '',
            'trityl': '',
            'tert-butyldimethylsilyl': '',
            'pseudoprolines': ''
        }

        ser_thr_hyp_protecting_groups_removed_by_acid_smarts = {

        }

        ser_thr_hyp_protecting_groups_removed_by_acid_acronym_smiles = {
            'bn': '',
            'chx': '',
            'bu': '',
            'trt': '',
            'tbdms': '',
        }

        ser_thr_hyp_protecting_groups_acronym_removed_by_acid_smarts = {

        }

        other_ser_thr_hyp_protecting_groups_smiles = {
            'tert-butyldiphenylsilyl': '',
            '4,5-dimethoxy-2-nitrobenzyloxycarbonyl': '',
            'propargyloxycarbonyl': '',
        }

        other_ser_thr_hyp_protecting_groups_smarts = {

        }

        other_ser_thr_hyp_protecting_groups_acronym_smiles = {
            'tbdps': '',
            'dmnb': '',
            'poc': ''
        }

        other_ser_thr_hyp_protecting_groups_acronym_smarts = {

        }

        tyr_protecting_groups_removed_by_acid_smiles = {
            'benzyl': '',
            'tert-butyl': '',
            '2,6-dichlorobenzyl': '',
            '2-bromobenzyl': '',
            'benzyloxycarbonyl': '',
            '2-bromobenzyloxycarbonyl': '',
            '3-pentyl': '',
            'tert-butyloxycarbonyl': '',
            'trityl': '',
            '2-chlorotrityl': '',
            'tert-butyldimethylsilyl': '',
            '4-(3,6,9-trioxadecyl)oxybenzyl': ''

        }

        tyr_protecting_groups_removed_by_acid_smarts = {

        }

        tyr_protecting_groups_removed_by_acid_acronym_smiles = {
            'bn': '',
            'bu': '',
            'dcb': '',
            'brbn': '',
            'z': '',
            'brz': '',
            'pen': '',
            'boc': '',
            '2-cl-trt': '',
            'tbdms': '',
            'tegb': '',
        }

        tyr_protecting_groups_removed_by_acid_acronym_smarts = {

        }

        other_tyr_protecting_group_smiles = {
            'allyl': '',
            'o-nitrobenzyl': '',
            'propargyloxycarbonyl': '',
            'boc-n-methyl-n-[2-(methylamino)ethyl]carbamoyl': ''
        }

        other_tyr_protecting_group_smarts = {

        }

        other_tyr_protecting_group_acronym_smiles = {
            'al': '',
            'onb': '',
            'poc': '',
            'boc-nmec': '',
        }

        other_tyr_protecting_group_acronym_smarts = {

        }

        trp_protecting_groups_removed_by_acid_smiles = {
            'formyl': '',
            'tert-butyloxycarbonyl': '',
            'cyclohexyloxycarbonyl': '',
            'mesityl-2-sulfonyl': '',
            'allyloxycarbonyl': '',
        }

        trp_protecting_groups_removed_by_acid_smarts = {

        }

        trp_protecting_groups_removed_by_acid_acronym_smiles = {
            'for': '',
            'boc': '',
            'hoc': '',
            'mts': '',
            'alloc'
        }

        trp_protecting_groups_removed_by_acid_acronym_smarts = {

        }


    def _get_common_synthetic_dyes_in_medicine():

       raise NotImplementedError

       non_ionic_dyes_with_acidic_colligators_smiles = {
            'chyrazine': '',
            'sudan_1': '',
            'sudan_2': '',
            'sudan_r': '',
            'sudan_3': '',
            'sudan_4': '',
       }

       non_ionic_dyes_with_acidic_colligators_smarts = {

       }

       non_ionic_dyes_with_basic_colligators_smiles = {
           'oil_yellow_b': '',
           'duranol_violet_2r': '',
           'sudan_blue': '',
           'sudan_black_b': '',
       }

       non_ionic_dyes_with_basic_colligators_smarts = {

       }

       non_ionic_dyes_neutral_smiles = {
          'dimethyl_yellow': '',
          'indophenol': '',
       }

       non_ionic_dyes_neutral_smarts = {

       }

       non_ionin_dyes_amphoteric_smiles = {
            'sudan_purple': '',
            'sudan_green': '',

       }

       non_ionin_dyes_amphoteric_smarts = {

       }

       cationic_dyes_wholly_basic_smiles = {
           'chrysoidine_y': '',
           'neutral_red': '',
           'chrysoidine_r': '',
           'thionine': '',
           'acridine_yellow_gr': '',
           'azur_c': '',
           'p-methoxychrysoidine': '',
           'euchrysine_2gnx': '',
           'aurophosphine': '',
           'toluylene_blue': '',
           'p-ethoxychrysoidine': '',
           'azur_a': '',
           'methylene_violet': '',
           'acridine_organe': '',
           'pyronine_y': '',
           'auramine_o': '',
           'toluidine_blue_o': '',
           'azur_b': '',
           'meldola_blue': '',
           'methylene_blue': '',
           'fuchsin_basic': '',
           'pararosaniline_chloride': '',
           'rosaniline_chloride': '',
           'safranine_o': '',
           'astrazone_orange_g': '',
           'astrazone_pink_fg': '',
           'nile_blue': '',
           'bismarck_brown_r': '',
           'pyronine_b': '',
           'malachite_green': '',
           'methylene_green': '',
           'new_fuchsin': '',
           'brilliant_basic_red_b': '',
           'acronol_phloxine_ffs': '',
           'setoglaucine': '',
           'zapon_fast_blue_3g': '',
           'crystal_violet': '',
           'neutral_violet': '',
           'astrazone_red_6b': '',
           'brilliant_green': '',
           'methyl_green_oo': '',
           'hofmann_violent': '',
           'setocyanine': '',
           'astrazone_orange_r': '',
           'amethyst_violet': '',
           'mauveine': '',
           'rhodamine_6g': '',
           'victoria_blue_r': '',
           'janus_green_b': '',
           'victoria_blue_b': '',
           'victoria_blue_4r': '',
           'induline': '',
           'brilliant_glacier_blue': '',
           'night_blue': '',
           'alcian_blue_8gx': '',
       }

       cationic_dyes_wholly_basic_smarts = {

       }

       cationic_dyes_acidic_colligators_smiles = {
           'janus_red': '',
           'rhodamine_b': '',
           'janus_black_b': '',
           'janus_blue': '',
           'methyl_red': '',
       }

       cationic_dyes_acidic_colligators_smarts = {

       }

       anionic_dyes_with_wholly_acid_cooh_oh_colligators_smiles = {
           'eriochrome_flavine_a': '',
           'alizarin_yellow_gg': '',
           'alizarin_yellow_g': '',
           'uranine': '',
           'fluorescenin_acid': '',
           'gallein': '',
           'chrome_brilliant_violet_2r': '',
           'solochrome_azurine_b': '',
           'brilliant_monochrome_violet_2b': '',
           'naphthochrome_green': '',
           'diamond_blue_fbg': '',
           'dibromofluorescein': '',
           'chyromoxane_brilliant_red_bl': '',
           'metachrome_yellow_2rd': '',
           'eosin_bn': '',
           'erythrosine_y': '',
           'benzo_yellow_ltrl' :'',
           'eosin_acid': '',
           'eosin_y': '',
           'mercurochrome': '',
           'phloxine_b': '',
           'erythrosine_b': '',
           'rose_bengale': '',
       }

       anionic_dyes_with_wholly_acid_cooh_oh_colligators_smarts = {
           ''
       }

       anionic_dyes_with_wholly_acid_sulphonated_without_oh_smiles = {
           'methyl_orange': '',
           'quinoline_yellow_kt': '',
           'soledon_yellow_g': '',
           'durazol_yellow_g': '',
           'chrysophenine': '',
           'supranol_yellow_o': '',
           'remastral_violet_frl': '',
           'durazol_blue_8g': '',
           'sun_yellow_g': '',
           'naphthol_green_b': '',
           'remastral_blue_ffrl': '',
           'remastral_blue_f3gl': '',
           'sirius_orange_g': '',
       }

       anionic_dyes_with_wholly_acid_sulphonated_without_oh_smarts = {

       }

       anionic_dyes_with_wholly_acid_sulphonated_with_oh_smiles = {
           'naphthol_green_y': '',
           'tropaeolin_o': '',
           'eriochrome_bordeaux': '',
           'naphthol_yellow_s': '',
           'alizarin_red_s': '',
           'tropaeoloin_ooo_no_1': '',
           'tropaeoloin_ooo_no_2': '',
           'eriochrome_violet': '',
           'brilliant_orange_r': '',
           'flavazine': '',
           'azoeosine_g': '',
           'roccellin': '',
           'monochrome_red_g': '',
           'acid_alizarin_black_r': '',
           'eriochrome_blue_black_b': '',
           'palatine_fast_orange_rn': '',
           'orange_6': '',
           'orange_ggn': '',
           'sunset_yellow_fcf': '',
           'alizarin_blue_black': '',
           'ponceau_scarlet': '',
           'eriochrome_red_8': '',
           'ponceau_2r': '',
           'acilan_scarlet_a': '',
           'eriochrome_black_t': '',
           'acid_levelling_red_3gs': '',
           'flavazine_e3gl': '',
           'chromazone_red_a': '',
           'scarlet_2re': '',
           'fd8c_red_no_6': '',
           'fast_navy_2r': '',
           'naphthalene_red_eas': '',
           'bordeaux_b': '',
           'crystal_ponceau': '',
           'carmoisine_a': '',
           'carmoisine_l': '',
           'croceine_scarlet_38x': '',
           'eriochrome_verdone_a': '',
           'diamond_black': '',
           'acid_alizarin_blue_bb': '',
           'anthralane_yellow_g': '',
           'chromotrope_io_b': '',
           'supramine_red_b': '',
           'solochrome_green_v': '',
           'lissamine_fast_yellow': '',
           'biebrich_scarlet_water_soluble': '',
           'brilliant_croceine': '',
           'chrome_fast_navy_blue_r': '',
           'ponceau_4r': '',
           'amaranth': '',
           'xylene_fast_orange_po': '',
           'thiazine_red': '',
           'solochrome_black_f': '',
           'polar_yellow_5g': '',
           'resorcine_brown_r': '',
           'paper_yellow_g': '',
           'alizarin_black_r': '',
           'acilan_ponceau_6r': '',
           'benzo_orange_brown_gr': '',
           'baygenal_brown_cm': '',
           'congo_violet': '',
           'supranol_orange_g': '',
           'sulphon_black_4b': '',
           'benzoazurine_g': '',
           'chlorazol_violet_r': '',
           'wool_fast_yellow_gg': '',
           'dianil_blue_2r': '',
           'supranol_fast_red_88': '',
           'benzo_azurine_fbs': '',
           'supranol_bordeaux_g': '',
           'dianil_blue_b': '',
           'sirius_supra_blue_gl': '',
           'milling_yellow_3g': '',
           'direct_brilliant_blue_c': '',
           'supranol_fast_red_br': '',
           'sirius_supra_grey_r': '',
       }

       anionic_dyes_with_wholly_acid_sulphonated_with_oh_smarts = {

       }

       anionic_dyes_with_wholly_acid_sulphonated_with_cooh_and_oh_smiles = {
           'xylenol_yellow': '',
           'solochrome_orange_grs': '',
           'acid_alizarin_red_2b': '',
           'tartrazine': '',
           'solochrome_cyanine_r': '',
           'chrome_azurol_red': '',
           'benzo_fast_copper_brown_nl': '',
       }

       anionic_dyes_with_wholly_acid_sulphonated_with_cooh_and_oh_smarts = {

       }

       anionic_dyes_with_wholly_acid_sulphonated_with_oh_colligators_smiles = {
           'fast_green_o': '',
           'picric_acid': '',
           'alizarin': '',
           'martius_yellow': '',
           'anthrapurpurine': '',
           'alizarin_cyanine_2r': '',
           'rosolic_acid': '',
           'aurantia': '',
           'ethyl_eosin': '',
           'cyanosine_b': '',
       }

       anionic_dyes_with_wholly_acid_sulphonated_with_oh_colligators_smarts = {

       }

       anionic_dyes_with_weakly_amphoteric_sulphonated_without_oh_smiles = {
           'alkali_green': '',
           'xylene_red_b': '',
           'fast_acid_violet_iob': '',
           'acilan_brilliant_blue_r': '',
           'guine_a_green_b': '',
           'erioglaucine_xs': '',
           'eriocyanine_a': '',
           'acilan_violet_4bl': '',
           'disulphine_green_b': '',
           'acilan_violet_s4bn': '',
           'acilan_fast_green_10g': '',
           'acid_violet_6b': '',
           'light_green_sf_yellowish': '',
           'acilan_brilliant_blue_ffr': '',
           'supranol_blue_b': '',
           'brillant_indo_blue_5g': '',
       }

       anionic_dyes_with_weakly_amphoteric_sulphonated_without_oh_smarts = {

       }

       anionic_dyes_with_weakly_amphoteric_sulphonated_with_oh_smiles = {
           'wool_green_5': '',
           'patent_blue_a': '',
       }

       anionic_dyes_with_weakly_amphoteric_sulphonated_with_oh_smarts = {
           'wool_green_5': '',
           'patent_blue_a': '',
       }

       anionic_dyes_with_strongly_amphoteric_sulphonated_with_nh_without_oh_smiles = {
           'diazol_light_brown_jrn': '',
           'sirius_supra_orange_prl': '',
           'durazol_scarlet_gg': '',
           'metanil_yellow': '',
           'tropaeolin_oo': '',
           'fast_yellow_g': '',
           'lissamine_flavine_f5': '',
           'fast_yellow_r': '',
           'alizarin_direct_violet_ebb': '',
           'alizarin_brilliant_sky_blue_r': '',
           'supracen_violet_48f': '',
           'indigo_carmine': '',
           'acilan_fast_blue_rx': '',
           'alizarin_celestol_b': '',
           'alazarin_rubinol_r': '',
           'alizarin_blue_a': '',
           'amido_napthol_brown_3g': '',
           'benzyl_red_3b': '',
           'supramine_bordeaux_b': '',
           'alizarin_sky_blue_ffg': '',
           'alizarin_sky_blue_b': '',
           'acilan_fast_blue_rbx': '',
           'alizarin_rubinol_3g': '',
           'benzopurpurine_10b': '',
           'fuchsin_acid': '',
           'benzamine_brown_3r': '',
           'alkali_blue_4b': '',
           'fast_acid_blue_b': '',
           'azocarmine_g': '',
           'wool_fast_blue_fgll': '',
           'anthraquinone_violet_3r': '',
           'alizarin_cyanine_green': '',
           'carbolan_violet_2r': '',
           'supracen_violet_3r': '',
           'violamine_r': '',
           'alkali_blue_6b': '',
           'acilan_fast_violet_fb': '',
           'polar_brillant_blue': '',
           'acid_violet_6b': '',
           'supranol_fast_cyanine_5r': '',
           'azocarmine_b': '',
           'carbolan_blue_bs': '',
           'supranol_blue_bl': '',
           'titan_yellow': '',
           'cloth_blue_r': '',
           'supranol_fast_cyanine_g': '',
           'congo_red': '',
           'carbolan_green_g': '',
           'methyl_blue': '',
           'coomassie_blue_gl': '',
           'benzopurpurine_4b': '',
           'cloth_fast_black_b': '',
           'aniline_blue': '',
           'solophenyl_brilliant_blue_bl': '',
           'benzo_fast_copper_red_ggl': '',
           'coomassie_fast_black_g': '',
           'isamine_blue': '',
           'alizarin_cyanine_green_gwa': '',
           'acilan_fast_green_bbf': '',
           'soluble_blue_8b': '',
           'polar_orange_r': '',
           'supranol_fast_cyanine_b': '',
           'acilan_brilliant_blue_ffb': '',
           'wool_fast_blue_fbl': '',
           'coomassie_brilliant_blue_r': '',
           'sirius_supra_yellow_r': '',
           'benzo_brilliant_red_8bs': '',
           'trypan_red': '',
           'diazol_light_yellow_rs': '',
           'sirius_supra_brown_g': '',
       }

       anionic_dyes_with_strongly_amphoteric_sulphonated_with_nh_without_oh_smarts = {

       }

       anionic_dyes_with_strongly_amphoteric_sulphonated_with_nh_with_oh_smiles = {
           'diamond_brown_b': '',
           'acilan_brown_r': '',
           'lignin_pink': '',
           'alizarin_brilliant_blue_b': '',
           'diamond_brown_rh': '',
           'supracen_blue_ses': '',
           'supramine_green_bl': '',
           'celestine_blue_sulphonate': '',
           'supramine_orange_r': '',
           'brilliant_delphine_blue': '',
           'chromazurine': '',
           'alizarin_saphirol': '',
           'chrome_blue_black': '',
           'salicene_chrome_bordeaux_b': '',
           'acid_violet_4bs': '',
           'kiton_fast_red_b2r': '',
           'chrome_fast_green_g': '',
           'supramine_red_gl': '',
           'supramine_black_br': '',
           'lissamine_fast_red_b': '',
           'zambesi_black_d': '',
           'diamond_chrome_olive_bl': '',
           'chrome_green_n': '',
           'supramine_red_bl': '',
           'xylene_cyanol_ff': '',
           'azofuchsin_6b': '',
           'omega_chrome_fast_blue_2g': '',
           'azo_dark_green': '',
           'diazol_light_scarlet_5b': '',
           'benzamine_brilliant_orange_grn': '',
           'acid_chrome_blue_c': '',
           'benzo_orange_r': '',
           'naphthol_blue_black': '',
           'supramine_blue_r': '',
           'chlorazol_fast_red_f': '',
           'toluylene_orange': '',
           'alizarin_cyanine_green_5g': '',
           'sirius_supra_yellow_5g': '',
           'anthosine_5b': '',
           'fast_acid_blue_a': '',
           'trisulphon_violet_2b': '',
           'dianil_brown': '',
           'salicene_chrome_blue_ffg': '',
           'chlorantine_fast_red_5b': '',
           'dianil_yellow_3g': '',
           'napthalene_blue_black': '',
           'congo_rubine': '',
           'erie_garnet_b': '',
           'chlorazol_paper_brown': '',
           'supranol_brilliant_red_3b': '',
           'sirius_violet_2b': '',
           'owens_blue': '',
           'chlorazol_violet_n': '',
           'benzamine_brilliant_blue_bbls': '',
           'supranol_fast_orange_rr': '',
           'supranol_fast_scarlet_gn': '',
           'chlorazol_blue_rw': '',
           'chlorazol_black_e': '',
           'baygenal_brown_ct': '',
           'benzo_rubine_r': '',
           'supranol_red_3_bl': '',
           'renol_black': '',
           'manchester_blue': '',
           'chlorazol_green_bns': '',
           'benzo_fast_scarlet': '',
           'benzo_blue_fbl': '',
           'benzo_scarlet_5bs': '',
           'durazol_blue_4r': '',
           'airedale_brown_bd': '',
           'benzamine_rubine_fdg': '',
           'benzo_fast_copper_brown_3gl': '',
           'diazo_light_blue_b': '',
           'dianil_green_b': '',
           'sirius_scarlet_b': '',
           'benzo_blue_2b': '',
           'sirius_supra_green_bb': '',
           'trypan_blue': '',
           'dianil_black_cr': '',
           'benzo_fast_copper_yellow_ggl': '',
           'chlorazol_fast_pink_bk': '',
           'pontamine_sky_blue_5b': '',
           'chlorazol_sky_blue_ff': '',
           'benzo_fast_copper_blue_f3gl': '',
           'sirius_supra_red_violet_b': '',
           'chlorazol_catechine_g': '',
           'suprexcel_red_6bl': '',
           'benzo_fast_copper_yellow_grl': '',
           'chlorantine_fast_blue_4gl': '',
           'sirius_supra_blue_3rl': '',
           'sirius_grey_g': '',
           'benzo_brilliant_green_l3g': '',
           'sirius_supra_blue_bl': '',
           'benzo_deep_brown_nz': '',
           'sirius_supra_grey_gg': '',
           'benzo_fast_copper_navy_blue_bl': '',
           'benzo_fast_copper_violet_f3bl': '',
           'sirius_grey_gb': '',
           'sirius_supra_green_btl': '',
           'chlorantine_fast_green_bill': '',
       }

       anionic_dyes_with_strongly_amphoteric_sulphonated_with_nh_with_oh_smarts = {

       }

       anionic_dyes_with_amphoteric_sulphonated_with_oh_acidic_colligator_nh_basic_colligator_smiles = {
           'metachrome_brown_r': '',
           'metachrome_brown_b': '',
       }

       anionic_dyes_with_amphoteric_sulphonated_with_oh_acidic_colligator_nh_basic_colligator_smarts = {

       }

       disperse_dyes_smiles = {
           'acetoquinone_yello_5je': '',
           'supracet_fast_yellow_2r': '',
           'celliton_blue_ffb': '',
           'acetoquinone_blue_bf': '',
           'duranol_blue_green_2g': '',
           'dispersol_fast_red_r': '',
           'celliton_yellow_3g': '',
       }

       disperse_dyes_smarts = {

       }

       vat_dyes_smiles = {
           'indanthrene_turquoise_blue_3gk': '',
           'indanthrene_bordeaux_b': '',
           'indanthrene_brilliant_blue_4g': '',
       }

       vat_dyes_smarts = {

       }

       reactive_dyes_smiles = {
           'procion_brilliant_blue_hrgt': '',
           'procion_red_mgs': '',
           'luxol_brilliant_green_bl': '',
       }

       reactive_dyes_smarts = {

       }

       #------------------------- Property Declaration for GlobalChem ---------------------------#

    # Biological Compounds

    (
        amino_acid_side_smiles,
        amino_acid_side_smarts
    ) = _get_amino_acids()

    (
        vitamins_smiles,
        vitamins_smarts
    ) = _get_essential_vitamins()

    # Common Organic Solvents
    # -----------------------

    (
        common_organic_solvents_smiles,
        common_organic_solvents_smarts
    ) = _get_common_organic_solvents()

    # Commonly Used R Group Replacements
    # ----------------------------------

    (
        r_groups_replacements_smiles,
        r_groups_replacements_smarts
    ) = _get_commonly_used_r_group_replacements()

    # Open Smiles
    # -----------

    (
        open_smiles_functional_groups_smiles,
        open_smiles_functional_groups_smarts
    ) = _get_open_smiles_functional_groups()

    # Rings in Drugs
    # --------------

    (
        rings_in_drugs_smiles,
        rings_in_drugs_smarts
    ) = _get_rings_in_drugs()

    # Iupac Blue Book
    # ---------------

    (
        iupac_blue_book_radical_smiles,
        iupac_blue_book_radical_smarts,
        iupac_blue_book_rings_smiles,
        iupac_blue_book_rings_smarts
    ) = _get_iupac_blue_book_common_functional_groups()

    # Common Phase 2 Hetereocyclic Rings
    # ----------------------------------
    (
        phase_2_hetereocyclic_rings_smiles,
        phase_2_hetereocyclic_rings_smarts
    ) = _get_common_heterocyclic_rings_phase_2()

    # Privileged Scaffolds
    # --------------------

    (
        privileged_scaffolds_smiles,
        privileged_scaffolds_smarts
    ) = _get_common_privileged_scaffolds()

    (
        kinase_privileged_scaffolds_smiles,
        kinase_privileged_scaffolds_smarts
    ) = _get_privileged_scaffolds_for_kinase_inhibitors()


    (
        ribose_subpocket_smiles,
        ribose_subpocket_smarts,
        adenine_subpocket_smiles,
        adenine_subpocket_smarts,
        hydrophobic_subpocket_smiles,
        hydrophobic_subpocket_smarts,
        type_1_subpocket_smiles,
        type_1_subpocket_smarts,
        type_2_subpocket_smiles,
        type_2_subpocket_smarts,
        exposed_to_solvent_smiles,
        exposed_to_solvent_smarts
    ) = _get_braf_kinase_inhibitors_for_cancer()

    # Warheads
    # --------

    (
        common_warheads_smiles,
        common_warheads_smarts
    ) = _get_major_warhead_functional_groups()

    (
        kinase_electrophilic_warheads_smiles,
        kinase_electrophilic_warheads_smarts

    ) = _get_common_electrophilic_warheads_for_kinases()

    # Common Polymers

    (
        common_polymer_repeating_units_smiles,
        common_polymer_repeating_units_smarts

    ) = _get_common_polymer_repeating_units()

    # Regex Patterns
    # --------------

    (
        common_regex_patterns
    ) = _get_common_regex_patterns()
