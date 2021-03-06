#include<iostream>
#include<math.h>

void * LeapFrog(float, float, float, float, float, float, int, float, float);

float m=1000.0;
float k=2000.0;
float w=1.0*sqrt(k/m);
float a=k/m;
float D=w*0.028; //el espacio entre w a probar para graficar amplitudes maximas

int main()
{
 LeapFrog(0,0,0,0,0,0,1000,0.1, w);//Parte 1
 for(int n=0; n<100; n++)
 {
  LeapFrog(0,0,0,0,0,0,1000,0.1,(0.2*w)+(n*D));   //Parte 2
 }
 return 0;
}

void * LeapFrog(float u10, float v10, float u20, float v20, float u30, float v30, int N, float h, float W)
{
 float *V1;
 float *V2;
 float *V3;   
 float *U1;
 float *U2;
 float *U3;  
 
 V1=new float [N];
 V2=new float [N];
 V3=new float [N];
 U1=new float [N];
 U2=new float [N];
 U3=new float [N];
 //Es casi indistinto a Euler dado que las velocidades en t medios atras es cero en todos los pisos 
 V1[0]=0;
 V2[0]=0;
 V3[0]=0;
 U1[0]=0;
 U2[0]=0;
 U3[0]=0;
    
 std::cout<<0<<","<<V1[0]<<","<<V2[0]<<","<<V3[0]<<","<<U1[0]<<","<<U2[0]<<","<<U3[0]<<","<<W<<std::endl;
 for(int t=1; t<N; t++)
 {
  float V1_old=V1[t-1];
  float V2_old=V1[t-1];
  float V3_old=V1[t-1];
     
  V1[t]=V1[t-1]+h*(-2*a*U1[t-1]+a*U2[t-1]+sin(W*t*h));
  V2[t]=V2[t-1]+h*(a*U1[t-1]-2*a*U2[t-1]+a*U3[t-1]);
  V3[t]=V3[t-1]+h*(a*U2[t-1]-a*U3[t-1]);
     
  U1[t]=U1[t-1]+h*V1[t];
  U2[t]=U2[t-1]+h*V2[t];
  U3[t]=U3[t-1]+h*V3[t];
  std::cout<<t<<","<<V1[t]<<","<<V2[t]<<","<<V3[t]<<","<<U1[t]<<","<<U2[t]<<","<<U3[t]<<","<<W<<std::endl;
 }
}
