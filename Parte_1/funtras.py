global iterMax, tolerancia, pi

#se definen las variables globales
iterMax=2500
tolerancia=1*10**-8
pi=3.141592653589793
#------------------------Función Factorial------------------------------------------------

def factorial(num):
    if(num>1):
        value=num   #Valor que almacena el resultado

        while (num-1)!=1:   #Itera hasta llegar a 1
            value = value*(num-1)
            num=num-1
        return value
    elif num==0 or num==1:
        return 1
    else:
        return "error"

#-----------------------------Función x^-1-------------------------------------------
def div_t(num):

    if num>0:   #Verifica que sea posible calcularlo

        eps = 2.2204*10**-16
        xk_1=0
        error=0

        #Determina cual debe de ser el valor inicial de Xk
        if factorial(80) < num < factorial(100):
            xk=eps**15
        elif factorial(60) < num <= factorial(80):
            xk = eps ** 11
        elif factorial(40) < num <= factorial(60):
            xk = eps ** 8
        elif factorial(20) < num <= factorial(40):
            xk = eps ** 4
        elif factorial(0) < num <= factorial(20):
            xk = eps ** 2
        elif num >=100:
            return 0
        else:
            xk = eps
        for k in range(1, iterMax):

            xk_1=xk*(2-num*xk)  #Función para aproximar
            error=abs(xk_1-xk)  #calculo del error

            if error < tolerancia*xk_1:
                xk=xk_1
                break
            xk = xk_1

        return xk
    elif num==1:
        return 1
    else:
        return "Error"

#---------------------------Función exponencial---------------------------------------------

def exp_t(num):

    sk_1=0
    sk=1
    error=0

    for k in range(1, iterMax):

        i=0
        # While para calcular la sumatoria
        while(i<=k):

            sk_1= sk_1+((num**i)*div_t(factorial(i)))   #Se calcula el sk+1
            i=i+1

        error=abs(sk_1-sk)      #Se calcula el error usando el resultado anterior

        if error < tolerancia:
            sk=sk_1
            break
        sk = sk_1       #Se guarda el dato para calcular el error en la siguiente iteración
        sk_1=0          #Se inicializa el valor para la siguiente iteración

    return sk

#------------------------Función sin------------------------------------------------

def sin_t(num):
    # Se inicializa variables
    sk_1=0
    sk=1
    error=0

    for k in range(1, iterMax):

        i=0
        # While para calcular la sumatoria
        while(i<=k):

            sk_1= sk_1+(((-1)**i)*((num**((2*i)+1))*div_t(factorial((2*i)+1)))) #Se calcula el sk+1
            i=i+1

        error=abs(sk_1-sk) #Se calcula el error usando el resultado anterior

        if error < tolerancia:
            sk=sk_1
            break
        sk = sk_1           #Se guarda el dato para calcular el error en la siguiente iteración
        sk_1=0              #Se inicializa el valor para la siguiente iteración

    return sk
#--------------------------Función Cos----------------------------------------------
def cos_t(num):

    #Se inicializa variables

    sk_1=0
    sk=1
    error=0

    for k in range(1, iterMax):

        i=0

        #While para calcular la sumatoria
        while(i<=k):

            mul=((-1)**i)
            nume=(num**(2*i))
            den=factorial(2*i)

            sk_1= sk_1+(mul*(nume*div_t(den)))#Se calcula el sk+1
            i=i+1

        error=abs(sk_1-sk)  #Se calcula el error usando el resultado anterior

        if error < tolerancia:
            sk=sk_1
            break
        sk = sk_1   #Se guarda el dato para calcular el error en la siguiente iteración
        sk_1=0      #Se inicializa el valor para la siguiente iteración

    return sk
#----------------------------Función sin^-1(x)--------------------------------------------
def asint_t(num):

    #Se inicializa las variables a usar
    if -1<= num <=1:
        sk_1 = 0
        sk = 1
        error = 0

        for k in range(1, iterMax):

            i = 0
            #El while nos ayuda a hacer la sumatoria

            while (i <= k):

                #Se calcula por partes la operación

                fact= factorial(2*i)
                den= (4**i)*((factorial(i))**2)*((2*i)+1)
                mul=(num**((2*i)+1))

                sk_1 = sk_1 + (fact*div_t(den))*mul
                i = i + 1

            error = abs(sk_1 - sk)  #Se calcula el error

            if error < tolerancia:
                sk = sk_1
                break
            sk = sk_1   #Se guarda el dato para calcular el error en la siguiente iteración
            sk_1 = 0    #Se inicializa el valor para la siguiente iteración

        return sk
    else:
        return "error"
