for(int i=0;i<n;i++){}     -->O(n)

for(int i=0;i<n;i=i+2){}   -->O(n)

for(int i=n;i>1;i--){}  -->O(n)

for(int i=1;i<n;i++){}   -->O(n)

for(int i=1;i<n;i++){}
for(int j=1;j<n;j++){}  -->"n+n"  :   O(n)

for(int i=0;i<n;i++){
    for(int i=0;i<n;i++){
        }
    }                                   -->"n*n"   :  O(n^2)

for(int i=1;i<n;i=i*2){}
-->   1,2,2^2,2^3.........2^k
-->     i>n => 2^k>n =>  k>=log(2)(n)
-->    O(log(2)(n))

for(int i=1;i<n;i=i*3){}
--> similarly  3^k     and          k>=log(3)(n)
-->O(log(3)(n))

for(int i=n;i>1;i=i/2){}
-->n,n/2,n/2^2,n/2^3..............n/2^k
-->k>=log(2)(n)
-->    O(log(2)(n))

int p=0
for( int i=1;i<n;i=i*2){
    P+=1;
    }
for( int j=1;j<p;j=j*2){} 

