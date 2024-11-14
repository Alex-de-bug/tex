dimL: WORD 4
dimM: WORD 4
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


;func get[i][j] i-&2 j-&1; result( dimL*j+i+address ) -> AC
GET: 
    PUSH
    PUSH
    LD &4
    ST &0
    LD $dimL
    ST &1
    CALL MUL
    ADD &1
    ADD $addr

    SWAP
    ST &2
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
DEREF: WORD ?
START:
    ;check borders N != 1
    LD J 
    BMI CHECK_BORDERS
    LD I 
    BMI CHECK_BORDERS
    ;get list element
    LD I 
    PUSH
    LD J 
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
    LD J 
    DEC
    ST J 
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
    CMC
    LD I
    BEQ ENDING
    DEC
    ST I 
    LD #3
    ST J
    JUMP START
ENDING:
    LD ANS
    HLT



org 0x140
WORD 0x06
WORD 0x01 ;MIN
WORD 0x02
WORD 0x03

WORD 0x15
WORD 0x14
WORD 0x12 ;MIN
WORD 0x13

WORD 0x2A
WORD 0x27
WORD 0x29
WORD 0x23 ;MIN

WORD 0x38
WORD 0x34
WORD 0x13 ;MIN
WORD 0x67

;MAX 23

