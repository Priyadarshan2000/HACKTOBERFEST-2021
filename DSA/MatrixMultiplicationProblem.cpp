//01 Matrix Multiplication Problem


/*Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order 
to perform the multiplications.We have many options to multiply a chain of matrices because 
matrix multiplication is associative. In other words, no matter how we parenthesize the product, 
the result will be the same.*/

#include<iostream>
using namespace std;


int matrixMultiplication(int arr[],int n){
	int dp[n][n];
	int s[n][n];
	for(int i=1;i<n;i++) dp[i][i]=0;
	
	for(int j=2;j<n;j++){
		for(int i=1;i<n-j+1;i++){
			int k=i+j-1;
			dp[i][k] = INT_MAX;
			for(int l=i;l<=k-1;l++){
				int cost = dp[i][l] + dp[l+1][k] + arr[i-1] * arr[k] * arr[l];
				if (cost<dp[i][k]){
					dp[i][k] = cost;
					s[i][k]=l;
				}	
			}
		}
	}
	return dp[1][n-1];
}

int main(){
	cout<<"Enter the size of the array: ";
	int n;
	cin>>n;
	cout<<"Enter the array elements: ";
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	cout<< "Minimum number of multiplication is: "<< matrixMultiplication(a,n)<<endl;

	return 0;
}




