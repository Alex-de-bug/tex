dimL: WORD 4
dimM: WORD 4
dimN: WORD 4
addr: WORD 0x140

; func a*b -> AC
MUL: 
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


;func get[i][j][k] i-&3 j-&2 k-&1; result( dimL*dimM*i + dim*j + k + address ) -> AC
GET: 
    PUSH
    PUSH
     
    LD $dimL
    ST &1
    LD $dimM
    ST &0
    CALL $MUL
    PUSH
    LD &4
    PUSH
    CALL $MUL
    ST &3
    ;dimL*dimM*i -> STACK &(-1)

    LD &2
    PUSH
    LD $dimM
    PUSH
    CALL $MUL
    ;dim*j

    ADD &3
    ADD &1
    ADD addr
    ;dimL*dimM*i + dimM*j + k + address

    SWAP
    ST &3
    POP
    SWAP
    POP
    SWAP
    POP
    RET

org 0x100
MAX: WORD 0x7FF
ANS: WORD 0x0
X: WORD 0x7FF
I: WORD 3
J: WORD 3
K: WORD 3
DEREF: WORD ?
START:
    ;check borders N != 1
    LD K
    BMI CHECK_BORDERS
    ;get list element
    LD I 
    PUSH
    LD J 
    PUSH
    LD K 
    PUSH
    CALL $GET
    ST DEREF
    LD (DEREF)
    ;begin action on element
    CMP X
    BLO EPILOG
    ST X
    ;end action on element
EPILOG:
    ;preparing indexes
    LD K 
    DEC
    ST K 
    JUMP START

CHECK_BORDERS:
    ;begin intermediate calculation
    LD X
    CMP ANS
    BHIS BODY_CHECK
    ST ANS
    BODY_CHECK:
    LD MAX
    ST X
    ;end intermediate calculation

    LD K 
    INC
    ADD J 
    ADD I
    BEQ ENDING    

    LD #3
    ST K

    LD J 
    BEQ CHECK_I
    DEC
    ST J
    JUMP START

    CHECK_I:
    LD #3
    ST J
    LD I 
    DEC
    ST I
    JUMP START
    
ENDING:
    LD ANS
    HLT



org 0x140

WORD 0x000
WORD 0x001 
WORD 0x002
WORD 0x003

WORD 0x010
WORD 0x011
WORD 0x012 
WORD 0x013

WORD 0x020
WORD 0x021
WORD 0x022 
WORD 0x023

WORD 0x030
WORD 0x031
WORD 0x032 
WORD 0x033


WORD 0x100
WORD 0x101 
WORD 0x102
WORD 0x103

WORD 0x110
WORD 0x111
WORD 0x112 
WORD 0x113

WORD 0x120
WORD 0x121
WORD 0x122 
WORD 0x123

WORD 0x130
WORD 0x131
WORD 0x132 
WORD 0x133


WORD 0x200
WORD 0x201 
WORD 0x202
WORD 0x203

WORD 0x210
WORD 0x211
WORD 0x212 
WORD 0x213

WORD 0x220
WORD 0x221
WORD 0x222 
WORD 0x223

WORD 0x230
WORD 0x231
WORD 0x232 
WORD 0x233


WORD 0x300
WORD 0x301 
WORD 0x302
WORD 0x303

WORD 0x310
WORD 0x311
WORD 0x312 
WORD 0x313

WORD 0x320
WORD 0x321
WORD 0x322 
WORD 0x323

WORD 0x330
WORD 0x331
WORD 0x332 
WORD 0x333

;MAX 23

