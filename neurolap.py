import numpy as np
import neurolab as nl
target=[
         [0, 0, 1, 0, 0, #A
         0, 1, 0, 1, 0, 
         1, 0, 0, 0, 1, 
         1, 1, 1, 1, 1, 
         1, 0, 0, 0, 1],

         [1, 0, 0, 0, 1, #V
          0, 1, 0, 1, 0, 
          0, 1, 0, 1, 0, 
          0, 0, 1, 0, 0, 
          0, 0, 0, 0, 0],

        [1, 1, 1, 1, 1, #Z
         0, 0, 0, 1, 0, 
         0, 0, 1, 0, 0, 
         0, 1, 0, 0, 0, 
         1, 1, 1, 1, 1],

        [1, 0, 0, 1, 0,#K
         1, 0, 1, 0, 0,
         1, 1, 0, 0, 0, 
         1, 0, 1, 0, 0, 
         1, 0, 0, 1, 0],
]
# N E R O
target1 =  [
          [1,0,0,0,1,#N
           1,1,0,0,1,
           1,0,1,0,1,
           1,0,0,1,1,
           1,0,0,0,1],

          [1,1,1,1,1,#E
           1,0,0,0,0,
           1,1,1,1,1,
           1,0,0,0,0,
           1,1,1,1,1],

          [1,1,1,1,0,#R
           1,0,0,0,1,
           1,1,1,1,0,
           1,0,0,1,0,
           1,0,0,0,1],

          [0,1,1,1,0,#O
           1,0,0,0,1,
           1,0,0,0,1,
           1,0,0,0,1,
           0,1,1,1,0]]
target2=[
        [ 0, 1, 1, 1, 0, #J
          0, 0, 1, 0, 0, 
          0, 0, 1, 0, 0, 
          1, 0, 1, 0, 0, 
          1, 1, 1, 0, 0],
          [ 1, 0, 0, 0, 1, #H
            1, 0, 0, 0, 1, 
            1, 1, 1, 1, 1, 
            1, 0, 0, 0, 1, 
            1, 0, 0, 0, 1]


]

chars=['A','V','Z','K']
chars1 = ['N', 'E', 'R', 'O']
chars2=['J','H']

def hop(xtarget,xchars):

      target = np.asfarray(xtarget)
      target[target == 0] = -1

      # Create and train network
      net = nl.net.newhop(target)

      output = net.sim(target)
      print("Test on train samples:")
      for i in range(len(target)):
          print(xchars[i], (output[i] == target[i]).all())


      test =np.asfarray([1, 1, 1, 1, 0, #Z
         0, 0, 0, 1, 0, 
         0, 0, 1, 0, 0, 
         0, 1, 1, 0, 0, 
         1, 1, 1, 1, 1])
      test[test==0] = -1
      out = net.sim([test])
      for i in range(len(target)):
        if((out[0] == target[i]).all()):
          test[test==-1] = 0
          print(test[0:5])
          print(test[5:10])
          print(test[10:15])
          print(test[15:20])
          print(test[20:25])
          print("the char is :-",xchars[i])


hop(target,chars)
hop(target1,chars1)
hop(target2,chars2)