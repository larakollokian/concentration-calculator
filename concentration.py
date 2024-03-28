'''
(c) @larakollokian 2024/03/24

Script for babig's chemistry problem
All volumes are in litres (L), and concentrations are in g/L.

How to use:

This script expects 3 arguments as input, in order, separated by spaces. They must be in the correct order and must be floating point 
values. There is no input verification, I made the assumption that you will use the script as intended after having read these docs. 

To run, input the following values in this order, in litres:

python3 concentration.py <syringe_volume> <concentrated_solution_container_volume> <diluted_solution_container_volume>

example:

python3 concentration.py 0.01 0.5 2

will give the following answer:

You will need to dilute 64.32 grams of solute into 0.5 litres of water. 
Afterwards, 0.01 litres of this solution diluted into a container of 2.0 
litres of water will have the recommended concentration of 0.64 g/L.

You are free to add default values for any of these variables, or make changes to the program. If you wish to make changes, I've left some
doctest strings, which you can run as follows to make sure all is good:

python3 concentration.py -v
'''
import sys
import doctest

RECOMMENDED_CONCENTRATION = 0.64

def concentration(solute_weight, solution_volume):
    '''
    solute_weight: weight of the solute in grams (g)
    solution_volume: final volume of the solution in litres (L)

    Returns the concentration of the solution in g/L

    >>> concentration(20, 3)
    6.666666666666667
    >>> concentration(3, 20)
    0.15
    '''
    return solute_weight / solution_volume

def weight_of_solute_in_concentration(solution_volume, concentration):
    '''
    volume: volume of the final concentrated solution in litres (L)
    concentration: desired concentration of the solution in g/L

    Returns the weight of solute necessary to have the recommended concentration in the provided volume following the C=n/V formula

    >>> weight_of_solute_in_concentration(0.5, 128.64)
    64.32
    '''
    return concentration * solution_volume

def dilution(concentration_a=None, volume_a=None, concentration_b=None, volume_b=None):
    '''
    concentration_a: concentration of solution a to be diluted in g/L
    volume_a: volume of solution a to be diluted in L
    concentration_b: desired final concentration of solution b after dilution in g/L
    volume_b: desired final volume of solution b after dilution in g/L

    This function has 4 params but expects one to be None. The result will be the value of the blank 
    param following the C1*V1=C2*V2 formula

    >>> dilution(None, 0.01, 0.64, 2.01)
    128.64
    >>> dilution(128.64, None, 0.64, 2.01)
    0.01
    >>> dilution(128.64, 0.01, None, 2.01)
    0.64
    >>> dilution(128.64, 0.01, 0.64, None)
    2.01
    '''
    if concentration_a == None:
        return (concentration_b * volume_b) / volume_a
    elif volume_a == None:
        return (concentration_b * volume_b) / concentration_a
    elif concentration_b == None:
        return (concentration_a * volume_a) / volume_b
    else:
        return (concentration_a * volume_a) / concentration_b

def calculate(syringe_volume, concentrated_solution_container_volume, diluted_solution_container_volume):
    '''
    syringe_volume: volume of the syringe (i.e. volume of the concentrated solution to be diluted) in litres (L)
    concentrated_solution_container_volume: volume of the concentrated solution to be diluted in litres (L)
    diluted_solution_container_volume: volume of the final diluted solution's contrainer in litres (L)

    Returns the weight of solute required to be dissolved into a solution of volume concentrated_solution_container_volume. A sample
    of this solution of volume syringe_volume then diluted into a solution of volume diluted_solution_container_volume will have the 
    desired RECOMMENDED_CONCENTRATION.

    >>> calculate(0.01, 0.5, 2)
    64.32
    >>> calculate(0.00446, 0.5, 1)
    72.0688789237668
    >>> calculate(0.0121, 0.6, 1)
    32.119537190082646
    '''
    final_solution_volume = syringe_volume + diluted_solution_container_volume
    concentration_for_dilution = dilution(None, syringe_volume, RECOMMENDED_CONCENTRATION, final_solution_volume)
    return weight_of_solute_in_concentration(concentrated_solution_container_volume, concentration_for_dilution)

def main():
    if sys.argv[1] == "-v":
        return

    syringe_volume = float(sys.argv[1])
    concentrated_solution_container_volume = float(sys.argv[2])
    diluted_solution_container_volume = float(sys.argv[3])

    solute_weight = calculate(syringe_volume, concentrated_solution_container_volume, diluted_solution_container_volume)
    solution = f'''
    You will need to dilute {solute_weight} grams of solute into {concentrated_solution_container_volume} litres of water. 
    Afterwards, {syringe_volume} litres of this solution diluted into a container of {diluted_solution_container_volume} 
    litres of water will have the recommended concentration of {RECOMMENDED_CONCENTRATION} g/L.
    '''

    print(solution)

if __name__ == "__main__":
    doctest.testmod()
    main()