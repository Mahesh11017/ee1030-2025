#include <math.h>

double OA[3] = {1, 2, 3};
double OB[3] = {-3, -2, 1};

double cross_product[3];

// Function to compute cross product OA x OB
void compute_cross_product() {
    cross_product[0] = OA[1]*OB[2] - OA[2]*OB[1];
    cross_product[1] = OA[2]*OB[0] - OA[0]*OB[2];
    cross_product[2] = OA[0]*OB[1] - OA[1]*OB[0];
}

// Function to compute magnitude of cross product vector
double compute_area() {
    compute_cross_product();
    return 0.5 * sqrt(cross_product[0]*cross_product[0] +
                      cross_product[1]*cross_product[1] +
                      cross_product[2]*cross_product[2]);
}

