#include <stdio.h>
#include <math.h>

void linespace(float start, float stop, float step, float* t_values, double* Gt_values, int num_values) {
    for (int i = 0; i < num_values; ++i) {
        t_values[i] = start + i * step;
        Gt_values[i] =  (10 * (exp(-21 * t_values[i]/ 11.0) - exp(-10 * t_values[i]))) / 89.0;
    }
}

int main() {
    // Define the range and step size
    float start = 0;
    float stop = 40;
    float step = 0.25;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    float t_values[num_values];
    double Gt_values[num_values];

    // Call the linespace function
    linespace(start, stop, step, t_values, Gt_values, num_values);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");
    
  
    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%.6f %.30lf\n", t_values[i], Gt_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}
