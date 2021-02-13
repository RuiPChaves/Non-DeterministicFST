# ====================================================================
# Define NFST (Pinyin numerals to Hindu-Arabic numerals; tokenized)
# ====================================================================

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
      ('q2','san1','3','q1'),
      ('q2','si4','4','q1'),
      ('q2','wu3','5','q1'),
      ('q2','liu4','6','q1'),
      ('q2','qi1','7','q1'),
      ('q2','ba1','8','q1'),
      ('q2','jiu3','9','q3'),
      ('q0','shi2','1','q2'),
      ('q0','yi1','1','q3'),
      ('q0','bai3','100','q3'),
      ('q0','ling2','0','q3')]

# Define input as token list (Pinyin numbers correspond to tones)
Input = ['jiu3','shi2','liu4']     

# Run NFST
tNFST(S,F,T,Input)
