
#include<iostream> 
using namespace std; 


void display() 
{ 
static int global = 5; 
	cout<<global<<endl; 
	global+= 10;
} 

// main function 
int main() 
{ 
	display();  

	display();
	display(); 
} 
