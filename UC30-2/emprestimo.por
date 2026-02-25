programa {
    funcao inicio() {
        real valorCasa, salario, prestacao
        inteiro anos, meses

        escreva("Qual o valor da casa: ")
        leia(valorCasa)

        escreva("Qual o seu salário: ")
        leia(salario)

        escreva("Em quantos anos você deseja pagar: ")
        leia(anos)

        meses = anos * 12
        prestacao = valorCasa / meses

        escreva("O valor da prestação é: ", prestacao)

        se(prestacao <= salario * 0.30) {
            escreva("Empréstimo aprovado \n")
        } senao {
            escreva("Empréstimo não aprovado \n")
        }
    }
}