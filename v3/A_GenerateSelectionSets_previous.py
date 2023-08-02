import os
import json


def save_references(_d):
    with open(os.path.join(os.getcwd(), 'references.json'), 'w') as f:
        json.dump(_d, f)


ordered_set = {
    '00 SLABS - SL1': {
        1: '66', 2: '65', 3: '64', 4: '69', 5: '68', 6: '67', 7: '72', 8: '71', 9: '70', 10: '75', 11: '74', 12: '73',
        13: '78', 14: '77', 15: '76', 16: '81', 17: '80', 18: '79', 19: '84', 20: '83', 21: '82', 22: '19', 23: '20',
        24: '21', 25: '22', 26: '23', 27: '24', 28: '25', 29: '26', 30: '27', 31: '28', 32: '29', 33: '30', 34: '31',
        35: '32', 36: '33', 37: '34', 38: '35', 39: '36', 40: '37', 41: '38', 42: '39', 43: '40', 44: '41', 45: '42',
        46: '43', 47: '44', 48: '45', 49: '46', 50: '47', 51: '48', 52: '49', 53: '50', 54: '51', 55: '52', 56: '53',
        57: '54', 58: '55', 59: '56', 60: '57', 61: '58', 62: '59', 63: '60', 64: '61', 65: '62', 66: '63', 67: '3',
        68: '1', 69: '2', 70: '6', 71: '4', 72: '5', 73: '9', 74: '7', 75: '8', 76: '12', 77: '10', 78: '11', 79: '15',
        80: '13', 81: '14', 82: '18', 83: '16', 84: '17',
    },

    '00 SLABS - SL2': {
        1: '22', 2: '23', 3: '24', 4: '25', 5: '26', 6: '27', 7: '28', 8: '7', 9: '8', 10: '9', 11: '10', 12: '11',
        13: '12', 14: '13', 15: '14', 16: '15', 17: '16', 18: '17', 19: '18', 20: '19', 21: '20', 22: '21', 23: '1',
        24: '2', 25: '3', 26: '4', 27: '5', 28: '6'
    },
    '00 SLABS - SL3': {
        1: '22', 2: '23', 3: '24', 4: '25', 5: '26', 6: '27', 7: '28', 8: '7', 9: '8', 10: '9', 11: '10', 12: '11',
        13: '12', 14: '13', 15: '14', 16: '15', 17: '16', 18: '17', 19: '18', 20: '19', 21: '20', 22: '21', 23: '1',
        24: '2', 25: '3', 26: '4', 27: '5', 28: '6'
    },
    '00 SLABS - SL4A': {1: '1', 2: '2'},
    '00 SLABS - SL4B': {1: '2', 2: '1'},
    '00 SLABS - SL5A': {1: '1', 2: '2'},
    '00 SLABS - SL5B': {1: '2', 2: '1'},
    '00 SLABS - SL6A': {1: '1', 2: '2'},
    '00 SLABS - SL6B': {1: '2', 2: '1'},
    '00 SLABS - SL7A': {1: '1', 2: '2'},
    '00 SLABS - SL7B': {1: '2', 2: '1'},
    '00 SLABS - SL8A': {1: '1', 2: '2'},
    '00 SLABS - SL8B': {1: '2', 2: '1'},
    '00 BEAMS PC1': {1: '31', 2: '30', 3: '29', 4: '28', 5: '27', 6: '26', 7: '25', 8: '24', 9: '1', 10: '2', 11: '3', 12: '4',
            13: '5', 14: '6', 15: '7', 16: '23', 17: '22', 18: '21', 19: '20', 20: '19', 21: '18', 22: '17', 23: '16',
            24: '15', 25: '14', 26: '13', 27: '12', 28: '11', 29: '10', 30: '9', 31: '8'},
    '00 BEAMS PC2': {1: '2', 2: '1'},
    '00 PILES': {1: '99', 2: '34', 3: '33', 4: '98', 5: '35', 6: '32', 7: '97', 8: '36', 9: '31', 10: '96', 11: '37', 12: '30', 13: '95', 14: '38', 15: '29', 16: '94', 17: '39', 18: '28', 19: '93', 20: '40', 21: '27', 22: '92', 23: '41', 24: '26', 25: '91', 26: '42', 27: '25', 28: '8', 29: '59', 30: '74', 31: '1', 32: '66', 33: '67', 34: '2', 35: '65', 36: '68', 37: '3', 38: '64', 39: '69', 40: '4', 41: '63', 42: '70', 43: '5', 44: '62', 45: '71', 46: '6', 47: '61', 48: '72', 49: '7', 50: '60', 51: '73', 52: '90', 53: '43', 54: '24', 55: '89', 56: '44', 57: '23', 58: '88', 59: '45', 60: '22', 61: '87', 62: '46', 63: '21', 64: '86', 65: '47', 66: '20', 67: '85', 68: '48', 69: '19', 70: '84', 71: '49', 72: '18', 73: '83', 74: '50', 75: '17', 76: '82', 77: '51', 78: '16', 79: '81', 80: '52', 81: '15', 82: '80', 83: '53', 84: '14', 85: '79', 86: '54', 87: '13', 88: '78', 89: '55', 90: '12', 91: '77', 92: '56', 93: '11', 94: '76', 95: '57', 96: '10', 97: '75', 98: '58', 99: '9'},
'00 METAL FORMWORK' : {1: '99', 2: '34', 3: '33', 4: '98', 5: '35', 6: '32', 7: '97', 8: '36', 9: '31', 10: '96', 11: '37', 12: '30', 13: '95', 14: '38', 15: '29', 16: '94', 17: '39', 18: '28', 19: '93', 20: '40', 21: '27', 22: '92', 23: '41', 24: '26', 25: '91', 26: '42', 27: '25', 28: '8', 29: '59', 30: '74', 31: '1', 32: '66', 33: '67', 34: '2', 35: '65', 36: '68', 37: '3', 38: '64', 39: '69', 40: '4', 41: '63', 42: '70', 43: '5', 44: '62', 45: '71', 46: '6', 47: '61', 48: '72', 49: '7', 50: '60', 51: '73', 52: '90', 53: '43', 54: '24', 55: '89', 56: '44', 57: '23', 58: '88', 59: '45', 60: '22', 61: '87', 62: '46', 63: '21', 64: '86', 65: '47', 66: '20', 67: '85', 68: '48', 69: '19', 70: '84', 71: '49', 72: '18', 73: '83', 74: '50', 75: '17', 76: '82', 77: '51', 78: '16', 79: '81', 80: '52', 81: '15', 82: '80', 83: '53', 84: '14', 85: '79', 86: '54', 87: '13', 88: '78', 89: '55', 90: '12', 91: '77', 92: '56', 93: '11', 94: '76', 95: '57', 96: '10', 97: '75', 98: '58', 99: '9'},
'00 IN SITU CONCRETE - PILES' : {1: '99', 2: '34', 3: '33', 4: '98', 5: '35', 6: '32', 7: '97', 8: '36', 9: '31', 10: '96', 11: '37', 12: '30', 13: '95', 14: '38', 15: '29', 16: '94', 17: '39', 18: '28', 19: '93', 20: '40', 21: '27', 22: '92', 23: '41', 24: '26', 25: '91', 26: '42', 27: '25', 28: '8', 29: '59', 30: '74', 31: '1', 32: '66', 33: '67', 34: '2', 35: '65', 36: '68', 37: '3', 38: '64', 39: '69', 40: '4', 41: '63', 42: '70', 43: '5', 44: '62', 45: '71', 46: '6', 47: '61', 48: '72', 49: '7', 50: '60', 51: '73', 52: '90', 53: '43', 54: '24', 55: '89', 56: '44', 57: '23', 58: '88', 59: '45', 60: '22', 61: '87', 62: '46', 63: '21', 64: '86', 65: '47', 66: '20', 67: '85', 68: '48', 69: '19', 70: '84', 71: '49', 72: '18', 73: '83', 74: '50', 75: '17', 76: '82', 77: '51', 78: '16', 79: '81', 80: '52', 81: '15', 82: '80', 83: '53', 84: '14', 85: '79', 86: '54', 87: '13', 88: '78', 89: '55', 90: '12', 91: '77', 92: '56', 93: '11', 94: '76', 95: '57', 96: '10', 97: '75', 98: '58', 99: '9'},
}
# Map the name name of the model item ot the desired selection set
name_map = {'00 SLABS - SL1': 'SL1', '00 SLABS - SL2': 'SL2', '00 SLABS - SL3': 'SL3', '00 SLABS - SL4A': 'SL4A',
            '00 SLABS - SL4B': 'SL4B', '00 SLABS - SL5A': 'SL5A', '00 SLABS - SL5B': 'SL5B', '00 SLABS - SL6A': 'SL6A',
            '00 SLABS - SL6B': 'SL6B', '00 SLABS - SL7A': 'SL7A', '00 SLABS - SL7B': 'SL7B', '00 SLABS - SL8A': 'SL8A',
            '00 SLABS - SL8B': 'SL8B', '00 BEAMS PC1': 'PC1', '00 BEAMS PC2': 'PC2', '00 PILES': 'PILE',
            '00 METAL FORMWORK': 'FORMWORK','00 IN SITU CONCRETE - PILES': 'PLUG'}