#------------------------Función ln(x)------------------------------------------------
def ln_t(num):
    # Se inicializa las variables a usar
    if num>0:
        sk_1=0
        sk = 1
        error = 0
        #Es la parte constante de la aproximación
        mul_fin = (2 * (num - 1)) * div_t(num + 1)

        for k in range(1, iterMax):

            i = 0
            # El while nos ayuda a hacer la sumatoria

            while (i <= k):
                # Se calcula por partes la operación

                mul = ((num-1)*div_t(num+1))**(2*i)


                sk_1 = sk_1 + (mul_fin*(div_t((2*i)+1)*mul))
                i = i + 1

            error = abs(sk_1 - sk)  # Se calcula el error

            if error < tolerancia:
                sk = sk_1
                break
            sk = sk_1  # Se guarda el dato para calcular el error en la siguiente iteración
            sk_1=0
        return sk
    else:
        return "error"
#-------------------------Función Tangente-----------------------------------------------
def tan_t(num):
    return sin_t(num)*div_t(cos_t(num))
#----------------------------Función logaritmo--------------------------------------------
def log_t(x,y):
    if x>0:
        return ln_t(x)*div_t(ln_t(y))
    else:
        return "error"
#----------------------------Función sinh(x)--------------------------------------------
def sinh_t(num):
    sk_1 = 0
    sk = 1
    error = 0


    for k in range(1, iterMax):

        i = 0
        # El while nos ayuda a hacer la sumatoria

        while (i <= k):
            # Se calcula por partes la operación

            nume=(num**((2*i)+1))
            den= factorial((2*i)+1)

            sk_1 = sk_1 + (nume*div_t(den))
            i = i + 1

        error = abs(sk_1 - sk)  # Se calcula el error

        if error < tolerancia:
            sk = sk_1
            break
        sk = sk_1  # Se guarda el dato para calcular el error en la siguiente iteración
        sk_1 = 0
    return sk
#------------------------Función cosh(x)------------------------------------------------
def cosh_t(num):
    sk_1 = 0
    sk = 1
    error = 0


    for k in range(1, iterMax):

        i = 0
        # El while nos ayuda a hacer la sumatoria

        while (i <= k):
            # Se calcula por partes la operación

            nume=(num**(2*i))
            den= factorial(2*i)

            sk_1 = sk_1 + (nume*div_t(den))
            i = i + 1

        error = abs(sk_1 - sk)  # Se calcula el error

        if error < tolerancia:
            sk = sk_1
            break
        sk = sk_1  # Se guarda el dato para calcular el error en la siguiente iteración
        sk_1 = 0
    return sk
#-----------------------Función tanh(x)-------------------------------------------------
def tanh_t(num):
    return sinh_t(num)*div_t(cosh_t(num))
#------------------------función x^y------------------------------------------------
def power_t(x,y):

    if(y<0):
        y=-y
        cambiarsigno=0

        valor=1
        if (x<0):
            cambiarsigno=1
            x=-x

        for k in range(0,y):
            valor= valor*div_t(x)
        if cambiarsigno==1:
            valor=-valor

        return valor
    elif y>0:

        valor = 1
        for k in range(0, y):
            valor = valor *x
        return valor
