import funtras


def script():

    num = funtras.root_t((funtras.sin_t(3/7)+funtras.ln_t(2)),3)
    den = funtras.sinh_t(funtras.sqrt_t(2))
    sum = funtras.tanh_t(funtras.exp_t(-1))

    resultado = (num*funtras.div_t(den))+sum

    print("Este es el resultado del script: ", resultado)

if __name__ == '__main__':
    script()