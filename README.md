# Syntax-Analyzer(bottom-up parser)
The goal of the project is to implement a syntax analyzer (a.k.a., parser) as we’ve 
learned. More specifically, you will implement the syntax analyzer for a simplified C programming 
language with the following context free grammar G within python3; 



CFG G: 
01:				CODE→VDECL	CODE	|	FDECL	CODE	|	ϵ 
02:				VDECL→vtype	id	semi 
03:				FDECL→vtype	id	lparen	ARG	rparen	lbrace	BLOCK	𝐑𝐄𝐓𝐔𝐑𝐍	rbrace 
04:				ARG→vtype	id	MOREARGS	|	ϵ 
05:				MOREARGS→comma	vtype	id	MOREARGS	|	ϵ 
06:				BLOCK→STMT	BLOCK	|	ϵ 
07:				STMT→VDECL	|	id	assign	RHS	semi 
08:				STMT→if	lparen	COND	rparen	lbrace	BLOCK	rbrace	else	lbrace	BLOCK	rbrace 
09:				STMT→while	lparen	COND	rparen	lbrace	BLOCK	rbrace	|	FCALL	semi 
10:				RHS→EXPR	|	FCALL	|	literal 
11:				EXPR→TERM	addsub	EXPR	|	TERM 
12:				TERM→FACTOR	multdiv	TERM	|	FACTOR 
13:				FACTOR→lparen	EXPR	rparen	|	id	|	num 
14:				FCALL→id	lparen	ARG	rparen 
15:				COND→FACTOR	comp	FACTOR 
𝟏𝟔:				𝐑𝐄𝐓𝐔𝐑𝐍→𝐫𝐞𝐭𝐮𝐫𝐧	𝐅𝐀𝐂𝐓𝐎𝐑	𝐬𝐞𝐦𝐢 
 
#### Terminals (18) 
1. vtype for the types of variables and functions 
2. num for signed integers 
3. literal for literal strings 
4. id for the identifiers of variables and functions 
5. if, else, while, and return for if, else, while, and return statements respectively 
6. addsub for + and - arithmetic operators 
7. multdiv for * and / arithmetic operators 
8. assign for assignment operators 
9. comp for comparison operators 
10. semi and comma for semicolons and commas respectively 
11. lparen, rparen, lbrace, and rbrace for (, ), {, and } respectively 
#### Non-terminals (14) 
CODE, VDECL, FDECL, ARG, MOREARGS, BLOCK, STMT, RHS, EXPR, TERM, FACTOR, COND, 
FCALL, RETURN 
#### Start symbol: CODE 
 
#### Descriptions 
###### The given CFG G is not ambiguous and non-left recursive.  
###### But, left factoring is required if you want to implement a top-down parser 
###### Source codes include zero or more declarations of functions and variables (CFG line 1) 
###### Variables are always declared without initialization (CFG line 2) 
###### Functions can have zero or more input arguments (CFG line 3 ~ 5) 
###### Function blocks include zero or more statements (CFG line 6) 
###### There are five types of statements: 1) variable declarations, 2) assignment operations, 3) if
###### else statements, 4) while statements, and 5) function calls (CFG line 7 ~ 9) 
###### if-else statements without else are not allowed (CFG line 8) 
###### The right hand side of assignment operations can be classified into three types; 1) arithmetic 
###### operations (expressions), 2) function calls, and 3) literal strings (CFG line 10 ~ 14) 
###### Arithmetic operations are the combinations of +, -, *, / operators (CFG line 11 ~ 13)


If you want to implement a bottom-up parser, then you are required 1) to construct an NFA 
for recognizing viable prefixes of G, 2) to convert the NFA into a DFA, 3) to compute follow 
sets, 4) to construct a SLR parsing table, and 5) to implement a SLR parser. 
 
 
