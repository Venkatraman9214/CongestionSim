/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, Perl, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#define N 5

int max_thr(int b[])
//{   int max_val(int b[])
{
    //int max=0;
   float max=b[1];
    for(int i=0;i<5;i++)
    {
        if (b[i]>=max)
        {
            max=b[i];
           
        }
    
    }
  printf("throuput-MAX:%f\n  ",max); //max throughput in gbps
}


float average(int a, int rate){
   int sum=0,i;
     for(int i=0;i<N;i++){
         sum= sum+ rate;
        
    }
    float avg= (a+rate)/2;
   //  printf("sum is%f",avg);
   return avg;
}

int probe_packets()
{   int s_flow[N];
    int probe_traffic[10]={1,2,3,4,5,6,7,8,9,10};
    for(int i=0;i<N;i++){
        s_flow[i]=probe_traffic[i];
    }
}

int main()
{   float bdp;
    int a[5]={1,2,3,4,5};
    float rtt[5]={100,200,300,400};
    int state_a=1, state_i=0;
    int state[N];
    float min_rtt=0.8;
    float thr[N];
    float factor[N];
    float data=2000;
    float interval= 3;
    int rate[N];
    for(int i=0;i<N;i++)
    {
        thr[i]= data/rtt[i];            //calculate throughput-->inflight data(in gb)/rtt (in ms)
        printf("throuput is: %f\n sub-flow: %d\n",thr[i],a[i]);
        factor[i]= thr[i]/max_thr(thr);
         printf("factor: %f\n",factor[i]);
    }
    
    for(int i=0;i<N;i++)
    {
   //   factor[i]= thr[i]/max_thr(thr,i);
   //   printf("factor %d",factor[i]);
      if(factor[i]>=min_rtt){
          rate[i]=1;
          printf("  \nrate is%d\n", rate[i]);
      }
      else
      {
          rate[i]=0;
          printf("  \nrate1 is%d\n", rate[i]);
      }
        
    }
    for(int i=0;i<N;i++)
    {
        if(state_a){
            printf("avg:%d\n",average(interval,rate));
            if(average(interval,rate[i])==0){
                printf("Probing state, no payload\n");
                state[i]= probe_packets();
            }
        }
        else
        {
            rate[i]=1;
           state_a=1;
         printf("active \n");
            
        }
        
    }
    

    return 0;
}

