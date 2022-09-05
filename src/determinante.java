
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
        else if (isPentadiagonal(matriz) == true){

        }
        
        return 0;
    }

    public static void main(String[] args){
        determinante det = new determinante();
        int [][] matriz = {{0,7,5,0,0},
                           {3,8,4,1,0},
                           {1,5,0,1,9},
                           {0,5,2,1,0},
                           {0,0,1,2,1}};
        det.det_penta(matriz);
    }
}
