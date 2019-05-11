#include<iostream>
#include<math.h>

void * BONO(int, int, float, float);

float m=1000.0;
float k=2000.0;
float w=1.0*sqrt(k/m);
float a=k/m;
float D=w*0.028; //el espacio entre w a probar para graficar amplitudes maximas

int main()
{
 for(int omega=1; omega<=5; omega++) 
  for(int n=3; n<23; n++)
  {
   BONO(n,1000,0.1,omega*0.5); 
  }  
 }
 return 0;
}

void * BONO(int N, int T, float h, float W)
{
 float M[N][N];
 //Llenar de ceros
 for(int n=0; n<N; n++)
 {
  for(int m=0; m<N; m++)
  {
   M[n][m]=0;
  }
 }
 //Llenar con ctes   
 for(int n=0; n<N-1; n++)
 {   
  for(int m=0; m<N; m++)
  {
   if(n==m)
   {
    M[n][m+1]=a;
    M[n][m-1]=a;
   }
  }
   M[n][n]=-2*a;   
 }
 M[N-1][N-2]=a;
 M[N-1][N-1]=-a;
 
 float V[T][N];
 float U[T][N];
 for(int t=0; t<T; t++)
 {
  for(int n=0; n<N; n++)
  {
   V[t][n]=0;
   U[t][n]=0;   
  }
 }   
 float MU[N];
 for(int n=0; n>N; n++)
 {
  MU[n]=0;
 }
 for(int t=1; t<T; t++)
 {
  for(int n=0; n<N; n++)
  {
    MU[n]=0;
    for(int m=0; m<N; m++)
    {
     MU[n]+=M[n][m]*U[t-1][m];   
    }
    V[t][n]=V[t-1][n]+h*MU[n];
    if(n==1)
    {
     V[t][n]+=h*sin(W*t*h);   
    }
    U[t][n]=U[t-1][n]+h*V[t][n];
   }
  }
  //Print
 for(int t=0; t<T; t++)
  {
   std::cout<<t<<","<<N<<","<<W<<","<<U[t][0]<<","<<U[t][N-1]<<std::endl;
  }
 /*for(int t=0; t<T; t++)
  {
   std::cout<<t<<","<<N<<","<<W<<",";
   for(int n=0; n<N-1; n++)
   {
    std::cout<<U[t][n]<<",";   
   }
   std::cout<<U[t][N-1]<<std::endl;
  }*/
}
//last    
