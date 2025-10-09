// Define vectors V and W
double V[3] = {2, 1, -1};
double W[3] = {1, 0, 3};

// Array to store cross product
double cross_V_W[3];

// Function to compute cross product
void compute_cross_product() {
    cross_V_W[0] = V[1]*W[2] - V[2]*W[1];
    cross_V_W[1] = V[2]*W[0] - V[0]*W[2];
    cross_V_W[2] = V[0]*W[1] - V[1]*W[0];
}

// Functions to access cross product components
double* get_cross_product() {
    return cross_V_W;
}

