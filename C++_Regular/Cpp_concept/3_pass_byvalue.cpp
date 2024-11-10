#include<iostream>
using namespace std;

void my_fun(int x)
{
    x = 30;
    cout << "x is:" <<x<<endl;
}
int main(){
    int x = 20;
    my_fun(x);
    cout << "x is:" <<x<<endl;
}


