#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846
#define N_MIN -5
#define N_MAX 5

double an(int n) {
    return 0;
}

int a0 =0;
double bn(int n) {
    double omega0 = PI;
    return (-2 / (pow(n * omega0, 2))) * (-n * omega0 + sin(n * omega0));
}

double f(double x) {

	/*if(x<-1)
	x+=2;
	else if (x>1)
	x-=2;*/

   
    if (x<-1)
        for(;x<-1;x+=2);
    else if (x>1)
        for(;x>1;x-=2);
        
    if (x >= -1 && x < 0)
        return -1 - x;
    else if (x > 0 && x <= 1)
        return 1 - x;
    else if (x==0)
        return 0;
        
   
}



int main() {
    FILE *file;
    file = fopen("output.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double x;
    for (x = N_MIN; x <=N_MAX ; x+=0.125) {
        double result=0;
        int n;
        result +=a0;
        for (n = 1; n <= N_MAX; n++) {
            
            result +=  (an(n) * cos(n * PI * x)) + (bn(n) * sin(n * PI * x));
                  }
       
        fprintf(file, "%9lf %9lf %9lf\n", x,f(x), result);
    }

    fclose(file);
    return 0;
}

