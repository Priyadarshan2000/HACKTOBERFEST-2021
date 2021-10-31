#include<iostream>
#include"1.cpp"
using namespace std;
class queue{
	stack a,b;
	int c=0;
	public:
	void enQ(int n){
			//b.push(n);
			
			while(!b.isEmpty()){
				int k=b.pop_return();
				a.push(k);
			}
			a.push(n);
			while(!a.isEmpty()){
				int k=a.pop_return();
				b.push(k);
			}	
			//b.push(n);		
			c++;	
		
		
	}
	void deQ(){
		

		b.pop();
	}
	void print(){
		b.print();
	}
};
int main(void){
	queue a;
	int c=1;
	while(c!=0){
		cout<<"1 to push"<<endl;
		cout<<"2 to pop"<<endl;
		cout<<"3 to peek"<<endl;
		cout<<"4 to isFull"<<endl;
		cout<<"5 to isEmpty"<<endl;
		cout<<"6 to print"<<endl;		
		cout<<"Enter -";
		//int c;
		cin>>c;
		system("CLS");
		switch(c){
			case 1:
				int n;
				cout<<"Enter value-";
				cin>>n;
				a.enQ(n);
				break;
			case 2:
				a.deQ();
				break;
		/*	case 3:
				a.Top();
				break;
			case 4:
				if(a.isFull())
					cout<<"Full"<<endl;
				else
					cout<<"Not Full"<<endl;
				break;
			case 5:
				if(a.isEmpty())
					cout<<"is Empty"<<endl;
				else
					cout<<"Not Empty"<<endl;
				break;*/
			case 6:
				a.print();
				break;
			case 0:
				cout<<"Ending..";
		}		
	}
} 
