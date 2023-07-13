arr: WORD 0x100
dimN: WORD 2
dimM: WORD 2
dimElement: WORD 2
DEREF: WORD ?
X_1: WORD ?
X_2: WORD ?
i: WORD 0
j: WORD 0
STARTold:
    LD i
    CMP dimN
    BZS EXT
    LD j
    CMP dimM
    BZS addI
    LD i
    PUSH
    LD j
    PUSH
    CALL GET_ADDR
    ST DEREF
    LD (DEREF)+
    ST X_1
    LD (DEREF)
    ST X_2
    LD (j)+
    JUMP START
addI:
    LD (i)+
    LD #0
    ST j
    JUMP START
EXT:
    HLT
MUL: ; MUL(a,b) = a*b
        LD &1
        ADD #1
        ST &1
        CLA
MUL_LP: LOOP &1
        JUMP MUL_ACT
        JUMP MUL_RT
MUL_ACT:ADD &2
        JUMP MUL_LP
MUL_RT: SWAP
        ST &2
        POP
        SWAP
        POP
        RET
GET_ADDR: ; GET_ADDR(i, j) = a[i][j]
        LD &2
        PUSH
        LD $dimN
        PUSH
        CALL MUL ; i*dimL
        ADD &1 ;+j
        PUSH
        LD $dimElement
        PUSH
        CALL MUL
        ADD $arr ;+array
        SWAP
        ST &2
        POP
        SWAP
        POP
        RET ; i*l+j+arr

ADD32: ; ADD32(a_1(6), a_2(5), b_1(4), b_2(3)) -> x_1, x_2
    LD &3
    ADD &1
    ST &3
    LD &4
    ADC &2
    ST &4
    SWAP
    ST &2
    POP
    POP
    CLA
    RET
SUB32_RET: WORD ?
SUB32: ; SUB32(a_1, a_2, b_1, b_2)
    LD &1
    BZS SUB32_B1_NEG
    NEG
    ST &1
    LD &2
    NOT
    ST &2
    JUMP SUB32_EXT
SUB32_B1_NEG:
    LD &2
    NEG
    ST &2
SUB32_EXT:
    POP
    ST $SUB32_RET
    CALL ADD32
    LD $SUB32_RET
    PUSH
    RET
DEREF1: WORD ?
DEREF2: WORD ?
START:
    LD #0
    PUSH
    LD #0
    PUSH
    CALL GET_ADDR
    ST DEREF1
    LD #0
    PUSH
    LD #1
    PUSH
    CALL GET_ADDR
    ST DEREF2
    LD (DEREF1)+
    PUSH
    LD (DEREF1)
    PUSH
    LD (DEREF2)+
    PUSH
    LD (DEREF2)
    PUSH
    CALL SUB32
    POP
    ST $X_2
    POP
    ST $X_1
    HLT
; x_1
; x_2
; RET

ORG 0x100

WORD 0x1010 ; 0 0
WORD 0x1111

WORD 0x2030 ; 0 1
WORD 0xF323

WORD 0x05FF ; 1 0
WORD 0xF3FF

WORD 0xA000 ; 1 1
WORD 0x1634