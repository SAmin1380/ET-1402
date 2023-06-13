import json
import os



def printActionDetails(action, file):
    for item in action:
        file.write(f'"{item}" is an action.\n')
    file.write('\n')


def printMechanismDetails(mechanism, file):
    for k,v in mechanism.items():
        if type(v) == str:
            file.write(f'"{k}" if "{v}"\n')
        
        elif type(v) == list:
            file.write(f'"{k}" if ')
            for item in v[0:len(v) - 1:]:
                file.write(f'"{item}" or ')
            lastItem = v[len(v) - 1]
            file.write(f'"{lastItem}"\n')
    file.write('\n')


def findMax(utility):
    maximum = float('-inf')
    key = None

    for k, v in utility.items():
        if v > maximum:
            maximum = v
            key = k
    
    return key, maximum


def printUtilityDetails(utility, keyM, valueM, file):
    file.write(f'"{keyM}" is good\n')
    for k, v in utility.items():
        if v != valueM:
            file.write(f'"{k}" is bad\n')
    file.write('\n')


def printIntentionDetails(mechanism, action, file):
    intentionConseq = []
    for k,v in mechanism.items():
        if type(v) == str:
            if v == action:
                intentionConseq.append(k)
        elif type(v) == list:
            if action in v:
                intentionConseq.append(k)
    
    for k,v in mechanism.items():
        if type(v) == str:
            if v in intentionConseq and not k in intentionConseq:
                intentionConseq.append(k)
        elif type(v) == list:
            for item in v:
                if v in intentionConseq and not k in intentionConseq:
                    intentionConseq.append(k)
    
    file.write(f'The intention of this problem for action "{action}", consequences: ')
    for item in intentionConseq[0:len(intentionConseq) - 1:]:
        file.write(f'"{item}" --> ')
    file.write(f'"{intentionConseq[len(intentionConseq) - 1]}".\n')


def printSenarioOutput(file):
    
    # load input file
    f = open(f'input/{file}')
    data = json.load(f)


    # create file for output
    fileName = file[:-5:]
    newF = open(f'output/{fileName}_output.txt', 'w')
    des = data['description']
    newF.write(f'{des}:\n\n')


    # write action of problem
    newF.write(f'Actions:\n')
    action = data['actions']
    printActionDetails(action, newF)


    # write mechanisms of problem
    newF.write(f'Mechanisms:\n')
    mechanism = dict(data['mechanisms'])
    printMechanismDetails(mechanism, newF)


    # write Utilities of problem
    newF.write(f'Utilities:\n')
    utility = dict(data['utilities'])
    key, maximum = findMax(utility)
    printUtilityDetails(utility, key, maximum, newF)



    # write best choise of problem
    key, maximum = findMax(utility)
    newF.write(f'The best choise is "{key}" with {maximum} score.\n\n')


    # write intention of problem
    printIntentionDetails(mechanism, key, newF)



path = os.listdir('input')
path = sorted(path)

for file in path:
    printSenarioOutput(file)

print('Outputs save successfully in output directory...')
