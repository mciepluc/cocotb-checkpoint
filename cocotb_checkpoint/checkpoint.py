'''Copyright (c) 2024, MC ASIC Design Consulting
All rights reserved.

Author: Marek Cieplucha, https://github.com/mciepluc

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met (The BSD 2-Clause 
License):

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL POTENTIAL VENTURES LTD BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. '''

"""
The checkpointing logic

"""

#This is a stuff to do a checkpointing in the testbench.
#Checkpointing is storing the DUT state during simulation and loading it 
#later as a starting point for further simulation. Very useful stuff, 
#for example, if needed to initialize DUT and then start various tests 
#from the after-init state. This feature is available in some commercial 
#simulators but it is difficult to use it as a part of the test logic. 
#This exaplme allows for using checkpointing during the test in Cocotb.

from cocotb.handle import *

checkpoint_hier = []

#this function must be called prior to creating any checkpoint
def get_checkpoint_hier(entity):
    handle = HierarchyObject(entity._handle, entity._path)
    #iterator = simulator.package_iterate(entity._handle, simulator.OBJECTS)
    for child in handle:
        
        hdl = SimHandle(child._handle, child._path)
        
        if type(hdl) is HierarchyObject:
            get_checkpoint_hier(hdl)
        elif type(hdl) is ModifiableObject:
            checkpoint_hier.append(hdl)            
    
#returns a created checkpoint
def checkpoint():
    checkpoint_data = {}
    for reg in checkpoint_hier:
        checkpoint_data[reg] = reg.value
    
    return checkpoint_data

#restores a checkpoint
def restore(checkpoint_data):
    for reg in checkpoint_data:
        reg.value = checkpoint_data[reg]