#----------------------Función tan^-1(x)--------------------------------------------------
def atan_t(num):

    #Se verifica cual debe ser la sumatoria a realizar dependiendo
    #del valor de entrada
    op=0
    if(-1<=num<=1):
        op=0
    elif(num>1):
        op=1
    elif(num<1):
        op=2
    sk_1_aux=0
    sk_1 = 0
    sk = 1
    error = 0

    for k in range(1, iterMax):

        i = 0
        # El while nos ayuda a hacer la sumatoria

        while (i <= k):
            # Se calcula por partes la operación
            if(op==0):
                mul=(-1)**i
                nume = (num ** ((2 * i)+1))
                den = (2*i)+1

                sk_1 = sk_1 + (mul*(nume * div_t(den)))
            elif(op==1):
                mul = (-1) ** i
                den = ((2 * i) + 1)*(num**((2*i)+1))

                sk_1_aux = sk_1_aux + (mul * div_t(den))
            elif (op == 2):
                mul = (-1) ** i
                den = ((2 * i) + 1) * (num ** ((2 * i) + 1))

                sk_1_aux = sk_1_aux + (mul * power_t(den,-1))

            i = i + 1

        if (op == 1):
            sk_1=(pi/2)-sk_1_aux
            sk_1_aux=0
        elif (op == 2):
            sk_1=-(pi/2)-sk_1_aux
            sk_1_aux=0

        error = abs(sk_1 - sk)  # Se calcula el error

        if error < tolerancia:
            sk = sk_1
            break
        sk = sk_1  # Se guarda el dato para calcular el error en la siguiente iteración
        sk_1 = 0
    return sk

#-----------------------Función raíz cuadrada-------------------------------------------------
def sqrt_t(x):
    #Se inicializa las variables
    xk=x/2
    xk_1=0
    error=0
    if(x>0):    #Se verifica que esté en el dominio
        for k in range(1, iterMax):
            xk_1= xk - (((xk**2)-x)*div_t(2*(xk**(2-1))))   #Se calcula el x+1

            error= abs(xk_1-xk) #Se calcula el error
            if(error<(tolerancia*xk_1)):
                xk=xk_1
                break

            xk = xk_1

        return xk
    else:
        return "Error"

#------------------------Secante------------------------------------------------
def sec_t(x):
    return power_t(cos_t(x),-1) #Se hace uso de la función cos ya hecha
#---------------------Cotangente---------------------------------------------------
def cot_t(x):
    return div_t(tan_t(x))  #Se hace uso de la función tan ya hecha
#----------------------cos^-1(x)--------------------------------------------------
def acos_t(num):
    if -1<num<1:
        return ((pi/2)-asint_t(num))
    else:
        return "error"
#----------------------Cosecante--------------------------------------------------

def csc_t(x):
    return power_t(sin_t(x),-1) #Se hace uso de la función sin ya hecha
#------------------------Raíz------------------------------------------------
def root_t(x,y):
    xk = x / 2
    xk_1 = 0
    error = 0
    #Se verificar si y es par y x mayor a 0
    if (x > 0 & y % 2 == 0):
        for k in range(1, iterMax):
            xk_1 = xk - (((xk ** y) - x) * div_t(y * (xk ** (y - 1))))  #Se calcula el x+1

            error = abs(xk_1 - xk)  #Se calcula el error
            if (error < (tolerancia * xk_1)):
                xk = xk_1
                break

            xk = xk_1

        return xk   #Retorna el valor

    #Se verifica si y es impar para saber si puede aceptar numeros negativos
    elif (y % 2 == 1):
        for k in range(1, iterMax):
            xk_1 = xk - (((xk ** y) - x) * div_t(y * (xk ** (y - 1)))) #Se calcula el x+1

            error = abs(xk_1 - xk)  #Se calcula el error
            if (error < (tolerancia * xk_1)):
                xk = xk_1
                break

            xk = xk_1

        return xk

    else:
        return "error"

#------------------------------------------------------------------------


if __name__ == '__main__':
    #print(factorial(100))
    #print(div_t(1/2))
    #print(exp_t(-1))
    #print(exp_t(3))
    #print(sin_t(4))
    #print(cos_t(40))
    #print(tan_t(100))
    #print(asint_t(1/3))
    #print(ln_t(0))
    #print(tan_t(2))
    #print(sin_t(5))
    #print(div_t(cos_t(5)))
    #print(log_t(32,3))
    #print(sinh_t(5))
    #print(cosh_t(5))
    #print(tanh_t(5))
    #print(atan_t(-5))
    #print(power_t(4,3))
    #print(sqrt_t(2))
    #print(sec_t(11))
    #print(cot_t(2))
    #print(csc_t(4))
    #print(root_t(4,2))
    print(acos_t(1/2))