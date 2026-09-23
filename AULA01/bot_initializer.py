"""Inicializa e exibe as configuracoes basicas do robo."""


BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 30.0
IS_PRODUCTION = False


def main():
    """Exibe os valores configurados e seus respectivos tipos."""
    print("=== Inicializacao do Robo ===")
    print(f"BOT_NAME: {BOT_NAME} | tipo: {type(BOT_NAME)}")
    print(f"MAX_RETRIES: {MAX_RETRIES} | tipo: {type(MAX_RETRIES)}")
    print(
        f"EXECUTION_TIMEOUT: {EXECUTION_TIMEOUT} | "
        f"tipo: {type(EXECUTION_TIMEOUT)}"
    )
    print(f"IS_PRODUCTION: {IS_PRODUCTION} | tipo: {type(IS_PRODUCTION)}")


if __name__ == "__main__":
    main()
