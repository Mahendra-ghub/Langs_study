#include<iostream>
using namespace std;

void printstring(string str,string &ref, string* ptr)
{
    cout<<str<<endl;
    cout<<ref<<endl;
    cout<<ptr<<endl;
    cout<<*ptr<<endl;
}

int main()
{
    string mystring = "Hello world";
    string myreference =" may i come in";
    string mypointer = "No get lost";
    printstring(mystring,myreference,&mypointer);


}