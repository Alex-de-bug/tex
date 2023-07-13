arr: WORD 0x100
dimN: WORD 2
dimM: WORD 2
dimL: WORD 2
DEREF: WORD ?
i: WORD 0
j: WORD 0
k: WORD 0
START:
    LD i
    CMP dimN
    BZS EXT
    LD j
    CMP dimM
    BZS addI
    LD k
    CMP dimM
    BZS addJ
    LD i
    PUSH
    LD j
    PUSH
    LD k
    PUSH
    CALL GET
    ST DEREF
    LD (k)+
    JUMP START
addI:
    LD (i)+
    LD #0
    ST j
    JUMP START
addJ:
    LD (j)+
    LD #0
    ST k
    JUMP START
EXT:
    HLT