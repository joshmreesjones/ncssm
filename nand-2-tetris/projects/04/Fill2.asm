(MAIN)
	@KBD
	D=M
	@KDOWN
	D;JGT

(KDOWN)
	@index
	M=0

	(FILL)
		// 

		@FILL
		0;JMP

(KUP)
	@index
	M=0

	(CLEAR)
		@index
		D=M
		@8096

		@CLEAR
		0;JMP