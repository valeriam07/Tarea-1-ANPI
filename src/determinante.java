
public class determinante {
    public void printMatriz(int [][] matriz){
        for (int i = 0; i < matriz.length; i++) { 
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
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

    public static void main(String[] args){
        determinante det = new determinante();
        int [][] matriz = {{0,7,5,0},
                           {3,0,4,1},
                           {1,5,0,1},
                           {0,0,4,1}};
        det.det_penta(matriz);
    }
}
