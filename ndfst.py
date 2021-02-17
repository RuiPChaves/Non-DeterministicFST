'''
    File name: ndfst.py
    Author: Rui P. Chaves
    Date created: 10/Feb/2021
    Python version: 3.6
'''

# NFST(startState,FinalStates,TransitionTable,InputToProcess)
# =============================================================================================================
def NFST(qS,F,T,Input):
    # Initialize search stack with dummy initial state transition (input and output slots will work as stacks)
    StepLoop = [['','','',qS]]
    # Initialize temporary search list
    TStepLoop = []
    # Search for epsilon transitions before any transitions are used
    loop = True
    while loop:
        OldListlen = len(StepLoop)
        for i in range(0,len(StepLoop)):       
         #Find all epsilon transitions
            StepLoop.extend([(Cq,I,StepLoop[i][2]+O,Nq) for (Cq,I,O,Nq) in T if (Cq in StepLoop[i][3] and I == '' and (Cq,I,StepLoop[i][2]+O,Nq) not in StepLoop)])             
        if OldListlen == len(StepLoop):
            loop = False                                 
    # Scan input 
    for j in Input:
        for i in range(0,len(StepLoop)):   
            # Extend temporary search list with accessible states and append prior input token and priot output token to current token                     
            TStepLoop.extend([(Cq,StepLoop[i][1]+I,StepLoop[i][2]+O,Nq) for (Cq,I,O,Nq) in T if (Cq in StepLoop[i][3] and j == I)])                                           
        # Promote temporary search list as new search list to loop over            
        StepLoop = TStepLoop  
        # Reinitialize temporary search list
        TStepLoop = []
        # Search for epsilon transitions after new transitions are added
        loop = True
        while loop:
            OldListlen = len(StepLoop)
            for i in range(0,len(StepLoop)):       
                # Find all epsilon transitions
                StepLoop.extend([(Cq,I,StepLoop[i][2]+O,Nq) for (Cq,I,O,Nq) in T if (Cq in StepLoop[i][3] and I == '' and (Cq,I,StepLoop[i][2]+O,Nq) not in StepLoop)])             
            if OldListlen == len(StepLoop):
                loop = False                                           
    # Extract only traversals that reached a final state
    output = {s[2] for s  in StepLoop if s[3] in F}
    return output
# =============================================================================================================


# Define FST (Pinyin numerals to Hindu-Arabic numerals; tokenized)
# =============================================================================================================
#start state
S = 'q0'

#final states
F = ['q1','q3']

#transitions (current_state, input, output, new_state)
T = [ ('q0','er4','2','q1'),
      ('q0','san1','3','q1'),
      ('q0','si4','4','q1'),
      ('q0','wu3','5','q1'),
      ('q0','liu4','6','q1'),
      ('q0','qi1','7','q1'),
      ('q0','ba1','8','q1'),
      ('q0','jiu3','9','q1'),
      ('q1','shi2','','q2'),
      ('q2','','0','q3'),
      ('q2','yi1','1','q3'),
      ('q2','er4','2','q3'),
      ('q2','san1','3','q3'),
      ('q2','si4','4','q3'),
      ('q2','wu3','5','q3'),
      ('q2','liu4','6','q3'),
      ('q2','qi1','7','q3'),
      ('q2','ba1','8','q3'),
      ('q2','jiu3','9','q3'),
      ('q0','shi2','1','q2'),
      ('q0','yi1','1','q3'),
      ('q0','bai3','100','q3'),
      ('q0','ling2','0','q3')]


# Define input as token list
# =============================================================================================================
Input = ['jiu3','shi2','liu4']     

# Run NFST
# =============================================================================================================
print(NFST(S,F,T,Input))
