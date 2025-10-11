#include <math.h>

// Given data
// Point on first line: P1 = (1,1,0)
// Direction vector of first line: d1 = (2,-1,1)
// Point on second line: P2 = (2,1,-1)
// Direction vector of second line (same as d1 since parallel)

double P1[3] = {1, 1, 0};
double d1[3] = {2, -1, 1};
double P2[3] = {2, 1, -1};
double d2[3] = {2, -1, 1};

double cross[3];

double cross_norm;

double distance;

// Function to compute cross product
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute dot product
double dot_product(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute norm
double norm(double a[3]) {
    return sqrt(dot_product(a, a));
}

void compute_distance() {
    double P2_minus_P1[3] = {P2[0]-P1[0], P2[1]-P1[1], P2[2]-P1[2]};
    
    // Compute cross product of direction vectors (should be zero or near zero since parallel)
    cross_product(d1, d2, cross);
    cross_norm = norm(cross);

    if (cross_norm < 1e-8) {
        // Lines are parallel
        // distance = |(P2 - P1) x d1| / |d1|
        double temp[3];
        cross_product(P2_minus_P1, d1, temp);
        distance = norm(temp) / norm(d1);
    } else {
        // Lines are skew
        // distance = |(P2 - P1) . (d1 x d2)| / |d1 x d2|
        distance = fabs(dot_product(P2_minus_P1, cross)) / cross_norm;
    }
}

// Getter function for distance
double get_distance() {
    return distance;
}

// Getter functions for points and direction vectors

void get_P1(double* arr) {
    for (int i=0; i<3; i++)
        arr[i] = P1[i];
}

void get_P2(double* arr) {
    for (int i=0; i<3; i++)
        arr[i] = P2[i];
}

void get_direction(double* arr) {
    for (int i=0; i<3; i++)
        arr[i] = d1[i];
}

