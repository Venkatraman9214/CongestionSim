# CongestionSim
This simulator is under development. Specifically built for congestion control simulation.
Congestion control evalutation---
In order to perform senstivity analysis of congestion control, we use a modified bin-packing algorithm that is evaluated in the code. 
Certain features like receive window limitations and Head of Line blocking will be examined in the future.

The modified bin-packing produces new request buffers dynamically. The heuristics works in the best-fit manner.


Before using this, create a topology generator specific to your experiment. It would be called as "toporeader" or "topoexec". Change the rand(in_value1, in_value2) values for specific uniform generation of sequences.
