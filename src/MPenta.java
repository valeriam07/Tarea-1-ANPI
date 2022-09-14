import java.text.DecimalFormat;
/**
 * Clase que contiene todos los metodos requeridos para matrices pentadianales segun lo solicitado
 */

 /*
  * Pregunta 1: Metodo det_penta (linea 67)
  * Pregunta 2: Metodo ptrans_1 (linea 124)
  * Pregunta 3: Main (linea 254)
  */
public class MPenta {
    /**
     * Metodo que se encarga de imprimir cualquier matriz para una facil visualizacion
     * @param matriz Matriz a imprimir
     */
    public void printMatriz(float [][] matriz){
        for (int i = 0; i < matriz.length; i++) { 
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    /**
     * Metodo que se encarga de imprimir cualquier vector para una facil visualizacion
     * @param vector Vector a imprimir
     * @param name Nombre del vector 
     */
    public void printVector(float [] vector, String name){
        System.out.println(name + ": ");
        for (int i = 0; i < vector.length; i++){
            System.out.print(vector[i]+ " ");
        }
        System.out.println();
    }

    /**
     * Verifica si una matriz es pentadiagonal
     * @param matriz Matriz que se desea analizar
     * @return Verdadero si la matriz es pentadiagonal, de lo contrario Falso
     */
    public boolean isPentadiagonal(float[][] matriz){            
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

    /**
     * Calcula el determinante, mediante el metodo de Evans, de una matriz, siempre y cuando esta sea pentadiagonal
     * @param matriz Matriz a la que se le desea calcular el determinante
     * @return Determinante de la matriz
     */
    public float det_penta(float [][] matriz){
        if (matriz.length != matriz[0].length){ 
            System.out.println("Error: La matriz no es cuadrada");
        }
        else if (isPentadiagonal(matriz) == true){      
            float[] P = new float[matriz.length];  
            float[] R = new float[matriz.length];
            float[] S = new float[matriz.length];

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
            float det = P[matriz.length-1];
            return det;
        }
        return 0;
    }

    /**
     * Obtiene una diagonal cualquiera en una matriz a partir de una posicion dada
     * @param matrizA Matriz donde se encuentra la diagonal buscada
     * @param i Posicion segun filas
     * @param j Posicion segun columnas
     * @return Vector que contiene los valores de la diagonal
     */
    public float[] getDiagonal(float[][] matrizA, int i, int j){
        float [] diagonal = new float[matrizA.length];

        for (int fila = i; fila < matrizA.length; fila++){
            if(j == matrizA.length){
                break;
            }
            diagonal[fila] = matrizA[fila][j];
            j++;
        }
        return diagonal;
    }

    /**
     * Metodo para solucionar un sistema de ecuaciones con una matriz pentadiagonal
     * @param matrizA Matriz pentadiagonal con los coeficientes asignados a cada variable
     * @param vectn Vector con las constantes a las cuales se iguala el sistema
     * @return Vector que contiene la solucion para cada variable del sistema
     */
    public float[] ptrans_1(float[][] matrizA, float[] vectn){
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
        z[0] = vectn[0]/mu[0];

        gamma[1] = c[1];
        mu[1] = d[1] - alpha[0]*gamma[1];
        alpha[1] = (a[1]-beta[0]*gamma[1])/mu[1];
        beta[1] = b[1]/mu[1];
        z[1] = (vectn[1] - z[0]*gamma[1])/mu[1];

        for (int i = 2; i <= n-2; i++){
            gamma[i] = c[i] - alpha[i-2]*e[i];
            mu[i] = d[i] - beta[i-2]*e[i] - alpha[i-1]*gamma[i];
            alpha[i] = (a[i]-beta[i-1]*gamma[i])/mu[i];
            beta[i] = b[i]/mu[i];
            z[i] = (vectn[i] - z[i-2]*e[i] - z[i-1]*gamma[i])/mu[i];

        }

        gamma[n-1] = c[n-1] - alpha[n-3]*e[n-1];
        mu[n-1] = d[n-1] - beta[n-3]*e[n-1] - alpha[n-2]*gamma[n-1];
        alpha[n-1] = (a[n-1] - beta[n-2]*gamma[n-1])/mu[n-1];
        gamma[n] = c[n] - alpha[n-2]*e[n];
        mu[n] = d[n] - beta[n-2]*e[n] - alpha[n-1]*gamma[n];
        z[n-1] = (vectn[n-1] - z[n-3]*e[n-1] - z[n-2]*gamma[n-1])/mu[n-1];
        z[n] = (vectn[n] - z[n-2]*e[n] - z[n-1]*gamma[n])/mu[n];
        
        float[] x = new float[n+1];
        x[n] = z[n];
        x[n-1] = z[n-1] - alpha[n-1]*x[n];

        for (int i = n-2; i >= 0; i--){
            x[i] = z[i] - alpha[i]*x[i+1] - beta[i]*x[i+2];
        }

        //printVector(x, "Solucion");
        System.out.println("\n");
        return x;

    }

    /**
     * Genera una matriz de orden n segun los valores propuestos
     * @param n Orden de la matriz
     * @return Matriz de orden n 
     */
    public float[][] nOrderMatrix(int n){
        System.out.println("___________________________________________________\nMatriz de orden " + n + "\n");
        float[][] matriz = new float[n][n];

        for (int i = 0; i < n; i++){
            if (i == 0){
                matriz[i][i] = 9;
            }else if (i == n-2){
                matriz[i][i] = 5;
                matriz[i+1][i] = -2;
                matriz[i][i+1] = -2;
            }else if (i == n-1){  
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

    /**
     * Genera un vector de orden n segun los valores propuestos
     * @param n Orden del vector
     * @return Vector de orden n 
     */
    public float[] nOrderVect(int n){
        float [] vect = new float[n];
        vect[0] = 6;
        vect[1] = -1;
        return vect;
    } 

    /**
     * Calcula el error existente en la solucion de un sistema de ecuaciones pentadiagonal
     * @param A Matriz de coeficientes
     * @param vectn Vector de las constantes a las cuales se iguala el sistema
     * @param x Vector solucion del sistema
     * @return Valor del error en la solucion 
     */
    public float error(float [][] A, float[] vectn, float [] x){
        int n = A.length;
        float error = 0;

        for (int i = 0; i < n; i++){
            float sum_Ax = 0;
            for (int j = 0; j < n; j++){
                sum_Ax += A[i][j]*x[j];
            }
            error += Math.pow(sum_Ax - vectn[i], 2);
        }
        error = (float) Math.sqrt(error);
        System.out.println("Error: " + error);
        return error;
    }

    public void pregunta3(int n){
        long startTime = System.currentTimeMillis();
        DecimalFormat df = new DecimalFormat("0.000");

        float [][] matrizn = nOrderMatrix(n);
        float [] vectn = nOrderVect(n);
        float [] solucion = ptrans_1(matrizn, vectn);
        error(matrizn, vectn, solucion);

        long endTime = System.currentTimeMillis();
        float tiempo_ms = (float) ((endTime - startTime));
        String tiempo_s = df.format(tiempo_ms/1000);
        System.out.println("\nTiempo de ejecucion: " + tiempo_s);

    }

    public static void main(String[] args){
        MPenta A = new MPenta();

        A.pregunta3(50);
        A.pregunta3(500);
        A.pregunta3(5000);
        A.pregunta3(10000);

    }
}
