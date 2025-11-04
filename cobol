       IDENTIFICATION DIVISION.
       PROGRAM-ID.  JC45A02.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INFILE  ASSIGN TO 'JC45A01'
               ORGANIZATION IS SEQUENTIAL.
           SELECT OUTFILE ASSIGN TO 'JC4SA02'
               ORGANIZATION IS SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  INFILE
           RECORD CONTAINS 80 CHARACTERS
           RECORDING MODE IS F
           BLOCK CONTAINS 0 RECORDS.
       01  IN-REC.
           05  IN-SALE-NO        PIC X(10).
           05  FILLER            PIC X(70).

       FD  OUTFILE
           RECORD CONTAINS 80 CHARACTERS
           RECORDING MODE IS F
           BLOCK CONTAINS 0 RECORDS.
       01  OUT-REC.
           05  OUT-SALE-NO       PIC X(10).
           05  OUT-PLC-CTM-NO    PIC X(10).
           05  OUT-KND-CD        PIC X(05).
           05  OUT-MNG-AGT-NO    PIC X(10).
           05  OUT-PMM-AM        PIC 9(13)V99.
           05  FILLER            PIC X(32).

       WORKING-STORAGE SECTION.
       01  SQLCODE              PIC S9(9) COMP.
       01  WS-EOF               PIC X VALUE 'N'.
           88  END-OF-FILE      VALUE 'Y'.
           88  NOT-END-OF-FILE  VALUE 'N'.

       EXEC SQL
           INCLUDE CBVMFA01
       END-EXEC.

       EXEC SQL
           DECLARE C1 CURSOR FOR
           SELECT SALE_NO,
                  PLC_CTM_NO,
                  KND_CD,
                  MNG_AGT_NO,
                  PMM_AM
           FROM CBVMFA01
           WHERE SALE_NO = :IN-SALE-NO
       END-EXEC.

       PROCEDURE DIVISION.
       MAIN-LOGIC SECTION.
       0000-MAIN.
           PERFORM 1000-INITIALIZE.
           PERFORM 2000-PROCESS UNTIL END-OF-FILE.
           PERFORM 3000-FINALIZE.
           STOP RUN.

       1000-INITIALIZE.
           OPEN INPUT INFILE
                OUTPUT OUTFILE.
           PERFORM 1100-READ-INPUT.
           EXEC SQL
               CONNECT TO :WS-DB2-ENV
           END-EXEC.
           EXIT.

       1100-READ-INPUT.
           READ INFILE
               AT END
                   SET END-OF-FILE TO TRUE
           END-READ.
           EXIT.

       2000-PROCESS.
           IF NOT-END-OF-FILE
              PERFORM 2100-DB2-SELECT
              PERFORM 2200-WRITE-OUTPUT
              PERFORM 1100-READ-INPUT
           END-IF.
           EXIT.

       2100-DB2-SELECT.
           EXEC SQL
               SELECT SALE_NO,
                      PLC_CTM_NO,
                      KND_CD,
                      MNG_AGT_NO,
                      PMM_AM
               INTO :OUT-SALE-NO,
                    :OUT-PLC-CTM-NO,
                    :OUT-KND-CD,
                    :OUT-MNG-AGT-NO,
                    :OUT-PMM-AM
               FROM CBVMFA01
               WHERE SALE_NO = :IN-SALE-NO
           END-EXEC.
           IF SQLCODE NOT = 0
              DISPLAY 'DB2 SELECT FAILED, SALE_NO=' IN-SALE-NO
              DISPLAY 'SQLCODE=' SQLCODE
           END-IF.
           EXIT.

       2200-WRITE-OUTPUT.
           WRITE OUT-REC.
           EXIT.

       3000-FINALIZE.
           CLOSE INFILE OUTFILE.
           EXEC SQL
               COMMIT
           END-EXEC.
           EXIT.
