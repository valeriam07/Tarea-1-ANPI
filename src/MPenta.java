
public class MPenta {
    public void printMatriz(int [][] matriz){
        for (int i = 0; i < matriz.length; i++) { 
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void printVector(float [] vector, String name){
        System.out.println(name + ": ");
        for (int i = 0; i < vector.length; i++){
            System.out.print(vector[i]+ " ");
        }
        System.out.println();
    }

    public boolean isPentadiagonal(int [][] matriz){            //analiza por columnas si los valores por abajo y por encima de las diagonales son 0
        int diagIndex = 3;      //valor a partir del cual se analiza en la respectiva columna, aumenta 1 segun avanza la busqueda
        if (matriz.length < 4){
            System.out.println("Error: La matriz no es pentadiagonal");
            return false;
        }
        for (int j = 0; j < matriz.length; j++){
            for (int i = diagIndex; i < matriz.length; i++){
                if (matriz[i][j] != 0 || matriz[j][i] != 0){
                    System.out.println("Error: La matriz no es pentadiagonal");
                    return false;
                }
            }
            diagIndex += 1;
        }
        System.out.println("La matriz SI es pentadiagonal");
        return true;
    }

    public int det_penta(int [][] matriz){
        if (matriz.length != matriz[0].length){ //Comprobar que la matriz es cuadrada
            System.out.println("Error: La matriz no es cuadrada");
        }
        else if (isPentadiagonal(matriz) == true){      //Si es pentadiagonal hace el metodo de Evans
            int[] P = new int[matriz.length];  
            int[] R = new int[matriz.length];
            int[] S = new int[matriz.length];

            P[0] = matriz[0][0];
            R[1] = matriz[0][1];
            S[1] = matriz[1][0];
            P[1] = matriz[1][1]*P[0] - S[1]*R[1];
            P[2] = matriz[2][2]*P[1] - matriz[2][1]*matriz[1][2]*P[0] - matriz[2][0]*matriz[0][2]*matriz[1][1] + matriz[2][0]*matriz[1][2]*R[1] + matriz[2][1]*matriz[0][2]*S[1];
            R[2] = matriz[1][2]*P[0] - matriz[0][2]*S[1];
            S[2] = matriz[2][1]*P[0] - matriz[2][0]*R[1];
            P[3] = matriz[3][3]*P[2] - matriz[3][2]*matriz[2][3]*P[1] - matriz[3][1]*matriz[1][3]*(matriz[2][2]*P[0] - matriz[2][0]*matriz[0][2]) + matriz[3][1]*matriz[2][3]*R[2] + matriz[3][2]*matriz[1][3]*S[2];
            
            for (int i = 4; i < matriz.length; i++){
                R[i-1] = matriz[i-2][i-1]*P[i-3] - matriz[i-3][i-1]*S[i-2];
                S[i-1] = matriz[i-1][i-2]*P[i-3] - matriz[i-1][i-3]*R[i-2];
                P[i] = matriz[i][i]*P[i-1] - matriz[i][i-1]*matriz[i-1][i]*P[i-2] - matriz[i][i-2]*matriz[i-2][i]*(
                    matriz[i-1][i-1]*P[i-3] - matriz[i-1][i-3]*matriz[i-3][i-1]*P[i-4]) + matriz[i][i-2]*matriz[i-1][i]*R[i-1] + matriz[i][i-1]*matriz[i-2][i]*S[i-1]; 
            }
            System.out.println("det(matriz) = " + P[matriz.length-1]);
            int det = P[matriz.length-1];
            return det;
        }
        return 0;
    }

    public float[] getDiagonal(int [][] matriz, int i, int j){
        float [] diagonal = new float[matriz.length];

        for (int fila = i; fila < matriz.length; fila++){
            if(j == matriz.length){
                break;
            }
            diagonal[fila] = matriz[fila][j];
            j++;
        }
        return diagonal;
    }

    public float[] ptrans_1(int [][] matrizA, int [] vectb){
        if(det_penta(matrizA) == 0){
            System.out.println("El sistema no tiene soluciones");
            float[] x = new float[0];
            return x;
        }
        int n = matrizA.length-1;

        float d [] = getDiagonal(matrizA, 0, 0);
        float a [] = getDiagonal(matrizA, 0, 1);
        float c [] = getDiagonal(matrizA, 1, 0);
        float e [] = getDiagonal(matrizA, 2, 0);
        float b [] = getDiagonal(matrizA, 0, 2);

        float[] mu = new float[n+1];  
        float[] alpha = new float[n+1];
        float[] beta = new float[n+1];
        float[] z = new float[n+1];
        float[] gamma = new float[n+1];

        mu[0] = d[0];
        alpha[0] = a[0]/mu[0];
        beta[0] = b[0]/mu[0];
        z[0] = vectb[0]/mu[0];

        gamma[1] = c[1];
        mu[1] = d[1] - alpha[0]*gamma[1];
        alpha[1] = (a[1]-beta[0]*gamma[1])/mu[1];
        beta[1] = b[1]/mu[1];
        z[1] = (vectb[1] - z[0]*gamma[1])/mu[1];

        for (int i = 2; i <= n-2; i++){
            gamma[i] = c[i] - alpha[i-2]*e[i];
            mu[i] = d[i] - beta[i-2]*e[i] - alpha[i-1]*gamma[i];
            alpha[i] = (a[i]-beta[i-1]*gamma[i])/mu[i];
            beta[i] = b[i]/mu[i];
            z[i] = (vectb[i] - z[i-2]*e[i] - z[i-1]*gamma[i])/mu[i];

        }

        gamma[n-1] = c[n-1] - alpha[n-3]*e[n-1];
        mu[n-1] = d[n-1] - beta[n-3]*e[n-1] - alpha[n-2]*gamma[n-1];
        alpha[n-1] = (a[n-1] - beta[n-2]*gamma[n-1])/mu[n-1];
        gamma[n] = c[n] - alpha[n-2]*e[n];
        mu[n] = d[n] - beta[n-2]*e[n] - alpha[n-1]*gamma[n];
        z[n-1] = (vectb[n-1] - z[n-3]*e[n-1] - z[n-2]*gamma[n-1])/mu[n-1];
        z[n] = (vectb[n] - z[n-2]*e[n] - z[n-1]*gamma[n])/mu[n];
        
        float[] x = new float[n+1];
        x[n] = z[n];
        x[n-1] = z[n-1] - alpha[n-1]*x[n];

        for (int i = n-2; i >= 0; i--){
            x[i] = z[i] - alpha[i]*x[i+1] - beta[i]*x[i+2];
        }

        printVector(x, "Solucion: ");
        return x;

    }

    public int[][] nOrderMatrix(int n){
        int[][] matriz = new int[n][n];

        for (int i = 0; i < n; i++){
            if (i == 0){
                matriz[i][i] = 9;
            }else if (i == n-2){
                matriz[i][i] = 5;
                matriz[i+1][i] = -2;
                matriz[i][i+1] = -2;
            }else if (i == n-1){  //ultimo caso
                matriz[i][i] = 1;
                break;
            }else{
                matriz[i][i] = 6;
            }
            if((i+1) < n-1){
                matriz[i][i+1] = -4;
                matriz[i+1][i] = -4;
            }if((i+2) < n){
                matriz[i][i+2] = 1;
                matriz[i+2][i] = 1; 
            }
               
        }
        return matriz;
    }

    public int[] nOrderVect(int n){
        int [] vect = new int[n];
        vect[0] = 6;
        vect[1] = -1;
        return vect;
    } 

    public static void main(String[] args){
        MPenta A = new MPenta();
        int [][] matriz = {{1,2,1,0,0,0,0,0,0,0},       //matriz ejemplo 1
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

        int [][] matriz2 = {{10,-1,2,0},        //matriz ejemplo 2
                            {-1,11,-1,3},
                            {2,-1,10,-1},
                            {0,3,-1,8}};
        int [] vectb2 = {6,25,-11,15};

        int [][] matrizn = A.nOrderMatrix(50);
        int [] vectn = A.nOrderVect(500);
        A.ptrans_1(matrizn, vectn);


    }
}
