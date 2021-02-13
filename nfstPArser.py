'''
    File name: nfst.py
    Author: Rui P. Chaves
    Date created: 10/Feb/2021
    Python version: 3.6
'''

# =============================================== 
# Token-level NFST Parser
# =============================================== 

# tNFST(startState,FinalStates,TransitionTable,InputToProcess)
def tNFST(qS,F,T,Input):
    # Initialize search stack with dummy initial state transition (input and output slots will work as stacks)
    StepLoop = [['','','',qS]]
    # Initialize temporary search list
    TStepLoop = []
    # For every token in the input
    for j in Input:
        # For every transition in the list
        for i in range(0,len(StepLoop)):   
            # Extend temporary search list with accessible states and append prior input token and priot output token to current token         
            TStepLoop.extend([(Cq,StepLoop[i][1]+I,StepLoop[i][2]+O,Nq) for (Cq,I,O,Nq) in T if (Cq in StepLoop[i][3] and j == I)])
        # Promote temporary search list as new search list to loop over            
        StepLoop = TStepLoop  
        # Reinitialize temporary search list
        TStepLoop = []          
    # Output is a set of all output tokens in accessible final states    
    output = {s[2] for s  in StepLoop if s[3] in F}
    return output
