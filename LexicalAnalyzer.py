# File name: Lexer.py
# Student Number: 20166450
# Student Name: YoungMin Kim


#define TOKENS based on requirements.
keyword = ['return','RETURN' , 'WHILE','while','ELSE' ,'else','IF', 'if']
type1 = ['int','INT']
type2 = ['char','CHAR']
number=['0','1','2','3','4','5','6','7','8','9']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
operator=['=','<','>','<=','>=','==','!=']
addsub=['+','-']
multdiv=['*','/']
terminate_symbol=[';']
white_space=[ '\n' , '\t',' ']
pair_symbol=['{','}','(',')']
comma=[',']

#Combine all of Tokens which i defined.
KEYWORDS = addsub+multdiv+terminate_symbol+pair_symbol+keyword+type1+comma+type2+operator+white_space


lexeme=''
blank=' '

# Function of True, False based on following dfa which is accepted. or not.
def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        if c in transitions[state].keys():
             state = transitions[state][c]
        else:
            return bool(0)
    b= state in accepting
    return b

#Integer DFA
Integer_dfa = {0:{'0':3,'-':1, '1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2},
               1:{'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2, '8':2,'9':2},
               2:{'0':2,'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2, '8':2,'9':2},
               3:{}}
#Literal DFA
Literal_dfa={ 0:{'"':1},
              1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                 'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1,
                 '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'A':1,'B':1,'C':1,
                 'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'M':1,'N':1,'0':1,'P':1,'Q':1,
                 'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1,'\n':1,'\t':1,' ':1,'"':2},
              2:{}}

#Identifier DFA
Identifier_dfa={ 0:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                    'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1},
                 1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                    'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1,
                    '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'A':1,'B':1,'C':1,
                    'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'M':1,'N':1,'0':1,'P':1,'Q':1,
                    'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1}}

#open the file
file = open('allG_test.c','r')
str=file.read()
print(type(str))

#save it on the test.out
fileout= open('allG_test.out','w')
print("    <Lexical Analyzer Table>    ")
print("________________________________")

#i is index of 'str' and char is value of 'str' about index.
for i,char in enumerate(str):
    #Not to show whit_space in lexical table.
    if char not in white_space:
        lexeme += char

    #to prevent an error
    if (i+1) < len(str):
        #This is not to confuse about each comparison_operators
        if (str[i] in operator) and str[i + 1] == '=':
            continue
        #Keyword is all of tokens.
        elif str[i+1] == blank or str[i+1] in KEYWORDS or lexeme in KEYWORDS :

            #Devide Tokens more specific.
            #Print and save it as a Token's name.
            if lexeme in type1:
                a='VTYPE'
                print(a)
            elif lexeme in type2:
                a='VTYPE'
                print(a)
            elif lexeme == 'return':
                a='RETURN'
                print(a)
            elif lexeme == '(':
                a='LPAREN'
                print(a)
            elif lexeme == ')':
                a='RPAREN'
                print(a)
            elif lexeme == '{':
                a='LBRACE'
                print(a)
            elif lexeme == '}':
                a='RBRACE'
                print(a)
            elif lexeme == '=':
                a='ASSIGN'
                print(a)
            elif lexeme == 'while':
                a ='WHILE'
                print(a)
            elif lexeme == 'else':
                a ='ELSE'
                print(a)
            elif lexeme == 'if':
                a ='IF'
                print(a)
            #Use Integer DFA
            elif accepts(Integer_dfa,0,{2}|{3},lexeme):
                a='INTEGER'
                print(a)
            #Use Literal DFA
            elif accepts(Literal_dfa,0,{2},lexeme):
                a='LITERAL'
                print(a)
            #Use Identifier DFA
            elif accepts(Identifier_dfa, 0, {1}, lexeme):
                a='IDENTIFIER'
                print(a)
            #This is additional code for an error that i've found.
            elif str[i] == '-':
                d = i
                while str[d] == blank:
                    d -= 1
                if str[d] in operator or addsub:
                    continue
            elif lexeme in addsub:
                a='ADDSUB'
                print(a)
            elif lexeme in multdiv:
                a='MULTDIV'
                print(a)
            elif lexeme in operator:
                a='COMPARISON'
                print(a)
            elif lexeme == ',':
                a='COMMA'
                print(a)
            elif lexeme == ';':
                a='SEMI'
                print(a)
            if lexeme != '':
                b=lexeme.replace('\n','<next line>')
                lexeme = ''
                fileout.write(a+' ')
    #This is because of the end of 'str'. So it is same as upside.
    elif  i+1 == len(str) :
        if lexeme in 'int':
            g='VTYPE'
        elif lexeme == 'char':
            g='VTYPE'
        elif lexeme == '(':
            g='LPAREN'
        elif lexeme == ')':
            print('RPAREN')
        elif lexeme == '{':
            print('LBRACE')
        elif lexeme == '}':
            g='RBRACE'
        elif accepts(Integer_dfa, 0, {2} | {3}, lexeme):
            g='INTEGER'
        elif accepts(Literal_dfa, 0, {2}, lexeme):
            g='LITERAL'
        elif accepts(Identifier_dfa, 0, {1}, lexeme):
            g='IDENTIFIER'
        elif lexeme in white_space:
            g='WHITESPACE'
        elif lexeme in addsub:
            g='ADDSUB'
        elif lexeme in multdiv:
            g='MULTDIV'
        elif lexeme in keyword:
            g='KEYWORD'
        elif lexeme in operator:
            g='COMPARISON'
        elif lexeme == 'return':
            g='RETURN'
        elif lexeme == ',':
            g='COMMA'
        elif lexeme == ';':
            g='SEMI'
        elif lexeme == '=':
            g='ASSIGNMENT'
        if lexeme != '':
            lexeme = ''
            fileout.write(g)


file.close()
fileout.close()
