// projection.c
#include <stdio.h>

void vector_projection(double a[3], double b[3], double proj[3]) {
    double b_norm_sq = b[0]*b[0] + b[1]*b[1] + b[2]*b[2];
    double dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2];

    double scalar = dot_product / b_norm_sq;

    proj[0] = scalar * b[0];
    proj[1] = scalar * b[1];
    proj[2] = scalar * b[2];
}

