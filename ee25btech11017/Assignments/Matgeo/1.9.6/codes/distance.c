#include <math.h>

// Array to store roots
static float roots[2];

// Function to return pointer to roots array
float* get_roots() {
    // distance between Q(0,1) and P(5,-3)
    float d1 = sqrt((5-0)*(5-0) + (-3-1)*(-3-1)); // sqrt(41)
    
    // Solve for x: x^2 + 25 = d1^2 -> x^2 = 16
    roots[0] = 4.0;
    roots[1] = -4.0;
    
    return roots;
}

