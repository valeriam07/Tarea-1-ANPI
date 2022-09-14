Algunos ejemplos con los que se pueden probar los metodos de la clase MPenta:

Ejemplo 1)
    int [][] matriz =  {{1,2,1,0,0,0,0,0,0,0},       
                        {3,2,2,5,0,0,0,0,0,0},
                        {1,2,3,1,-2,0,0,0,0,0},
                        {0,3,1,-4,5,1,0,0,0,0},
                        {0,0,1,2,5,-7,5,0,0,0},
                        {0,0,0,5,1,6,3,2,0,0},
                        {0,0,0,0,2,2,7,-1,4,0},
                        {0,0,0,0,0,2,1,-1,4,-3},
                        {0,0,0,0,0,0,2,-2,1,5},
                        {0,0,0,0,0,0,0,-1,4,8}};
    int [] vectb = {8,33,8,24,29,82,71,17,57,108};

Ejemplo 2)
    float [][] matriz2 =   {{10,-1,2,0},        
                            {-1,11,-1,3},
                            {2,-1,10,-1},
                            {0,3,-1,8}};
    int [] vectb2 = {6,25,-11,15};

Ejemplo 3) Matriz de orden n
    float [][] matrizn = A.nOrderMatrix(n);
    float [] vectn = A.nOrderVect(n);
