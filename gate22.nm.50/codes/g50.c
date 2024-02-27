#include <stdio.h>
#include <math.h>

void linespace(float start, float stop, float step, float* t_values, double* y_values, int num_values) {
    for (int i = 0; i < num_values; ++i) {
        t_values[i] = start + i * step;
        y_values[i] =   exp(6 * t_values[i]) - 3*(exp(5 * t_values[i]))/7 + (2*exp(-2 * t_values[i]));
    }
}

int main() {
    // Define the range and step size
    float start = -3;
    float stop = 1.25;
    float step = 0.125;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    float t_values[num_values];
    double y_values[num_values];

    // Call the linespace function
    linespace(start, stop, step, t_values, y_values, num_values);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");
    
  
    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%.6f %.8lf\n", t_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}
