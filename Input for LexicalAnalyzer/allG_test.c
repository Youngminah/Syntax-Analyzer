int a;
int foo(int a, int b){
    b = "hello";
    a = -12342;
    if( a == b){
    }
    else{
        while( a < b) {
            a = ( a + b ) - a;
            a = a / ( a - b );
            a = a + b;
            a = a - b;
        }
    }
    return ( a+b );
}