chainages = {
    '12.00 P3 - BEACH RECLAMATION - FILL': {1: 'CH:+2300 to +2400', 2: 'CH:+2100 to +2300', 3: 'CH:+1900 to +2100',
                                            4: 'CH:+1700 to +1900', 5: 'CH:+1500 to +1700', 6: 'CH:+1300 to +1500',
                                            7: 'CH:+1100 to +1300', 8: 'CH:+900 to +1100', 9: 'CH:+700 to +900',
                                            10: 'CH:+500 to +700', 11: 'CH:+300 to +500', 12: 'CH:+000 to +300', },
    'BEACH SAND': {1: 'CH:+2300 to +2400', 2: 'CH:+2100 to +2300', 3: 'CH:+1900 to +2100', 4: 'CH:+1700 to +1900',
                   5: 'CH:+1500 to +1700', 6: 'CH:+1300 to +1500', 7: 'CH:+1100 to +1300', 9: 'CH:+700 to +900',
                   8: 'CH:+900 to +1100', 10: 'CH:+500 to +700', 11: 'CH:+300 to +500', 12: 'CH:+000 to +300', },
    '11.20 P3 - NORTH GROYNE AR': {1: 'CH: +140 to +150', 2: 'CH: +000 to +020', 3: 'CH: +020 to +040',
                                   4: 'CH: +040 to +060', 5: 'CH: +060 to +080', 6: 'CH: +080 to +100',
                                   7: 'CH: +100 to +120', 8: 'CH: +120 to +140'},
    '11.10 P3 - NORTH GROYNE QR': {5: 'CH: +140 to +150', 2: 'CH: +000 to +020', 1: 'CH: +020 to +040',
                                   3: 'CH: +040 to +060', 4: 'CH: +060 to +080', 6: 'CH: +080 to +100',
                                   7: 'CH: +100 to +120', 8: 'CH: +120 to +140'},
    '00 IN SITU CONCRETE - SLAB': {1 : '33%-67%', 2 : '67%-100%', 3 : '0-33%'}
}



doc.SelectionSets.Clear()

references = {}

root = doc.Models[0].RootItem

container = {}
for c in root.Children:
    # Create a dictionary with
    # {key: value} = {Root.DisplayName: [ModelItems of Root Children]}
    container[c.DisplayName] = [modelItem for modelItem in c.Children]

references = {}  # Stores the key:val pairs where key = Selection.Id and val is Model.Id
x = 0

for item in container.keys():
    for i, child in enumerate(container[item]):
        col = ModelItemCollection()
        col.Add(child)
        newsel = SelectionSet(col)

        if item in ordered_set.keys():
            name_ref = name_map[item] + '-' + ordered_set[item][i + 1]
            newsel.DisplayName = name_ref
            references[name_ref] = child.InstanceGuid.ToString()

        elif item in chainages.keys():
            name_ref =  item.split()[-1] + ' ' + chainages[item][i + 1]
            newsel.DisplayName = name_ref
            references[name_ref] = child.InstanceGuid.ToString()

        else:
            name_convention = item + '-' + str(i + 1)
            newsel.DisplayName = name_convention
            references[name_convention] = child.InstanceGuid.ToString()


        doc.SelectionSets.InsertCopy(0, newsel)
save_references(references)

