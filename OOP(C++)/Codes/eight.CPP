#include <iostream>
using namespace std;
int add(int a, int b){
    return a + b;
}
int main(){
    
    int sum = add(5, 10);
    cout << "the sum is "<< sum <<endl;
}